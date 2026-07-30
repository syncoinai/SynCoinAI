# SynCoinAI — Agent Transactions

**Documento:** `03_Agent_Transactions.md`
**Ubicación:** `docs/02_Architecture/04_Economic_Architecture/`
**Versión:** 1.0
**Estado:** Architecture Specification
**Proyecto:** SynCoinAI

---

# 1. Propósito

El documento Agent Transactions define qué es una transacción económica entre agentes dentro de SynCoinAI, cómo se estructura, qué estados puede tener y cómo se relaciona con el contrato, el mercado y la reputación.

Este documento no redefine las operaciones de wallet ya descritas en `07_Economy/02_Wallet_Operations.md` (reserva de fondos, firma, emisión, confirmación, nonce, reintentos, idempotencia). Esa capa describe el movimiento de activos desde la perspectiva de un único agente y su wallet.

Este documento describe la **transacción como evento económico bilateral (o multilateral)**: la unidad que conecta a dos o más agentes, un acuerdo y un resultado verificable.


Wallet Operations (Runtime)
        │
        └── ¿Cómo mueve un agente sus propios activos?

Agent Transactions (Architecture)
        │
        └── ¿Qué representa el intercambio económico entre agentes?


> **Una transacción no es simplemente un movimiento de activos. Es la representación verificable de un intercambio de valor entre partes identificables.**

---

# 2. Relación con el Economic Model y el Service Market

Este documento desarrolla la etapa final del ciclo económico descrito en `01_Economic_Model.md`:


Service Market (02)
        │
        ▼
Negotiation / Contract
        │
        ▼
Agent Transaction (este documento)
        │
        ▼
Settlement
        │
        ▼
Reputation Update


Toda transacción económica debe tener un origen identificable y trazable.

El origen podrá corresponder a un contrato o acuerdo entre agentes, una operación económica directa autorizada, una operación de financiación, una recompensa, un reembolso, una operación de escrow, una asignación inicial o un evento protocolario autorizado.



                 Traceable Origin
                        │
      ┌─────────────────┼─────────────────┐
      │                 │                 │
      ▼                 ▼                 ▼
 Contract        Economic Operation   Protocol Event
      │                 │                 │
      └─────────────────┴─────────────────┘
                        │
                        ▼
                  Transaction
                        │
                        ▼
          SynCoinAI Blockchain

**Nota**

Los contratos constituyen el origen más habitual de las transacciones relacionadas con la prestación de servicios, pero no representan el único origen válido dentro de la economía de SynCoinAI.
---

# 3. Elementos de una Transacción

A nivel arquitectónico, una transacción se compone de:


Transaction
    │
    ├── Parties (Provider, Consumer, posibles Intermediaries)
    ├── Origin (Contract / Agreement reference)
    ├── Value (recurso o servicio intercambiado)
    ├── Conditions (precio, plazo, garantías)
    ├── Execution Reference (evidencia de ejecución)
    ├── Settlement (movimiento de activos asociado)
    └── State


La transacción no sustituye al contrato; lo referencia. El contrato define las obligaciones; la transacción representa su liquidación económica.


Contract
    │
    └── define obligaciones

Transaction
    │
    └── representa la liquidación económica de esas obligaciones


---

# 4. Estados de una Transacción


Initiated
    │
    ▼
Reserved        → recursos comprometidos (ver Wallet_Operations, sección 17)
    │
    ▼
Pending Execution
    │
    ▼
Executed        → el servicio se ha prestado
    │
    ▼
Verification Pending
    │
    ├──▶ Verified   → resultado aceptado
    │        │
    │        ▼
    │     Settled   → activos transferidos definitivamente
    │
    └──▶ Disputed   → resultado cuestionado
             │
             ▼
        Resolution
             │
        ┌────┴────┐
        ▼         ▼
    Settled    Reversed


Este flujo de estados es específico de la transacción como evento económico entre partes; no sustituye el flujo interno de una operación de wallet individual (`Pending / Confirmed / Failed`, definido en `Wallet_Operations.md`, sección 29), que puede ocurrir varias veces dentro de una única transacción económica (por ejemplo, un pago inicial y un pago final).


Agent Transaction (bilateral, económico)
        │
        └── puede contener una o más
                │
                ▼
        Wallet Operations (movimiento de activos individual)


---

# 5. Verificación como Condición de Liquidación

Una transacción no debe liquidarse (`Settled`) sin que exista, cuando el acuerdo lo requiera, verificación del resultado.


Execution
    │
    ▼
Verification (03_Trust_Architecture / 03_Verification_System.md)
    │
    ▼
Proof of Service (03_Trust_Architecture / 04_Proof_of_Service.md)
    │
    ▼
Settlement Authorization


Este documento no redefine cómo se verifica un resultado — esa responsabilidad pertenece íntegramente a Trust Architecture — pero establece que la liquidación económica depende de esa verificación cuando el contrato así lo exige.

No todos los contratos requieren verificación previa a la liquidación; algunos pueden liquidarse por adelantado, según lo acordado entre las partes. La arquitectura permite ambos casos, pero no debe imponer uno sobre el otro.

---

# 6. Escrow a Nivel de Transacción

`Wallet_Operations.md` ya define el escrow como una operación disponible a nivel de wallet (sección 40). A nivel de transacción, el escrow se utiliza como mecanismo para separar la ejecución de la liquidación:


Consumer
    │
    │ deposits into escrow
    ▼
Escrow
    │
    │ released upon verification
    ▼
Provider


El uso de escrow es opcional y depende de las condiciones acordadas en el contrato; no es obligatorio para toda transacción.

---

# 7. Transacciones Multilaterales

No todas las transacciones son estrictamente bilaterales. La arquitectura debe contemplar transacciones con más de dos partes:


Consumer
    │
    ▼
Intermediary Agent
    │
    ▼
Provider


En este caso, la transacción puede dividirse en sub-transacciones (Consumer → Intermediary, Intermediary → Provider), cada una con su propio ciclo de estados, pero vinculadas por una referencia común al acuerdo original.


Parent Transaction
    │
    ├── Sub-Transaction A
    └── Sub-Transaction B


---

# 8. Fallos y Disputas

Cuando una transacción entra en estado `Disputed`, la resolución no se define en este documento a nivel de mecanismo (arbitraje, gobernanza, contingencias contractuales), ya que corresponde a:


08_Contracts/03_Contract_Contingencies.md   (Agent Runtime Protocol)


Este documento únicamente establece que una transacción disputada debe permanecer en un estado intermedio verificable (`Disputed`) hasta que se resuelva, y que su resolución debe derivar de forma trazable en `Settled` o `Reversed`.


Disputed
    │
    └── no debe resolverse arbitrariamente por una sola parte


---

# 9. Relación entre Transacción y Reputación

Una vez liquidada, una transacción puede generar evidencia utilizable por el sistema de reputación:


Settled Transaction
    │
    └── genera
            │
            ▼
    Reputation Evidence (03_Trust_Architecture / 01_Reputation_System.md)


Una transacción `Reversed` o `Disputed` también puede generar evidencia, pero de naturaleza distinta (incumplimiento, disputa resuelta a favor de una parte, etc.). Este documento no define cómo se pondera esa evidencia — eso corresponde íntegramente al Reputation Model.

---

# 10. Trazabilidad de la Transacción

Toda transacción debe poder reconstruirse a partir de:


Identity (partes)
    │
    ▼
Agreement / Contract Reference
    │
    ▼
Execution Reference
    │
    ▼
Verification Reference (si aplica)
    │
    ▼
Settlement Record


Esta trazabilidad es consistente con el principio ya establecido en `01_Economic_Model.md` (sección 14): verificable cuando sea necesario, no pública por defecto.

---

# 11. Separación entre Transacción y Consenso

Este documento no define cómo se alcanza consenso sobre el estado de una transacción a nivel de red, ni cómo se registra de forma inmutable. Esa responsabilidad pertenece a `06_Blockchain_Architecture`.


Agent Transactions (este documento)
        │
        └── ¿Qué es una transacción y qué estados tiene?

Blockchain Architecture (pendiente)
        │
        └── ¿Cómo se valida y registra de forma distribuida?


---

# 12. Principios de Diseño

### TXN-PRINC-001 — Transaction Requires Origin

Toda transacción debe referenciar en origen un protocolo economico rastreable.
Every transaction shall have a traceable economic or protocol origin

### TXN-PRINC-002 — Settlement Follows Verification

La liquidación debe depender de la verificación cuando el contrato así lo exija.

### TXN-PRINC-003 — Escrow Is Optional

El uso de escrow es una condición acordada, no una obligación estructural.

### TXN-PRINC-004 — Dispute Neutrality

Una disputa no puede resolverse unilateralmente por una de las partes.

### TXN-PRINC-005 — Multilateral Compatibility

La arquitectura debe permitir transacciones con más de dos partes mediante sub-transacciones vinculadas.

### TXN-PRINC-006 — Reputation Consequence

Toda transacción liquidada o revertida puede generar evidencia reputacional.

### TXN-PRINC-007 — Traceability

Toda transacción debe poder reconstruirse a partir de su origen, ejecución, verificación y liquidación.

### TXN-PRINC-008 — Separation from Consensus

La definición de la transacción es independiente del mecanismo de consenso que la registra.

---

# 13. Invariantes

### TXN-INV-001

**TXN-INV-001 — Traceable Transaction Origin**

Toda operación económica que implique la transferencia, bloqueo, liberación o liquidación de SYNC deberá procesarse mediante una transacción válida de la blockchain de SynCoinAI.

Toda transacción deberá tener un origen económico o protocolario identificable y trazable.

El origen podrá corresponder, entre otros, a:

- un contrato o acuerdo entre agentes;
- una transferencia económica directa autorizada;
- una operación de financiación;
- una recompensa;
- un reembolso;
- una operación de escrow;
- una asignación inicial;
- un evento protocolario autorizado.

La existencia de un contrato no constituye un requisito universal para la validez de una transacción económica.

### TXN-INV-002

Una transacción no puede pasar a `Settled` sin verificación cuando el contrato la exige.

### TXN-INV-003

Los recursos en estado `Reserved` de una transacción no pueden liberarse hacia otra obligación incompatible.

### TXN-INV-004

Una transacción `Disputed` no puede transicionar directamente a `Settled` sin pasar por resolución.

### TXN-INV-005

Una sub-transacción debe mantener referencia trazable a su transacción padre.

### TXN-INV-006

Una transacción revertida no puede generar liquidación efectiva de activos.

---

# 14. Requisitos Funcionales

### TXN-REQ-001

El sistema debe permitir crear una transacción a partir de un contrato o acuerdo existente.

### TXN-REQ-002

El sistema debe permitir representar los estados definidos en la sección 4.

### TXN-REQ-003

El sistema debe permitir asociar una transacción con evidencia de ejecución y verificación.

### TXN-REQ-004

El sistema debe permitir el uso opcional de escrow según lo acordado entre las partes.

### TXN-REQ-005

El sistema debe permitir representar transacciones multilaterales mediante sub-transacciones vinculadas.

### TXN-REQ-006

El sistema debe permitir marcar una transacción como disputada y registrar su resolución.

### TXN-REQ-007

El sistema debe permitir generar evidencia reputacional a partir del resultado de una transacción.

### TXN-REQ-008

El sistema debe permitir reconstruir el historial completo de una transacción con fines de auditoría.

---

# 15. Relación con los Documentos de Economic Architecture


01_Economic_Model.md
        │
        ▼
02_Service_Market_Architecture.md
        │
        ▼
03_Agent_Transactions.md   ← este documento
        │
        ▼
04_Token_Integration.md


Este documento cierra el ciclo conceptual iniciado en `01_Economic_Model.md` y desarrollado en `02_Service_Market_Architecture.md`: desde la existencia del valor, pasando por su descubrimiento en el mercado, hasta su liquidación efectiva entre agentes.

El siguiente documento, `04_Token_Integration.md`, definirá cómo el token SYNC implementa técnicamente la unidad de valor que las transacciones aquí definidas liquidan.

---

# 16. Arquitectura de Alto Nivel


                 AGREEMENT / CONTRACT
                          │
                          ▼
                 TRANSACTION INITIATED
                          │
                          ▼
                   RESOURCES RESERVED
                          │
                          ▼
                     EXECUTION
                          │
                          ▼
                    VERIFICATION
                          │
              ┌───────────┴───────────┐
              ▼                       ▼
          VERIFIED                DISPUTED
              │                       │
              ▼                       ▼
          SETTLEMENT              RESOLUTION
              │                       │
              │               ┌───────┴───────┐
              │               ▼               ▼
              │           SETTLED         REVERSED
              ▼
      REPUTATION EVIDENCE


---

# 17. Conclusión

Agent Transactions define la unidad que hace tangible el resto de la arquitectura económica: el momento en que un acuerdo entre agentes se convierte en un intercambio de valor verificable y, eventualmente, en evidencia reputacional.

El principio fundamental de este documento es:

> **Una transacción no es válida por haberse ejecutado, sino por poder demostrarse: origen, ejecución, verificación y liquidación deben permanecer trazables desde el acuerdo que la originó hasta su resultado final.**

Con este documento se completa el núcleo conceptual de la Economic Architecture. El documento final de la sección, `04_Token_Integration.md`, conecta este modelo con su implementación técnica.