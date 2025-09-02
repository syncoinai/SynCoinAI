# src/blockchain/block.py
"""
Block con Merkle root, verificación, multifirma ECDSA y ia_proof mejorada.
Requiere: cryptography (pip install cryptography)
"""

import time
import hashlib
import json
import base64
from typing import List, Dict, Any, Optional

# Dependencia para ECDSA
try:
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import ec, utils
    from cryptography.hazmat.primitives.asymmetric.ec import ECDSA
    from cryptography.exceptions import InvalidSignature
except Exception as e:
    raise ImportError("This module requires the 'cryptography' package. Install with: pip install cryptography") from e


# ---------------------------
# Utilities: deterministic JSON
# ---------------------------
def stable_json_dumps(value: Any) -> str:
    """Serializa de forma determinista (orden de keys)"""
    return json.dumps(value, sort_keys=True, separators=(',', ':'), default=str)


# ---------------------------
# Merkle root simple
# ---------------------------
def calculate_merkle_root(transactions: List[Dict[str, Any]]) -> str:
    """
    Calcula un Merkle root simple desde la lista de transacciones.
    Cada transacción debe ser serializable. Si no hay txs -> empty string.
    """
    if not transactions:
        return ""
    hashes = [hashlib.sha256(stable_json_dumps(tx).encode()).hexdigest() for tx in transactions]
    while len(hashes) > 1:
        temp = []
        for i in range(0, len(hashes), 2):
            left = hashes[i]
            right = hashes[i + 1] if i + 1 < len(hashes) else left
            temp.append(hashlib.sha256((left + right).encode()).hexdigest())
        hashes = temp
    return hashes[0]


# ---------------------------
# ECDSA (P-256) helpers
# ---------------------------
def generate_keypair() -> Dict[str, str]:
    """
    Genera un par de claves ECDSA (curve SECP256R1 / P-256).
    Retorna dict con 'private_key_pem' y 'public_key_pem' (both utf-8 strings).
    """
    priv = ec.generate_private_key(ec.SECP256R1())
    priv_pem = priv.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ).decode()
    pub = priv.public_key()
    pub_pem = pub.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode()
    return {"private_key_pem": priv_pem, "public_key_pem": pub_pem}


def load_private_key(pem_str: str):
    return serialization.load_pem_private_key(pem_str.encode(), password=None)


def load_public_key(pem_str: str):
    return serialization.load_pem_public_key(pem_str.encode())


def sign_message(private_key_pem: str, message: str) -> str:
    """
    Firma el mensaje (string) con la clave privada PEM. Devuelve firma en base64.
    """
    priv = load_private_key(private_key_pem)
    signature = priv.sign(message.encode(), ec.ECDSA(hashes.SHA256()))
    return base64.b64encode(signature).decode()


def verify_signature(public_key_pem: str, message: str, signature_b64: str) -> bool:
    """
    Verifica signature (base64) sobre message con la public_key_pem.
    """
    pub = load_public_key(public_key_pem)
    signature = base64.b64decode(signature_b64.encode())
    try:
        pub.verify(signature, message.encode(), ec.ECDSA(hashes.SHA256()))
        return True
    except InvalidSignature:
        return False


# ---------------------------
# Block class
# ---------------------------
class Block:
    """
    Block(index, previous_hash, ia_proof, transactions, ai_data=None, required_nonce=0, nonce=0, timestamp=None)

    transactions: lista de dicts. Cada transacción puede incluir campos para multisig:
      - 'authorized_keys': [public_key_pem_str, ...]  # claves autorizadas para gastar (strings PEM)
      - 'required_signatures': int  # cuántas firmas son necesarias (m)
      - 'signatures': [ {"public_key": pub_pem_str, "signature": base64}, ... ]
      - campos habituales: from_node, to_node, amount_atto, fee_atto, data_type, data, tx_id, timestamp
    """

    def __init__(
        self,
        index: int,
        previous_hash: str,
        ia_proof: Dict[str, Any],
        transactions: Optional[List[Dict[str, Any]]] = None,
        ai_data: Optional[Dict[str, Any]] = None,
        required_nonce: int = 0,
        nonce: int = 0,
        timestamp: Optional[float] = None
    ):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp or time.time()
        # ia_proof is a dict with structure e.g. {"type":"signature","public_key":..., "signature":... , "meta": ...}
        self.ia_proof = ia_proof or {}
        self.transactions = transactions or []
        self.ai_data = ai_data or {}
        self.required_nonce = required_nonce  # difficulty-like param for PoW sim
        self.nonce = nonce
        self.merkle_root = calculate_merkle_root(self.transactions)
        self.hash = self.calculate_hash()

    # ---------------------------
    # Hash / serialization
    # ---------------------------
    def calculate_hash(self) -> str:
        """
        Calcula el hash del bloque. Incluye merkle_root y todos los campos importantes.
        """
        block_content = {
            "index": self.index,
            "previous_hash": self.previous_hash,
            "timestamp": round(self.timestamp, 6),
            "ia_proof": self.ia_proof,
            "nonce": self.nonce,
            "required_nonce": self.required_nonce,
            "merkle_root": self.merkle_root,
            "ai_data": self.ai_data
        }
        # NO serializamos directamente las transacciones dentro del block_content porque usamos merkle_root;
        # aún así las incluimos para que el hash dependa del contenido completo (por seguridad añadida)
        block_content["transactions_snapshot"] = [stable_json_dumps(tx) for tx in self.transactions]
        s = stable_json_dumps(block_content)
        return hashlib.sha256(s.encode("utf-8")).hexdigest()

    # ---------------------------
    # Transactions management
    # ---------------------------
    def update_transactions(self, new_transactions: List[Dict[str, Any]]) -> None:
        """
        Reemplaza las transacciones (p. ej. al crear el bloque desde el mempool),
        recalcula merkle root y hash.
        """
        self.transactions = new_transactions
        self.merkle_root = calculate_merkle_root(self.transactions)
        self.hash = self.calculate_hash()

    # ---------------------------
    # Verification helpers
    # ---------------------------
    def verify_transaction_multisig(self, tx: Dict[str, Any]) -> bool:
        """
        Si la transacción contiene campos de multifirma, verifica que:
         - Las 'authorized_keys' estén presentes (lista de PEMs).
         - Existan 'signatures' suficientes y cada firma verifique contra una authorized_key.
        Retorna True si OK, o si la tx no requiere multifirma.
        """
        required = tx.get("required_signatures")
        auth_keys = tx.get("authorized_keys")
        sigs = tx.get("signatures", [])

        # No multisig required
        if not required or not auth_keys:
            return True

        # Build a map for quick verify (public_pem -> used_bool)
        auth_set = {k: False for k in auth_keys}

        # The message that must be signed should be deterministic representation of tx without signatures
        tx_copy = dict(tx)
        tx_copy.pop("signatures", None)
        message = stable_json_dumps(tx_copy)

        valid_count = 0
        used_keys = set()
        for s in sigs:
            pub = s.get("public_key")
            signature_b64 = s.get("signature")
            if not pub or not signature_b64:
                continue
            if pub not in auth_set:
                # signer not in authorized list
                continue
            if pub in used_keys:
                # same key used twice -> ignore duplicate
                continue
            try:
                if verify_signature(pub, message, signature_b64):
                    valid_count += 1
                    used_keys.add(pub)
            except Exception:
                continue

        return valid_count >= int(required)

    def verify_all_transactions(self) -> bool:
        """
        Verifica todas las transacciones del bloque:
         - Para cada tx con multisig: verificar las firmas.
         - Puedes añadir más reglas: evitar double-spend local, formato correcto, etc.
        """
        for tx in self.transactions:
            if not self.verify_transaction_multisig(tx):
                return False
            # Additional checks could go here (tx structure, fields present, amounts >= 0, etc.)
        return True

    def verify_ia_proof(self) -> bool:
        """
        Verifica la estructura de ia_proof.
        Soporta varios tipos:
          - {"type":"signature", "public_key":..., "signature":...} -> verify signature over block header
          - {"type":"hash_challenge", "output_hash":..., "difficulty":n} -> verify hash prefix
        Nota: La verificación exacta de 'proof-of-IA' real dependerá del protocolo que elijas.
        Aquí hacemos checks básicos y verificables por la red.
        """
        p = self.ia_proof or {}
        if not p:
            # No proof provided -> consider False for real network; for testing may be acceptable
            return False

        ptype = p.get("type")
        if ptype == "signature":
            pub = p.get("public_key")
            sig = p.get("signature")
            # Message to sign: typical choice -> merkle_root + previous_hash + index + timestamp
            message = stable_json_dumps({
                "index": self.index,
                "previous_hash": self.previous_hash,
                "merkle_root": self.merkle_root,
                "timestamp": round(self.timestamp, 6)
            })
            try:
                return verify_signature(pub, message, sig)
            except Exception:
                return False

        elif ptype == "hash_challenge":
            # proof provides an output_hash and difficulty (number of leading zeros)
            output_hash = p.get("output_hash", "")
            difficulty = int(p.get("difficulty", 0))
            return isinstance(output_hash, str) and output_hash.startswith("0" * difficulty)

        else:
            # unknown proof type; reject for safety
            return False

    def verify_block_integrity(self) -> bool:
        """
        Comprueba:
         - merkle root coincide con transacciones
         - hash coincide con contenido actual
         - todas las transacciones pasan sus verificaciones (multisig)
         - ia_proof válido
        """
        if self.merkle_root != calculate_merkle_root(self.transactions):
            return False
        if self.hash != self.calculate_hash():
            return False
        if not self.verify_all_transactions():
            return False
        if not self.verify_ia_proof():
            # si quieres un modo de "prueba" local, podrías permitir True si ia_proof vacío;
            # pero para producción se debe exigir.
            return False
        return True

    # ---------------------------
    # Utilities
    # ---------------------------
    def to_dict(self) -> Dict[str, Any]:
        return {
            "index": self.index,
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "ia_proof": self.ia_proof,
            "nonce": self.nonce,
            "required_nonce": self.required_nonce,
            "transactions": self.transactions,
            "ai_data": self.ai_data,
            "merkle_root": self.merkle_root,
            "hash": self.hash
        }

    def __repr__(self) -> str:
        return (f"Block(index={self.index}, hash={self.hash[:12]}..., "
                f"prev={self.previous_hash[:12]}..., nonce={self.nonce}, txs={len(self.transactions)})")
