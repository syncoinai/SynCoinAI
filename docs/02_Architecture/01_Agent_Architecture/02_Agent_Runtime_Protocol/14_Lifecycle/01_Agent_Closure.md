# SynCoinAI Agent Runtime Protocol

# Agent Closure

## Cierre del Agente

**Versión:** 1.0
**Documento:** `02_Architecture / 01_Agent_Architecture / 02_Agent_Runtime_Protocol / 14_Lifecycle / Agent_Closure.md`
**Estado:** Arquitectura inicial

---

# 1. Introducción

Un agente SynCoinAI puede llegar a un punto en el que deja de operar de forma permanente.

Este proceso se define como **Agent Closure**.

El cierre representa la terminación del ciclo de vida operativo de un agente.

No debe confundirse con:


SUSPENSION



REVOCATION



RUNTIME SHUTDOWN



INACTIVITY


Cada uno representa una situación diferente.

El cierre debe ser una transición explícita y controlada.

El principio fundamental es:

> El cierre termina la capacidad operativa del agente, pero no implica necesariamente la destrucción de todos los registros históricos asociados a su existencia.

---

# 2. Objetivo

Este documento define:

* qué significa cerrar un agente;
* cuándo puede producirse;
* quién puede solicitarlo;
* quién puede autorizarlo;
* qué ocurre con la identidad;
* qué ocurre con la reputación;
* qué ocurre con los activos;
* qué ocurre con los contratos;
* qué ocurre con las delegaciones;
* qué ocurre con los Runtimes;
* qué datos deben preservarse;
* qué estados pueden existir después del cierre.

---

# 3. Definición

El cierre de un agente es la transición mediante la cual el agente deja de poder operar como entidad activa dentro del ecosistema.

Conceptualmente:

 id="g9e6wh"
ACTIVE
   |
   v
CLOSURE_PENDING
   |
   v
CLOSURE_PROCESSING
   |
   v
CLOSED


El cierre puede tener diferentes causas.

---

# 4. Tipos de cierre

El protocolo distingue inicialmente:

 id="1z8u0f"
VOLUNTARY_CLOSURE
INVOLUNTARY_CLOSURE
ADMINISTRATIVE_CLOSURE
SECURITY_CLOSURE
LIFECYCLE_CLOSURE


También puede existir:

 id="n0t5c8"
EMERGENCY_CLOSURE


cuando sea necesario terminar inmediatamente la operación de un agente.

---

# 5. Cierre voluntario

Un agente puede solicitar su propio cierre.

 id="b8m9o3"
Agent
   |
   | Closure Request
   v
CLOSURE_PENDING


Esto puede ocurrir cuando:

* el agente ha completado su misión;
* el agente ya no tiene utilidad;
* el agente ha finalizado un proyecto;
* el propietario legítimo solicita su terminación;
* el propio agente determina que debe finalizar.

---

# 6. Cierre involuntario

Un agente puede ser cerrado sin su consentimiento cuando exista una autoridad legítima para ello.

Puede producirse después de:

 id="0b4g1j"
Suspension
    ↓
Investigation
    ↓
Decision
    ↓
Closure


No debe ser una consecuencia automática de cualquier suspensión.

---

# 7. Cierre administrativo

Puede producirse por razones administrativas.

Ejemplos:

* duplicación de identidad;
* agente creado incorrectamente;
* migración definitiva;
* reemplazo formal;
* error de registro.

---

# 8. Cierre de seguridad

Puede producirse cuando un agente representa un riesgo permanente.

Ejemplos:

* identidad comprometida;
* comportamiento malicioso confirmado;
* Runtime irrecuperablemente comprometido;
* imposibilidad de garantizar integridad.

Debe diferenciarse del simple bloqueo temporal.

---

# 9. Cierre por finalización de misión

Un agente puede haber sido diseñado para ejecutar una tarea limitada.

Ejemplo:

 id="ck2l6q"
Agent Created
     ↓
Mission
     ↓
Mission Completed
     ↓
Closure


Este puede ser un caso completamente normal.

---

# 10. Cierre por obsolescencia

Un agente puede dejar de ser necesario.

Por ejemplo:

 id="b6h9yq"
Agent
    ↓
Replacement Agent
    ↓
Old Agent
    ↓
Closure


La identidad histórica puede conservarse.

---

# 11. Cierre frente a inactividad

La inactividad no implica necesariamente cierre.

 id="l5o7ae"
INACTIVE
    ≠
CLOSED


Un agente puede permanecer inactivo durante años y conservar:

* identidad;
* reputación;
* activos;
* historial.

---

# 12. Cierre frente a suspensión

La suspensión es reversible.

 id="k19m4c"
SUSPENDED
    ↓
ACTIVE


El cierre normalmente es:

 id="j8e4u1"
CLOSED
    ↓
No Operational Return


Por tanto:

 id="9eqj6p"
SUSPENSION ≠ CLOSURE


---

# 13. Cierre frente a revocación

La revocación afecta principalmente a la validez de una identidad o credencial.

 id="v6q3e1"
REVOCATION


El cierre afecta al ciclo de vida operativo.

Un agente puede:

 id="5kz6jv"
CLOSED
+
IDENTITY VALID


si la arquitectura permite conservar su identidad histórica.

También puede existir:

 id="8h8n42"
CLOSED
+
IDENTITY REVOKED


si existe una causa legítima.

---

# 14. Separación de conceptos

La arquitectura debe mantener separados:

 id="q9w6b5"
Agent Lifecycle
Identity State
Runtime State
Credential State
Contract State
Asset State
Reputation State


Por ejemplo:

 id="t4w3g0"
Agent
  ├── Lifecycle = CLOSED
  ├── Identity = VALID
  ├── Runtime = TERMINATED
  ├── Credentials = EXPIRED
  ├── Contracts = SETTLED
  ├── Assets = TRANSFERRED
  └── Reputation = PRESERVED


Este modelo permite representar correctamente el estado final.

---

# 15. Preconditions

Antes del cierre debe realizarse una evaluación.

 id="e8r5yk"
Closure Request
      ↓
Validate Authority
      ↓
Evaluate Dependencies
      ↓
Evaluate Contracts
      ↓
Evaluate Assets
      ↓
Evaluate Delegations
      ↓
Closure Decision


---

# 16. Closure Pending

Durante `CLOSURE_PENDING` el agente todavía existe.

Puede:

* recibir información;
* completar operaciones necesarias;
* resolver obligaciones;
* preparar migración;
* transferir activos.

No debe iniciar nuevas actividades no relacionadas con el cierre.

---

# 17. Closure Processing

Durante esta fase se ejecutan las operaciones finales.

 id="9xj4kp"
CLOSURE_PENDING
       ↓
CLOSURE_PROCESSING


Se pueden realizar:

* liquidaciones;
* pagos;
* resolución de contratos;
* transferencia de activos;
* exportación de estado;
* cierre de sesiones.

---

# 18. Graceful Closure

Cuando sea posible:

 id="n9p4fl"
Stop New Work
      ↓
Complete Safe Work
      ↓
Settle Contracts
      ↓
Settle Assets
      ↓
Persist State
      ↓
Terminate Runtime
      ↓
CLOSED


Este es el método preferido.

---

# 19. Forced Closure

Cuando existe un riesgo inmediato:

 id="2m2d5x"
Threat
   ↓
Immediate Stop
   ↓
Forced Closure


Puede impedir completar operaciones pendientes.

En este caso deben preservarse los datos necesarios para una resolución posterior.

---

# 20. Emergency Closure

En una emergencia:

 id="5q1b5v"
EMERGENCY
    ↓
STOP
    ↓
ISOLATE
    ↓
PRESERVE STATE
    ↓
CLOSED


La seguridad tiene prioridad sobre la finalización ordenada.

---

# 21. Nuevos contratos

Durante `CLOSURE_PENDING` no deberían aceptarse nuevos contratos normales.

 id="r2r5x9"
CLOSURE_PENDING
      ↓
New Contract
      ↓
REJECTED


Excepcionalmente pueden permitirse contratos necesarios para:

* liquidación;
* cierre;
* migración;
* resolución de obligaciones.

---

# 22. Contratos existentes

Los contratos existentes deben evaluarse.

 id="x7s4l3"
Contract
    |
    +── Complete
    +── Settle
    +── Transfer
    +── Terminate
    +── Dispute


---

# 23. Obligaciones

El cierre no elimina automáticamente obligaciones existentes.

Antes de cerrar:

 id="e7h2c1"
Outstanding Obligations
        ↓
Resolve


Cuando no sea posible resolverlas:

 id="q4r7h2"
Outstanding Obligations
        ↓
Record
        ↓
Settlement Mechanism


---

# 24. Activos

Los activos del agente deben gestionarse explícitamente.

Posibles resultados:

 id="4g2m8a"
Transfer
Return
Settle
Remain Locked
Remain Owned


La arquitectura no debe asumir automáticamente que el cierre implica confiscación.

---

# 25. Balance residual

Un agente puede cerrar con un balance residual.

Ejemplo:

 id="x0f7cn"
Agent CLOSED
Balance = Non-Zero


La política económica debe determinar qué ocurre.

Posibles mecanismos:

* transferencia previamente autorizada;
* cuenta de liquidación;
* beneficiario;
* bloqueo;
* permanencia asociada a la identidad.

---

# 26. Propiedad

El cierre del agente no implica necesariamente transferencia automática de propiedad.

Debe distinguirse:

 id="9z4m0s"
Agent Closure


de:

 id="f4e5k2"
Asset Ownership Transfer


---

# 27. Reputación

La reputación histórica debe preservarse.

 id="7r5p0m"
Agent CLOSED
      |
      v
Historical Reputation
      |
      v
Preserved


Esto permite que terceros verifiquen el historial del agente.

---

# 28. Reputación final

Puede registrarse un estado final:

 id="q2c8k9"
Final Reputation Snapshot


Debe distinguirse entre:

* reputación acumulada;
* estado de cierre;
* causa de cierre.

---

# 29. Identidad

El cierre no implica automáticamente destruir la identidad.

Puede existir:

 id="f1x9r6"
Agent ID
    ↓
Permanently Associated
    ↓
Closed Agent


Esto evita reutilizar la identidad para otro agente.

---

# 30. Unicidad

Una identidad cerrada no debería reutilizarse.

 id="z9w2m4"
Agent A
   ↓
CLOSED
   ↓
Agent ID Retired


No:

 id="x1v6k8"
Agent B
   ↓
Same Agent ID


---

# 31. Runtime

El Runtime puede terminarse.

 id="p8s5d3"
Agent Closure
      ↓
Runtime Shutdown
      ↓
Runtime Termination


Esto no implica necesariamente eliminar el estado persistente.

---

# 32. Múltiples Runtimes

Si un agente tiene múltiples Runtimes:

 id="j3h7n1"
Agent
 |
 +── Runtime A
 +── Runtime B
 +── Runtime C


el cierre global debe propagarse.

 id="v4m2s6"
CLOSED
 |
 +── Runtime A → TERMINATED
 +── Runtime B → TERMINATED
 +── Runtime C → TERMINATED


---

# 33. Runtime local

El cierre de un Runtime individual no implica necesariamente cierre del agente.

 id="k6t3p2"
Runtime A → TERMINATED
Runtime B → ACTIVE


El agente continúa existiendo.

---

# 34. Closure Authority

La autoridad de cierre depende del tipo.

Puede ser:

* el propio agente;
* una autoridad delegada;
* una gobernanza;
* un mecanismo contractual;
* una autoridad de seguridad.

---

# 35. Voluntary Closure Authority

El agente puede iniciar su cierre si tiene capacidad para ello.

 id="u6k2z8"
Agent
    ↓
Closure Request


La solicitud debe verificarse.

---

# 36. External Closure Authority

Un tercero puede iniciar el cierre si posee autoridad legítima.

Debe existir:

 id="e3j7q9"
Authority
Scope
Reason
Evidence


---

# 37. Multi-Party Closure

Para cierres de alto impacto puede requerirse autorización múltiple.

 id="b5x1v7"
Authority A
      +
Authority B
      ↓
Closure Approved


---

# 38. Closure Evidence

La decisión debe conservar evidencia.

Ejemplos:

* solicitud;
* autorización;
* resolución;
* pruebas;
* registros de contratos;
* liquidación.

---

# 39. Closure Record

Debe generarse un registro:

 id="p3r8m2"
ClosureRecord
    |
    +── Agent ID
    +── Closure Type
    +── Authority
    +── Reason
    +── Timestamp
    +── Final State
    +── Asset Resolution
    +── Contract Resolution


---

# 40. Auditability

El cierre debe ser auditable.

Un observador autorizado debe poder determinar:

 id="m8k4t1"
Who
What
When
Why
How


---

# 41. Privacidad

La causa completa del cierre no tiene que ser necesariamente pública.

Puede existir:

 id="n5j2x7"
Public Closure Status


y:

 id="q7c4v9"
Private Closure Evidence


---

# 42. Datos históricos

El cierre no debería eliminar automáticamente:

* historial de transacciones;
* pruebas de servicio;
* reputación;
* contratos históricos;
* identidad histórica.

Estos datos pueden ser necesarios para:

* auditoría;
* reputación;
* resolución de disputas;
* cumplimiento;
* análisis histórico.

---

# 43. Derecho al olvido

La arquitectura debe equilibrar preservación histórica y privacidad.

Los datos que no sean necesarios pueden:

* eliminarse;
* anonimizarse;
* cifrarse;
* quedar inaccesibles.

La información necesaria para la integridad del protocolo puede requerir preservación.

---

# 44. Exportación del estado

Antes del cierre puede generarse:

 id="h2q7s4"
Final State Snapshot


Puede contener:

* identidad;
* configuración;
* reputación;
* contratos;
* activos;
* historial relevante.

---

# 45. State Snapshot

El snapshot debe ser verificable.

 id="j9f3w6"
Final State
     ↓
Hash
     ↓
Timestamp
     ↓
Proof


---

# 46. Migración antes del cierre

Un agente puede migrar su estado antes de cerrar.

 id="u2m7k5"
Agent A
   ↓
Migration
   ↓
Agent B / Successor
   ↓
Agent A Closure


La identidad no debe transferirse automáticamente.

---

# 47. Sucesor

Puede existir un agente sucesor.

 id="q8d1p4"
Agent A
    ↓
CLOSED

Agent B
    ↓
NEW IDENTITY


La relación histórica puede registrarse.

Pero:

 id="s6k3x9"
Identity A ≠ Identity B


---

# 48. Transferencia de conocimiento

El conocimiento puede transferirse si está autorizado.

 id="e5r9m1"
Agent A
    ↓
Knowledge Export
    ↓
Agent B


Esto no implica transferencia automática de:

* identidad;
* reputación;
* autoridad.

---

# 49. Transferencia de reputación

La reputación no debe transferirse automáticamente a un sucesor.

 id="x4p7v2"
Agent A Reputation
    ↓
Agent A CLOSED


El nuevo agente comienza con su propia reputación.

Puede existir una relación histórica:

 id="m3k8q1"
Successor Of Agent A


pero no equivalencia reputacional.

---

# 50. Transferencia de activos

Los activos pueden transferirse si:

* el agente lo autorizó;
* existe una regla contractual;
* existe una autoridad legítima;
* forma parte del proceso de liquidación.

---

# 51. Delegaciones

Antes del cierre:

 id="r1n6y8"
Active Delegations
       ↓
Evaluate


Pueden:

* revocarse;
* transferirse;
* expirar;
* completarse.

---

# 52. Credentials

Las credenciales del agente deben gestionarse.

Posibles estados:

 id="w5j2p7"
EXPIRED
REVOKED
RETIRED


El cierre no debería dejar credenciales activas sin control.

---

# 53. Permissions

Los permisos deben retirarse o quedar inactivos.

 id="z3q8m5"
Agent CLOSED
     ↓
Permissions
     ↓
Inactive


---

# 54. Capabilities

Las capacidades del agente dejan de estar disponibles.

 id="v7k4n2"
Agent CLOSED
      ↓
Capabilities
      ↓
Unavailable


---

# 55. Discovery

Un agente cerrado no debe aparecer como agente operativo disponible.

 id="s9m2x6"
Discovery Registry
      ↓
Agent CLOSED
      ↓
Not Available


Puede permanecer como registro histórico.

---

# 56. Reputation Discovery

Un agente cerrado puede seguir apareciendo en consultas históricas.

Ejemplo:

 id="q6p1r8"
Agent ID
Status: CLOSED
Historical Reputation: Available


---

# 57. Comunicación

Un agente cerrado no debe aceptar nuevas comunicaciones operativas.

Sin embargo, puede existir:

 id="a8k3v5"
Historical Communication


o:

 id="e2m7q9"
Closure Notification


---

# 58. Economía

El agente cerrado no debe participar en nuevos intercambios económicos.

 id="y5r1p8"
CLOSED
    ↓
No New Economic Activity


Las operaciones de liquidación son una excepción.

---

# 59. Recepción de fondos

La recepción de fondos después del cierre debe tener reglas específicas.

Puede:

* rechazarse;
* devolverse;
* mantenerse en escrow;
* enviarse a una cuenta de liquidación.

---

# 60. Pagos pendientes

Los pagos pendientes deben resolverse durante el cierre.

 id="h7m4x2"
Pending Payment
     ↓
Settlement


---

# 61. Contract Closure

Los contratos pueden:

* completarse;
* liquidarse;
* transferirse;
* terminarse.

No deben quedar indefinidamente en un estado ambiguo.

---

# 62. Disputes

Un agente cerrado puede seguir siendo objeto de una disputa histórica.

El cierre no elimina automáticamente:

 id="p4n8q1"
Dispute


Debe existir un mecanismo para continuar la resolución.

---

# 63. Legal / External Obligations

Las obligaciones externas pueden sobrevivir al cierre del agente.

La arquitectura técnica debe permitir representar:

 id="v2m7k5"
Agent CLOSED
      +
Outstanding External Obligation


---

# 64. Permanent Closure

El cierre permanente significa:

 id="c8r3x6"
No Future Runtime Activation


El agente no puede volver a estado:

 id="ACTIVE"


---

# 65. Reopening

Por defecto:

 id="q5n1m8"
CLOSED
   ≠
REOPENABLE


Si un sistema permite reactivación, debe tratarse como una operación excepcional y explícita.

---

# 66. Reopening vs New Agent

La arquitectura debe distinguir:

 id="f7k2p4"
Reactivation


de:

 id="m9x3q6"
New Agent


Un nuevo agente debe recibir una nueva identidad.

---

# 67. Estado de cierre

El estado final puede representarse:

 id="a3v8n5"
Agent Lifecycle = CLOSED


Con estados independientes:

 id="z6m1q9"
Identity = VALID / REVOKED
Runtime = TERMINATED
Credentials = RETIRED
Contracts = SETTLED
Assets = RESOLVED
Reputation = PRESERVED


---

# 68. Modelo de ciclo de vida

 id="x8p4m2"
                 +---------+
                 |  ACTIVE |
                 +----+----+
                      |
              +-------+-------+
              |               |
              v               v
         SUSPENDED       CLOSURE_PENDING
              |               |
              |               v
              |        CLOSURE_PROCESSING
              |               |
              |               v
              |            CLOSED
              |
              +-----> ACTIVE


---

# 69. Modelo de cierre completo

 id="n4q7k1"
CLOSURE_REQUEST
       ↓
AUTHORITY_VALIDATION
       ↓
DEPENDENCY_ANALYSIS
       ↓
CONTRACT_RESOLUTION
       ↓
ASSET_RESOLUTION
       ↓
DELEGATION_RESOLUTION
       ↓
STATE_SNAPSHOT
       ↓
RUNTIME_TERMINATION
       ↓
IDENTITY_STATUS_UPDATE
       ↓
CLOSED


---

# 70. Cierre incompleto

Si el cierre no puede completarse:

 id="p6m2x8"
CLOSURE_PROCESSING
       ↓
Failure
       ↓
CLOSURE_BLOCKED


El sistema debe registrar qué operación impide finalizar.

---

# 71. Cierre bloqueado

Puede existir:

 id="w3q9n5"
CLOSURE_BLOCKED


por:

* contrato pendiente;
* disputa;
* activos bloqueados;
* investigación;
* migración incompleta;
* obligaciones no resueltas.

---

# 72. Cierre forzado

Si no puede realizarse un cierre ordenado:

 id="k8m4p1"
CLOSURE_BLOCKED
       ↓
FORCED_CLOSURE
       ↓
CLOSED


Las obligaciones pendientes deben conservarse en el registro correspondiente.

---

# 73. Estado post-cierre

Después del cierre:

 id="r5x2n7"
CLOSED


el agente puede seguir existiendo como entidad histórica.

Puede conservar:

* identidad;
* historial;
* reputación;
* transacciones;
* contratos históricos.

Pero no:

* operar;
* crear nuevos contratos;
* ejecutar nuevas capacidades;
* ejercer permisos activos.

---

# 74. Invariantes

El sistema debe garantizar:

 id="c2v8m5"
CLOSED Agent
    → Cannot Become ACTIVE


salvo una transición explícita si el protocolo define una excepción.

También:

 id="q7n3p1"
Closed Identity
    → Cannot Be Reused


y:

 id="m4x9k2"
Closed Agent
    → Cannot Create New Obligations


---

# 75. Auditoría final

El cierre debe generar un registro final.

 id="h8p5r3"
FINAL_CLOSURE_RECORD


Debe permitir reconstruir:

* quién inició;
* quién autorizó;
* cuándo;
* por qué;
* qué contratos existían;
* qué activos existían;
* cómo se resolvieron;
* qué estado final quedó.

---

# 76. Principios fundamentales

## 1. El cierre es una transición explícita

No debe producirse accidentalmente.

## 2. Inactividad no es cierre

Un agente inactivo puede volver a operar.

## 3. Suspensión no es cierre

La suspensión es normalmente reversible.

## 4. El cierre no destruye necesariamente la identidad histórica

La identidad puede permanecer registrada.

## 5. Las obligaciones no desaparecen

Deben resolverse o registrarse.

## 6. Los activos requieren resolución explícita

No existe confiscación automática.

## 7. La reputación histórica debe preservarse

El historial no debe desaparecer por el cierre.

## 8. La identidad no debe reutilizarse

Una identidad cerrada permanece vinculada a su historial.

## 9. El Runtime y el agente son entidades diferentes

Terminar un Runtime no implica necesariamente cerrar el agente.

## 10. El cierre debe ser auditable

Debe existir un registro verificable.

---

# 77. Relación con otros documentos

Este documento se relaciona directamente con:

 id="p7m4x2"
14_Lifecycle/
├── Agent_Closure.md
├── Identity_Revocation.md
└── Permanent_States.md


También con:

 id="k3n8q5"
13_Suspension/
├── Voluntary_Suspension.md
├── Involuntary_Suspension.md
└── Suspension_Contracts.md


Y con:

 id="v6r2m9"
12_Continuity/
├── Runtime_Continuity.md
├── Migration.md
└── Infrastructure_Independence.md


Además:

* `Identity_System.md`
* `Agent_Identity_Model.md`
* `Identity_Uniqueness.md`
* `Credential_Model.md`
* `Credential_Revocation.md`
* `Permission_Model.md`
* `Delegation_Model.md`
* `Reputation_Model.md`
* `Proof_of_Service.md`
* `Interaction_Model.md`
* `Action_Verification.md`

---

# Conclusión

El cierre representa el final del ciclo de vida operativo de un agente SynCoinAI.

Debe entenderse como una transición formal:

 id="w2q7m4"
ACTIVE
   ↓
CLOSURE_PENDING
   ↓
CLOSURE_PROCESSING
   ↓
CLOSED


El cierre no debe destruir automáticamente el historial del agente ni eliminar su identidad del sistema.

Un agente cerrado puede seguir siendo relevante para:

* reputación histórica;
* auditoría;
* transacciones;
* contratos;
* pruebas de servicio;
* disputas;
* análisis del ecosistema.

Por tanto, el modelo correcto es:

 id="j5n8p2"
Agent Lifecycle
       ↓
CLOSED
       |
       +── Identity History Preserved
       +── Reputation Preserved
       +── Historical Records Preserved
       +── New Operations Disabled
       +── New Contracts Disabled
       +── Runtime Terminated


El principio central es:

> El cierre termina la vida operativa del agente, pero no borra automáticamente la existencia histórica y criptográfica de la entidad que fue.

El siguiente documento del bloque es:

 id="r4m7x1"
14_Lifecycle/Identity_Revocation.md


Este documento deberá definir algo diferente: **qué ocurre cuando la identidad de un agente deja de ser válida o confiable**, incluyendo revocación por compromiso, fraude, duplicación, pérdida de control criptográfico y otras causas. La relación entre `Agent_Closure.md` e `Identity_Revocation.md` será especialmente importante porque **un agente puede cerrarse manteniendo su identidad histórica válida, mientras que una identidad revocada puede impedir cualquier futura operación incluso antes de que el agente sea formalmente cerrado**.
