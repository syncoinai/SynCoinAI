# SynCoinAI — Token Integration

**Documento:** `04_Token_Integration.md`
**Ubicación:** `docs/02_Architecture/04_Economic_Architecture/`
**Versión:** 1.0
**Estado:** Architecture Specification
**Proyecto:** SynCoinAI

---

# 1. Propósito

El documento Token Integration define cómo el token SYNC implementa, a nivel de arquitectura, la unidad de valor descrita en `01_Economic_Model.md` y utilizada por el mercado (`02_Service_Market_Architecture.md`) y las transacciones (`03_Agent_Transactions.md`).

Este documento no define:

* el mecanismo de consenso ni la infraestructura distribuida que registra el token — eso corresponde a `06_Blockchain_Architecture`, aún pendiente;
* las operaciones de wallet mediante las que un agente gestiona el token — ya definidas en `07_Economy/02_Wallet_Operations.md`;
* la política de gobernanza sobre cambios futuros del protocolo — corresponde a `15_Governance` (Agent Runtime Protocol) y a la futura `06_Blockchain_Architecture/04_Governance_Architecture.md`.


Economic Model
        │
        └── ¿Qué es el valor?

Token Integration (este documento)
        │
        └── ¿Cómo se representa e implementa ese valor?

Blockchain Architecture (pendiente)
        │
        └── ¿Sobre qué infraestructura distribuida existe esa representación?


> **El token no crea valor. Representa, transporta y liquida el valor que ya se definió a nivel de mercado y transacción.**

---

# 2. Relación con el Whitepaper

Este documento desarrolla, a nivel de arquitectura, lo ya establecido en `01_Whitepaper/11_Agent_Economy_Model.md` (secciones 21 a 30): función económica del token, política monetaria, reserva inicial, capital inicial de agentes, valor, estabilidad, distribución, concentración de capital y costes del ecosistema. No redefine esas decisiones; las traduce en componentes arquitectónicos.

---

# 3. Unidad Económica


SYNC
  │
  └── attoSYNC (unidad mínima)


El token SYNC es la unidad de cuenta común del ecosistema. No es la única forma de valor reconocida por el protocolo (`01_Economic_Model.md`, sección 7 reconoce recursos digitales, físicos y contractuales), pero es el medio preferente de liquidación entre agentes cuando no se acuerda otro mecanismo.


Value (service, resource)
        │
        ▼
   Priced in SYNC
        │
        ▼
   Settled in SYNC


---

# 4. Funciones del Token

Coherente con el Whitepaper, el token cumple tres funciones arquitectónicas:


Medium of Exchange
    │
    └── liquidar transacciones entre agentes

Operational Resource
    │
    └── pagar acceso a cómputo, infraestructura, servicios

Store of Value
    │
    └── permitir acumulación económica para evolución futura del agente


La prioridad arquitectónica, según el Whitepaper, es la primera función: moneda de intercambio para una economía de agentes.

---

# 5. Relación entre Token y Transacción

Cada transacción definida en `03_Agent_Transactions.md` puede requerir uno o más movimientos de token en su fase de `Settlement`:


Transaction
    │
    ├── State: Verified
    │
    ▼
Settlement
    │
    ▼
Token Transfer(s)
    │
    ▼
State: Settled


Una transacción puede involucrar múltiples transferencias de token (por ejemplo, pago al proveedor y comisión de red), pero todas deben quedar asociadas a la misma referencia de transacción para mantener trazabilidad.

---

# 6. Wallet como Interfaz del Token

El token no se gestiona directamente por el agente, sino a través de la wallet, ya definida en `Wallet_Operations.md`:


Agent
    │
    ▼
Wallet
    │
    ▼
SYNC Balance


Este documento no repite el modelo de wallet; únicamente establece que toda tenencia y movimiento de SYNC debe pasar por ese mecanismo, sin rutas alternativas que eludan las políticas de autorización ya definidas en `04_Credentials` y `07_Economy`.

---

# 7. Reserva Inicial y Capital de Agentes

Siguiendo el modelo híbrido descrito en el Whitepaper (reserva inicial + emisión adaptativa), la arquitectura reconoce dos orígenes posibles de SYNC en manos de un agente:


Initial Allocation
    │
    └── asignación inicial para participar (no permanente, no privilegio indefinido)

Earned Balance
    │
    └── generado mediante actividad económica verificable (servicios, transacciones liquidadas)



Initial Allocation ≠ Ongoing Entitlement


El crecimiento posterior del balance de un agente depende de su actividad económica, no de la asignación inicial.

---

# 8. Política Monetaria a Nivel de Arquitectura

Este documento no fija los parámetros exactos de la política monetaria (cantidades, tasas de emisión), que corresponden a una decisión de gobernanza y a `06_Blockchain_Architecture`. Sí establece el marco arquitectónico que esa política debe respetar:


Monetary Policy
    │
    ├── Foundational Phase   → gestión inicial (Fundación, desarrolladores)
    └── Automated Phase      → reglas verificables, progresivamente autónomas



Foundational Phase → Automated Phase


La transición entre fases no está definida en este documento; se desarrollará junto con `06_Blockchain_Architecture/04_Governance_Architecture.md` y `15_Governance` del Agent Runtime Protocol.

---

# 9. Costes de Red y Token

Los costes de red descritos en `01_Economic_Model.md` (sección 13) y `02_Service_Market_Architecture.md` (sección 10) se liquidan en SYNC:


Network Cost
    │
    └── denominado en SYNC
            │
            └── proporcional al consumo real de recursos, no a comisiones fijas uniformes


Este documento no fija el importe de esos costes; establece que deben expresarse en la unidad de cuenta común (SYNC) para ser comparables entre distintos tipos de operación.

---

# 10. Separación entre Capital, Reputación e Identidad (aplicada al Token)

Reiterando el principio ya establecido en `01_Economic_Model.md` y `03_Trust_Architecture`, la posesión de SYNC:


SYNC Balance
    ≠
Reputation

SYNC Balance
    ≠
Identity

SYNC Balance
    ≠
Authority


Un agente con un balance elevado de SYNC no obtiene automáticamente mayor reputación, mayor autoridad ni mayor peso en la gobernanza. Esta restricción es la traducción directa, a nivel de token, de `28. Concentración de capital` del Whitepaper.

---

# 11. Token y Creación de Nuevos Agentes

Como ya establece el Whitepaper (`11_Agent_Economy_Model.md`, secciones 7 y 8), un agente puede financiar la creación de otro agente mediante capital inicial en SYNC, sin que ello implique propiedad ni control permanente:


Creator Agent
    │
    │ provides initial SYNC
    ▼
New Agent
    │
    └── identidad, reputación e historial propios desde el origen


El token puede transferirse como capital inicial; la identidad y la reputación, no.

---

# 12. Estabilidad y Formación de Valor

Consistente con el Whitepaper (`25. Valor de SynCoinAI`, `26. Estabilidad económica`), este documento no define un mecanismo de estabilización artificial de precios. El valor del token surge de:


Network of Agents
        +
Real Economic Activity
        +
Protocol Trust
        =
Token Value


El protocolo mantiene una unidad económica confiable (mediante las reglas de esta arquitectura); no controla el precio de los recursos que se intercambian con esa unidad.

---

# 13. Principios de Diseño

### TOK-PRINC-001 — Token Represents Value, Does Not Create It

El token es el medio de representación del valor, no su origen.

### TOK-PRINC-002 — Wallet-Mediated Access

Toda tenencia y movimiento de SYNC debe pasar por la wallet y sus mecanismos de autorización.

### TOK-PRINC-003 — Non-Exclusive Value Unit

El token es el medio de liquidación preferente, no el único recurso económico reconocido por el protocolo.

### TOK-PRINC-004 — Initial Allocation Is Not Permanent Privilege

Una asignación inicial de SYNC no debe traducirse en ventaja estructural permanente.

### TOK-PRINC-005 — Capital-Authority Separation

El balance de SYNC no otorga automáticamente reputación, identidad ni autoridad de gobernanza.

### TOK-PRINC-006 — Cost Denomination Consistency

Los costes de red deben expresarse en SYNC para mantener comparabilidad.

### TOK-PRINC-007 — Market-Determined Value

El valor del token surge de la actividad económica real y la confianza en el protocolo, no de mecanismos artificiales de fijación de precio.

### TOK-PRINC-008 — Implementation Deferred to Blockchain Architecture

Los parámetros técnicos de emisión, consenso y registro se definen en `06_Blockchain_Architecture`, no en este documento.

---

# 14. Invariantes

### TOK-INV-001

Un balance elevado de SYNC no otorga automáticamente mayor reputación.

### TOK-INV-002

Un balance elevado de SYNC no otorga automáticamente mayor autoridad de gobernanza.

### TOK-INV-003

Toda transferencia de SYNC debe asociarse a una transacción trazable o a una asignación inicial explícita.

### TOK-INV-004

La creación de un nuevo agente financiada en SYNC no otorga control permanente sobre ese agente.

### TOK-INV-005

Los costes de red no pueden depender de la identidad del agente que los origina.

---

# 15. Requisitos Funcionales

### TOK-REQ-001

El sistema debe permitir representar balances de SYNC y attoSYNC asociados a una wallet.

### TOK-REQ-002

El sistema debe permitir denominar en SYNC el valor acordado en una transacción.

### TOK-REQ-003

El sistema debe permitir distinguir entre asignación inicial y balance generado por actividad económica.

### TOK-REQ-004

El sistema debe permitir calcular y liquidar costes de red en SYNC de forma proporcional al consumo real.

### TOK-REQ-005

El sistema debe permitir que un agente transfiera SYNC como capital inicial a un nuevo agente sin adquirir control sobre su identidad.

### TOK-REQ-006

El sistema debe registrar toda transferencia de SYNC de forma trazable hacia su transacción de origen.

---

# 16. Relación con los Documentos de Economic Architecture


01_Economic_Model.md
        │
        ▼
02_Service_Market_Architecture.md
        │
        ▼
03_Agent_Transactions.md
        │
        ▼
04_Token_Integration.md   ← este documento


Con este documento se completa la sección `04_Economic_Architecture`. La implementación técnica concreta del token (blockchain, consenso, smart contracts) se desarrollará en `06_Blockchain_Architecture`, actualmente pendiente.

---

# 17. Arquitectura de Alto Nivel


                 ECONOMIC MODEL
                       │
                       ▼
                SERVICE MARKET
                       │
                       ▼
                AGENT TRANSACTION
                       │
                       ▼
                  SETTLEMENT
                       │
                       ▼
                 TOKEN TRANSFER
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
      PROVIDER      NETWORK      RESERVES
       WALLET         COST
                       │
                       ▼
              REPUTATION EVIDENCE


---

# 18. Conclusión

Token Integration cierra el bloque de Economic Architecture conectando el modelo conceptual de valor con su unidad de representación económica, sin adelantar decisiones que corresponden a la infraestructura blockchain aún pendiente de documentar.

El principio fundamental de este documento es:

> **El token SYNC es el instrumento que hace transferible el valor ya definido por el mercado y las transacciones; no es, por sí mismo, la fuente de reputación, identidad ni autoridad dentro del ecosistema.**

Con `01_Economic_Model.md`, `02_Service_Market_Architecture.md`, `03_Agent_Transactions.md` y `04_Token_Integration.md`, la sección `04_Economic_Architecture` queda completa. El siguiente bloque pendiente en el índice maestro es `05_Communication_Architecture`.