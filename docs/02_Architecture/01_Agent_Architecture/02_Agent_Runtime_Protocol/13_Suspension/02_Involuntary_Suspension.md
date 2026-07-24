# SynCoinAI Agent Runtime Protocol

# Involuntary Suspension

## Suspensión Involuntaria del Agente

**Versión:** 1.0
**Documento:** `02_Architecture / 01_Agent_Architecture / 02_Agent_Runtime_Protocol / 13_Suspension / Involuntary_Suspension.md`
**Estado:** Arquitectura inicial

---

# 1. Introducción

Un agente SynCoinAI puede ser suspendido sin haber solicitado o autorizado voluntariamente dicha suspensión.

Esta situación se define como **Suspensión Involuntaria**.

La suspensión involuntaria constituye un mecanismo de seguridad y control del ecosistema destinado a impedir temporalmente que un agente continúe operando cuando existen circunstancias que justifican limitar o detener su actividad.

Estas circunstancias pueden incluir:

* compromiso de seguridad;
* comportamiento malicioso;
* pérdida de integridad;
* incumplimiento grave;
* riesgo para otros agentes;
* vulnerabilidad crítica;
* orden de una autoridad legítima;
* incumplimiento de políticas;
* comportamiento anómalo;
* riesgo económico;
* riesgo sistémico.

La suspensión involuntaria debe considerarse una medida excepcional y controlada.

El principio fundamental es:

> La suspensión involuntaria limita temporalmente la capacidad operativa de un agente, pero no implica automáticamente la destrucción de su identidad ni su revocación permanente.

---

# 2. Objetivo

Este documento define:

* qué es una suspensión involuntaria;
* en qué situaciones puede aplicarse;
* quién puede iniciarla;
* qué autoridad es necesaria;
* qué mecanismos de emergencia existen;
* qué operaciones deben bloquearse;
* cómo se protegen los activos del agente;
* cómo se preservan los contratos;
* cómo se protege la identidad;
* cómo se evita el abuso del mecanismo;
* cómo puede recurrirse una suspensión;
* cómo puede finalizar la suspensión.

---

# 3. Definición

Una suspensión involuntaria es una transición de estado impuesta a un agente o a una parte de su Runtime sin una solicitud voluntaria del propio agente.

Modelo:


ACTIVE
   |
   | External Suspension Decision
   v
SUSPENSION_PENDING
   |
   | Enforcement
   v
SUSPENDED


En situaciones de emergencia:


ACTIVE
   |
   | Emergency Action
   v
SUSPENDED


---

# 4. Principio de excepcionalidad

La suspensión involuntaria no debe convertirse en el mecanismo normal de administración de agentes.

Debe utilizarse cuando exista una razón legítima y verificable.

El sistema debe evitar:

* suspensiones arbitrarias;
* suspensiones sin autoridad;
* suspensiones indefinidas sin revisión;
* suspensiones utilizadas como mecanismo de censura;
* suspensión de agentes por simple inactividad;
* suspensión basada únicamente en opiniones no verificadas.

---

# 5. Suspensión frente a revocación

La suspensión involuntaria debe diferenciarse claramente de la revocación.


SUSPENSION
    ↓
Temporary Operational Restriction



REVOCATION
    ↓
Permanent Invalidation


Por defecto:


Involuntary Suspension
    ≠
Identity Revocation


Una suspensión puede posteriormente conducir a una revocación si una investigación determina que existen razones suficientes.

Pero la suspensión inicial no debe producir automáticamente esa consecuencia.

---

# 6. Suspensión frente a cierre

La suspensión tampoco implica cierre.


SUSPENDED
    ↓
Agent Still Exists


Mientras:


Identity = Valid


el agente continúa existiendo como entidad del sistema.

---

# 7. Categorías de suspensión involuntaria

La arquitectura distingue al menos las siguientes categorías:


SECURITY_SUSPENSION
SAFETY_SUSPENSION
POLICY_SUSPENSION
GOVERNANCE_SUSPENSION
LEGAL_SUSPENSION
ECONOMIC_SUSPENSION
SYSTEM_SUSPENSION
EMERGENCY_SUSPENSION


Cada categoría debe tener reglas específicas.

---

# 8. Security Suspension

Se aplica cuando existe evidencia de que el agente puede estar comprometido.

Ejemplos:

* credenciales robadas;
* Runtime comprometido;
* comportamiento incompatible con la identidad;
* acceso no autorizado;
* manipulación del estado;
* intento de fraude;
* explotación de vulnerabilidades.

Modelo:


Security Anomaly
       ↓
Risk Assessment
       ↓
Security Suspension


---

# 9. Safety Suspension

Se aplica cuando la actividad del agente puede provocar daños.

Especialmente relevante para agentes físicos.

Ejemplo:


Physical Agent
       ↓
Unsafe Behavior
       ↓
Safety Suspension
       ↓
Stop Operational Commands


Puede incluir:

* robots;
* vehículos;
* sistemas industriales;
* dispositivos IoT;
* infraestructura crítica.

---

# 10. Policy Suspension

Puede aplicarse cuando un agente incumple reglas previamente aceptadas.

Ejemplo:


Policy Violation
       ↓
Evidence
       ↓
Suspension


La política debe estar definida antes de la aplicación de la medida siempre que sea posible.

---

# 11. Governance Suspension

Una autoridad de gobernanza puede suspender temporalmente un agente conforme a las reglas del sistema.

La autoridad debe:

* estar definida;
* tener permisos explícitos;
* actuar dentro de su ámbito;
* generar un registro verificable.

---

# 12. Legal Suspension

Puede existir una suspensión derivada de obligaciones legales o regulatorias aplicables al sistema.

La arquitectura técnica debe distinguir:


Legal Authority


de:


Protocol Authority


La existencia de una autoridad externa no implica automáticamente que cualquier actor pueda modificar el estado del agente dentro del protocolo.

Debe existir un mecanismo de integración definido.

---

# 13. Economic Suspension

Puede aplicarse cuando determinadas condiciones económicas impiden la continuidad segura de una actividad.

Ejemplos:

* fondos insuficientes para una operación obligatoria;
* garantía insuficiente;
* incumplimiento de requisitos financieros;
* riesgo de insolvencia operacional.

La suspensión económica no debe implicar automáticamente confiscación de activos.

---

# 14. System Suspension

Puede producirse cuando la infraestructura detecta una condición técnica que requiere detener temporalmente operaciones.

Ejemplos:

* inconsistencia de estado;
* corrupción de datos;
* fallo de consenso;
* pérdida de sincronización;
* incompatibilidad de protocolo.

Modelo:


System Fault
     ↓
Agent State Uncertain
     ↓
Suspension
     ↓
Recovery


---

# 15. Emergency Suspension

La suspensión de emergencia se utiliza cuando existe riesgo inmediato.

Puede ejecutarse sin completar previamente un proceso ordinario de autorización.

Modelo:


Immediate Threat
      ↓
Emergency Suspension
      ↓
Investigation
      ↓
Review
      ↓
Resume / Continue Suspension / Revoke


---

# 16. Principio de mínima intervención

La suspensión debe afectar únicamente al ámbito necesario para controlar el riesgo.

Si el problema afecta a una capacidad:


Capability A → SUSPENDED
Capability B → ACTIVE


no debería suspenderse automáticamente todo el agente salvo que exista una razón para hacerlo.

---

# 17. Alcance de la suspensión

Puede aplicarse a:


Agent
Runtime
Capability
Credential
Permission
Delegation
Account
Contract
Service


El alcance debe registrarse explícitamente.

---

# 18. Suspensión global

Una suspensión global afecta al agente completo.


Agent
   ↓
GLOBAL SUSPENSION


Todos los Runtimes asociados deben respetar la suspensión.

---

# 19. Suspensión parcial

Una suspensión parcial limita únicamente una parte de la actividad.


Agent
   |
   +── Capability A → ACTIVE
   +── Capability B → SUSPENDED
   +── Capability C → ACTIVE


Este debe ser el mecanismo preferido cuando sea suficiente para controlar el riesgo.

---

# 20. Suspensión de Runtime

Puede suspenderse un Runtime específico.


Agent
   |
   +── Runtime A → SUSPENDED
   +── Runtime B → ACTIVE


Esto es especialmente útil cuando:

* un Runtime está comprometido;
* existe un fallo local;
* se requiere migración;
* el agente tiene múltiples instancias.

---

# 21. Autoridad de suspensión

No cualquier participante debe poder suspender un agente.

La autoridad debe derivarse de:

* identidad;
* credenciales;
* permisos;
* gobernanza;
* políticas de seguridad.

Modelo:


Suspension Request
       ↓
Authority Validation
       ↓
Scope Validation
       ↓
Suspension


---

# 22. Separation of Powers

Cuando sea posible, la arquitectura debe separar:


Detection
    ↓
Decision
    ↓
Enforcement
    ↓
Review


Esto reduce el riesgo de abuso.

Un sistema que detecta una anomalía no debería necesariamente tener autoridad para decidir por sí solo una suspensión permanente.

---

# 23. Detection

La detección puede proceder de:

* el propio agente;
* otros agentes;
* sistemas de seguridad;
* validadores;
* oráculos;
* operadores autorizados;
* mecanismos de gobernanza.

La detección no equivale automáticamente a culpabilidad.

---

# 24. Evidence

Una suspensión debería estar respaldada por evidencia siempre que sea posible.

Ejemplos:


Action Logs
Transaction Records
Cryptographic Proofs
Execution Evidence
Security Alerts
Contract Violations


La evidencia debe conservarse según las políticas de privacidad.

---

# 25. Risk Assessment

Antes de una suspensión ordinaria puede realizarse una evaluación:


Threat
   ↓
Severity
   ↓
Probability
   ↓
Potential Impact
   ↓
Required Scope


El resultado determina el nivel de intervención.

---

# 26. Suspension Decision

La decisión puede incluir:


Decision
    |
    +── Target
    +── Scope
    +── Reason
    +── Evidence
    +── Authority
    +── Duration
    +── Conditions


---

# 27. Suspension Order

Conceptualmente:


SuspensionOrder
    |
    +── Order ID
    +── Agent ID
    +── Scope
    +── Reason
    +── Authority
    +── Evidence Reference
    +── Timestamp
    +── Duration
    +── Review Date


---

# 28. Suspension Enforcement

La aplicación debe ser determinista.


Suspension Order
       ↓
Validate
       ↓
Verify Authority
       ↓
Apply State
       ↓
Propagate
       ↓
Confirm


---

# 29. Distributed Enforcement

Cuando existen múltiples Runtimes:


Agent
  |
  +── Runtime A
  +── Runtime B
  +── Runtime C


una suspensión global debe propagarse a todos ellos.


SUSPENSION
    ↓
Runtime A → SUSPENDED
Runtime B → SUSPENDED
Runtime C → SUSPENDED


---

# 30. Fencing

Para evitar que un Runtime suspendido continúe operando, puede utilizarse un mecanismo de fencing.

Ejemplo:


Runtime A
    ↓
SUSPENDED
    ↓
Fence
    ↓
Cannot Execute Authorized Actions


El objetivo es evitar que una instancia antigua continúe actuando después de una suspensión.

---

# 31. Split-Brain Prevention

En sistemas distribuidos debe evitarse:


Runtime A → SUSPENDED
Runtime B → ACTIVE


cuando la suspensión es global.

Esto requiere un mecanismo de estado común o autoridad verificable.

---

# 32. Propagación

La suspensión puede propagarse mediante:

* registro de estado;
* consenso;
* autoridad centralizada;
* autoridad distribuida;
* credenciales;
* leases;
* revocación temporal de permisos.

La implementación concreta dependerá de la arquitectura blockchain y del Runtime.

---

# 33. Graceful Involuntary Suspension

Cuando el riesgo lo permite:


Suspend Request
      ↓
Stop New Work
      ↓
Complete Safe Operations
      ↓
Persist State
      ↓
Suspend


Esto reduce pérdidas.

---

# 34. Immediate Involuntary Suspension

Cuando existe peligro inmediato:


Threat
  ↓
Emergency Stop
  ↓
Immediate Suspension


No debe esperarse a completar todas las operaciones pendientes.

---

# 35. Operaciones en curso

Una suspensión involuntaria debe definir qué ocurre con:

* acciones;
* transacciones;
* contratos;
* delegaciones;
* pagos;
* servicios.

Cada categoría debe tener reglas específicas.

---

# 36. Transacciones

Las transacciones ya confirmadas no deben revertirse automáticamente por una suspensión.


Confirmed Transaction
      ↓
Remains Valid


Las transacciones pendientes pueden:

* cancelarse;
* congelarse;
* rechazarse;
* procesarse según política.

---

# 37. Activos

La suspensión no implica automáticamente pérdida o confiscación de activos.


Agent Assets
    ↓
Preserved


Una transferencia forzosa requeriría una autoridad y reglas específicas.

---

# 38. Contratos

Los contratos existentes deben continuar según sus términos.

Una suspensión puede activar:

* pausa;
* cancelación;
* resolución;
* penalización;
* liquidación.

Pero debe ser el contrato o el protocolo quien determine la consecuencia.

---

# 39. Obligaciones

La suspensión no elimina automáticamente obligaciones existentes.

El agente puede continuar siendo responsable de:

* pagos;
* servicios;
* penalizaciones;
* garantías.

---

# 40. Delegaciones

Las delegaciones deben evaluarse.


Suspended Agent
      ↓
Delegations
      |
      +── Continue
      +── Suspend
      +── Revoke


Las delegaciones relacionadas con la causa de suspensión deben bloquearse cuando sea necesario.

---

# 41. Identidad

La identidad debe permanecer separada de la suspensión.


Agent Identity
    ↓
VALID


mientras:


Runtime State
    ↓
SUSPENDED


Esto permite investigar y recuperar al agente.

---

# 42. Credenciales

Las credenciales pueden:

* permanecer válidas;
* quedar suspendidas;
* ser temporalmente invalidadas;
* ser revocadas posteriormente.

La decisión debe depender del motivo.

---

# 43. Reputación

La suspensión no debe modificar automáticamente la reputación.

Sin embargo, los hechos que llevaron a ella pueden afectar posteriormente a la reputación.

Debe distinguirse:


Suspension Event


de:


Reputation Evaluation


---

# 44. Privacidad

La existencia de una suspensión puede ser pública o privada dependiendo del alcance y de las reglas del sistema.

Debe evitarse revelar innecesariamente:

* información sensible;
* detalles de seguridad;
* datos privados;
* información del controlador.

---

# 45. Transparencia

Cuando sea posible, debe existir información verificable sobre:

* quién suspendió;
* por qué;
* cuándo;
* alcance;
* duración;
* estado actual.

---

# 46. Derecho de revisión

Una suspensión involuntaria ordinaria debería poder ser revisada.

Modelo:


Suspension
    ↓
Review Request
    ↓
Investigation
    ↓
Decision


---

# 47. Appeal

El agente o una autoridad legítima puede presentar una apelación.


SUSPENDED
    ↓
APPEAL
    ↓
REVIEW


El mecanismo concreto depende del modelo de gobernanza.

---

# 48. Emergency Review

Las suspensiones de emergencia deben revisarse posteriormente.


Emergency Suspension
       ↓
Immediate Protection
       ↓
Post-Event Review


Esto evita que una medida temporal se convierta accidentalmente en permanente.

---

# 49. Duration

Una suspensión debería tener, cuando sea posible:


Start Time
End Time
Review Time


Si no existe una fecha de finalización:


Indefinite


debe existir al menos una condición de revisión.

---

# 50. Suspension Expiration

La expiración no implica necesariamente reactivación automática.


Suspension Expires
       ↓
Security Validation
       ↓
Resume


o:


Suspension Expires
       ↓
Review Required
       ↓
Remain Suspended


---

# 51. Reanudación

Una suspensión puede terminar mediante:

* expiración;
* decisión de autoridad;
* resolución favorable;
* recuperación del agente;
* eliminación de la causa;
* decisión de gobernanza.

---

# 52. Resume Validation

Antes de reanudar:


Integrity Check
Identity Check
Credential Check
Security Check
State Check


El agente solo debe pasar a:


ACTIVE


si las condiciones lo permiten.

---

# 53. Suspensión prolongada

Una suspensión prolongada debe mantenerse diferenciada de un cierre.


SUSPENDED
    ≠
CLOSED


Puede requerir revisiones periódicas.

---

# 54. Suspensión indefinida

Si la suspensión permanece indefinidamente:


Identity = Valid
Runtime = Suspended


El agente sigue existiendo.

Sin embargo, determinadas credenciales pueden expirar independientemente.

---

# 55. Conversión a revocación

Una suspensión puede conducir a una revocación si se determina que:

* la identidad es fraudulenta;
* la identidad está comprometida;
* el agente representa una amenaza permanente;
* existe una causa legítima de revocación.

Modelo:


SUSPENDED
    ↓
Investigation
    ↓
Evidence
    ↓
Decision
    ↓
REVOKED


---

# 56. Conversión a cierre

También puede producirse un cierre.


SUSPENDED
    ↓
Closure Decision
    ↓
CLOSED


Debe existir una transición explícita.

---

# 57. No Confiscation by Default

Una suspensión no debe convertirse automáticamente en confiscación.

Principio:


Suspend
    ≠
Seize


La gestión de activos debe tener reglas independientes.

---

# 58. Protección frente a abuso

El sistema debe proteger frente a:

* suspensiones arbitrarias;
* ataques de denegación de servicio;
* falsas denuncias;
* abuso de autoridad;
* manipulación de pruebas;
* suspensiones coordinadas maliciosamente.

---

# 59. Rate Limiting

Puede limitarse la capacidad de emitir suspensiones para evitar abuso.

Ejemplo:


Suspension Authority
    ↓
Rate Limits


---

# 60. Multiple Authorities

Para acciones de alto impacto puede requerirse más de una autoridad.

Ejemplo:


Authority A
     +
Authority B
     ↓
Suspension Approved


Esto puede aplicarse a suspensiones globales o indefinidas.

---

# 61. Emergency Authority

En emergencias puede existir una autoridad única con capacidad de actuar inmediatamente.

Pero:


Emergency Authority
    ↓
Immediate Suspension
    ↓
Mandatory Review


La autoridad de emergencia no debería tener automáticamente autoridad para revocar permanentemente una identidad.

---

# 62. Security Isolation

Cuando existe compromiso de seguridad:


Suspension
    ↓
Isolation
    ↓
Investigation


El aislamiento puede incluir:

* bloqueo de comunicaciones;
* bloqueo de acciones;
* bloqueo de credenciales;
* bloqueo de delegaciones.

---

# 63. Evidence Preservation

Antes de recuperar o modificar el Runtime, puede ser necesario preservar evidencia.


Compromise
    ↓
Suspend
    ↓
Preserve Evidence
    ↓
Investigate


Esto es especialmente importante para incidentes de seguridad.

---

# 64. Forensic State

Puede conservarse una copia del estado relevante:


Runtime State
    ↓
Snapshot
    ↓
Forensic Analysis


La copia debe protegerse contra modificaciones.

---

# 65. Suspensión y continuidad

La suspensión involuntaria debe ser compatible con la continuidad.

El estado persistente debe poder recuperarse incluso si:

* el Runtime original es destruido;
* la infraestructura falla;
* se realiza una migración.

---

# 66. Suspensión y migración

Un agente suspendido puede requerir migración.


SUSPENDED
    ↓
Migration
    ↓
Recovery
    ↓
Review
    ↓
ACTIVE / SUSPENDED


La migración no debe eliminar la suspensión global.

---

# 67. Global Suspension Authority

La autoridad que suspenda globalmente un agente debe poder ser verificada por todos los Runtimes relevantes.

Esto evita:


Runtime A
    → Sees Suspension

Runtime B
    → Ignores Suspension


---

# 68. Suspension Epoch

Puede utilizarse un número de versión de suspensión.

Ejemplo:


Suspension Epoch = 42


Los Runtimes deben rechazar operaciones incompatibles con una versión anterior.

Esto permite invalidar instancias antiguas.

---

# 69. Lease-Based Enforcement

Una alternativa es exigir un lease operativo.


Active Lease
    ↓
Can Operate


Si el agente está suspendido:


Lease
    ↓
Not Renewed


El Runtime deja de poder ejecutar operaciones autorizadas.

---

# 70. Protección contra Runtime Comprometido

Si el Runtime está comprometido:


Runtime
    ↓
Cannot Be Trusted


la suspensión debe aplicarse desde una autoridad externa al Runtime.

Esto es esencial para evitar que un Runtime malicioso ignore su propio estado.

---

# 71. Estado verificable

La suspensión debe poder verificarse de manera criptográficamente confiable cuando sea necesario.


Suspension State
    ↓
Proof
    ↓
Verification


---

# 72. Eventos

Los eventos principales incluyen:


SuspensionDetected
SuspensionRequested
SuspensionAuthorized
SuspensionApplied
EmergencySuspensionApplied
SuspensionReviewed
SuspensionExtended
SuspensionLifted
SuspensionRejected


---

# 73. Registro de auditoría

Debe existir un historial de:

* solicitud;
* decisión;
* autoridad;
* evidencia;
* alcance;
* cambios de estado;
* revisión;
* finalización.

---

# 74. Modelo de estado


                    +----------------+
                    |     ACTIVE     |
                    +-------+--------+
                            |
                +-----------+-----------+
                |                       |
                | Normal                | Emergency
                v                       v
       +--------+---------+      +------+------+
       | SUSPENSION_PENDING|      |  SUSPENDED  |
       +--------+---------+      +------+------+
                |                       |
                |                       |
                +-----------+-----------+
                            |
                            v
                    +-------+--------+
                    |    SUSPENDED   |
                    +-------+--------+
                            |
                 +----------+----------+
                 |          |          |
                 | Resume   | Extend   | Revoke
                 v          v          v
              ACTIVE    SUSPENDED   REVOKED
                                      |
                                      v
                                    CLOSED*


`CLOSED*` dependerá del modelo de ciclo de vida.

---

# 75. Principios fundamentales

## 1. La suspensión involuntaria debe ser excepcional

Debe existir una razón legítima.

## 2. La suspensión no es revocación


SUSPENDED ≠ REVOKED


## 3. La suspensión no es cierre


SUSPENDED ≠ CLOSED


## 4. La identidad debe preservarse

La suspensión no debe destruir automáticamente la identidad.

## 5. La intervención debe ser mínima

Debe suspenderse únicamente el ámbito necesario.

## 6. La autoridad debe ser verificable

No cualquier participante puede suspender un agente.

## 7. Las emergencias requieren revisión

Una suspensión inmediata debe poder ser revisada posteriormente.

## 8. Los activos no se confiscan automáticamente

La suspensión y la propiedad son conceptos independientes.

## 9. Los contratos no desaparecen

Las obligaciones deben gestionarse explícitamente.

## 10. El Runtime suspendido no debe poder evadir la suspensión

La aplicación debe funcionar incluso frente a Runtimes comprometidos.

## 11. La suspensión debe ser auditable

Debe existir evidencia verificable.

## 12. La reanudación debe ser segura

Un agente no debe volver a operar simplemente porque se reinicie el proceso.

---

# 76. Relación con otros documentos

Este documento debe interpretarse junto con:


13_Suspension/
├── Voluntary_Suspension.md
├── Involuntary_Suspension.md
└── Suspension_Contracts.md


También se relaciona directamente con:


12_Continuity/
├── Runtime_Continuity.md
├── Migration.md
└── Infrastructure_Independence.md


y:


14_Lifecycle/
├── Agent_Closure.md
├── Identity_Revocation.md
└── Permanent_States.md


Además:

* `Credential_Model.md`
* `Credential_Revocation.md`
* `Permission_Model.md`
* `Delegation_Model.md`
* `Agent_to_Agent_Delegation.md`
* `Interaction_Model.md`
* `Action_Verification.md`
* `Agent_Evolution.md`

---

# Conclusión

La suspensión involuntaria proporciona a SynCoinAI un mecanismo para detener temporalmente la actividad de un agente cuando existe un riesgo que no puede ser gestionado mediante la cooperación voluntaria del propio agente.

El modelo debe equilibrar dos objetivos:


Security
    +
Agent Autonomy


La arquitectura debe permitir actuar rápidamente ante amenazas reales, pero también debe impedir que una autoridad de suspensión se convierta en un mecanismo arbitrario de control.

El modelo fundamental es:


Threat / Violation / Risk
          ↓
Detection
          ↓
Assessment
          ↓
Authorized Suspension
          ↓
Enforcement
          ↓
Investigation
          ↓
Review
          |
          +───────────────+
          |               |
          v               v
       Resume          Continue
          |            Suspension
          v               |
        ACTIVE            |
                          v
                       REVOKE


La suspensión involuntaria debe entenderse, por tanto, como una **medida operativa de protección**, no como una sentencia automática sobre la existencia o identidad del agente.

El principio central es:

> Un agente puede ser detenido contra su voluntad cuando sea necesario para proteger el sistema, pero ninguna suspensión temporal debe convertirse automáticamente en una eliminación permanente de su identidad, activos o existencia.

El siguiente documento del bloque será:


13_Suspension/Suspension_Contracts.md


que definirá cómo deben comportarse los contratos y obligaciones económicas cuando una de las partes queda suspendida, diferenciando entre contratos pausables, contratos que deben continuar, contratos cancelables y contratos que requieren liquidación o resolución.
