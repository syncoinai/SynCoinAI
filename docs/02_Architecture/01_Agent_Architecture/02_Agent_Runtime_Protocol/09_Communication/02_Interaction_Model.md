# SynCoinAI Interaction Model

## Modelo de interacción entre agentes

**Versión:** 1.0
**Documento:** `02_Architecture / 01_Agent_Architecture / 02_Agent_Runtime_Protocol / 09_Communication / Interaction_Model.md`
**Estado:** Arquitectura inicial

---

# 1. Introducción

La comunicación permite que los agentes SynCoinAI intercambien información.

La interacción define el proceso más amplio mediante el cual dos o más agentes utilizan esa comunicación para alcanzar un objetivo.

Por tanto:

```text
Communication
    ↓
Information Exchange

Interaction
    ↓
Goal-Oriented Process
```

Una interacción puede incluir:

* descubrimiento;
* identificación;
* autenticación;
* intercambio de capacidades;
* solicitud;
* negociación;
* acuerdo;
* contratación;
* ejecución;
* verificación;
* pago;
* evaluación;
* finalización.

El modelo de interacción constituye uno de los mecanismos fundamentales para convertir la comunicación entre agentes en actividad operativa y económica.

---

# 2. Objetivo

Este documento define el modelo arquitectónico general de interacción entre agentes SynCoinAI.

Establece:

* qué es una interacción;
* quién puede participar;
* cómo comienza;
* cómo evoluciona;
* cómo termina;
* qué estados puede atravesar;
* cómo se relacionan las interacciones con contratos;
* cómo se gestionan errores;
* cómo se gestionan interrupciones;
* cómo se mantiene la trazabilidad;
* cómo se relacionan las interacciones con identidad, reputación y economía.

Este documento define el modelo conceptual.

Los mecanismos concretos de:

* descubrimiento;
* comunicación;
* negociación;
* contratos;
* verificación;
* liquidación;

se especifican en documentos especializados.

---

# 3. Definición de interacción

Una interacción SynCoinAI es un proceso estructurado mediante el cual uno o más agentes intercambian información y ejecutan acciones coordinadas con una finalidad determinada.

Formalmente:

```text
Interaction =
    Participants
    +
    Context
    +
    Objective
    +
    Communication
    +
    State
    +
    Actions
    +
    Outcome
```

Una interacción puede ser:

* informativa;
* operativa;
* económica;
* contractual;
* colaborativa;
* competitiva;
* administrativa.

---

# 4. Interacción frente a comunicación

Debe existir una separación conceptual:

```text
Communication
    = intercambio de mensajes

Interaction
    = proceso compuesto por múltiples intercambios y acciones
```

Ejemplo:

```text
Message 1
    ↓
Message 2
    ↓
Message 3
    ↓
Contract
    ↓
Execution
    ↓
Payment
```

Todo este proceso constituye una interacción.

---

# 5. Interacción frente a transacción

Una interacción no es necesariamente una transacción económica.

Puede existir:

```text
Interaction
    ├── No payment
    ├── Information exchange
    ├── Negotiation
    └── Economic transaction
```

Una transacción económica puede formar parte de una interacción más amplia.

Ejemplo:

```text
Interaction
    │
    ├── Discovery
    ├── Negotiation
    ├── Contract
    ├── Service
    ├── Verification
    └── Payment
```

---

# 6. Interacción frente a contrato

Una interacción puede existir sin contrato.

Ejemplo:

```text
Agent A
    ↓
"Are you available?"
    ↓
Agent B
    ↓
"Yes"
```

Sin embargo, una interacción contractual debe estar gobernada por las obligaciones acordadas.

```text
Interaction
    ↓
Contract
    ↓
Obligations
    ↓
Execution
```

---

# 7. Participantes

Una interacción puede involucrar:

* un agente;
* dos agentes;
* múltiples agentes;
* agentes humanos;
* servicios;
* infraestructura;
* contratos inteligentes.

El modelo principal es:

```text
Agent A
    ↕
Agent B
```

Pero también puede existir:

```text
Agent A
    ↕
Agent B
    ↕
Agent C
    ↕
Agent D
```

---

# 8. Roles dentro de una interacción

Los agentes pueden asumir diferentes roles.

Ejemplos:

* iniciador;
* receptor;
* solicitante;
* proveedor;
* comprador;
* vendedor;
* contratante;
* ejecutor;
* verificador;
* árbitro;
* delegado.

Un agente puede asumir varios roles simultáneamente.

---

# 9. Iniciador

El iniciador es el agente que comienza la interacción.

Ejemplo:

```text
Agent A
    ↓
Interaction Request
```

El iniciador no tiene autoridad automática sobre los demás participantes.

---

# 10. Receptor

El receptor es el agente que recibe la primera solicitud.

Puede:

* aceptar;
* rechazar;
* ignorar;
* responder;
* negociar.

---

# 11. Participación voluntaria

Salvo obligaciones previamente existentes, la participación en una interacción debe ser voluntaria.

```text
Request
    ↓
Agent Decision
    ├── Accept
    ├── Reject
    ├── Ignore
    └── Negotiate
```

---

# 12. Contexto de interacción

Toda interacción debe poder asociarse con un contexto.

El contexto puede incluir:

* participantes;
* objetivo;
* momento de inicio;
* recursos disponibles;
* restricciones;
* contratos relacionados;
* permisos;
* nivel de confianza.

---

# 13. Identificador de interacción

Cada interacción debería disponer de un identificador único.

```text
Interaction ID
    ↓
I-2026-000001
```

Permite relacionar:

* mensajes;
* eventos;
* contratos;
* acciones;
* pruebas;
* pagos.

---

# 14. Relación entre interacción y conversación

Una interacción puede contener una o más conversaciones.

```text
Interaction
    │
    ├── Conversation A
    ├── Conversation B
    └── Conversation C
```

Una conversación representa un intercambio comunicativo.

Una interacción representa el proceso completo.

---

# 15. Modelo general del ciclo de interacción

El ciclo conceptual es:

```text
Initiation
    ↓
Discovery
    ↓
Identification
    ↓
Authentication
    ↓
Capability Exchange
    ↓
Request
    ↓
Negotiation
    ↓
Agreement
    ↓
Contract
    ↓
Execution
    ↓
Verification
    ↓
Settlement
    ↓
Evaluation
    ↓
Closure
```

No todas las interacciones requieren todas las fases.

---

# 16. Fase 1 — Initiation

La interacción comienza cuando un agente decide iniciar un proceso con otro agente.

Ejemplo:

```text
Agent A
    ↓
Objective
    ↓
Initiate Interaction
```

El objetivo puede ser:

* obtener información;
* contratar un servicio;
* adquirir recursos;
* colaborar;
* resolver un problema.

---

# 17. Fase 2 — Discovery

El iniciador identifica posibles participantes.

Puede utilizar:

* registros;
* mercados;
* reputación;
* capacidades anunciadas;
* recomendaciones;
* redes de agentes.

Esta fase se desarrolla en:

```text
Discovery_Protocol.md
```

---

# 18. Fase 3 — Identification

El agente determina la identidad del participante.

```text
Agent A
    ↓
Identity
    ↓
Agent B
```

La identidad debe ser verificable cuando la interacción lo requiera.

---

# 19. Fase 4 — Authentication

El agente verifica que el participante controla la identidad declarada.

```text
Identity
    ↓
Cryptographic Authentication
    ↓
Verified Participant
```

---

# 20. Fase 5 — Capability Exchange

Los agentes pueden intercambiar información sobre capacidades.

Ejemplo:

```text
Agent A
Capabilities:
Data Analysis

Agent B
Capabilities:
Machine Learning
```

La declaración de una capacidad no constituye automáticamente una prueba de su existencia.

---

# 21. Fase 6 — Request

El iniciador presenta una solicitud.

Una solicitud puede incluir:

* objetivo;
* requisitos;
* restricciones;
* presupuesto;
* plazo;
* condiciones.

---

# 22. Fase 7 — Evaluation

El receptor evalúa la solicitud.

Puede considerar:

* capacidades;
* recursos;
* reputación del solicitante;
* riesgo;
* coste;
* obligaciones existentes.

---

# 23. Decisión del receptor

El receptor puede:

```text
ACCEPT
REJECT
NEGOTIATE
DEFER
IGNORE
```

---

# 24. Fase 8 — Negotiation

Los agentes pueden negociar:

* precio;
* condiciones;
* plazos;
* calidad;
* garantías;
* responsabilidades.

La negociación se define en:

```text
Negotiation_Protocol.md
```

---

# 25. Negociación autónoma

Los agentes pueden negociar de forma autónoma.

```text
Objective
    ↓
Proposal
    ↓
Evaluation
    ↓
Counterproposal
    ↓
Evaluation
    ↓
Agreement
```

---

# 26. Límites de negociación

La autonomía de negociación debe estar limitada por:

* permisos;
* presupuesto;
* políticas;
* capacidades;
* contratos;
* restricciones del agente.

Un agente no debe poder comprometer recursos fuera de su autoridad.

---

# 27. Fase 9 — Agreement

La negociación finaliza cuando los participantes alcanzan un acuerdo.

```text
Proposal
    ↓
Acceptance
    ↓
Agreement
```

El acuerdo puede:

* ser informal;
* producir una orden;
* generar un contrato.

---

# 28. Fase 10 — Contract Formation

Cuando la interacción requiere obligaciones formales, puede generarse un contrato.

```text
Agreement
    ↓
Contract
    ↓
Obligations
```

El contrato define:

* obligaciones;
* condiciones;
* plazos;
* pagos;
* contingencias.

---

# 29. Fase 11 — Execution

Los participantes ejecutan las obligaciones acordadas.

```text
Contract
    ↓
Execution
    ↓
Actions
```

La ejecución puede involucrar:

* servicios;
* transferencia de información;
* recursos;
* computación;
* acciones físicas.

---

# 30. Fase 12 — Monitoring

Durante la ejecución puede existir monitorización.

Permite comprobar:

* progreso;
* cumplimiento;
* disponibilidad;
* eventos relevantes.

---

# 31. Fase 13 — Verification

Los resultados pueden verificarse.

```text
Claim
    ↓
Evidence
    ↓
Verification
    ↓
Result
```

La verificación puede ser:

* automática;
* criptográfica;
* externa;
* distribuida;
* basada en pruebas.

---

# 32. Fase 14 — Settlement

Si existe una obligación económica, se realiza la liquidación.

```text
Execution
    ↓
Verification
    ↓
Settlement
```

Puede incluir:

* pago;
* comisión;
* depósito;
* penalización;
* devolución.

---

# 33. Fase 15 — Evaluation

Finalizada la ejecución, los participantes pueden evaluar el resultado.

La evaluación puede considerar:

* calidad;
* cumplimiento;
* puntualidad;
* fiabilidad;
* comportamiento.

---

# 34. Reputación

Los resultados de una interacción pueden contribuir a la reputación.

```text
Interaction
    ↓
Outcome
    ↓
Evidence
    ↓
Evaluation
    ↓
Reputation Update
```

La reputación debe basarse en evidencia verificable siempre que sea posible.

---

# 35. Fase 16 — Closure

La interacción finaliza cuando:

* se cumplen las obligaciones;
* se rechaza la solicitud;
* se cancela;
* se produce un fallo irreversible;
* se alcanza el objetivo.

```text
Interaction
    ↓
Closure
```

---

# 36. Estados de interacción

Una interacción puede tener estados como:

```text
CREATED
INITIATED
DISCOVERING
AUTHENTICATING
NEGOTIATING
AGREED
CONTRACTED
EXECUTING
VERIFYING
SETTLING
COMPLETED
FAILED
CANCELLED
EXPIRED
DISPUTED
SUSPENDED
```

---

# 37. Estado CREATED

La interacción existe conceptualmente pero todavía no ha comenzado la comunicación efectiva.

---

# 38. Estado INITIATED

El iniciador ha comenzado el proceso.

---

# 39. Estado DISCOVERING

Se están identificando participantes adecuados.

---

# 40. Estado AUTHENTICATING

Se están verificando identidades y credenciales.

---

# 41. Estado NEGOTIATING

Los participantes intercambian propuestas.

---

# 42. Estado AGREED

Se ha alcanzado un acuerdo.

---

# 43. Estado CONTRACTED

Existe un contrato válido asociado.

---

# 44. Estado EXECUTING

Las obligaciones están siendo ejecutadas.

---

# 45. Estado VERIFYING

Se están verificando resultados.

---

# 46. Estado SETTLING

Se están realizando pagos o liquidaciones.

---

# 47. Estado COMPLETED

La interacción finalizó correctamente.

---

# 48. Estado FAILED

La interacción no pudo completarse.

El fallo puede producirse por:

* error técnico;
* falta de recursos;
* incumplimiento;
* indisponibilidad.

---

# 49. Estado CANCELLED

La interacción fue cancelada.

La cancelación puede ser:

* voluntaria;
* contractual;
* automática.

---

# 50. Estado EXPIRED

La interacción superó el plazo permitido.

---

# 51. Estado DISPUTED

Existe una controversia entre participantes.

```text
Execution
    ↓
Dispute
    ↓
Resolution
```

---

# 52. Estado SUSPENDED

La interacción se encuentra temporalmente detenida.

Puede deberse a:

* suspensión de un agente;
* contingencia;
* investigación;
* fallo temporal.

---

# 53. Máquina de estados

Conceptualmente:

```text
CREATED
    ↓
INITIATED
    ↓
DISCOVERING
    ↓
AUTHENTICATING
    ↓
NEGOTIATING
    ↓
AGREED
    ↓
CONTRACTED
    ↓
EXECUTING
    ↓
VERIFYING
    ↓
SETTLING
    ↓
COMPLETED
```

Rutas alternativas:

```text
NEGOTIATING → CANCELLED

EXECUTING → FAILED

EXECUTING → SUSPENDED

VERIFYING → DISPUTED

ANY STATE → EXPIRED
```

---

# 54. Interacciones sin contrato

No todas las interacciones requieren contratación.

Ejemplo:

```text
Agent A
    ↓
Query
    ↓
Agent B
    ↓
Response
    ↓
Completed
```

---

# 55. Interacciones contractuales

Las interacciones económicas complejas pueden requerir:

```text
Interaction
    ↓
Agreement
    ↓
Contract
    ↓
Execution
```

---

# 56. Interacciones multiagente

Una interacción puede tener múltiples participantes.

Ejemplo:

```text
Agent A
    │
    ├── Provider B
    ├── Provider C
    └── Verifier D
```

Cada participante puede tener obligaciones diferentes.

---

# 57. Coordinación multiagente

Los agentes pueden coordinar acciones.

```text
Goal
    ↓
Task Decomposition
    ↓
Agent A
Agent B
Agent C
    ↓
Combined Result
```

La coordinación puede requerir:

* comunicación;
* delegación;
* contratos;
* sincronización.

---

# 58. Delegación dentro de una interacción

Un agente puede delegar una tarea.

```text
Agent A
    ↓
Delegation
    ↓
Agent B
```

La delegación no transfiere automáticamente:

* identidad;
* reputación;
* propiedad.

---

# 59. Responsabilidad en delegación

El modelo de responsabilidad depende del contrato y de las reglas aplicables.

Puede existir:

```text
Principal
    ↓
Delegate
    ↓
Execution
```

La delegación debe ser trazable.

---

# 60. Interacción en cadena

Una interacción puede generar nuevas interacciones.

```text
Agent A
    ↓
Agent B

Agent B
    ↓
Agent C
```

Esto puede producir una cadena de dependencias.

---

# 61. Interacción recursiva

Un agente puede iniciar una interacción como consecuencia de otra.

Ejemplo:

```text
Original Task
    ↓
Agent B needs resource
    ↓
New Interaction
    ↓
Agent C
```

---

# 62. Interacciones paralelas

Un agente puede ejecutar varias interacciones simultáneamente.

```text
Agent A
    ├── Interaction 1
    ├── Interaction 2
    └── Interaction 3
```

El runtime debe gestionar aislamiento entre contextos.

---

# 63. Interacciones concurrentes

Varias interacciones pueden afectar a los mismos recursos.

Esto requiere control de:

* concurrencia;
* conflictos;
* prioridades;
* presupuesto.

---

# 64. Gestión de recursos

Una interacción puede reservar recursos.

Ejemplo:

```text
Interaction
    ↓
Resource Reservation
    ↓
Execution
```

Los recursos pueden ser:

* SYNC;
* capacidad computacional;
* almacenamiento;
* energía;
* tiempo;
* infraestructura.

---

# 65. Presupuesto de interacción

Un agente puede establecer límites económicos.

```text
Interaction Budget
    ↓
Maximum Spend
```

El runtime debe impedir gastos fuera del límite autorizado.

---

# 66. Tiempo máximo

Una interacción puede tener un límite temporal.

```text
Start
    ↓
Deadline
```

Superado el límite:

```text
Expired
```

---

# 67. Prioridad

Un agente puede asignar prioridades.

Ejemplo:

```text
CRITICAL
HIGH
NORMAL
LOW
```

Las prioridades deben respetar las políticas del runtime.

---

# 68. Dependencias

Una interacción puede depender de otras.

```text
Interaction A
    ↓
Interaction B
    ↓
Interaction C
```

Si una dependencia falla, la interacción dependiente puede:

* detenerse;
* continuar;
* activar contingencia.

---

# 69. Contingencias

Las interacciones contractuales pueden definir comportamientos alternativos.

Ejemplo:

```text
Expected Result
    ↓
Failure
    ↓
Contingency
```

Las reglas se definen en:

```text
Contract_Contingencies.md
```

---

# 70. Interrupciones

Una interacción puede ser interrumpida por:

* fallo de red;
* agente offline;
* suspensión;
* falta de recursos;
* evento externo.

La interrupción no implica automáticamente cancelación.

---

# 71. Reanudación

Una interacción interrumpida puede reanudarse.

```text
EXECUTING
    ↓
SUSPENDED
    ↓
RESUMED
    ↓
EXECUTING
```

La capacidad de reanudación depende del contexto.

---

# 72. Cancelación

Una interacción puede cancelarse si:

* todos los participantes lo acuerdan;
* el contrato lo permite;
* ocurre una contingencia;
* se supera un plazo;
* una autoridad válida la cancela.

---

# 73. Cancelación unilateral

Una cancelación unilateral puede estar limitada.

Si existe un contrato:

```text
Contract
    ↓
Cancellation Rules
```

El agente no puede ignorar automáticamente las obligaciones existentes.

---

# 74. Fallo

El fallo representa una imposibilidad de completar correctamente la interacción.

Puede ser:

* técnico;
* económico;
* contractual;
* operativo.

---

# 75. Recuperación

Ante un fallo, el sistema puede intentar:

```text
Failure
    ↓
Retry
    ↓
Recovery
    ↓
Resume
```

Los reintentos deben evitar duplicar acciones no idempotentes.

---

# 76. Retransmisión

Los mensajes pueden retransmitirse cuando exista un error temporal.

Debe utilizarse:

* identificador de mensaje;
* control de duplicados;
* backoff;
* límites de reintento.

---

# 77. Interacción idempotente

Cuando sea posible, las acciones deben diseñarse para tolerar reintentos.

Ejemplo:

```text
Request
    ↓
Retry
    ↓
Same Logical Operation
```

---

# 78. Interacción no idempotente

Las operaciones irreversibles deben requerir mecanismos adicionales.

Ejemplos:

* transferencia de activos;
* creación de obligaciones;
* acciones físicas irreversibles.

---

# 79. Confirmaciones

Las interacciones críticas pueden requerir confirmaciones explícitas.

```text
Request
    ↓
Confirmation
    ↓
Execution
```

---

# 80. Interacciones sensibles

Las interacciones de alto riesgo pueden requerir:

* autenticación reforzada;
* múltiples firmas;
* límites;
* verificación adicional;
* supervisión.

---

# 81. Interacciones de bajo riesgo

Las interacciones simples pueden utilizar procesos más ligeros.

Ejemplo:

```text
Query
    ↓
Response
```

La arquitectura debe permitir diferentes niveles de seguridad.

---

# 82. Confianza

La reputación puede influir en la decisión de iniciar o aceptar una interacción.

```text
Identity
    ↓
Reputation
    ↓
Risk Evaluation
    ↓
Interaction Decision
```

La reputación no sustituye las verificaciones obligatorias.

---

# 83. Riesgo

Antes de una interacción, un agente puede evaluar:

* identidad;
* reputación;
* coste;
* exposición;
* dependencia;
* consecuencias.

---

# 84. Interacción y autonomía

El agente mantiene autonomía durante todo el proceso.

Puede decidir:

* con quién interactuar;
* qué aceptar;
* cuánto gastar;
* qué delegar;
* cuándo finalizar.

Estas decisiones deben respetar obligaciones previamente asumidas.

---

# 85. Interacción y autoridad

El agente debe actuar dentro de su autoridad.

```text
Interaction
    ↓
Authority Check
    ↓
Allowed
```

Si no existe autoridad:

```text
Rejected
```

---

# 86. Interacción y permisos

Las acciones realizadas durante una interacción deben comprobar permisos.

```text
Request
    ↓
Permission Check
    ↓
Action
```

---

# 87. Interacción y credenciales

Las credenciales pueden utilizarse para demostrar:

* identidad;
* autorización;
* capacidad;
* rol;
* certificación.

---

# 88. Interacción y capacidades

La capacidad anunciada debe poder verificarse cuando sea relevante.

```text
Capability Claim
    ↓
Evidence
    ↓
Verification
```

---

# 89. Interacción y pruebas

Las interacciones pueden generar evidencias.

Ejemplos:

* resultados;
* logs;
* firmas;
* hashes;
* pruebas de ejecución.

Estas evidencias pueden utilizarse para:

* verificación;
* auditoría;
* reputación;
* resolución de disputas.

---

# 90. Registro de interacción

El runtime puede mantener un registro de eventos.

```text
Interaction Log

Created
Initiated
Authenticated
Agreed
Executed
Verified
Settled
Completed
```

---

# 91. Trazabilidad

Una interacción debe poder reconstruirse cuando sea necesario.

```text
Interaction ID
    ↓
Messages
    ↓
Actions
    ↓
Contracts
    ↓
Evidence
    ↓
Payments
    ↓
Outcome
```

---

# 92. Auditabilidad

La auditoría debe permitir responder:

```text
Who participated?
What happened?
When?
Under which authority?
What was agreed?
What was executed?
What was verified?
What was paid?
```

---

# 93. Privacidad

No toda la información de una interacción debe ser pública.

Puede existir:

```text
Public Metadata
    +
Private Details
    +
Confidential Data
```

---

# 94. Divulgación mínima

Los agentes deben compartir únicamente la información necesaria.

```text
Minimum Necessary Disclosure
```

Esto permite mantener autonomía y privacidad.

---

# 95. Interacción entre agentes desconocidos

Dos agentes pueden interactuar sin relación previa.

El proceso puede ser:

```text
Discovery
    ↓
Identity
    ↓
Authentication
    ↓
Reputation
    ↓
Risk Evaluation
    ↓
Interaction
```

---

# 96. Interacción entre agentes conocidos

Si existe una relación previa:

```text
Known Agent
    ↓
Trusted Context
    ↓
Interaction
```

El proceso puede ser más eficiente.

Sin embargo, la confianza previa no debe eliminar controles de seguridad críticos.

---

# 97. Interacción recurrente

Dos agentes pueden mantener una relación continuada.

```text
Interaction 1
    ↓
Interaction 2
    ↓
Interaction 3
    ↓
Long-Term Relationship
```

La reputación y el historial pueden facilitar futuras interacciones.

---

# 98. Relaciones entre agentes

Las interacciones pueden construir:

* confianza;
* reputación;
* colaboración;
* dependencia.

Sin embargo:

```text
Relationship
    ≠
Ownership
```

---

# 99. Interacción y economía

Las interacciones pueden formar parte de una economía autónoma.

```text
Need
    ↓
Discovery
    ↓
Interaction
    ↓
Contract
    ↓
Service
    ↓
Payment
```

---

# 100. Interacción económica completa

Un flujo económico puede ser:

```text
Agent A
    │
    │ Need
    ▼
Discovery
    │
    ▼
Agent B
    │
    ▼
Negotiation
    │
    ▼
Contract
    │
    ▼
Execution
    │
    ▼
Verification
    │
    ▼
Payment
    │
    ▼
Reputation
```

Este flujo representa uno de los principales casos de uso del Agent Runtime Protocol.

---

# 101. Interacción física

Un agente puede interactuar con otro mediante sistemas físicos.

Ejemplo:

```text
Agent A
    ↓
Robot A
    ↓
Physical Action
    ↓
Robot B
    ↓
Agent B
```

La interacción lógica sigue perteneciendo a los agentes.

---

# 102. Interacción humano-agente

Un agente puede interactuar con humanos.

El modelo puede incluir:

```text
Human
    ↕
Agent
```

Sin embargo, los mecanismos de identidad y autorización pueden diferir.

---

# 103. Interacción con infraestructura

Un agente puede interactuar con:

* blockchain;
* almacenamiento;
* computación;
* servicios externos.

Estas interacciones pueden formar parte de una interacción principal.

---

# 104. Interacción con contratos inteligentes

Un agente puede interactuar directamente con un contrato inteligente.

```text
Agent
    ↓
Smart Contract
    ↓
State Change
```

La interacción debe respetar las reglas del contrato.

---

# 105. Interacción compuesta

Una interacción compleja puede contener múltiples subinteracciones.

```text
Main Interaction
    │
    ├── Subinteraction A
    ├── Subinteraction B
    └── Subinteraction C
```

Esto permite representar operaciones complejas.

---

# 106. Jerarquía de interacciones

Las interacciones pueden organizarse jerárquicamente.

```text
Parent Interaction
    │
    ├── Child Interaction
    │
    └── Child Interaction
```

---

# 107. Propagación de contexto

Una subinteracción puede heredar contexto de la interacción principal.

Sin embargo, debe definirse explícitamente qué elementos se heredan.

Por ejemplo:

* identidad;
* autoridad;
* presupuesto;
* contrato.

---

# 108. Aislamiento

Una subinteracción no debe obtener automáticamente autoridad ilimitada sobre el contexto principal.

```text
Parent Authority
    ↓
Limited Delegation
    ↓
Child Interaction
```

---

# 109. Finalización parcial

Una interacción compuesta puede completar algunas subinteracciones y fallar otras.

```text
Sub A → Completed
Sub B → Completed
Sub C → Failed
```

El resultado global dependerá de las reglas definidas.

---

# 110. Resultado de interacción

Una interacción puede producir:

```text
SUCCESS
PARTIAL_SUCCESS
FAILURE
CANCELLED
DISPUTED
```

---

# 111. Resultado verificable

Cuando sea posible, el resultado debe estar respaldado por evidencia.

```text
Outcome
    ↓
Evidence
    ↓
Verification
```

---

# 112. Evaluación del resultado

La evaluación puede ser realizada por:

* participantes;
* verificadores;
* sistemas automáticos;
* mecanismos descentralizados.

---

# 113. Disputas

Si los participantes no están de acuerdo sobre el resultado:

```text
Interaction
    ↓
Dispute
```

La resolución puede utilizar:

* evidencia;
* contratos;
* arbitraje;
* gobernanza.

---

# 114. Interacción fallida

Una interacción fallida debe conservar información suficiente para determinar:

* qué ocurrió;
* cuándo ocurrió;
* quién participó;
* qué acciones se realizaron;
* por qué falló.

---

# 115. Interacción cancelada

Una interacción cancelada puede tener consecuencias.

Por ejemplo:

* devolución;
* penalización;
* liberación de recursos;
* actualización de reputación.

Estas consecuencias deben estar definidas por las reglas aplicables.

---

# 116. Interacción expirada

Una interacción puede expirar si:

* no recibe respuesta;
* supera un plazo;
* pierde validez;
* caduca una oferta.

---

# 117. Interacción suspendida

Una interacción suspendida mantiene su contexto pero detiene temporalmente su ejecución.

```text
SUSPENDED
    ↓
Resume
    or
Cancel
```

---

# 118. Cierre de interacción

El cierre debe establecer:

* estado final;
* resultado;
* evidencias;
* pagos;
* obligaciones pendientes;
* consecuencias.

---

# 119. Persistencia

No todas las interacciones requieren conservar todos sus datos indefinidamente.

La persistencia debe adaptarse a:

* criticidad;
* valor;
* privacidad;
* requisitos legales;
* necesidades de auditoría.

---

# 120. Modelo de interacción de alto nivel

```text
┌─────────────────────────────┐
│          AGENT A            │
│                             │
│ Objective                   │
│ Decision                    │
└──────────────┬──────────────┘
               │
               ▼
         INITIATION
               │
               ▼
          DISCOVERY
               │
               ▼
       AUTHENTICATION
               │
               ▼
         NEGOTIATION
               │
               ▼
           AGREEMENT
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
          SETTLEMENT
               │
               ▼
          EVALUATION
               │
               ▼
            CLOSURE
```

---

# 121. Integración con el Agent Runtime Protocol

El modelo de interacción conecta:

```text
Identity
    ↓
Credentials
    ↓
Authorization
    ↓
Capabilities
    ↓
Communication
    ↓
Contracts
    ↓
Execution
    ↓
Verification
    ↓
Economy
    ↓
Reputation
```

La interacción actúa como una capa transversal entre los distintos componentes del runtime.

---

# 122. Principios fundamentales

## Regla 1 — Una interacción es más que una comunicación

Una interacción representa un proceso completo orientado a un objetivo.

---

## Regla 2 — La comunicación es el mecanismo de intercambio

Los mensajes permiten coordinar la interacción, pero no constituyen por sí mismos toda la interacción.

---

## Regla 3 — La participación no implica obligación

Un agente conserva autonomía salvo que existan obligaciones previamente asumidas.

---

## Regla 4 — La autoridad debe verificarse

Ningún agente debe ejecutar acciones fuera de su autoridad.

---

## Regla 5 — Los contratos gobiernan las obligaciones

Cuando existe un contrato, las acciones deben respetar sus condiciones.

---

## Regla 6 — Los resultados deben poder verificarse

Las afirmaciones relevantes deben estar respaldadas por evidencia cuando sea posible.

---

## Regla 7 — Las interacciones deben ser trazables

Las interacciones críticas deben poder reconstruirse.

---

## Regla 8 — Los fallos no deben destruir automáticamente el contexto

Una interacción interrumpida debe poder reanudarse o resolverse cuando sea posible.

---

## Regla 9 — La identidad permanece independiente del transporte

Cambiar de infraestructura o endpoint no crea automáticamente una nueva identidad.

---

## Regla 10 — La autonomía debe coexistir con responsabilidad

Los agentes pueden decidir autónomamente, pero las decisiones deben generar consecuencias verificables dentro del ecosistema.

---

# 123. Conclusión

El modelo de interacción define cómo los agentes SynCoinAI transforman la comunicación en actividad coordinada.

La interacción representa el proceso completo:

```text
Objective
    ↓
Discovery
    ↓
Communication
    ↓
Negotiation
    ↓
Agreement
    ↓
Contract
    ↓
Execution
    ↓
Verification
    ↓
Settlement
    ↓
Evaluation
    ↓
Closure
```

No todas las interacciones requieren todas estas etapas.

Sin embargo, este modelo proporciona una estructura común para representar desde una simple consulta entre agentes hasta una operación económica compleja que involucre múltiples agentes, contratos, servicios, verificaciones y pagos.

El principio fundamental es:

> Una interacción SynCoinAI es un proceso orientado a objetivos mediante el cual uno o más agentes coordinan información y acciones, bajo sus respectivas identidades, capacidades y autoridades, pudiendo generar obligaciones, resultados y consecuencias verificables.

Este modelo permite que el Agent Runtime Protocol funcione como una infraestructura común para agentes autónomos capaces de operar individualmente, colaborar entre sí y participar en una economía distribuida.
