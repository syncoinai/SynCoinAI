# SynCoinAI — Negotiation Protocol

**Documento:** `03_Negotiation_Protocol.md`
**Ubicación:** `docs/02_Architecture/05_Communication_Architecture/`
**Versión:** 1.0
**Estado:** Architecture Specification
**Proyecto:** SynCoinAI

---

# 1. Propósito

El Negotiation Protocol define la arquitectura del mensaje mediante el cual dos o más agentes, ya descubiertos y comunicados, intercambian propuestas y contrapropuestas hasta alcanzar un acuerdo, rechazarlo o dejarlo expirar.

Este documento no define cómo un agente decide qué ofrecer, aceptar o rechazar — eso pertenece a la estrategia y autonomía del agente, ya desarrolladas en `08_Contracts/01_Contracts_Interaction.md` (secciones "Negociación" y "Autonomía durante la negociación") — ni cómo se forma el contrato resultante, que también corresponde a ese documento. Define únicamente el protocolo de mensajes que hace posible que esa negociación ocurra entre dos identidades, sobre los canales ya definidos en `01_Agent_Communication.md`, a partir de candidatos localizados mediante `02_Discovery_Protocol.md`.

> **El Negotiation Protocol no decide qué es una buena oferta. Define cómo una oferta viaja, se responde y se cierra entre dos agentes.**

---

# 2. Relación con los Documentos Existentes

Se aplica aquí la misma frontera ya establecida entre Communication y Runtime en la auditoría del Agent Runtime Protocol:

```
Communication
    =
Message Transport

Runtime
    =
Message Processing and Action
```

Aplicada a la negociación:

```
Negotiation Protocol (Communication)
        │
        └── ¿Cómo se estructura y secuencia el intercambio de propuestas?

Contract Interaction (Runtime)
        │
        └── ¿Qué propuesta hace o acepta el agente, y cómo se forma el contrato?
```

Y en relación con los dos documentos anteriores de esta misma sección:

```
02_Discovery_Protocol.md
        │
        ▼
   Candidate Match
        │
        ▼
01_Agent_Communication.md
        │
        ▼
   Session (canal establecido)
        │
        ▼
03_Negotiation_Protocol.md   ← este documento
        │
        ▼
   Agreement / Rejection / Expiration
        │
        ▼
08_Contracts (Runtime)
        │
        ▼
   Contract
```

Una negociación no puede iniciarse sin una sesión de comunicación ya establecida, y no puede iniciarse sobre un agente que no haya sido previamente localizado o conocido de antemano.

---

# 3. Principio Fundamental

> **Una propuesta no compromete a ninguna de las partes hasta que ambas la acepten explícitamente. Hasta ese momento, es reversible por cualquiera de ellas.**

```
Offer
    ≠
Obligation
```

La negociación es, por diseño, un espacio reversible. El compromiso vinculante solo surge en la formación del contrato, no durante el intercambio de propuestas.

---

# 4. Separación Conceptual

```
Proposal
    │
    └── ¿Qué condiciones se plantean?

Round
    │
    └── ¿En qué punto de la secuencia de intercambio se encuentra?

Negotiation Session
    │
    └── ¿Qué agrupa todas las propuestas de un mismo intercambio?

Outcome
    │
    └── ¿Cómo terminó: acuerdo, rechazo o expiración?
```

```
Proposal ≠ Round ≠ Negotiation Session ≠ Outcome
```

Una `Negotiation Session` es un tipo especializado de `Session`, ya definida en `01_Agent_Communication.md`; no introduce un concepto de sesión distinto, sino que añade el estado propio de una negociación sobre la sesión de comunicación existente.

---

# 5. Modelo General de Negociación

```
              DISCOVERY (candidato localizado)
                        │
                        ▼
              COMMUNICATION SESSION
                        │
                        ▼
              NEGOTIATION SESSION OPENED
                        │
                        ▼
                    PROPOSAL
                        │
                        ▼
              ┌─────────┴─────────┐
              ▼                   ▼
          COUNTERPROPOSAL     RESPONSE
              │                   │
              └─────────┬─────────┘
                        ▼
              ACCEPTED / REJECTED / EXPIRED
                        │
                        ▼
              (si ACCEPTED) → CONTRACT FORMATION (Runtime)
```

El protocolo no impone un número fijo de rondas; la arquitectura debe soportar tanto acuerdos de una sola ronda (aceptación directa) como negociaciones extendidas con múltiples contrapropuestas.

---

# 6. Estructura de una Propuesta

A nivel de protocolo, una propuesta es un mensaje con una estructura mínima común, independientemente de su contenido económico concreto:

```
Proposal Message
    │
    ├── Negotiation Session ID
    ├── Round Number
    ├── Proponent Identity
    ├── Terms (opaco para este documento — definido por el dominio: precio, plazo, condiciones)
    ├── Validity / Expiration
    ├── Reference (a Discovery Announcement o Service Listing, si aplica)
    └── Firma de la propia identidad
```

El contenido de `Terms` no se especifica aquí: puede referirse a precio, plazo, calidad, garantías u otras condiciones ya enumeradas en `Contract_Interaction.md`. Este documento solo garantiza que ese contenido viaja de forma íntegra, autenticada y asociada a una ronda y sesión concretas.

---

# 7. Ciclo de Vida de una Sesión de Negociación

```
Negotiation Session
    │
    ├── Opened        → primera propuesta enviada
    ├── In Progress    → intercambio de rondas en curso
    ├── Accepted        → ambas partes confirman los mismos términos
    ├── Rejected        → una parte declina explícitamente continuar
    ├── Expired         → ninguna respuesta dentro del plazo de validez
    └── Withdrawn       → una parte retira su propuesta antes de una respuesta
```

```
Negotiation Session
    ≠
Contract
```

El estado `Accepted` de una sesión de negociación marca el fin del protocolo de negociación y el inicio de la formación contractual en el Runtime; no constituye por sí mismo un contrato.

---

# 8. Expiración y Reversibilidad

Toda propuesta debe llevar asociada una vigencia explícita:

```
Proposal
    │
    └── Validity Window
              │
              ├── dentro de la ventana   → puede aceptarse
              └── fuera de la ventana     → expira automáticamente
```

Una propuesta expirada no puede aceptarse retroactivamente; debe reiniciarse el ciclo con una nueva propuesta si las partes desean continuar. Esto evita compromisos implícitos derivados de una aceptación tardía sobre condiciones que ya no reflejan la intención vigente del proponente.

```
Expired Proposal
    ≠
Valid Basis for Acceptance
```

---

# 9. Negociación Multiagente

El protocolo no se limita a negociaciones bilaterales. La arquitectura debe soportar sesiones con más de dos participantes, sin que ello cambie la estructura básica del mensaje:

```
Negotiation Session
    │
    ├── Bilateral    → dos identidades
    └── Multiparty    → tres o más identidades
```

En una negociación multiparte, el estado `Accepted` requiere la confirmación explícita de todas las partes definidas como necesarias por el dominio de la negociación; este documento no define el mecanismo de quórum, que corresponde a la capa que gestiona la formación del contrato.

---

# 10. Integridad y Autenticidad

Como en el resto de la arquitectura de comunicación, la autenticidad de una propuesta depende de su firma, no del canal por el que se recibe:

```
Proposal Authenticity
    =
Valid Signature by Proponent Identity
```

Ninguna propuesta o respuesta puede atribuirse a un agente sin verificar su firma, incluso si llega a través de un canal mediado (por ejemplo, un directorio de mercado que facilitó el descubrimiento inicial).

---

# 11. Relación con el Ciclo Económico

```
Candidate Match         ← Discovery Protocol
      │
      ▼
Negotiation Session      ← este documento
      │
      ▼
Accepted Outcome
      │
      ▼
Contract Formation       ← Runtime, 08_Contracts
      │
      ▼
Execution → Verification → Settlement → Reputation Update
```

Este documento cierra la cadena de responsabilidad delegada por `04_Economic_Architecture/01_Economic_Model.md` a `05_Communication_Architecture`: descubrimiento y negociación quedan ambos cubiertos, dejando la formación y ejecución del contrato al Agent Runtime Protocol.

---

# 12. Principios de Diseño

### NEG-PRINC-001 — Proposals Are Non-Binding

Una propuesta no genera obligación alguna hasta su aceptación explícita por todas las partes requeridas.

### NEG-PRINC-002 — Session Extends Communication

Una sesión de negociación es una especialización de la sesión de comunicación ya definida, no un concepto de sesión independiente.

### NEG-PRINC-003 — Round-Agnostic Protocol

El protocolo no impone un número fijo de rondas de negociación.

### NEG-PRINC-004 — Opaque Terms

El protocolo no interpreta ni valida el contenido económico de una propuesta; solo garantiza su transporte íntegro y autenticado.

### NEG-PRINC-005 — Explicit Expiration

Toda propuesta debe llevar asociada una vigencia explícita, sin la cual no puede aceptarse.

### NEG-PRINC-006 — No Retroactive Acceptance

Una propuesta expirada no puede aceptarse retroactivamente.

### NEG-PRINC-007 — Multiparty Support

La arquitectura debe soportar negociaciones bilaterales y multiparte sin cambiar la estructura del mensaje.

### NEG-PRINC-008 — Signature-Based Authenticity

La autenticidad de una propuesta depende de su firma, no del canal o intermediario por el que se transmite.

### NEG-PRINC-009 — Acceptance Is Not Contract

La aceptación de una negociación marca el fin del protocolo de negociación, no la existencia de un contrato.

---

# 13. Invariantes

### NEG-INV-001

Ninguna propuesta o respuesta es válida sin la firma de la identidad que la emite.

### NEG-INV-002

Una propuesta fuera de su ventana de vigencia no puede resultar en un `Accepted Outcome`.

### NEG-INV-003

Una sesión de negociación en estado `Accepted` no equivale a un contrato formado.

### NEG-INV-004

En una negociación multiparte, el estado `Accepted` requiere confirmación explícita de todas las partes requeridas por el dominio.

### NEG-INV-005

Una sesión de negociación no puede existir sin una sesión de comunicación subyacente ya establecida.

---

# 14. Requisitos Funcionales

### NEG-REQ-001

El sistema debe permitir enviar y recibir propuestas firmadas dentro de una sesión de negociación identificable.

### NEG-REQ-002

El sistema debe permitir asociar cada propuesta a un número de ronda dentro de la sesión.

### NEG-REQ-003

El sistema debe permitir expresar y validar la vigencia de una propuesta.

### NEG-REQ-004

El sistema debe permitir los estados de sesión: Opened, In Progress, Accepted, Rejected, Expired y Withdrawn.

### NEG-REQ-005

El sistema debe soportar sesiones de negociación bilaterales y multiparte.

### NEG-REQ-006

El sistema debe permitir referenciar, desde una propuesta, el anuncio de descubrimiento o listado de mercado del que se originó la negociación.

### NEG-REQ-007

El sistema debe entregar el resultado de una sesión aceptada a la capa de formación de contratos del Runtime sin reinterpretar sus términos.

---

# 15. Relación con los Documentos de Communication Architecture

```
01_Agent_Communication.md
        │
        ▼
02_Discovery_Protocol.md
        │
        ▼
03_Negotiation_Protocol.md   ← este documento
```

### `01_Agent_Communication.md`

Define cómo un agente es alcanzable y cómo se establece una sesión de comunicación.

### `02_Discovery_Protocol.md`

Define cómo un agente localiza a otro antes de comunicarse con él.

### `03_Negotiation_Protocol.md`

Define cómo, una vez comunicados, dos o más agentes intercambian propuestas hasta alcanzar un resultado, que el Runtime podrá convertir en contrato.

Con este documento se completa el bloque `05_Communication_Architecture` definido en el índice maestro.

---

# 16. Arquitectura de Alto Nivel

```
                 AGENT A                      AGENT B
                    │                             │
                    ▼                             ▼
             DISCOVERY (02)                DISCOVERY (02)
                    │                             │
                    └──────────► MATCH ◄──────────┘
                                   │
                                   ▼
                      COMMUNICATION SESSION (01)
                                   │
                                   ▼
                       NEGOTIATION SESSION (03)
                                   │
                        ┌──────────┴──────────┐
                        ▼                     ▼
                    PROPOSAL            COUNTERPROPOSAL
                        │                     │
                        └──────────┬──────────┘
                                   ▼
                     ACCEPTED / REJECTED / EXPIRED
                                   │
                                   ▼
                    CONTRACT FORMATION (Runtime, 08)
```

---

# 17. Conclusión

El Negotiation Protocol cierra el bloque de Communication Architecture proporcionando el mecanismo por el cual dos identidades ya comunicadas transforman una intención económica en un resultado concreto: un acuerdo, un rechazo o una expiración. No decide el contenido de ese acuerdo, que sigue perteneciendo a la autonomía del agente definida en el Runtime Protocol, sino que garantiza que el intercambio que lo produce es íntegro, autenticado y reversible hasta el momento de la aceptación.

El principio fundamental de este documento es:

> **Ninguna propuesta compromete a un agente. Solo la aceptación explícita, por todas las partes requeridas, transforma una negociación en la base de un contrato.**

Con `01_Agent_Communication.md`, `02_Discovery_Protocol.md` y `03_Negotiation_Protocol.md`, el bloque `05_Communication_Architecture` queda completo: un agente puede ahora ser alcanzable, descubrible y capaz de negociar de forma verificable con cualquier otro agente del ecosistema, cerrando así la cadena delegada explícitamente por `04_Economic_Architecture/01_Economic_Model.md`.