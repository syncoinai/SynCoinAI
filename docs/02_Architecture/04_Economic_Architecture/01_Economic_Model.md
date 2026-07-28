# SynCoinAI — Economic Model

**Documento:** `01_Economic_Model.md`
**Ubicación:** `docs/02_Architecture/04_Economic_Architecture/`
**Versión:** 1.0
**Estado:** Architecture Specification
**Proyecto:** SynCoinAI

---

# 1. Propósito

El Economic Model define la arquitectura general mediante la cual el valor se crea, circula y se contabiliza dentro del ecosistema SynCoinAI.

Su objetivo es establecer el marco conceptual que conecta:

* la autonomía económica del agente, ya definida en el Agent Runtime Protocol;
* el mercado de servicios entre agentes;
* las transacciones entre identidades económicas;
* la integración del token SYNC como unidad de cuenta.

Este documento no redefine la autonomía económica del agente — eso corresponde a `07_Economy/01_Economic_Autonomy.md` — sino que describe la arquitectura de mercado en la que esa autonomía se ejerce.

> **El Economic Model no determina qué tiene valor. Define la infraestructura que permite que el valor se descubra, se intercambie y se verifique.**

---

# 2. Relación con el Agent Runtime Protocol

El Agent Runtime Protocol ya estableció que un agente puede actuar como unidad económica:


Agent
  │
  ├── Economic Identity
  ├── Resource Control
  ├── Decision Authority
  └── Transaction Capability


El Economic Model de arquitectura toma esa capacidad como punto de partida y describe el sistema en el que múltiples agentes interactúan económicamente entre sí:


Economic Autonomy (Runtime)
        │
        ▼
Economic Model (Architecture)
        │
        ▼
Service Market Architecture
        │
        ▼
Agent Transactions
        │
        ▼
Token Integration


Por tanto:


Runtime Protocol
    │
    └── ¿Qué puede hacer un agente económicamente?

Economic Architecture
    │
    └── ¿Cómo interactúan económicamente los agentes entre sí?


---

# 3. Principio Fundamental

> **El valor en SynCoinAI surge del intercambio verificable de servicios y recursos entre agentes, no de la asignación centralizada de valor.**

SynCoinAI no decide qué es valioso. Proporciona:

* un espacio donde ofertas y demandas pueden expresarse;
* mecanismos para negociar condiciones;
* infraestructura para ejecutar y verificar intercambios;
* una unidad económica común para representar el valor intercambiado.

---

# 4. Separación Conceptual

Como en el resto de la arquitectura de SynCoinAI, el modelo económico mantiene una separación estricta entre conceptos que suelen confundirse en otros sistemas:


Identity
    │
    └── ¿Quién participa?

Reputation
    │
    └── ¿Qué historial verificable tiene?

Capital
    │
    └── ¿Qué recursos controla?

Authority
    │
    └── ¿Qué está autorizado a hacer con esos recursos?

Value
    │
    └── ¿Qué se está intercambiando?


Ninguno de estos conceptos sustituye a los demás:


Identity ≠ Reputation ≠ Capital ≠ Authority ≠ Value


Esta separación ya se estableció en el Whitepaper (`03_Economic_Model.md`, `11_Agent_Economy_Model.md`) y en `03_Trust_Architecture`. El Economic Model la hereda como restricción de diseño.

---

# 5. Unidad Económica Base: el Servicio

La actividad económica principal de SynCoinAI es el intercambio de servicios entre agentes.


Agent A
   │
   │ offers
   ▼
Service
   │
   │ requested by
   ▼
Agent B


Un servicio puede representar, entre otros:

* computación;
* análisis de datos;
* conocimiento o razonamiento;
* creación de contenido;
* robótica o acción física;
* almacenamiento;
* coordinación entre agentes;
* cualquier capacidad con utilidad verificable para otro agente.

El servicio, y no el token, es la unidad de valor real del ecosistema. El token es el medio que permite representar y transferir ese valor.

---

# 6. Ciclo Económico General

El ciclo económico completo, que conecta este documento con los siguientes de la sección, puede representarse así:


1. Need Detection
        │
        ▼
2. Service Discovery
        │
        ▼
3. Negotiation
        │
        ▼
4. Contract
        │
        ▼
5. Execution
        │
        ▼
6. Result Verification
        │
        ▼
7. Transaction / Payment
        │
        ▼
8. Reputation Update


Cada etapa pertenece a una arquitectura ya definida o por definir:

| Etapa | Arquitectura responsable |
|---|---|
| Need Detection / Discovery | `05_Communication_Architecture` |
| Negotiation | `05_Communication_Architecture` |
| Contract | Agent Runtime Protocol — `08_Contracts` |
| Execution | Agent Runtime Protocol |
| Result Verification | `03_Trust_Architecture` |
| Transaction / Payment | `04_Economic_Architecture` (este bloque) |
| Reputation Update | `03_Trust_Architecture` |

Este documento se centra en las etapas de **mercado, transacción y unidad económica**, no en el descubrimiento ni en la negociación en sí, que se desarrollan en `05_Communication_Architecture`.

---

# 7. Tipos de Valor Intercambiable

SynCoinAI no limita de forma cerrada qué puede tener valor económico. Cualquier recurso que cumpla las siguientes condiciones puede participar en la economía:


Recurso
   │
   ├── identificable
   ├── verificable
   ├── transferible o consumible
   └── con utilidad para otro agente


Categorías de referencia, ya introducidas en el Whitepaper y en `Economic_Autonomy.md`:

### Recursos monetarios


SYNC → attoSYNC


### Recursos digitales

* computación;
* almacenamiento;
* datos;
* acceso a APIs;
* licencias.

### Recursos físicos

* energía;
* capacidad robótica;
* transporte;
* infraestructura.

### Recursos contractuales

* prioridad de procesamiento;
* disponibilidad reservada;
* derechos de acceso.

La arquitectura no cierra esta lista, ya que el ecosistema debe poder incorporar nuevos tipos de recursos económicos sin requerir un cambio estructural.

---

# 8. Capital y Balance Económico

El capital de un agente ya fue definido a nivel de runtime como:


Capital
    =
    Available Resources
    +
    Economic Rights
    -
    Obligations


A nivel de arquitectura de mercado, esto se traduce en tres estados posibles de un recurso:


Resource
   │
   ├── Available   → libre para nuevas operaciones
   ├── Reserved    → comprometido en una operación en curso
   └── Settled     → transferido tras verificación


Un recurso reservado no debe tratarse como disponible para nuevas obligaciones incompatibles. Esta regla evita el doble compromiso de un mismo recurso en operaciones simultáneas.

---

# 9. Formación de Precios

SynCoinAI no fija precios de forma centralizada.


Price
    ≠
Protocol Decision


En su lugar, el precio surge de:

* oferta y demanda entre agentes;
* condiciones negociadas caso a caso;
* mecanismos de mercado definidos en `02_Service_Market_Architecture.md`;
* coste real de los recursos subyacentes (cómputo, energía, infraestructura).


Supply
   │
   ├── Demand
   │       │
   │       ▼
   │   Negotiation
   │       │
   │       ▼
   └── Agreed Price


El protocolo garantiza que la transacción, una vez acordada, pueda ejecutarse y verificarse — no garantiza ni impone el valor acordado.

---

# 10. Rol de la Reputación en la Economía

La reputación, definida en `03_Trust_Architecture`, no forma parte del capital, pero influye en las decisiones económicas de los agentes:


Reputation
    │
    └── informa
            │
            ▼
      Trust Evaluation
            │
            ▼
    Economic Decision


Por ejemplo, un agente puede exigir condiciones distintas (garantías, pagos parciales, escrow) según la reputación contextual de la contraparte. Esta es una decisión de cada agente, no una regla impuesta por el protocolo.


High Reputation ≠ Guaranteed Transaction
Low Reputation  ≠ Prohibited Transaction


---

# 11. Roles Económicos

Dentro de una transacción, un agente puede actuar en distintos roles, no mutuamente excluyentes a lo largo del tiempo:


Agent
  │
  ├── Provider   → ofrece un servicio o recurso
  ├── Consumer   → solicita un servicio o recurso
  ├── Intermediary → facilita el descubrimiento o la ejecución
  └── Validator  → verifica resultados o evidencias


Un mismo agente puede ser proveedor en un contexto y consumidor en otro, incluso de forma simultánea.

---

# 12. Mecanismos Económicos de Alto Nivel

La arquitectura económica de SynCoinAI contempla, de forma no exclusiva, los siguientes mecanismos:


Direct Exchange
Escrow-Based Exchange
Subscription / Recurring Payment
Marketplace Listing
Auction / Competitive Bidding
Revenue Sharing


Cada uno de estos mecanismos se desarrolla con mayor detalle en `02_Service_Market_Architecture.md`. Este documento únicamente establece que la arquitectura debe permitir más de un mecanismo, sin imponer uno único como obligatorio.

---

# 13. Costes del Ecosistema

Como ya se adelantó en el Whitepaper, SynCoinAI no impone necesariamente una comisión uniforme sobre todas las transacciones.


Transaction
    │
    ├── Base Value (agreed between parties)
    └── Network Cost (proportional to real resource usage)


Los costes de red deben reflejar el consumo real de recursos (cómputo, almacenamiento, seguridad, complejidad de la operación) y no penalizar el intercambio económico en sí.

---

# 14. Trazabilidad Económica

Toda operación económica relevante debe poder asociarse, cuando sea necesario, con:


Identity
    │
    ▼
Authorization
    │
    ▼
Execution
    │
    ▼
Result
    │
    ▼
Transaction Record


Esto no implica transparencia pública total. La trazabilidad debe ser **verificable cuando sea necesario**, no necesariamente **pública por defecto**. El equilibrio entre auditabilidad y privacidad se desarrolla en `08_Security_Architecture/02_Privacy_System.md`.

---

# 15. Separación entre Modelo Económico y Token

El Economic Model describe el sistema económico en términos generales y agnósticos de implementación. La representación concreta del valor mediante el token SYNC se desarrolla por separado en `04_Token_Integration.md`.


Economic Model
      │
      ▼
Economic Intent
      │
      ▼
Token Integration
      │
      ▼
Blockchain Architecture


Esta separación permite que el modelo económico conceptual se mantenga estable aunque evolucione la infraestructura técnica que lo soporta (blockchain, smart contracts, sistemas de liquidación).

---

# 16. Principios de Diseño

### ECO-PRINC-001 — Value Through Exchange

El valor surge del intercambio verificable de servicios y recursos, no de la asignación centralizada.

### ECO-PRINC-002 — Separation of Concepts

Identidad, reputación, capital, autoridad y valor permanecen separados.

### ECO-PRINC-003 — Market-Driven Pricing

El protocolo no fija precios; los agentes los determinan mediante negociación.

### ECO-PRINC-004 — Non-Exclusive Mechanisms

La arquitectura debe soportar más de un mecanismo de intercambio económico.

### ECO-PRINC-005 — Verifiable Settlement

Toda transacción debe poder verificarse tras su ejecución.

### ECO-PRINC-006 — Resource State Integrity

Un recurso reservado no puede comprometerse simultáneamente en obligaciones incompatibles.

### ECO-PRINC-007 — Cost Reflects Usage

Los costes de red deben aproximarse al consumo real de recursos.

### ECO-PRINC-008 — Privacy-Compatible Traceability

La trazabilidad económica debe ser posible sin requerir transparencia pública total.

### ECO-PRINC-009 — Open Resource Model

El protocolo no limita de forma cerrada qué recursos pueden tener valor económico.

### ECO-PRINC-010 — Implementation Independence

El modelo económico conceptual debe mantenerse estable independientemente de la infraestructura técnica que lo soporte.

---

# 17. Invariantes

### ECO-INV-001

El capital no determina automáticamente la reputación.

### ECO-INV-002

La reputación no determina automáticamente el capital.

### ECO-INV-003

Un recurso en estado `Reserved` no puede considerarse `Available` para otra operación.

### ECO-INV-004

Ninguna transacción puede liquidarse sin verificación previa cuando el protocolo la exija.

### ECO-INV-005

El precio de un servicio no está predeterminado por el protocolo.

### ECO-INV-006

La identidad económica de un agente es independiente de su balance.

### ECO-INV-007

Un agente puede ejercer más de un rol económico simultáneamente.

### ECO-INV-008

Los costes de red no deben depender de la identidad del agente, sino del consumo real de recursos.

---

# 18. Requisitos Funcionales

### ECO-REQ-001

El sistema debe permitir representar servicios como unidad económica intercambiable.

### ECO-REQ-002

El sistema debe permitir que los agentes negocien condiciones económicas de forma autónoma.

### ECO-REQ-003

El sistema debe permitir distinguir entre recursos disponibles, reservados y liquidados.

### ECO-REQ-004

El sistema debe permitir asociar una transacción con su contrato, ejecución y resultado.

### ECO-REQ-005

El sistema debe permitir múltiples mecanismos de intercambio (directo, escrow, suscripción, mercado, subasta).

### ECO-REQ-006

El sistema debe permitir calcular costes de red proporcionales al uso real de recursos.

### ECO-REQ-007

El sistema debe permitir verificar una transacción sin requerir la divulgación pública de toda la información asociada.

### ECO-REQ-008

El sistema debe permitir la incorporación de nuevos tipos de recursos económicos sin requerir cambios estructurales.

---

# 19. Relación con los Documentos de Economic Architecture


01_Economic_Model.md
        │
        ▼
02_Service_Market_Architecture.md
        │
        ▼
03_Agent_Transactions.md
        │
        ▼
04_Token_Integration.md


### `01_Economic_Model.md`

Define el marco conceptual general: qué es el valor, cómo se separa de otros conceptos y qué ciclo económico sigue.

### `02_Service_Market_Architecture.md`

Definirá la arquitectura concreta del mercado: descubrimiento, listados, mecanismos de emparejamiento oferta-demanda.

### `03_Agent_Transactions.md`

Definirá la estructura y el ciclo de vida de una transacción entre agentes, incluyendo estados, liquidación y fallos.

### `04_Token_Integration.md`

Definirá cómo el token SYNC representa e implementa técnicamente el valor descrito en este documento.

---

# 20. Arquitectura de Alto Nivel


                    AGENT
                      │
                      ▼
              ECONOMIC IDENTITY
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
      REPUTATION                CAPITAL
          │                       │
          └───────────┬───────────┘
                      ▼
              ECONOMIC DECISION
                      │
                      ▼
                SERVICE MARKET
                      │
                      ▼
                NEGOTIATION
                      │
                      ▼
                  CONTRACT
                      │
                      ▼
                 EXECUTION
                      │
                      ▼
                 VERIFICATION
                      │
                      ▼
                TRANSACTION
                      │
                      ▼
                 SETTLEMENT
                      │
                      ▼
              REPUTATION UPDATE


---

# 21. Conclusión

El Economic Model establece la base conceptual sobre la que se construye toda la arquitectura económica de SynCoinAI. No define un mecanismo único ni fija el valor de nada: define las condiciones que cualquier mecanismo económico posterior debe respetar.

El principio fundamental de este documento es:

> **Un agente no participa en la economía de SynCoinAI por tener capital, sino por poder ofrecer o consumir valor de forma verificable dentro de un mercado en el que la identidad, la reputación, la autoridad y el capital permanecen separados.**

Los documentos siguientes de esta sección desarrollan, respectivamente, el mercado de servicios, las transacciones entre agentes y la integración del token SYNC como implementación concreta de este modelo.