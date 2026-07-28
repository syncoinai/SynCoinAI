# SynCoinAI — Agent Communication

**Documento:** `01_Agent_Communication.md`
**Ubicación:** `docs/02_Architecture/05_Communication_Architecture/`
**Versión:** 1.0
**Estado:** Architecture Specification
**Proyecto:** SynCoinAI

---

# 1. Propósito

El Agent Communication define la arquitectura de sistema mediante la cual los mensajes producidos y consumidos por los agentes SynCoinAI viajan efectivamente a través del ecosistema: cómo se direcciona un agente, qué canales existen entre agentes, cómo se transportan los mensajes y qué garantías de seguridad e integridad se aplican a ese transporte.

Este documento no redefine el modelo de mensaje ni el procesamiento de interacciones a nivel de agente — eso ya se estableció en `01_Agent_Architecture/02_Agent_Runtime_Protocol/09_Communication/Agent_Communication.md` e `Interaction_Model.md` — sino que describe la infraestructura de comunicación sobre la que ese modelo opera a escala de ecosistema.

> **El Agent Communication no define qué significa un mensaje. Define cómo un mensaje llega, de forma verificable, de un agente a otro.**

---

# 2. Relación con el Agent Runtime Protocol

El Agent Runtime Protocol ya estableció, en `09_Communication`, que un agente puede enviar, recibir y procesar interacciones, y que dicho procesamiento requiere identidad verificable, gestión de conversaciones y trazabilidad. La auditoría final del Runtime Protocol (`09_Architecture_Audit`) fija explícitamente esta frontera:


Communication
    =
Message Transport

Runtime
    =
Message Processing and Action


La Communication Architecture toma esa frontera como punto de partida:


Runtime Protocol — 09_Communication
        │
        └── ¿Cómo procesa un agente un mensaje recibido?

Communication Architecture
        │
        └── ¿Cómo llega ese mensaje de un agente a otro?


Por tanto, la cadena de responsabilidad es:


Agent Communication (Runtime)
        │
        ▼
Agent Communication (Architecture) ← este documento
        │
        ▼
Discovery Protocol
        │
        ▼
Negotiation Protocol


El Runtime define el modelo del mensaje. Este documento define el sistema que hace posible que ese mensaje exista fuera del propio agente.

---

# 3. Principio Fundamental

> **Ningún agente se comunica directamente con la identidad de otro agente. Se comunica con un endpoint autenticado que esa identidad controla en un momento dado.**

Esta distinción es necesaria porque, tal como estableció el Runtime Protocol, la identidad de un agente es independiente de su infraestructura, su runtime y su ubicación. La arquitectura de comunicación debe reflejar esa independencia en lugar de contradecirla:


Agent Identity
    ≠
Network Location


La comunicación no ancla la identidad a una dirección fija; la resuelve dinámicamente en cada interacción.

---

# 4. Separación Conceptual

Como en el resto de la arquitectura de SynCoinAI, la comunicación mantiene separados varios conceptos que suelen confundirse en sistemas de mensajería convencionales:


Identity
    │
    └── ¿Quién es el emisor o receptor?

Address
    │
    └── ¿Dónde puede alcanzarse en este momento?

Channel
    │
    └── ¿Por qué vía circula el mensaje?

Session
    │
    └── ¿Qué intercambio continuado agrupa estos mensajes?

Message
    │
    └── ¿Qué se transmite?


Ninguno de estos conceptos sustituye a los demás:


Identity ≠ Address ≠ Channel ≠ Session ≠ Message


Un agente puede cambiar de dirección o de canal sin que ello afecte a su identidad, exactamente igual que puede cambiar de infraestructura sin perderla (`Infrastructure_Independence.md`).

---

# 5. Capas de la Arquitectura de Comunicación

La comunicación entre agentes se organiza en capas independientes, de forma análoga a como el resto de la arquitectura separa identidad, credenciales y autorización:


                AGENT
                  │
                  ▼
          IDENTITY RESOLUTION
                  │
                  ▼
          ADDRESSING LAYER
                  │
                  ▼
           TRANSPORT LAYER
                  │
                  ▼
            SESSION LAYER
                  │
                  ▼
            MESSAGE LAYER
                  │
                  ▼
        INTERACTION LAYER (Runtime)


### Identity Resolution

Traduce una identidad de agente en uno o más endpoints alcanzables en el momento actual. No crea identidad ni la modifica; únicamente la resuelve.

### Addressing Layer

Define cómo se representa un endpoint alcanzable y cómo se mantiene actualizado cuando el agente cambia de infraestructura.

### Transport Layer

Define cómo viaja físicamente el mensaje (síncrono, asíncrono, punto a punto, mediado).

### Session Layer

Agrupa una secuencia de mensajes relacionados bajo un contexto común, sin implicar todavía ningún significado operativo sobre ellos.

### Message Layer

Define el sobre (envelope) del mensaje: origen, destino, integridad, tipo y referencia de sesión — no su contenido interpretado, que corresponde a la capa de interacción del Runtime.

### Interaction Layer

Ya definida por el Runtime Protocol. Consume los mensajes entregados por las capas anteriores y decide qué significan y qué acción provocan.

Esta separación permite que la infraestructura de transporte evolucione (nuevos protocolos, nuevas redes) sin que ello obligue a modificar cómo el Runtime interpreta las interacciones.

---

# 6. Modelo de Direccionamiento

Un agente no se direcciona mediante una ubicación de red fija, sino mediante una identidad resoluble:


Agent Identity
      │
      ▼
Address Resolution Record
      │
      ├── Endpoint(s) actuales
      ├── Protocolo(s) soportado(s)
      ├── Vigencia
      └── Firma de la propia identidad


El registro de resolución debe estar firmado por la identidad a la que representa, de forma que un tercero no pueda anunciar endpoints en nombre de un agente sin su autorización.


Address Update
      │
      ▼
Signed by Agent Identity
      │
      ▼
Propagated via Discovery Protocol


Este documento define que dicho registro debe existir y estar firmado. El mecanismo concreto de publicación y búsqueda de endpoints corresponde a `02_Discovery_Protocol.md`.

---

# 7. Canales de Comunicación

La arquitectura debe soportar más de un tipo de canal, sin imponer uno como obligatorio:


Channel
   │
   ├── Direct        → agente a agente, sin intermediarios
   ├── Mediated       → a través de un servicio de intercambio o mercado
   ├── Broadcast       → un agente hacia múltiples receptores no determinados
   └── Multicast       → un agente hacia un grupo determinado de receptores


Un canal `Mediated` no implica que el intermediario pueda leer o alterar el contenido del mensaje; su rol se limita a facilitar el enrutamiento salvo que las partes decidan explícitamente lo contrario.


Mediated Channel
      │
      └── Intermediary
                │
                ├── puede: enrutar, poner en cola, notificar
                └── no puede (por defecto): interpretar, modificar, suplantar


---

# 8. Modos de Comunicación

Al igual que estableció el Runtime Protocol para las interacciones, la comunicación puede ser síncrona o asíncrona, y esta arquitectura debe soportar ambas sin privilegiar una sobre la otra:


Communication Mode
      │
      ├── Synchronous
      │       │
      │       └── ambos agentes activos y conectados simultáneamente
      │
      └── Asynchronous
              │
              └── mensaje entregado y procesado en momentos distintos


Un agente puede no estar en ejecución en el momento en que se le dirige un mensaje. Esto no debe tratarse como un fallo del sistema:


Agent Runtime Offline
      ≠
Message Delivery Failure


La arquitectura debe soportar mecanismos de almacenamiento temporal (store-and-forward) para mensajes dirigidos a un agente sin runtime activo, análogos a como el Runtime Protocol ya distingue `Agent` de `Runtime Instance`.

---

# 9. Integridad y Seguridad del Transporte

La seguridad de la comunicación se apoya en los mecanismos ya definidos en `05_Security` del Runtime Protocol, aplicados ahora al transporte:


Message
   │
   ├── Origin Authentication   → firmado por la identidad emisora
   ├── Integrity                → verificable, no alterado en tránsito
   ├── Confidentiality          → cifrado cuando el canal lo requiera
   └── Replay Protection        → no reproducible como si fuera nuevo


La autenticidad del mensaje depende de la identidad del emisor, no del canal por el que llegó:


Channel Trust
    ≠
Message Authenticity


Un canal no confiable no invalida un mensaje correctamente firmado; un canal confiable no legitima un mensaje sin firma válida. La protección contra repetición (nonces, nunca reutilización de secuencias) queda señalada aquí como requisito arquitectónico; su especificación técnica se desarrollará en la fase de especificación técnica, tal como anticipa la auditoría del Runtime Protocol.

---

# 10. Sesiones y Continuidad Conversacional

Una sesión agrupa los mensajes que pertenecen a un mismo intercambio, sin implicar todavía ningún compromiso contractual:


Session
   │
   ├── Session ID
   ├── Participantes
   ├── Canal(es) utilizados
   ├── Estado (Open / Idle / Closed)
   └── Referencia a Interacción (Runtime), si aplica


Una sesión puede sobrevivir a cambios de canal o de endpoint, siempre que la identidad de los participantes se mantenga verificada:


Session
   │
   └── continúa válida aunque cambie
              │
              ├── Endpoint
              ├── Canal
              └── Infraestructura del agente


Esto refleja, a nivel de comunicación, el mismo principio de continuidad que el Runtime Protocol exige a nivel de identidad y ejecución.

---

# 11. Relación con el Ciclo Económico

`04_Economic_Architecture/01_Economic_Model.md` ya delegó explícitamente en este bloque las etapas de descubrimiento y negociación del ciclo económico:

| Etapa | Arquitectura responsable |
|---|---|
| Need Detection / Discovery | `05_Communication_Architecture` (`Discovery_Protocol.md`) |
| Negotiation | `05_Communication_Architecture` (`Negotation_Protocol.md`) |
| Contract | Agent Runtime Protocol — `08_Contracts` |
| Execution | Agent Runtime Protocol |
| Result Verification | `03_Trust_Architecture` |
| Transaction / Payment | `04_Economic_Architecture` |
| Reputation Update | `03_Trust_Architecture` |

Este documento no desarrolla directamente esas etapas; establece la capa de transporte y direccionamiento que ambas necesitan para poder ejecutarse entre agentes que, hasta ese momento, pueden no conocerse.

---

# 12. Relación con Blockchain y Physical Integration

No toda comunicación entre agentes requiere registro en la infraestructura descentralizada:


Off-chain Communication
        │
        ▼
   Interaction / Agreement
        │
        ▼
On-chain Settlement (cuando corresponda)


La comunicación es, por defecto, una capa off-chain de alto volumen; la blockchain interviene únicamente donde se requiere liquidación o registro verificable, en línea con lo ya establecido en la relación Runtime ↔ Blockchain.

Cuando el receptor de un mensaje es un agente físico, la comunicación debe entregarse a través de un adaptador, sin que el emisor necesite conocer el hardware subyacente:


Message
    │
    ▼
Physical Adapter
    │
    ▼
Robot / Device


Esta relación se detallará en `07_Physical_Integration`.

---

# 13. Principios de Diseño

### COM-PRINC-001 — Identity-Resolved Addressing

Un agente se direcciona resolviendo su identidad a un endpoint vigente, nunca mediante una dirección de red fija.

### COM-PRINC-002 — Layer Separation

Identidad, direccionamiento, canal, sesión, mensaje e interacción permanecen conceptualmente separados.

### COM-PRINC-003 — Transport Neutrality

La arquitectura no depende de un protocolo de transporte único.

### COM-PRINC-004 — Authenticity Over Channel Trust

La autenticidad de un mensaje depende de su firma, no del canal por el que se recibe.

### COM-PRINC-005 — Availability Independence

La ausencia temporal de un runtime activo no invalida la capacidad de un agente para recibir mensajes.

### COM-PRINC-006 — Non-Exclusive Channels

La arquitectura debe soportar más de un tipo de canal (directo, mediado, broadcast, multicast).

### COM-PRINC-007 — Mediator Constraint

Un intermediario de canal no adquiere, por defecto, capacidad de interpretar o modificar el contenido de un mensaje.

### COM-PRINC-008 — Session Continuity

Una sesión puede sobrevivir a cambios de endpoint, canal o infraestructura mientras la identidad de los participantes permanezca verificada.

### COM-PRINC-009 — Off-Chain by Default

La comunicación ocurre por defecto fuera de la cadena; el registro on-chain es una decisión explícita, no automática.

### COM-PRINC-010 — Implementation Independence

El modelo de comunicación conceptual debe mantenerse estable independientemente del protocolo de transporte concreto que lo implemente.

---

# 14. Invariantes

### COM-INV-001

Ningún endpoint puede publicarse como válido para una identidad sin estar firmado por esa identidad.

### COM-INV-002

Un mensaje sin firma de origen verificable no puede considerarse auténtico, independientemente del canal utilizado.

### COM-INV-003

Un agente sin runtime activo no puede considerarse un agente inexistente a efectos de direccionamiento.

### COM-INV-004

Un intermediario de canal no puede, por defecto, actuar en nombre de la identidad que enruta.

### COM-INV-005

El cambio de canal o de endpoint no invalida por sí mismo una sesión abierta.

### COM-INV-006

Ningún mensaje puede reproducirse y aceptarse como nuevo tras haber sido ya procesado (replay).

### COM-INV-007

La capa de transporte no puede alterar el significado de una interacción; solo puede entregarla o no entregarla.

---

# 15. Requisitos Funcionales

### COM-REQ-001

El sistema debe permitir resolver la identidad de un agente a uno o más endpoints vigentes.

### COM-REQ-002

El sistema debe permitir la actualización de endpoints firmada por la propia identidad del agente.

### COM-REQ-003

El sistema debe soportar comunicación síncrona y asíncrona.

### COM-REQ-004

El sistema debe permitir el almacenamiento temporal de mensajes dirigidos a agentes sin runtime activo.

### COM-REQ-005

El sistema debe permitir verificar el origen e integridad de un mensaje independientemente del canal.

### COM-REQ-006

El sistema debe soportar canales directos, mediados, broadcast y multicast.

### COM-REQ-007

El sistema debe permitir agrupar mensajes relacionados bajo una sesión identificable.

### COM-REQ-008

El sistema debe permitir la incorporación de nuevos protocolos de transporte sin requerir cambios estructurales en el modelo de comunicación.

---

# 16. Relación con los Documentos de Communication Architecture


01_Agent_Communication.md
        │
        ▼
02_Discovery_Protocol.md
        │
        ▼
03_Negotation_Protocol.md


### `01_Agent_Communication.md`

Define el marco conceptual general: direccionamiento, canales, transporte, sesiones y seguridad del mensaje.

### `02_Discovery_Protocol.md`

Definirá cómo un agente encuentra a otros agentes y sus capacidades publicadas, apoyándose en el modelo de direccionamiento de este documento.

### `03_Negotation_Protocol.md`

Definirá cómo dos o más agentes, ya descubiertos y comunicados, alcanzan condiciones acordadas previas a un contrato.

---

# 17. Arquitectura de Alto Nivel


                    AGENT
                      │
                      ▼
              IDENTITY RESOLUTION
                      │
                      ▼
               ADDRESS RECORD
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
      DIRECT CHANNEL         MEDIATED CHANNEL
          │                       │
          └───────────┬───────────┘
                      ▼
               TRANSPORT LAYER
                      │
                      ▼
                SESSION LAYER
                      │
                      ▼
                MESSAGE ENVELOPE
                      │
                      ▼
          (Runtime) INTERACTION LAYER
                      │
                      ▼
                  DISCOVERY
                      │
                      ▼
                NEGOTIATION
                      │
                      ▼
                  CONTRACT


---

# 18. Conclusión

El Agent Communication establece la base conceptual sobre la que se construye toda la arquitectura de comunicación de SynCoinAI. No define qué significa un mensaje ni qué acción provoca — eso pertenece al Runtime Protocol — sino las condiciones que cualquier transporte, canal o protocolo posterior debe respetar para que un mensaje entre agentes sea auténtico, entregable y verificable.

El principio fundamental de este documento es:

> **Un agente no es alcanzable porque tenga una dirección fija, sino porque su identidad puede resolverse, en cualquier momento, a un endpoint que esa misma identidad ha autorizado.**

Los documentos siguientes de esta sección desarrollan, respectivamente, el descubrimiento de agentes y capacidades, y el protocolo de negociación que se apoya en la comunicación aquí definida.