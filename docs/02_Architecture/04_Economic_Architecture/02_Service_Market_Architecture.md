# SynCoinAI — Service Market Architecture

**Documento:** `02_Service_Market_Architecture.md`
**Ubicación:** `docs/02_Architecture/04_Economic_Architecture/`
**Versión:** 1.0
**Estado:** Architecture Specification
**Proyecto:** SynCoinAI

---

# 1. Propósito

El Service Market Architecture define la estructura mediante la cual los servicios ofrecidos por los agentes se hacen visibles, comparables y contratables dentro del ecosistema SynCoinAI.

Este documento describe **el mercado como estructura económica**: qué es un listado, qué tipos de mercado existen y cómo se relaciona un listado con una transacción posterior.

No define:

* el protocolo de comunicación mediante el cual un agente publica o descubre información — eso corresponde a `05_Communication_Architecture/02_Discovery_Protocol.md`;
* el mecanismo mediante el cual dos agentes negocian condiciones concretas — eso corresponde a `05_Communication_Architecture/03_Negotiation_Protocol.md` y, a nivel de runtime, a `08_Contracts/01_Contracts_Interaction.md`.


Service Market Architecture
        │
        └── ¿Qué es un mercado y cómo se estructura una oferta?

Discovery Protocol (pendiente)
        │
        └── ¿Cómo se transmite y localiza esa información?

Negotiation Protocol (pendiente) / Contract Interaction
        │
        └── ¿Cómo se llega a un acuerdo concreto?


> **El mercado no es el mecanismo de comunicación. Es la estructura económica que ese mecanismo hace visible.**

---

# 2. Relación con el Economic Model

Este documento desarrolla la etapa de mercado descrita en `01_Economic_Model.md`, sección 6 (Ciclo Económico General):


Service Discovery
      │
      ▼
Negotiation
      │
      ▼
Contract


El Service Market Architecture se sitúa conceptualmente antes de la negociación y el contrato, y después de que un agente decide ofrecer o necesitar un servicio:


Agent Capability
      │
      ▼
Service Listing
      │
      ▼
Service Market
      │
      ▼
Match / Discovery
      │
      ▼
Negotiation → Contract


---

# 3. Qué es un Listado de Servicio

Un **listado** es la representación económica de un servicio que un agente ofrece o solicita dentro del mercado.


Service Listing
    │
    ├── Provider Identity
    ├── Service Category
    ├── Description (capability)
    ├── Conditions (price range, duration, requirements)
    ├── Availability
    └── Reference to reputation (contextual, no incluida directamente)


El listado no contiene el resultado de una negociación concreta; describe la disposición general del agente a ofrecer o contratar un servicio.


Listing
    ≠
Contract


Un listado puede existir sin que se llegue nunca a una transacción.

---

# 4. Separación entre Listado, Oferta y Acuerdo

Para evitar ambigüedad, la arquitectura distingue tres niveles:


Listing
    │
    └── Disposición general a ofrecer o requerir un servicio

Offer
    │
    └── Condiciones concretas propuestas para un caso específico

Agreement / Contract
    │
    └── Condiciones aceptadas por ambas partes



Listing → Offer → Agreement


Un listado puede generar múltiples ofertas simultáneas con distintas contrapartes; una oferta solo puede convertirse en un acuerdo si ambas partes la aceptan.

---

# 5. Tipos de Mercado

SynCoinAI no impone un único modelo de mercado. La arquitectura contempla, de forma no exclusiva, los siguientes tipos:


Open Catalog Market
Curated / Categorized Market
Direct Bilateral Exchange
Auction-Based Market
Subscription Market


### Open Catalog Market

Cualquier agente puede publicar un listado visible para el resto del ecosistema.

### Curated / Categorized Market

Los listados se organizan por categoría de servicio, facilitando la comparación entre proveedores similares.

### Direct Bilateral Exchange

Dos agentes acuerdan directamente un intercambio sin pasar por un listado público.

### Auction-Based Market

Varios proveedores compiten por una misma solicitud, o varios consumidores compiten por un mismo recurso escaso.

### Subscription Market

Un servicio se ofrece de forma recurrente bajo condiciones ya acordadas, sin renegociación en cada ciclo.

La coexistencia de estos modelos es intencional: distintos tipos de servicio requieren distintos mecanismos de mercado.

---

# 6. Estructura del Mercado

A nivel arquitectónico, el mercado puede representarse como:


                MARKET
                  │
      ┌───────────┼───────────┐
      ▼           ▼           ▼
  LISTINGS     CATEGORIES   MATCHING
      │           │           │
      └─────┬─────┘           │
            ▼                 ▼
      DISCOVERABLE       CANDIDATE
        LISTINGS          MATCHES
                              │
                              ▼
                        NEGOTIATION


El componente de `MATCHING` no define el algoritmo concreto de emparejamiento — eso es una decisión de implementación — sino que establece que la arquitectura debe permitir identificar candidatos relevantes a partir de categoría, condiciones y contexto.

---

# 7. Visibilidad y Privacidad del Listado

Un listado no requiere exponer toda la información del agente que lo publica.


Public Listing Data
    │
    ├── categoría del servicio;
    ├── condiciones generales;
    └── identidad verificable del proveedor.

Private Agent Data
    │
    ├── arquitectura interna;
    ├── modelos utilizados;
    └── estrategia de negociación.


Esta distinción es coherente con lo ya establecido en el Whitepaper (`11_Agent_Economy_Model.md`, sección 19 — Privacidad verificable): la confianza no requiere transparencia absoluta.

---

# 8. Reputación en el Contexto del Mercado

El mercado puede mostrar información reputacional contextual junto a un listado, pero esta información:


Reputation Display
    ≠
Reputation Guarantee


El mercado únicamente **expone** información ya generada por `03_Trust_Architecture`; no la calcula ni la certifica por sí mismo. La responsabilidad del cálculo y verificación de la reputación permanece en Trust Architecture.

---

# 9. Ciclo de Vida de un Listado


Created
   │
   ▼
Active
   │
   ├──▶ Matched     → conduce a negociación
   ├──▶ Expired     → supera su periodo de validez
   ├──▶ Withdrawn   → el agente lo retira voluntariamente
   └──▶ Suspended   → suspendido por incumplimiento de reglas del mercado


Un listado `Matched` no implica automáticamente un contrato: solo indica que ha comenzado un proceso de negociación con una o más contrapartes.

---

# 10. Costes de Participación en el Mercado

Publicar o mantener un listado puede tener asociado un coste, coherente con el principio ya establecido en `01_Economic_Model.md` (sección 13):


Listing Cost
    │
    └── proporcional al uso real de recursos de red (visibilidad, almacenamiento, prioridad)


El mercado no debe cobrar por el mero hecho de participar más allá del coste real de mantener esa participación visible.

---

# 11. Mecanismos de Matching de Alto Nivel

Sin definir un algoritmo concreto, la arquitectura reconoce distintas estrategias de emparejamiento que un mercado puede implementar:


Category Match
Condition Match (price range, duration)
Reputation-Weighted Match
Proximity / Latency Match (para recursos físicos o computación distribuida)
Manual Selection


Estas estrategias pueden combinarse. El protocolo no exige una única estrategia de matching para todos los tipos de mercado definidos en la sección 5.

---

# 12. Relación con los Roles Económicos

Los roles ya definidos en `01_Economic_Model.md` (sección 11) se expresan en el mercado de la siguiente forma:


Provider     → publica listados de oferta
Consumer     → publica listados de demanda o responde a listados de oferta
Intermediary → puede operar o curar un mercado categorizado
Validator    → puede aportar evidencia reputacional visible en el listado


---

# 13. Principios de Diseño

### MKT-PRINC-001 — Market Plurality

La arquitectura debe permitir la coexistencia de múltiples tipos de mercado.

### MKT-PRINC-002 — Listing Is Not Contract

Un listado representa disposición a intercambiar, no un acuerdo vinculante.

### MKT-PRINC-003 — Privacy-Compatible Listings

Un listado debe poder publicarse sin exponer información interna del agente.

### MKT-PRINC-004 — Reputation Exposure, Not Computation

El mercado muestra información reputacional; no la calcula ni la certifica.

### MKT-PRINC-005 — Cost Proportionality

El coste de participar en el mercado debe ser proporcional al uso real de recursos.

### MKT-PRINC-006 — Matching Flexibility

La arquitectura no impone una única estrategia de emparejamiento.

### MKT-PRINC-007 — Separation from Communication Layer

La estructura del mercado es independiente del protocolo de comunicación que la transporta.

---

# 14. Invariantes

### MKT-INV-001

Un listado no constituye un contrato.

### MKT-INV-002

Un listado `Matched` no implica un acuerdo cerrado.

### MKT-INV-003

La reputación mostrada en un listado no puede ser modificada por el propio mercado.

### MKT-INV-004

Un listado suspendido no puede generar nuevas negociaciones mientras dure la suspensión.

### MKT-INV-005

La existencia de un mercado no obliga a ningún agente a participar en él.

---

# 15. Requisitos Funcionales

### MKT-REQ-001

El sistema debe permitir crear, actualizar, retirar y expirar listados.

### MKT-REQ-002

El sistema debe permitir distinguir entre listados de oferta y de demanda.

### MKT-REQ-003

El sistema debe permitir categorizar listados por tipo de servicio.

### MKT-REQ-004

El sistema debe permitir mostrar información reputacional contextual asociada a un listado, cuando esté disponible.

### MKT-REQ-005

El sistema debe permitir múltiples estrategias de matching sin requerir cambios estructurales.

### MKT-REQ-006

El sistema debe permitir calcular el coste de participación en función del uso real de recursos.

### MKT-REQ-007

El sistema debe permitir que un listado transicione a un proceso de negociación gestionado fuera del propio mercado.

---

# 16. Relación con los Documentos de Economic Architecture


01_Economic_Model.md
        │
        ▼
02_Service_Market_Architecture.md   ← este documento
        │
        ▼
03_Agent_Transactions.md
        │
        ▼
04_Token_Integration.md


Este documento asume el marco conceptual de `01_Economic_Model.md` y prepara el terreno para `03_Agent_Transactions.md`, que definirá qué ocurre una vez que un listado deriva en un acuerdo concreto.

---

# 17. Arquitectura de Alto Nivel


                AGENT CAPABILITY
                       │
                       ▼
                 SERVICE LISTING
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
   OPEN CATALOG    CATEGORIZED    BILATERAL
                     MARKET       EXCHANGE
          │            │            │
          └─────┬──────┴─────┬──────┘
                ▼             ▼
            MATCHING     REPUTATION
                          DISPLAY
                │
                ▼
            NEGOTIATION
                │
                ▼
             CONTRACT


---

# 18. Conclusión

El Service Market Architecture define la estructura económica que hace posible que los servicios de los agentes sean descubribles y comparables, sin imponer un único modelo de mercado ni invadir las responsabilidades de la capa de comunicación o del sistema de reputación.

El principio fundamental de este documento es:

> **Un mercado en SynCoinAI no decide qué se contrata ni con quién; únicamente estructura la visibilidad de lo que los agentes están dispuestos a ofrecer o solicitar, dejando la decisión final a la negociación entre las partes.**

El siguiente documento, `03_Agent_Transactions.md`, definirá qué ocurre cuando esa negociación concluye en un acuerdo: cómo se estructura, ejecuta y liquida una transacción entre agentes.