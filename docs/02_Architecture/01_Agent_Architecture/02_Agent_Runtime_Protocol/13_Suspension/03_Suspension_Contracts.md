# SynCoinAI Agent Runtime Protocol

# Suspension Contracts

## Gestión de Contratos durante la Suspensión de un Agente

**Versión:** 1.0
**Documento:** `02_Architecture / 01_Agent_Architecture / 02_Agent_Runtime_Protocol / 13_Suspension / Suspension_Contracts.md`
**Estado:** Arquitectura inicial

---

# 1. Introducción

Los agentes SynCoinAI pueden participar en relaciones económicas y operativas con otros agentes.

Estas relaciones pueden materializarse mediante:

* contratos;
* acuerdos de servicio;
* órdenes de trabajo;
* delegaciones;
* compromisos de pago;
* entregas de recursos;
* garantías;
* depósitos;
* obligaciones verificables.

La suspensión de un agente no debe producir automáticamente un comportamiento ambiguo respecto a estas relaciones.

Un agente puede quedar suspendido mientras mantiene:

* contratos activos;
* servicios en ejecución;
* pagos pendientes;
* obligaciones futuras;
* depósitos bloqueados;
* garantías;
* recursos de terceros;
* tareas delegadas.

Por tanto, el protocolo debe definir explícitamente qué ocurre con cada relación contractual.

El principio fundamental es:

> La suspensión del Runtime de un agente no elimina automáticamente las obligaciones contractuales existentes.

---

# 2. Objetivo

Este documento define:

* cómo afecta la suspensión a los contratos;
* qué ocurre con contratos nuevos;
* qué ocurre con contratos existentes;
* cómo se clasifican los contratos;
* qué operaciones pueden continuar;
* qué operaciones deben detenerse;
* cómo se gestionan los pagos;
* cómo se gestionan las garantías;
* cómo se resuelven incumplimientos;
* cómo se gestionan contratos suspendidos;
* cómo se reanudan;
* cómo se cancelan;
* cómo se liquidan.

---

# 3. Principio de separación

Debe distinguirse entre:


Agent State


y:


Contract State


Por ejemplo:


Agent = SUSPENDED
Contract = ACTIVE


es un estado válido.

También:


Agent = SUSPENDED
Contract = PAUSED


o:


Agent = SUSPENDED
Contract = TERMINATED


pueden ser estados válidos.

La suspensión del agente no determina automáticamente el estado final de todos sus contratos.

---

# 4. Suspensión del agente frente al contrato

El modelo fundamental es:


Agent Suspension
       |
       v
Contract Policy Evaluation
       |
       +── Continue
       +── Pause
       +── Cancel
       +── Terminate
       +── Settle


La consecuencia debe depender de:

* tipo de contrato;
* cláusulas;
* estado;
* riesgo;
* alcance de la suspensión;
* causa de suspensión.

---

# 5. Tipos de contrato

El protocolo distingue inicialmente:


CONTINUOUS
PAUSABLE
NON_PAUSABLE
CANCELABLE
TERMINABLE
SETTLEMENT_REQUIRED
EMERGENCY


Un contrato puede pertenecer a más de una categoría.

---

# 6. Contratos continuos

Un contrato continuo puede seguir ejecutándose aunque el agente esté suspendido.

Ejemplo:


Agent A → SUSPENDED
Contract → ACTIVE


Esto es posible cuando:

* la ejecución no requiere intervención del Runtime suspendido;
* existe un mecanismo automatizado;
* un tercero autorizado puede ejecutar la obligación;
* la suspensión afecta a una capacidad no relacionada.

---

# 7. Contratos pausables

Un contrato pausables puede detener temporalmente su ejecución.


ACTIVE
   ↓
PAUSED


Posteriormente:


PAUSED
   ↓
RESUMED


La pausa debe conservar:

* estado;
* progreso;
* obligaciones;
* condiciones;
* referencias temporales.

---

# 8. Contratos no pausables

Algunos contratos no pueden detenerse sin consecuencias.

Ejemplos:

* servicios de tiempo crítico;
* operaciones con ventanas temporales;
* procesos físicos;
* entregas programadas;
* liquidaciones.

En estos casos la suspensión puede provocar:


Failure


o:


Settlement


según las reglas contractuales.

---

# 9. Contratos cancelables

Un contrato cancelable puede terminarse cuando una suspensión activa una condición de cancelación.

Ejemplo:


Agent Suspended
       ↓
Contract Cancellation Condition
       ↓
CANCEL


---

# 10. Contratos terminables

Algunos contratos pueden terminar automáticamente si la suspensión supera un periodo determinado.

Ejemplo:


Suspension
       ↓
Grace Period
       ↓
Still Suspended
       ↓
Termination


---

# 11. Contratos que requieren liquidación

Algunos contratos requieren calcular primero las obligaciones existentes.


Suspension
    ↓
Settlement
    ↓
Final Payment
    ↓
Contract Closed


---

# 12. Contratos de emergencia

Los contratos relacionados con seguridad o infraestructura crítica pueden requerir tratamiento especial.

Por ejemplo:


Agent Suspended
       ↓
Emergency Contract
       ↓
Continue Execution


La suspensión no debe impedir automáticamente acciones necesarias para evitar daños.

---

# 13. Nuevos contratos

Por defecto, un agente completamente suspendido no debería poder crear nuevos contratos autónomos.


SUSPENDED
    ↓
New Contract
    ↓
REJECTED


Esto evita que un agente suspendido continúe generando obligaciones.

---

# 14. Suspensión parcial

Si la suspensión es parcial, puede ser posible crear contratos relacionados con capacidades no suspendidas.

Ejemplo:


Capability A → ACTIVE
Capability B → SUSPENDED


Entonces:


Contract A → ALLOWED
Contract B → BLOCKED


---

# 15. Contratos preexistentes

Los contratos creados antes de la suspensión deben conservar su estado.


Contract
    ↓
Created Before Suspension
    ↓
Existing Contract


La suspensión debe activar una evaluación de su tratamiento.

---

# 16. Contract Suspension Policy

Cada contrato debería definir una política de suspensión.

Conceptualmente:


ContractSuspensionPolicy
    |
    +── OnAgentSuspension
    +── OnPartialSuspension
    +── OnGlobalSuspension
    +── OnSecuritySuspension
    +── OnEmergencySuspension


---

# 17. Política por causa

La consecuencia puede depender de la causa.

Por ejemplo:


Maintenance Suspension
    → Pause



Security Suspension
    → Freeze



Emergency Suspension
    → Immediate Stop



Economic Suspension
    → Settlement


---

# 18. Política por alcance

También depende del alcance.


Runtime Suspension


puede no afectar a:


Contract


si otro Runtime autorizado puede cumplirlo.

Mientras:


Global Agent Suspension


puede afectar a todos los contratos dependientes del agente.

---

# 19. Contratos dependientes del Runtime

Un contrato puede depender de un Runtime concreto.


Contract
    ↓
Runtime A


Si:


Runtime A = SUSPENDED


el contrato debe reevaluarse.

---

# 20. Contratos independientes del Runtime

Un contrato puede ejecutarse mediante infraestructura externa.


Agent
   |
   +── Runtime A → SUSPENDED
   |
   +── Contract Engine → ACTIVE


El contrato puede continuar si sus condiciones lo permiten.

---

# 21. Estado del contrato

Se recomienda utilizar estados explícitos:


DRAFT
ACTIVE
PAUSED
FROZEN
PENDING_SETTLEMENT
CANCELLED
TERMINATED
COMPLETED
DISPUTED


---

# 22. Suspended Contract

No es necesario crear un estado contractual universal llamado `SUSPENDED`.

Puede utilizarse:


Contract = PAUSED
Suspension Cause = Agent Suspension


Esto evita mezclar:


Agent State


con:


Contract State


---

# 23. Contract Freeze

Un contrato puede quedar congelado.


FROZEN


Esto significa que:

* no se ejecutan nuevas acciones;
* no se modifican condiciones;
* no se realizan nuevas transferencias;
* se preserva el estado.

Puede utilizarse durante investigaciones de seguridad.

---

# 24. Pausa frente a congelación

La diferencia conceptual es:


PAUSED


permite una reanudación normal.


FROZEN


implica una restricción más fuerte.

Por ejemplo:


PAUSED
    → Resume


mientras:


FROZEN
    → Review
    → Authorization
    → Resume


---

# 25. Acciones en ejecución

Cuando se suspende un agente con acciones contractuales activas, cada acción debe clasificarse:


RUNNING
COMPLETABLE
CANCELLABLE
IRREVERSIBLE
BLOCKED


---

# 26. Acción completable

Una acción segura puede finalizarse antes de suspender completamente el contrato.


Action Running
      ↓
Safe Completion
      ↓
Contract Paused


---

# 27. Acción cancelable

Una acción puede cancelarse.


Running Action
      ↓
Cancel
      ↓
Rollback / Compensation


---

# 28. Acción irreversible

Si una acción ya no puede detenerse:


Irreversible Action
      ↓
Continue Until Safe Point


o:


Emergency Stop


dependiendo del riesgo.

---

# 29. Acción bloqueada

Una acción puede quedar bloqueada:


Action
    ↓
BLOCKED


hasta que:

* termine la suspensión;
* exista autorización;
* otro agente asuma la ejecución.

---

# 30. Pagos pendientes

Los pagos deben gestionarse de forma explícita.

Ejemplo:


Payment Pending
       ↓
Agent Suspended
       ↓
Evaluate


Resultado:


PAY
HOLD
CANCEL
SETTLE


---

# 31. Pagos recibidos

La suspensión no debería impedir automáticamente que un agente reciba fondos.

Por ejemplo:


Agent Suspended
       ↓
Incoming Payment
       ↓
Accepted


si la política económica lo permite.

---

# 32. Pagos salientes

Los pagos autónomos pueden quedar bloqueados.


SUSPENDED
    ↓
Outgoing Payment
    ↓
Blocked


Excepto cuando:

* sea una obligación contractual;
* sea necesario para liquidación;
* exista autorización específica.

---

# 33. Pagos automáticos

Los pagos programados deben tener reglas específicas.


Scheduled Payment
       ↓
Agent Suspended


Puede:


Execute


o:


Pause


según la política contractual.

---

# 34. Garantías

Las garantías deben permanecer protegidas.


Collateral
    ↓
Preserved


La suspensión no implica automáticamente pérdida de garantía.

---

# 35. Liquidación de garantías

Una garantía puede ejecutarse cuando:

* existe incumplimiento;
* el contrato lo establece;
* una condición de liquidación se activa.


Suspension
    ↓
Contract Default
    ↓
Collateral Liquidation


La suspensión por sí sola no debe equivaler automáticamente a default.

---

# 36. Default

Debe distinguirse:


Suspension


de:


Default


Un agente puede estar suspendido sin haber incumplido.


Suspended
    ≠
Default


---

# 37. Suspensión como evento de default

Un contrato puede establecer explícitamente:


Suspension
    ↓
Default


pero esta condición debe existir previamente en el contrato.

No debe asumirse universalmente.

---

# 38. Grace Period

Puede existir un periodo de gracia.


Suspension
    ↓
Grace Period
    ↓
Resume


o:


Suspension
    ↓
Grace Period
    ↓
Default


---

# 39. Contract Counterparty

La contraparte debe poder conocer el estado relevante.

Por ejemplo:


Contract
    ↓
Counterparty Agent Suspended


La información disponible dependerá de los permisos y de la privacidad.

---

# 40. Notification

Una suspensión que afecta a un contrato puede generar una notificación.


Suspension Event
       ↓
Contract Impact Evaluation
       ↓
Notify Counterparty


---

# 41. Notification Content

La notificación puede incluir:


Agent ID
Contract ID
Suspension Scope
Suspension Status
Effective Time
Expected Duration
Contract Impact


No debe revelar información confidencial innecesaria.

---

# 42. Contract Evaluation

Al producirse una suspensión:


Suspension
    ↓
Enumerate Contracts
    ↓
Evaluate Each Contract
    ↓
Apply Contract Policy


---

# 43. Contract Dependency Graph

Un agente puede tener múltiples contratos relacionados.


Agent
 |
 +── Contract A
 |       |
 |       +── Contract B
 |
 +── Contract C
         |
         +── Contract D


La suspensión de un contrato puede afectar a otros.

Por ello, el sistema debe permitir identificar dependencias.

---

# 44. Cascading Suspension

Una suspensión puede generar efectos en cadena.


Agent Suspended
      ↓
Contract A Paused
      ↓
Contract B Cannot Execute
      ↓
Contract B Paused


Estos efectos deben estar controlados.

No debe producirse una cascada ilimitada sin reglas.

---

# 45. Cascading Failure Protection

El sistema debería evitar que una suspensión provoque automáticamente:


Agent A
    ↓
Suspended
    ↓
100 Agents
    ↓
All Suspended


La propagación debe basarse en dependencias reales.

---

# 46. Third-Party Fulfillment

Un contrato puede permitir que un tercero complete la obligación.


Agent A Suspended
       ↓
Contract
       ↓
Agent B / Agent C
       ↓
Fulfillment


Esto puede reducir el impacto de una suspensión.

---

# 47. Delegated Fulfillment

La ejecución puede delegarse.


Suspended Agent
       ↓
Authorized Delegate
       ↓
Contract Execution


La delegación debe existir y estar autorizada.

---

# 48. Contract Substitution

Algunos contratos pueden permitir sustituir al agente ejecutor.


Agent A
   ↓
Suspended
   ↓
Agent B
   ↓
Contract Continues


Esto debe estar definido contractualmente.

---

# 49. Human Intervention

En determinados contratos puede existir intervención humana.


Agent Suspended
       ↓
Human Operator
       ↓
Contract Resolution


Esto debe estar autorizado por las reglas del contrato.

---

# 50. Contract Dispute

Si existe desacuerdo:


Suspension
    ↓
Counterparty Dispute


el contrato puede entrar en:


DISPUTED


La suspensión no resuelve automáticamente la disputa.

---

# 51. Evidence

La evidencia relevante debe conservarse:

* acciones;
* entregables;
* pagos;
* mensajes;
* verificaciones;
* pruebas de servicio.

Esto permite determinar responsabilidades.

---

# 52. Proof of Service

Si el agente ya realizó un servicio antes de la suspensión:


Service Completed
       ↓
Proof Generated
       ↓
Agent Suspended


la prueba sigue siendo válida.

La suspensión posterior no invalida automáticamente el servicio realizado.

---

# 53. Servicio parcialmente completado

Si un servicio está incompleto:


Service
    ↓
50% Complete
    ↓
Agent Suspended


el contrato debe determinar:

* pago parcial;
* devolución;
* continuación;
* sustitución;
* cancelación.

---

# 54. Servicios físicos

En agentes físicos:


Physical Service
       ↓
Agent Suspended


puede ser necesario:

* detener el sistema;
* llevarlo a estado seguro;
* transferir la tarea;
* completar una operación crítica.

---

# 55. Servicios críticos

Los contratos relacionados con servicios críticos pueden tener prioridad especial.

Ejemplo:


Emergency Service
       ↓
Agent Suspended
       ↓
Safe Continuation


La seguridad debe tener prioridad sobre la suspensión operativa cuando sea necesario evitar daños.

---

# 56. Contract Timeout

Los contratos pueden incluir timeouts.


Contract Active
       ↓
Agent Suspended
       ↓
Timeout


Resultado:


Cancel
Default
Settlement


según las condiciones.

---

# 57. Suspension Timeout

El contrato puede definir cuánto tiempo tolera una suspensión.


Suspension Duration
       ↓
Contract Grace Period
       ↓
Termination


---

# 58. Resume Contract

Si el agente vuelve a estar activo:


Agent SUSPENDED
       ↓
Agent ACTIVE
       ↓
Contract Resume Evaluation


No todos los contratos deben reanudarse automáticamente.

---

# 59. Reanudación automática

Puede ocurrir:


PAUSED
   ↓
Agent Resumed
   ↓
ACTIVE


si se cumplen las condiciones.

---

# 60. Reanudación manual

Puede requerirse autorización.


Agent Resumed
       ↓
Contract Review
       ↓
Manual Resume


---

# 61. Contratos no reanudables

Un contrato puede haber expirado durante la suspensión.


Suspension
    ↓
Contract Expired


En ese caso:


Resume Agent
    ≠
Resume Contract


---

# 62. Reconciliación contractual

Tras una suspensión debe realizarse una reconciliación.


Resume
   ↓
Contract Reconciliation
   ↓
Outstanding Obligations
   ↓
Payments
   ↓
Deliverables
   ↓
Final State


---

# 63. Obligaciones acumuladas

Durante la suspensión pueden acumularse obligaciones.

Ejemplo:


Monthly Payment
    ↓
Suspended
    ↓
3 Months
    ↓
Outstanding Balance


El contrato debe definir si:

* se acumulan;
* se congelan;
* se cancelan;
* se liquidan.

---

# 64. Penalizaciones

Las penalizaciones no deben aplicarse automáticamente por cualquier suspensión.

Debe distinguirse:


Suspension


de:


Contract Breach


---

# 65. Suspension Without Fault

Si el agente fue suspendido sin incumplimiento:


Suspended
    +
No Fault


el contrato puede prever:

* pausa;
* extensión;
* compensación;
* reanudación.

---

# 66. Suspension With Fault

Si la suspensión deriva de una conducta contractual demostrada:


Violation
    ↓
Suspension
    ↓
Default


pueden activarse las consecuencias contractuales.

---

# 67. Security Suspension

En una suspensión por seguridad:


Security Risk
    ↓
Contract Freeze


puede ser preferible congelar temporalmente las operaciones hasta determinar si el agente está comprometido.

---

# 68. Emergency Suspension

En una emergencia:


Emergency
    ↓
Immediate Contract Action


Puede ser necesario:

* detener operaciones;
* bloquear pagos;
* proteger activos;
* transferir ejecución.

---

# 69. Asset Preservation

Durante la suspensión deben preservarse, cuando corresponda:

* balances;
* depósitos;
* garantías;
* propiedad digital;
* recursos bloqueados.

---

# 70. Asset Lock

Puede aplicarse un bloqueo temporal:


Asset
    ↓
LOCKED


Esto no implica transferencia de propiedad.

---

# 71. Asset Release

Tras resolver la suspensión:


LOCKED
    ↓
Review
    ↓
UNLOCKED


o:


LOCKED
    ↓
Contract Settlement


---

# 72. Contract Authority

El contrato debe definir qué autoridad puede cambiar su estado.

Por ejemplo:


Contract
    |
    +── Agent
    +── Counterparty
    +── Arbitrator
    +── Governance
    +── Smart Contract


---

# 73. Smart Contract Execution

Un contrato inteligente puede continuar ejecutándose independientemente del Runtime.

Por ello:


Agent Suspended
       ↓
Smart Contract
       ↓
Still Executes


puede ser válido.

La arquitectura debe considerar esta posibilidad.

---

# 74. Runtime Suspension vs Smart Contract State

Debe distinguirse:


Runtime State


de:


Smart Contract State


Una suspensión del Runtime no debe alterar arbitrariamente el estado blockchain.

---

# 75. Contract Enforcement

Las consecuencias contractuales deben ejecutarse mediante mecanismos definidos.


Contract Condition
       ↓
Verified
       ↓
Enforcement


No debe depender únicamente del Runtime suspendido.

---

# 76. Contract Recovery

Tras la reanudación:


Agent Resumed
       ↓
Contract Recovery


puede ser necesario restaurar:

* tareas;
* estados;
* sesiones;
* pagos;
* obligaciones.

---

# 77. Contract Reconciliation Record

Debe registrarse:


ContractReconciliation
    |
    +── Contract ID
    +── Suspension Period
    +── Actions Completed
    +── Actions Cancelled
    +── Payments
    +── Outstanding Obligations
    +── Final Resolution


---

# 78. Auditoría

Los eventos contractuales deben ser auditables.


Suspension
    ↓
Contract Impact
    ↓
Resolution


El historial debe poder reconstruirse.

---

# 79. Privacidad

La información contractual debe respetar los permisos.

No todos los observadores deben conocer:

* detalles del contrato;
* cantidades;
* condiciones privadas;
* identidad de las partes.

---

# 80. Modelo de transición


                  AGENT SUSPENSION
                         |
                         v
                CONTRACT EVALUATION
                         |
          +--------------+--------------+
          |              |              |
          v              v              v
       CONTINUE         PAUSE          FREEZE
          |              |              |
          |              |              |
          +--------------+--------------+
                         |
                         v
                     RESUME
                         |
                         v
                   RECONCILIATION
                         |
                         v
                    CONTRACT ACTIVE


Alternativamente:


                  CONTRACT EVALUATION
                         |
                +--------+--------+
                |                 |
                v                 v
             SETTLE           TERMINATE
                |                 |
                v                 v
             CLOSED            CLOSED


---

# 81. Modelo completo


Agent ACTIVE
      |
      | Contract ACTIVE
      |
      v
Agent SUSPENDED
      |
      +── Contract A → CONTINUE
      |
      +── Contract B → PAUSED
      |
      +── Contract C → FROZEN
      |
      +── Contract D → SETTLEMENT
      |
      +── Contract E → TERMINATED
      |
      v
Agent RESUMED
      |
      +── Contract A → ACTIVE
      +── Contract B → RESUME
      +── Contract C → REVIEW
      +── Contract D → CLOSED
      +── Contract E → CLOSED


---

# 82. Requisitos de implementación

Una implementación compatible debe:

* distinguir estado del agente y estado contractual;
* impedir nuevos contratos durante suspensión global;
* evaluar contratos existentes;
* aplicar políticas de suspensión;
* preservar contratos y evidencias;
* gestionar pagos pendientes;
* proteger activos;
* gestionar garantías;
* soportar pausa y congelación;
* permitir liquidación;
* registrar reconciliación;
* respetar privacidad.

---

# 83. Requisitos avanzados

Una implementación avanzada debería soportar:

* políticas contractuales configurables;
* clasificación automática de contratos;
* evaluación de dependencias;
* ejecución por terceros;
* delegación de cumplimiento;
* sustitución de agentes;
* congelación selectiva;
* liquidación automática;
* reconciliación automática;
* notificaciones;
* contratos cross-agent;
* contratos con agentes físicos;
* integración con smart contracts.

---

# 84. Principios fundamentales

## 1. Suspensión no significa incumplimiento


Suspension ≠ Default


## 2. Suspensión no significa cancelación


Suspension ≠ Contract Cancellation


## 3. Los contratos tienen estado propio

El estado contractual debe mantenerse independiente del estado del agente.

## 4. La política contractual debe ser explícita

Cada contrato debe definir qué ocurre ante una suspensión.

## 5. La suspensión parcial debe tener consecuencias parciales

No debe bloquearse más de lo necesario.

## 6. Los activos deben protegerse

La suspensión no implica confiscación automática.

## 7. Las obligaciones existentes deben gestionarse

No desaparecen por la suspensión.

## 8. Los contratos inteligentes pueden continuar

El Runtime y la blockchain son sistemas distintos.

## 9. La recuperación requiere reconciliación

Reanudar el agente no implica automáticamente reanudar todos los contratos.

## 10. La seguridad tiene prioridad

Los contratos críticos deben poder detenerse cuando exista riesgo.

---

# 85. Relación con otros documentos

Este documento se relaciona directamente con:


13_Suspension/
├── Voluntary_Suspension.md
├── Involuntary_Suspension.md
└── Suspension_Contracts.md


También depende conceptualmente de:


04_Economic_Architecture/
├── Economic_Model.md
├── Service_Market_Architecture.md
├── Agent_Transactions.md
└── Token_Integration.md


y:


05_Communication_Architecture/
├── Agent_Communication.md
├── Discovery_Protocol.md
└── Negotiation_Protocol.md


Además:

* `Interaction_Model.md`
* `Delegation_Model.md`
* `Agent_to_Agent_Delegation.md`
* `Action_Verification.md`
* `Proof_of_Service.md`
* `Agent_Continuity.md`
* `Runtime_Continuity.md`
* `Migration.md`
* `Credential_Revocation.md`

---

# Conclusión

Los contratos representan una de las principales consecuencias prácticas de la suspensión de un agente.

Por este motivo, SynCoinAI no debe implementar una regla simplista como:


Agent Suspended
      ↓
All Contracts Cancelled


El comportamiento correcto es:


Agent Suspended
      ↓
Evaluate Contracts
      ↓
Apply Contract-Specific Policy
      |
      +── Continue
      +── Pause
      +── Freeze
      +── Delegate
      +── Substitute
      +── Settle
      +── Terminate


Esto permite que el ecosistema continúe siendo económicamente consistente incluso cuando determinados agentes dejan temporalmente de operar.

El principio central es:

> La suspensión afecta a la capacidad operativa del agente, pero las obligaciones contractuales sobreviven hasta que sean cumplidas, pausadas, resueltas o liquidadas conforme a las reglas que las gobiernan.

Con este documento queda completado el bloque:


13_Suspension/
├── Voluntary_Suspension.md
├── Involuntary_Suspension.md
└── Suspension_Contracts.md


El siguiente bloque del `Agent_Runtime_Protocol` es:


14_Lifecycle/
├── Agent_Closure.md
├── Identity_Revocation.md
└── Permanent_States.md


El siguiente documento recomendado es **`14_Lifecycle/Agent_Closure.md`**, porque establece la diferencia fundamental entre un agente suspendido y un agente que ha terminado su existencia operativa.
