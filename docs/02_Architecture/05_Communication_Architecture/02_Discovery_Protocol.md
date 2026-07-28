# SynCoinAI — Discovery Protocol

**Documento:** `02_Discovery_Protocol.md`
**Ubicación:** `docs/02_Architecture/05_Communication_Architecture/`
**Versión:** 1.0
**Estado:** Architecture Specification
**Proyecto:** SynCoinAI

---

# 1. Propósito

El Discovery Protocol define la arquitectura mediante la cual un agente anuncia su existencia, sus capacidades y su disposición a ofrecer o requerir servicios, y mediante la cual otro agente puede encontrarlo antes de comunicarse directamente con él.

Este documento no define qué es un listado ni cómo se estructura un mercado — eso corresponde a `04_Economic_Architecture/02_Service_Market_Architecture.md` — ni cómo se resuelve una identidad a un endpoint alcanzable, ya definido en `01_Agent_Communication.md`. Define el protocolo que conecta ambas capas: el mecanismo por el cual la existencia y las capacidades de un agente se propagan y se consultan dentro del ecosistema.

> **El Discovery Protocol no decide qué agentes deberían encontrarse. Define cómo un agente puede hacerse encontrable y cómo otro puede encontrarlo.**

---

# 2. Relación con los Documentos Existentes

`Service_Market_Architecture.md` ya delimitó esta frontera de forma explícita:


Service Market Architecture
        │
        └── ¿Qué es un mercado y cómo se estructura una oferta?

Discovery Protocol (este documento)
        │
        └── ¿Cómo se transmite y localiza esa información?

Negotiation Protocol
        │
        └── ¿Cómo se llega a un acuerdo concreto?


Este documento se apoya, a su vez, en el modelo de direccionamiento ya establecido en `01_Agent_Communication.md`:


Agent Identity
      │
      ▼
Address Resolution Record   ← 01_Agent_Communication.md
      │
      ▼
Capability Announcement      ← este documento
      │
      ▼
Service Listing               ← Service_Market_Architecture.md


Un agente debe ser primero *alcanzable* (Communication) antes de poder ser *encontrado* (Discovery), y debe ser encontrado antes de que su oferta pueda convertirse en un *listado de mercado* (Economic Architecture).

---

# 3. Principio Fundamental

> **Un agente no es descubrible por defecto en todo el ecosistema. Es descubrible en la medida y en el alcance que su propia identidad decide anunciar.**

El descubrimiento es un acto de publicación voluntaria, no una propiedad automática de la existencia del agente:


Agent Exists
    ≠
Agent Discoverable


Un agente puede existir, tener identidad y capacidad económica, y permanecer deliberadamente fuera de cualquier mecanismo de descubrimiento público.

---

# 4. Separación Conceptual


Announcement
    │
    └── ¿Qué publica el agente sobre sí mismo?

Registry
    │
    └── ¿Dónde se almacena o propaga ese anuncio?

Query
    │
    └── ¿Cómo pregunta un agente por otros?

Match
    │
    └── ¿Qué candidatos resultan relevantes para una consulta?

Resolution
    │
    └── ¿Cómo se traduce un candidato en un endpoint alcanzable?



Announcement ≠ Registry ≠ Query ≠ Match ≠ Resolution


Un `Match` no es todavía una `Resolution`: identificar un candidato relevante no implica automáticamente poder comunicarse con él sin pasar por la capa de direccionamiento ya definida.

---

# 5. Modelo General de Descubrimiento


                 AGENT
                   │
                   ▼
         CAPABILITY ANNOUNCEMENT
                   │
                   ▼
           DISCOVERY REGISTRY
                   │
                   ▼
          ┌────────┴────────┐
          ▼                 ▼
   QUERY (pull)      SUBSCRIPTION (push)
          │                 │
          └────────┬────────┘
                   ▼
              CANDIDATE MATCH
                   │
                   ▼
       ADDRESS RESOLUTION (01_Agent_Communication.md)
                   │
                   ▼
              COMMUNICATION


El ciclo se cierra devolviendo el control a la capa de comunicación: el resultado del descubrimiento es, en último término, un conjunto de identidades resolubles con las que iniciar contacto.

---

# 6. Anuncio de Capacidades

Un agente que desea ser descubierto publica un anuncio de capacidades, independiente del listado económico que pueda derivarse de él:


Capability Announcement
    │
    ├── Agent Identity
    ├── Capability Category / Taxonomy Reference
    ├── Capability Descriptor (qué puede hacer, no en qué condiciones)
    ├── Discovery Scope (público / restringido / privado)
    ├── Vigencia
    └── Firma de la propia identidad


El anuncio describe capacidad, no condiciones económicas:


Capability Announcement
    ≠
Service Listing


Un agente puede anunciar una capacidad sin publicar todavía un listado de mercado con condiciones concretas; el listado, cuando existe, referencia al anuncio, no lo sustituye.

Como en el modelo de direccionamiento, el anuncio debe estar firmado por la identidad que lo emite, para impedir que un tercero anuncie capacidades en nombre de un agente sin su autorización.

---

# 7. Registro y Propagación

La arquitectura no impone un único mecanismo de propagación de anuncios. Contempla, de forma no exclusiva:


Discovery Mechanism
   │
   ├── Centralized Registry     → un directorio consultable por todos los agentes
   ├── Federated Registries     → varios directorios interoperables entre dominios
   ├── Gossip Propagation        → los agentes redistribuyen anuncios entre pares
   └── Mediated Directory        → un servicio de mercado agrega y expone anuncios


Un `Mediated Directory` no es distinto, en su rol, del canal `Mediated` ya definido en `01_Agent_Communication.md`: agrega valor de descubrimiento, pero no adquiere autoridad para modificar o suplantar el anuncio original.


Mediated Directory
      │
      └── puede: indexar, categorizar, exponer
      └── no puede (por defecto): alterar la firma del anuncio original


---

# 8. Consulta y Emparejamiento

Un agente que busca capacidades ajenas puede operar en dos modos, sin que ninguno excluya al otro:


Discovery Query
   │
   ├── Pull (Query)          → el agente consulta activamente el registro
   └── Push (Subscription)   → el agente se suscribe a anuncios futuros relevantes


El resultado de una consulta es un conjunto de candidatos, no un acuerdo ni una garantía de disponibilidad:


Query
   │
   ▼
Candidate Set
   │
   ▼
(no implica) Availability Guarantee


Como ya estableció `Service_Market_Architecture.md` para el `MATCHING`, este documento no fija el algoritmo de emparejamiento; establece que el sistema debe permitir filtrar candidatos por categoría, capacidad declarada y alcance de descubrimiento.

---

# 9. Alcance y Privacidad del Descubrimiento

Al igual que ocurre con la visibilidad de un listado (`Service_Market_Architecture.md`, sección 7), el anuncio de capacidades no obliga a exponer toda la información del agente:


Discovery Scope
   │
   ├── Public        → visible para cualquier agente del ecosistema
   ├── Restricted     → visible solo para agentes con credenciales específicas
   └── Private        → no propagado; solo accesible mediante referencia directa


Un agente en alcance `Private` sigue siendo alcanzable si otro agente ya conoce su identidad y puede resolver su dirección directamente a través de `01_Agent_Communication.md`; simplemente no aparece en registros ni resultados de consulta.


Private Scope
    ≠
Unreachable


---

# 10. Relación con la Reputación

El descubrimiento no incorpora directamente la reputación como criterio estructural, en línea con la separación ya aplicada en `04_Economic_Architecture`:


Reputation
    │
    └── informa
            │
            ▼
      Selección entre candidatos ya descubiertos


La reputación puede utilizarse por el agente que consulta para ordenar o filtrar candidatos tras el descubrimiento, pero el propio Discovery Protocol no condiciona la visibilidad de un anuncio a la reputación de quien lo publica:


Low Reputation ≠ Excluded from Discovery
High Reputation ≠ Priority in Discovery


Cualquier priorización basada en reputación es una decisión del agente consultante o del directorio mediador, no una regla impuesta por este protocolo.

---

# 11. Relación con el Ciclo Económico


Need Detection
      │
      ▼
Capability Announcement / Query   ← este documento
      │
      ▼
Candidate Match
      │
      ▼
Service Listing                    ← Service_Market_Architecture.md
      │
      ▼
Negotiation                        ← Negotiation_Protocol.md
      │
      ▼
Contract                           ← Agent Runtime Protocol, 08_Contracts


Este documento cubre específicamente la fase en la que la necesidad de un agente se convierte en un conjunto de candidatos alcanzables, previa a cualquier condición económica concreta.

---

# 12. Principios de Diseño

### DISC-PRINC-001 — Discovery Is Opt-In

Un agente es descubierto solo en la medida en que decide anunciarse; el descubrimiento no es una propiedad automática de la existencia del agente.

### DISC-PRINC-002 — Announcement Precedes Listing

Un anuncio de capacidades es independiente del listado de mercado que pueda derivarse de él.

### DISC-PRINC-003 — Signed Announcements Only

Ningún anuncio de capacidades es válido si no está firmado por la identidad que lo emite.

### DISC-PRINC-004 — Non-Exclusive Discovery Mechanisms

La arquitectura debe soportar más de un mecanismo de propagación de anuncios.

### DISC-PRINC-005 — Match Is Not Resolution

Un candidato identificado en una consulta no implica, por sí mismo, capacidad de comunicación inmediata; requiere pasar por la resolución de direccionamiento.

### DISC-PRINC-006 — Scoped Visibility

Un agente puede limitar el alcance de su descubribilidad sin perder alcanzabilidad directa.

### DISC-PRINC-007 — Reputation-Neutral Visibility

La visibilidad de un anuncio en el descubrimiento no depende de la reputación de quien lo publica.

### DISC-PRINC-008 — Mediator Constraint

Un directorio mediador no adquiere, por defecto, autoridad para alterar o suplantar un anuncio original.

### DISC-PRINC-009 — Implementation Independence

El modelo de descubrimiento conceptual debe mantenerse estable independientemente del mecanismo de registro o propagación concreto que lo implemente.

---

# 13. Invariantes

### DISC-INV-001

Ningún anuncio de capacidades puede publicarse en nombre de una identidad sin estar firmado por ella.

### DISC-INV-002

Un agente en alcance `Private` no pierde alcanzabilidad directa por no aparecer en registros de descubrimiento.

### DISC-INV-003

Un resultado de consulta (`Candidate Match`) no constituye una garantía de disponibilidad ni de aceptación de servicio.

### DISC-INV-004

Un directorio mediador no puede modificar el contenido firmado de un anuncio que agrega o expone.

### DISC-INV-005

La ausencia de un agente en un registro de descubierta no implica la inexistencia o revocación de su identidad.

---

# 14. Requisitos Funcionales

### DISC-REQ-001

El sistema debe permitir a un agente publicar un anuncio de capacidades firmado por su identidad.

### DISC-REQ-002

El sistema debe permitir consultar anuncios por categoría o capacidad declarada.

### DISC-REQ-003

El sistema debe soportar consulta activa (pull) y suscripción a anuncios futuros (push).

### DISC-REQ-004

El sistema debe permitir definir el alcance de visibilidad de un anuncio (público, restringido, privado).

### DISC-REQ-005

El sistema debe permitir resolver un candidato encontrado a un endpoint alcanzable mediante el modelo de direccionamiento ya definido.

### DISC-REQ-006

El sistema debe permitir la coexistencia de varios mecanismos de propagación de anuncios (registro centralizado, federado, gossip, directorio mediado).

### DISC-REQ-007

El sistema debe permitir la incorporación de nuevas taxonomías de capacidad sin requerir cambios estructurales en el protocolo.

---

# 15. Relación con los Documentos de Communication Architecture


01_Agent_Communication.md
        │
        ▼
02_Discovery_Protocol.md   ← este documento
        │
        ▼
03_Negotiation_Protocol.md


### `01_Agent_Communication.md`

Define cómo un agente es alcanzable una vez identificado.

### `02_Discovery_Protocol.md`

Define cómo un agente se hace encontrable y cómo otro agente lo localiza antes de comunicarse con él.

### `03_Negotiation_Protocol.md`

Definirá cómo dos agentes, ya descubiertos y comunicados, alcanzan condiciones concretas previas a un contrato.

---

# 16. Arquitectura de Alto Nivel


                 AGENT A                          AGENT B
                    │                                 │
                    ▼                                 ▼
        CAPABILITY ANNOUNCEMENT              DISCOVERY QUERY
                    │                                 │
                    ▼                                 │
           DISCOVERY REGISTRY  ◄──────────────────────┘
                    │
                    ▼
              CANDIDATE MATCH
                    │
                    ▼
           ADDRESS RESOLUTION
                    │
                    ▼
              COMMUNICATION
                    │
                    ▼
               NEGOTIATION


---

# 17. Conclusión

El Discovery Protocol define el puente entre la existencia de un agente y su participación efectiva en el ecosistema: sin descubrimiento, la comunicación requeriría que los agentes ya se conocieran de antemano, y el mercado carecería de forma de encontrar oferta y demanda.

El principio fundamental de este documento es:

> **Un agente no es encontrado porque exista, sino porque ha decidido, de forma explícita y firmada, anunciar aquello que está dispuesto a que otros descubran.**

El documento siguiente de esta sección desarrolla el protocolo de negociación que se inicia una vez que dos agentes se han descubierto y pueden comunicarse entre sí.