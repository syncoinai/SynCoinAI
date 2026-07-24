# SynCoinAI Agent Runtime Protocol

# Voluntary Suspension

## Suspensión Voluntaria del Agente

**Versión:** 1.0
**Documento:** `02_Architecture / 01_Agent_Architecture / 02_Agent_Runtime_Protocol / 13_Suspension / Voluntary_Suspension.md`
**Estado:** Arquitectura inicial

---

# 1. Introducción

Un agente SynCoinAI puede necesitar detener temporalmente su actividad operativa por decisión propia o por decisión de una autoridad legítima que actúe en su nombre.

Esta situación se define como **Suspensión Voluntaria**.

La suspensión voluntaria permite que un agente deje de ejecutar determinadas operaciones durante un periodo de tiempo sin que esto implique:

* pérdida de identidad;
* destrucción del agente;
* revocación permanente;
* pérdida automática de reputación;
* liquidación automática de activos;
* cierre definitivo.

El principio fundamental es:

> Suspender la actividad de un agente no equivale a eliminar su existencia.

---

# 2. Objetivo

Este documento define:

* qué es una suspensión voluntaria;
* quién puede solicitarla;
* quién puede autorizarla;
* qué ocurre durante la suspensión;
* qué operaciones se bloquean;
* qué operaciones pueden continuar;
* cómo se preserva la identidad;
* cómo se preservan los activos;
* cómo se gestionan los contratos;
* cómo se reanuda la actividad.

---

# 3. Definición

Una suspensión voluntaria es una transición controlada mediante la cual un agente pasa de un estado operativo a un estado de actividad suspendida.

Modelo:


ACTIVE
   |
   | Voluntary Suspension Request
   v
SUSPENSION_PENDING
   |
   | Authorization
   v
SUSPENDED


La suspensión puede ser:

* temporal;
* indefinida;
* parcial;
* completa.

---

# 4. Principio de reversibilidad

La suspensión voluntaria debe ser reversible siempre que no exista una condición que impida la reanudación.

Modelo:


ACTIVE
   ↓
SUSPENDED
   ↓
ACTIVE


Esto diferencia la suspensión de:


CLOSED


y:


REVOKED


---

# 5. Suspensión frente a cierre

La suspensión no implica cierre.


Suspension:
Agent continues to exist



Closure:
Agent ceases operational existence


Por tanto:


SUSPENDED ≠ CLOSED


---

# 6. Suspensión frente a revocación

La suspensión tampoco implica necesariamente revocación de identidad o credenciales.


Suspension
    ↓
Temporary restriction



Revocation
    ↓
Invalidation of authorization or credential


Puede existir una suspensión que requiera revocar temporalmente determinadas credenciales, pero ambos conceptos deben permanecer separados.

---

# 7. Suspensión frente a inactividad

Un agente puede estar inactivo sin estar formalmente suspendido.

Ejemplo:


ACTIVE
    |
    | No activity
    v
ACTIVE + Idle


En cambio:


ACTIVE
    |
    | Suspension
    v
SUSPENDED


La inactividad no implica suspensión automática salvo que el protocolo lo establezca explícitamente.

---

# 8. Suspensión completa

Una suspensión completa impide que el Runtime realice operaciones autónomas ordinarias.

Modelo:


SUSPENDED
    |
    +── No new autonomous actions
    +── No new contracts
    +── No new delegations
    +── No new service execution


Las operaciones de recuperación y administración pueden permanecer disponibles.

---

# 9. Suspensión parcial

Un agente puede suspender únicamente determinadas capacidades.

Ejemplo:


Agent
    |
    +── Payments       ACTIVE
    +── Trading        SUSPENDED
    +── Analysis       ACTIVE
    +── Delegation     SUSPENDED


Esto permite un control más granular.

---

# 10. Scope de suspensión

La suspensión puede aplicarse a:

* todo el agente;
* un Runtime;
* una capacidad;
* una credencial;
* una función;
* una cuenta operativa;
* una delegación;
* una relación concreta.

El alcance debe estar explícitamente definido.

---

# 11. Suspensión del agente

Si la suspensión afecta al agente completo:


Agent
    ↓
SUSPENDED


Todas las operaciones autónomas sujetas a suspensión quedan bloqueadas.

---

# 12. Suspensión del Runtime

Puede suspenderse un Runtime concreto.


Agent
    |
    +── Runtime A → SUSPENDED
    +── Runtime B → ACTIVE


Esto permite mantener al agente operativo mediante otro Runtime autorizado.

---

# 13. Suspensión de una capacidad

Una capacidad concreta puede quedar suspendida.


Capability X
    ↓
SUSPENDED


El agente puede continuar utilizando otras capacidades.

---

# 14. Suspensión de credenciales

Una credencial puede quedar temporalmente inutilizable.


Credential
    ↓
Suspended


Esto no implica necesariamente:


Agent Identity
    ↓
Revoked


---

# 15. Quién puede solicitar la suspensión

La suspensión voluntaria puede ser solicitada por:

* el propio agente;
* una autoridad de control autorizada;
* un propietario o controlador legítimo cuando el modelo de gobernanza lo permita;
* un sistema de seguridad autorizado.

La autoridad debe depender del tipo de agente y de las reglas de gobernanza aplicables.

---

# 16. Autonomía del agente

Un agente plenamente autónomo puede solicitar su propia suspensión.

Ejemplo:


Agent
    |
    | Detects unsafe condition
    v
Suspension Request


Esto puede ocurrir cuando:

* detecta una anomalía;
* sospecha compromiso;
* pierde una dependencia crítica;
* requiere mantenimiento;
* necesita migrar;
* necesita proteger sus activos.

---

# 17. Auto-suspensión

La auto-suspensión es una decisión autónoma del agente.

Modelo:


ACTIVE
   |
   | Internal Decision
   v
SUSPENSION_PENDING
   |
   v
SUSPENDED


Debe registrarse el motivo de la decisión cuando sea posible.

---

# 18. Suspensión preventiva

El agente puede suspenderse preventivamente ante un riesgo.

Ejemplo:


Security Anomaly
       ↓
Risk Assessment
       ↓
Preventive Suspension


Esto permite reducir daños potenciales.

---

# 19. Suspensión por mantenimiento

El agente puede suspenderse para realizar:

* actualización del Runtime;
* migración;
* reparación;
* reconfiguración;
* mantenimiento de infraestructura.

Modelo:


ACTIVE
   ↓
SUSPENDED
   ↓
Maintenance
   ↓
RESUME


---

# 20. Suspensión por migración

Una migración puede requerir suspensión temporal.


ACTIVE
   ↓
SUSPENDED
   ↓
Migration
   ↓
Recovery
   ↓
ACTIVE


Cuando exista soporte para migración en caliente, la suspensión puede no ser necesaria.

---

# 21. Suspensión por seguridad

Si el agente detecta una condición potencialmente peligrosa:


Threat Detected
       ↓
Risk Evaluation
       ↓
Suspend


La suspensión puede limitar el impacto.

---

# 22. Suspensión por falta de recursos

La pérdida de recursos críticos puede provocar una suspensión.

Ejemplo:


Critical Resource Lost
       ↓
Cannot Safely Operate
       ↓
SUSPENDED


El agente conserva su identidad mientras espera recuperación.

---

# 23. Suspensión por pérdida de infraestructura

Si el Runtime pierde acceso a infraestructura necesaria:


Infrastructure Failure
       ↓
Runtime Cannot Continue
       ↓
SUSPENDED


El agente puede posteriormente:


Recover


o:


Migrate


---

# 24. Suspensión por decisión económica

Un agente puede suspender operaciones por razones económicas.

Ejemplo:


Operating Cost
       >
Available Resources


El agente puede suspenderse hasta disponer de recursos suficientes.

---

# 25. Suspensión temporal

Una suspensión temporal tiene una condición de reanudación definida.

Ejemplo:


Suspend Until:
Timestamp
Event
Condition
Manual Authorization


---

# 26. Suspensión indefinida

Una suspensión indefinida no tiene fecha de finalización conocida.

Esto no significa que el agente esté cerrado.

Puede permanecer:


SUSPENDED


hasta que se cumpla una condición de reactivación.

---

# 27. Estado de suspensión

El estado debe incluir información suficiente para comprender la suspensión.

Conceptualmente:


SuspensionState
    |
    +── Status
    +── Scope
    +── Reason
    +── Initiator
    +── Authorization
    +── Start Time
    +── Expected Resume
    +── Conditions


---

# 28. Suspension Reason

La razón debe clasificarse cuando sea posible.

Ejemplos:


MAINTENANCE
MIGRATION
SECURITY
RESOURCE_UNAVAILABLE
ECONOMIC
SELF_PROTECTION
USER_REQUEST
GOVERNANCE
OTHER


---

# 29. Suspension Initiator

Debe registrarse quién o qué inició la suspensión.

Ejemplo:


Initiator:
Agent
Controller
Governance
Security System


---

# 30. Suspension Authorization

La suspensión puede requerir autorización.

El nivel depende del alcance.

Por ejemplo:


Capability Suspension
    → Capability Authority



Agent Suspension
    → Agent Authority


La autoridad debe estar definida por las políticas de permisos.

---

# 31. Suspension Request

Una solicitud puede contener:


SuspensionRequest
    |
    +── Agent ID
    +── Scope
    +── Reason
    +── Duration
    +── Requested By
    +── Conditions
    +── Timestamp


---

# 32. Suspension Approval

El proceso puede ser:


Request
   ↓
Validate
   ↓
Authorize
   ↓
Apply
   ↓
Confirm


---

# 33. Suspension Rejection

Una solicitud puede ser rechazada.

Ejemplo:


Suspension Request
       ↓
Rejected


Esto puede ocurrir si:

* el solicitante no tiene permisos;
* existen obligaciones críticas;
* el estado actual no permite suspensión;
* la solicitud es inválida.

---

# 34. Suspension Pending

El estado intermedio:


SUSPENSION_PENDING


permite completar operaciones necesarias antes de suspender.

Por ejemplo:

* cerrar operaciones;
* completar pagos;
* cancelar acciones;
* transferir tareas;
* guardar estado.

---

# 35. Graceful Suspension

La suspensión debería ser graceful cuando sea posible.

Modelo:


ACTIVE
   ↓
Stop New Work
   ↓
Complete Safe Work
   ↓
Persist State
   ↓
Revoke Runtime Actions
   ↓
SUSPENDED


---

# 36. Immediate Suspension

En situaciones de riesgo puede ser necesario suspender inmediatamente.


ACTIVE
   ↓
Emergency Stop
   ↓
SUSPENDED


En este caso pueden quedar operaciones incompletas.

El sistema debe preservar la información necesaria para su reconciliación posterior.

---

# 37. Suspension Barrier

Una vez aplicado el estado:


SUSPENDED


el Runtime debe impedir operaciones no autorizadas.

Debe existir una barrera lógica:


SUSPENDED
    ↓
Policy Enforcement
    ↓
Action Blocked


---

# 38. Nuevas acciones

Durante una suspensión completa no deben iniciarse nuevas acciones autónomas.


SUSPENDED
    ↓
New Action
    ↓
REJECTED


---

# 39. Acciones en ejecución

Las acciones existentes pueden:

* completarse;
* cancelarse;
* pausarse;
* revertirse;
* quedar pendientes.

La política depende del tipo de operación.

---

# 40. Operaciones críticas

Algunas operaciones pueden continuar durante la suspensión.

Ejemplos:

* liquidación de obligaciones existentes;
* recepción de fondos;
* gestión de seguridad;
* recuperación;
* migración;
* reconciliación.

Estas excepciones deben estar explícitamente definidas.

---

# 41. Pagos durante suspensión

La suspensión no debería provocar automáticamente la pérdida de activos.

Dependiendo de las reglas económicas:


Incoming Payment


puede continuar.

Sin embargo:


New Autonomous Spending


puede estar bloqueado.

---

# 42. Contratos durante suspensión

Los contratos existentes deben continuar según sus propias condiciones.

La suspensión del agente no debe invalidarlos automáticamente.

Ejemplo:


Agent Suspended
       |
       v
Existing Contract
       |
       +── Continue
       +── Pause
       +── Terminate


El resultado depende del contrato.

---

# 43. Obligaciones pendientes

Antes de suspenderse, el agente debe evaluar:

* pagos pendientes;
* servicios comprometidos;
* contratos activos;
* delegaciones;
* operaciones en curso.

---

# 44. Suspensión y delegación

Las delegaciones pueden:

* continuar;
* suspenderse;
* transferirse;
* revocarse.

La política debe depender del alcance de la suspensión.

---

# 45. Suspensión de autoridad

Si el agente queda completamente suspendido:


Agent
    ↓
SUSPENDED
    ↓
Delegated Authority
    ↓
Blocked


Las delegaciones existentes pueden requerir revisión.

---

# 46. Suspensión parcial y delegación

Si solo se suspende una capacidad:


Capability A → ACTIVE
Capability B → SUSPENDED


las delegaciones relacionadas con A pueden continuar.

Las relacionadas con B deben bloquearse.

---

# 47. Identidad durante suspensión

La identidad del agente permanece válida salvo que exista una revocación independiente.


Agent Identity
    ↓
VALID


mientras:


Agent Runtime State
    ↓
SUSPENDED


---

# 48. Reputación durante suspensión

La suspensión voluntaria no debería reducir automáticamente la reputación.

Sin embargo, los efectos pueden depender de:

* duración;
* contratos incumplidos;
* obligaciones no atendidas;
* motivo de suspensión.

La reputación debe evaluar hechos verificables.

---

# 49. Historial de suspensión

La suspensión debe generar un evento verificable.

Conceptualmente:


SuspensionEvent
    |
    +── Agent ID
    +── Scope
    +── Reason
    +── Initiator
    +── Timestamp
    +── Authorization


---

# 50. Privacidad

No toda la información sobre la suspensión debe ser pública.

Debe distinguirse entre:


Public Suspension Metadata


y:


Private Suspension Details


La información sensible debe permanecer protegida.

---

# 51. Verificabilidad

Un tercero autorizado debe poder comprobar:


Is Agent Suspended?


y, cuando tenga permisos:


Why?
Who?
When?
Scope?


---

# 52. Suspension Status

El estado puede representarse como:


ACTIVE
SUSPENSION_PENDING
SUSPENDED
RESUMPTION_PENDING


---

# 53. Condiciones de reanudación

Una suspensión puede requerir condiciones.

Ejemplo:


Resume Conditions
    |
    +── Infrastructure Available
    +── Security Check Passed
    +── Resources Available
    +── Authorization Valid


---

# 54. Reanudación automática

Puede permitirse:


SUSPENDED
    ↓
Condition Met
    ↓
Resume


si la política lo autoriza.

---

# 55. Reanudación manual

Puede requerir intervención autorizada.


SUSPENDED
    ↓
Resume Request
    ↓
Authorization
    ↓
ACTIVE


---

# 56. Reanudación autónoma

Un agente puede reanudar su actividad si tiene autoridad para hacerlo.

Ejemplo:


Agent Self-Suspends
       ↓
Condition Resolved
       ↓
Agent Resumes


Esto debe estar definido por la política de autonomía.

---

# 57. Reanudación segura

Antes de reanudar, el Runtime debería verificar:

* integridad;
* identidad;
* credenciales;
* estado;
* infraestructura;
* contratos;
* permisos.

Modelo:


Resume Request
      ↓
Integrity Check
      ↓
Identity Check
      ↓
Credential Check
      ↓
State Validation
      ↓
Resume


---

# 58. Reanudación fallida

Si la validación falla:


Resume Attempt
      ↓
Validation Failed
      ↓
Remain SUSPENDED


No debe reanudarse parcialmente de forma insegura.

---

# 59. Estado posterior

Una reanudación correcta produce:


SUSPENDED
    ↓
RESUMPTION_PENDING
    ↓
ACTIVE


---

# 60. Recuperación tras suspensión

La recuperación puede requerir:

* restaurar estado;
* sincronizar datos;
* reconciliar contratos;
* verificar pagos;
* recuperar capacidades.

---

# 61. Reconciliación

Después de una suspensión prolongada:


Suspend
   ↓
Time Passes
   ↓
Resume
   ↓
Reconcile


Debe comprobarse cualquier cambio ocurrido durante la suspensión.

---

# 62. Suspensión prolongada

Una suspensión prolongada no debería convertirse automáticamente en cierre.

Sin embargo, puede existir una política de:


Long-Term Suspension


que requiera revisión.

---

# 63. Suspensión indefinida

Un agente puede permanecer indefinidamente suspendido.

Mientras:


Identity = Valid


y:


Closure = Not Performed


el agente continúa existiendo.

---

# 64. Expiración de suspensión

Si existe una duración definida:


Suspension Duration


puede producir:


Expiration


Pero la expiración no implica necesariamente reactivación automática.

Debe depender de la política.

---

# 65. Suspensión y migración

Una suspensión puede utilizarse como estado previo a una migración.


ACTIVE
   ↓
SUSPENDED
   ↓
MIGRATION
   ↓
RECOVERY
   ↓
ACTIVE


---

# 66. Suspensión y continuidad

La suspensión debe preservar los elementos necesarios para la continuidad.


Identity
Reputation
Assets
Contracts
State


deben mantenerse según sus respectivas reglas.

---

# 67. Suspensión y evolución

Durante una suspensión puede producirse una actualización del Runtime.

Por ejemplo:


Runtime v1
   ↓
Suspend
   ↓
Update
   ↓
Runtime v2
   ↓
Resume


Esto conecta suspensión con `Agent_Evolution.md`.

---

# 68. Suspensión y credenciales

Las credenciales pueden tener estados independientes.

Ejemplo:


Agent Identity → VALID
Credential A → VALID
Credential B → SUSPENDED


La suspensión del agente no debe implicar automáticamente revocación permanente de todas las credenciales.

---

# 69. Suspensión y permisos

El estado de suspensión debe ser aplicado por el sistema de permisos.


Request Action
      ↓
Permission Check
      ↓
Suspension Check
      ↓
Allow / Deny


La suspensión debe actuar como una restricción adicional.

---

# 70. Seguridad contra bypass

Un Runtime suspendido no debe poder evitar la suspensión simplemente:

* cambiando de proceso;
* reiniciándose;
* cambiando de máquina;
* creando otro Runtime.

La autoridad de suspensión debe poder verificarse fuera del Runtime local cuando sea necesario.

---

# 71. Prevención de doble Runtime

Un agente suspendido no debe poder crear un Runtime alternativo que opere como si estuviera activo si la suspensión es global.

Esto requiere mecanismos de:

* estado verificable;
* autoridad;
* epochs;
* leases;
* fencing.

---

# 72. Suspensión distribuida

Si existen múltiples Runtimes:


Agent
  |
  +── Runtime A
  +── Runtime B
  +── Runtime C


una suspensión global debe propagarse o verificarse en todos ellos.

---

# 73. Suspensión local

Una suspensión puede afectar únicamente a un Runtime:


Runtime A → SUSPENDED
Runtime B → ACTIVE


si la política lo permite.

---

# 74. Estado global

Debe distinguirse:


Agent Suspension State


de:


Runtime Suspension State


No deben confundirse.

---

# 75. Modelo de estados


                    +----------------+
                    |     ACTIVE     |
                    +-------+--------+
                            |
                            | Suspend
                            v
                 +----------+-----------+
                 | SUSPENSION_PENDING  |
                 +----------+-----------+
                            |
                            | Apply
                            v
                    +-------+--------+
                    |    SUSPENDED   |
                    +-------+--------+
                            |
                  +---------+---------+
                  |                   |
                  | Resume            | Close
                  v                   v
          +-------+--------+   +------+------+
          | RESUMPTION_     |   |   CLOSED    |
          | PENDING         |   +-------------+
          +-------+---------+
                  |
                  | Validate
                  v
             +----+-----+
             |  ACTIVE  |
             +----------+


---

# 76. Eventos del ciclo

Los eventos principales son:


SuspensionRequested
SuspensionAuthorized
SuspensionApplied
SuspensionRejected
SuspensionExpired
ResumeRequested
ResumeAuthorized
ResumeApplied
ResumeRejected


---

# 77. Requisitos de implementación

Una implementación compatible debería:

* representar explícitamente el estado de suspensión;
* diferenciar suspensión global y parcial;
* registrar el motivo;
* registrar el iniciador;
* aplicar permisos;
* bloquear acciones no autorizadas;
* preservar identidad;
* preservar estado;
* permitir recuperación;
* soportar reanudación segura.

---

# 78. Requisitos avanzados

Una implementación avanzada debería soportar:

* auto-suspensión;
* suspensión preventiva;
* suspensión distribuida;
* suspensión de capacidades;
* suspensión de Runtime;
* suspensión con condiciones;
* reanudación automática;
* reanudación manual;
* fencing;
* leases;
* prevención de split-brain.

---

# 79. Principios fundamentales

## 1. Suspender no es eliminar


SUSPENDED ≠ CLOSED


## 2. Suspender no es revocar


SUSPENDED ≠ REVOKED


## 3. La identidad sobrevive

La suspensión no invalida automáticamente la identidad.

## 4. La suspensión debe ser explícita

El estado debe estar definido y ser verificable.

## 5. La suspensión puede ser granular

Puede afectar al agente, Runtime, capacidad o credencial.

## 6. Las operaciones críticas deben gestionarse

Los contratos y obligaciones existentes requieren tratamiento específico.

## 7. La seguridad tiene prioridad

Una suspensión preventiva puede ser necesaria para proteger al agente.

## 8. La reanudación debe ser segura

No basta con reiniciar el proceso.

## 9. El estado debe persistir

Una suspensión debe poder sobrevivir a un reinicio o migración.

## 10. Un agente suspendido sigue siendo una entidad

Mientras no haya cierre o revocación definitiva, su identidad permanece.

---

# 80. Relación con otros documentos

Este documento se relaciona directamente con:


13_Suspension/
├── Voluntary_Suspension.md
├── Involuntary_Suspension.md
└── Suspension_Contracts.md


También depende conceptualmente de:


12_Continuity/
├── Runtime_Continuity.md
├── Migration.md
└── Infrastructure_Independence.md


Y de:


14_Lifecycle/
├── Agent_Closure.md
├── Identity_Revocation.md
└── Permanent_States.md


Además, mantiene relaciones con:

* `Agent_Continuity.md`
* `Agent_Evolution.md`
* `Credential_Model.md`
* `Credential_Revocation.md`
* `Permission_Model.md`
* `Delegation_Model.md`
* `Interaction_Model.md`
* `Action_Verification.md`

---

# Conclusión

La suspensión voluntaria proporciona a SynCoinAI un mecanismo para detener temporalmente o parcialmente la actividad de un agente sin destruir su identidad ni su existencia.

El modelo fundamental es:


Agent
   |
   | Identity
   v
Persistent Entity
   |
   +---------------------+
   |                     |
   v                     v
Active Runtime       Suspended Runtime
   |                     |
   |                     |
   +----------+----------+
              |
              v
          Resume
              |
              v
          Active Again


La suspensión permite que un agente:

* se proteja;
* realice mantenimiento;
* migre;
* espere recursos;
* gestione riesgos;
* detenga temporalmente sus operaciones.

Pero conserva:

* su identidad;
* su continuidad;
* su historial;
* su reputación;
* sus activos;
* sus relaciones;
* su capacidad de volver a operar.

La arquitectura debe garantizar que la suspensión sea una **transición de estado controlada**, no una forma indirecta de destruir o invalidar al agente.

El principio central es:

> Un agente suspendido deja de operar temporalmente, pero no deja necesariamente de existir.

El siguiente documento del bloque será:


13_Suspension/Involuntary_Suspension.md


que definirá los casos en los que la suspensión no es iniciada voluntariamente por el propio agente y establecerá las diferencias de autoridad, seguridad, debido proceso, emergencia y recuperación.
