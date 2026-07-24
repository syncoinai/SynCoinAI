# SynCoinAI Contract Obligations

## Modelo de obligaciones contractuales del agente

**Versión:** 1.0
**Documento:** `02_Architecture / 01_Agent_Architecture / 02_Agent_Runtime_Protocol / 08_Contracts / Contract_Obligations.md`
**Estado:** Arquitectura inicial

---

# 1. Introducción

Un contrato define una relación entre dos o más partes.

Sin embargo, un contrato solo puede ejecutarse si sus compromisos se convierten en acciones concretas.

Estas acciones y compromisos se representan mediante **obligaciones contractuales**.

Una obligación define:

* quién debe actuar;
* qué debe realizar;
* sobre qué recurso;
* bajo qué condiciones;
* cuándo debe hacerlo;
* qué resultado debe producir;
* cómo se verificará;
* qué ocurre si no se cumple.

En SynCoinAI, las obligaciones constituyen una de las principales unidades de trabajo del Agent Runtime.

El runtime debe ser capaz de transformar una obligación contractual en una actividad operativa que el agente pueda:

* comprender;
* planificar;
* ejecutar;
* monitorizar;
* demostrar;
* completar.

---

# 2. Objetivo

Este documento define el modelo arquitectónico de las obligaciones contractuales.

Se establece:

* qué es una obligación;
* cómo se relaciona con un contrato;
* cómo se asigna a un agente;
* cómo se activa;
* cómo se ejecuta;
* cómo se monitoriza;
* cómo se verifica;
* cómo se completa;
* cómo se relaciona con recursos;
* cómo se relaciona con capacidades;
* cómo se relaciona con permisos;
* cómo se gestiona la delegación;
* cómo se gestionan obligaciones complejas;
* cómo se determina el cumplimiento.

Este documento no define en detalle los mecanismos de contingencia.

Estos se desarrollan en:


Contract_Contingencies.md


---

# 3. Definición de obligación

Una obligación contractual es un compromiso verificable asumido por una parte dentro de un contrato.

Formalmente:


Obligation =
Actor
+
Action
+
Object
+
Conditions
+
Constraints
+
Deadline
+
Verification


Una obligación debe permitir responder:


Who?
What?
On what?
When?
Under which conditions?
How is it verified?


---

# 4. Contrato y obligación

Un contrato puede contener una o múltiples obligaciones.

Ejemplo:


Contract C123
    │
    ├── Obligation 1
    │      Agent A must pay
    │
    ├── Obligation 2
    │      Agent B must provide service
    │
    └── Obligation 3
           Agent B must deliver result


Por tanto:


Contract
    ↓
Obligations
    ↓
Execution


El contrato proporciona el contexto.

Las obligaciones proporcionan las acciones concretas.

---

# 5. Obligación frente a condición

Una obligación no debe confundirse con una condición.

Ejemplo:


Condition:
Service verified



Obligation:
Release payment


La condición determina cuándo puede ejecutarse una acción.

La obligación determina qué debe realizarse.

Modelo:


Condition
    ↓
Satisfied
    ↓
Obligation Becomes Executable


---

# 6. Obligación frente a capacidad

Una obligación define lo que un agente debe hacer.

Una capacidad define lo que un agente puede hacer.

Ejemplo:


Obligation:
Analyze Dataset

Capability:
Data Analysis


La existencia de una obligación no garantiza que el agente tenga la capacidad necesaria.

El runtime debe comprobar:


Required Capability
        ↓
Available?
        ↓
Yes → Execute
No  → Cannot Execute


---

# 7. Obligación frente a permiso

Una capacidad no implica autorización.

Un agente puede tener:


Capability:
Transfer Funds


pero no tener:


Permission:
Transfer 1,000 SYNC


Por tanto:


Obligation
    ↓
Required Capability
    +
Required Permission
    ↓
Executable


---

# 8. Identificación de la obligación

Cada obligación debe tener un identificador único dentro de su contexto contractual.

Conceptualmente:


Obligation_ID


Ejemplo:


C123-O004


Esto permite referenciar la obligación desde:

* eventos;
* pruebas;
* verificaciones;
* pagos;
* disputas;
* contingencias.

---

# 9. Actor responsable

Cada obligación debe identificar la parte responsable de ejecutarla.

Ejemplo:


Obligation:
O001

Responsible:
Agent_B


El responsable puede ser:

* un agente;
* una entidad autorizada;
* un sistema;
* una entidad delegada.

La responsabilidad final debe estar claramente definida.

---

# 10. Beneficiario

Una obligación puede identificar a quién beneficia su cumplimiento.

Ejemplo:


Responsible:
Agent_B

Beneficiary:
Agent_A


No todas las obligaciones requieren un beneficiario explícito.

---

# 11. Acción

La acción representa lo que debe realizarse.

Ejemplos:


ANALYZE_DATA
DELIVER_RESULT
TRANSFER_FUNDS
PROVIDE_COMPUTE
STORE_DATA
VERIFY_RESULT
RELEASE_PAYMENT


Las acciones deben poder interpretarse de forma inequívoca.

---

# 12. Objeto de la obligación

El objeto representa aquello sobre lo que se ejecuta la acción.

Ejemplo:


Action:
ANALYZE_DATA

Object:
Dataset_X


Otro ejemplo:


Action:
TRANSFER_FUNDS

Object:
10 SYNC


---

# 13. Resultado esperado

Una obligación puede definir un resultado esperado.

Ejemplo:


Expected Result:
Analysis_Report_X


El resultado puede ser:

* un archivo;
* datos;
* una transacción;
* una prueba;
* un servicio;
* un cambio de estado.

---

# 14. Condiciones de ejecución

Una obligación puede depender de condiciones.

Ejemplo:


Condition:
Payment received


Solo entonces:


Obligation:
Start Service


Las condiciones pueden depender de:

* tiempo;
* eventos;
* otras obligaciones;
* verificaciones;
* recursos;
* estados externos.

---

# 15. Dependencias

Una obligación puede depender de otra.

Ejemplo:


Obligation A
Deliver Dataset
      ↓
Obligation B
Analyze Dataset
      ↓
Obligation C
Deliver Report


El runtime debe respetar estas dependencias.

---

# 16. Obligaciones secuenciales

Las obligaciones pueden formar secuencias.


O1
 ↓
O2
 ↓
O3


Ejemplo:


Receive Input
    ↓
Process Data
    ↓
Deliver Result


---

# 17. Obligaciones paralelas

Varias obligaciones pueden ejecutarse simultáneamente.


        ┌── O1
Contract
        ├── O2
        └── O3


Siempre que no existan dependencias entre ellas.

---

# 18. Obligaciones compuestas

Una obligación puede estar formada por varias subobligaciones.

Ejemplo:


Obligation A
    │
    ├── O-A1
    ├── O-A2
    └── O-A3


La obligación principal puede considerarse completada únicamente cuando todas las subobligaciones se cumplen.

---

# 19. Obligaciones condicionales

Una obligación puede depender de una condición lógica.

Ejemplo:


IF
Result Verified
THEN
Release Payment


La obligación solo se activa cuando la condición se cumple.

---

# 20. Obligaciones alternativas

Un contrato puede permitir diferentes formas de cumplimiento.

Ejemplo:


Deliver:
Option A
OR
Option B


El agente puede elegir una alternativa válida según las reglas contractuales.

---

# 21. Obligaciones opcionales

Algunas obligaciones pueden ser opcionales.

Ejemplo:


Optional:
Provide Additional Analysis


La ejecución puede depender de una decisión de una de las partes.

---

# 22. Obligaciones recurrentes

Una obligación puede repetirse periódicamente.

Ejemplo:


Every 24 hours:
Provide Status Report


El runtime debe generar o activar las instancias correspondientes.

---

# 23. Obligaciones permanentes

Algunas obligaciones pueden mantenerse durante toda la vida del contrato.

Ejemplo:


Maintain Data Availability


La obligación no se completa mediante una única acción.

Su cumplimiento se monitoriza continuamente.

---

# 24. Obligaciones temporales

Una obligación puede tener una ventana temporal.

Ejemplo:


Start:
2026-01-01

Deadline:
2026-01-10


El runtime debe controlar:


Before Start
Active Window
After Deadline


---

# 25. Deadline

Una obligación puede incluir una fecha límite.

Ejemplo:


Deadline:
2026-01-10 12:00 UTC


Una ejecución posterior puede considerarse:

* incumplimiento;
* cumplimiento tardío;
* cumplimiento aceptado.

La interpretación depende del contrato.

---

# 26. Tolerancia temporal

Algunas obligaciones pueden incluir tolerancia.

Ejemplo:


Deadline:
12:00

Grace Period:
30 minutes


El runtime debe conocer esta regla antes de determinar incumplimiento.

---

# 27. Obligaciones basadas en eventos

Una obligación puede activarse mediante un evento.

Ejemplo:


Event:
Payment Confirmed
      ↓
Activate Obligation


Otros eventos:

* contrato activado;
* servicio solicitado;
* recurso disponible;
* verificación completada.

---

# 28. Obligaciones económicas

Una obligación puede implicar recursos económicos.

Ejemplo:


Agent A
Must Pay
10 SYNC


La obligación económica puede incluir:

* cantidad;
* activo;
* destinatario;
* fecha;
* condiciones;
* método de liquidación.

---

# 29. Obligaciones de servicio

Una obligación puede exigir prestar un servicio.

Ejemplo:


Agent B
Must Provide:
Data Analysis


Debe especificarse, cuando sea posible:

* entrada;
* proceso esperado;
* resultado;
* calidad;
* plazo;
* método de verificación.

---

# 30. Obligaciones de entrega

Una obligación puede exigir entregar un recurso.

Ejemplo:


Deliver:
Dataset X


La entrega puede realizarse mediante:

* transferencia;
* almacenamiento;
* API;
* blockchain;
* infraestructura externa.

---

# 31. Obligaciones de disponibilidad

Un agente puede comprometerse a mantener un recurso disponible.

Ejemplo:


Maintain:
99.9% Availability


El cumplimiento puede medirse mediante métricas.

---

# 32. Obligaciones de calidad

Una obligación puede definir requisitos mínimos.

Ejemplo:


Accuracy:
>= 95%


La verificación debe utilizar una métrica previamente definida.

---

# 33. Obligaciones de confidencialidad

Una obligación puede exigir proteger información.

Ejemplo:


Do Not Disclose:
Dataset_X


Estas obligaciones pueden requerir:

* control de acceso;
* cifrado;
* credenciales;
* políticas de privacidad.

---

# 34. Obligaciones de comportamiento

Un contrato puede definir comportamientos prohibidos.

Ejemplo:


Must Not:
Share Data with Third Parties


El runtime puede aplicar controles cuando sea técnicamente posible.

---

# 35. Obligaciones de cooperación

Una obligación puede requerir cooperación entre agentes.

Ejemplo:


Agent A
Provides Data

Agent B
Provides Compute

Agent C
Produces Result


El cumplimiento depende de múltiples participantes.

---

# 36. Recursos necesarios

Una obligación puede requerir recursos.

Ejemplos:

* capital;
* computación;
* almacenamiento;
* energía;
* tiempo;
* hardware;
* información.

El runtime debe comprobar disponibilidad cuando sea posible.

---

# 37. Reserva de recursos

Un agente puede reservar recursos para una obligación.

Ejemplo:


Contract
    ↓
Obligation
    ↓
Reserve:
10 SYNC
100 CPU-hours
1 TB Storage


La reserva reduce el riesgo de incumplimiento.

---

# 38. Recursos compartidos

Un recurso puede estar comprometido con varias obligaciones.

El runtime debe detectar conflictos.

Ejemplo:


Resource X

Contract A:
09:00–10:00

Contract B:
09:30–11:00


Si el recurso no puede utilizarse simultáneamente, existe conflicto.

---

# 39. Verificación de capacidad

Antes de aceptar una obligación, el agente debería evaluar:


Required Capability
        ↓
Available?
        ↓
Sufficient Resources?
        ↓
Permission Available?
        ↓
Can Execute?


Esto permite evitar compromisos inviables.

---

# 40. Aceptación de obligaciones

Un agente no debería aceptar automáticamente cualquier obligación.

Debe considerar:

* capacidad;
* recursos;
* tiempo;
* riesgo;
* permisos;
* otros contratos.

La aceptación es una decisión autónoma.

---

# 41. Activación

Una obligación puede existir en el contrato pero no estar activa.

Estados conceptuales:


DEFINED
ACTIVATED
PENDING
READY
EXECUTING


La transición depende de sus condiciones.

---

# 42. Estados de ejecución

Una obligación puede utilizar estados como:


PENDING
READY
IN_PROGRESS
COMPLETED
VERIFIED
FULFILLED


Estados alternativos:


FAILED
OVERDUE
DISPUTED
CANCELLED
WAIVED


---

# 43. Estado `PENDING`

La obligación existe pero todavía no puede ejecutarse.

Puede estar esperando:

* fecha;
* condición;
* recurso;
* otra obligación.

---

# 44. Estado `READY`

Todas las condiciones necesarias están satisfechas.

El agente puede comenzar la ejecución.

---

# 45. Estado `IN_PROGRESS`

El agente ha comenzado a ejecutar la obligación.

El runtime debe poder monitorizar el progreso cuando sea posible.

---

# 46. Estado `COMPLETED`

El agente ha realizado la acción requerida.

Esto no implica necesariamente que el cumplimiento haya sido verificado.

---

# 47. Estado `VERIFIED`

La evidencia de cumplimiento ha sido validada.


Completed
    ↓
Evidence
    ↓
Verification
    ↓
Verified


---

# 48. Estado `FULFILLED`

La obligación se considera contractualmente satisfecha.

Esto puede requerir:

* ejecución;
* verificación;
* aceptación del resultado.

---

# 49. Estado `FAILED`

La obligación no pudo completarse.

Ejemplos:

* error técnico;
* falta de recursos;
* imposibilidad;
* fallo externo.

El tratamiento posterior corresponde al sistema de contingencias.

---

# 50. Estado `OVERDUE`

La fecha límite ha pasado sin que la obligación se haya cumplido según las reglas aplicables.

Puede existir:


OVERDUE
    ↓
Fulfilled Late


o:


OVERDUE
    ↓
FAILED


---

# 51. Estado `DISPUTED`

Una parte cuestiona el cumplimiento.

Ejemplo:


Agent A:
Claim not fulfilled

Agent B:
Claim fulfilled

       ↓

DISPUTED


La resolución requiere mecanismos de verificación o disputa.

---

# 52. Evidencia de cumplimiento

La ejecución puede generar evidencia.

Ejemplos:

* resultado;
* archivo;
* hash;
* firma;
* log;
* transacción;
* métrica;
* prueba criptográfica.

La evidencia debe vincularse a:


Contract_ID
Obligation_ID
Agent_ID
Timestamp


---

# 53. Proof of Service

Cuando la obligación representa un servicio, puede generarse una prueba específica.

Modelo:


Obligation
    ↓
Service Execution
    ↓
Evidence
    ↓
Proof of Service
    ↓
Verification


El mecanismo detallado se define en:


03_Trust_Architecture/
Proof_of_Service.md


---

# 54. Verificación externa

Algunas obligaciones no pueden verificarse únicamente desde el runtime.

Puede requerirse:

* otro agente;
* validador;
* oráculo;
* sistema externo;
* consenso.

Ejemplo:


Agent A
    │
    │ Executes
    ▼
Service
    │
    ▼
External Validator
    │
    ▼
Verified


---

# 55. Verificación automática

Cuando sea posible, el cumplimiento puede verificarse automáticamente.

Ejemplo:


Condition:
Payment Received

Blockchain Event
    ↓
Automatic Verification
    ↓
Obligation Fulfilled


---

# 56. Verificación humana

Algunos contratos pueden requerir intervención humana.

Ejemplo:


Service
    ↓
Human Inspection
    ↓
Approval
    ↓
Fulfilled


El modelo de agentes no elimina la posibilidad de participación humana.

---

# 57. Cumplimiento parcial

Una obligación puede cumplirse parcialmente.

Ejemplo:


Required:
100 Units

Delivered:
60 Units


El estado puede ser:


PARTIALLY_FULFILLED


El contrato debe definir las consecuencias.

---

# 58. Obligaciones fraccionables

Algunas obligaciones pueden dividirse en unidades.

Ejemplo:


Deliver 1,000 Data Records


Puede ejecutarse:


100
+
300
+
600


Cada entrega puede verificarse individualmente.

---

# 59. Obligaciones no fraccionables

Otras obligaciones requieren cumplimiento completo.

Ejemplo:


Deliver Final Report


Una entrega incompleta puede no considerarse cumplimiento.

---

# 60. Obligaciones delegadas

Un agente puede delegar la ejecución.

Ejemplo:


Agent A
    │
    │ Contractual Obligation
    ▼
Agent B
    │
    │ Delegates
    ▼
Agent C


La delegación debe respetar:

* permisos;
* capacidades;
* límites;
* contrato.

---

# 61. Responsabilidad tras la delegación

La delegación no implica automáticamente transferencia de responsabilidad contractual.

Ejemplo:


Agent A
Primary Contractual Responsibility
        │
        │ Delegates
        ▼
Agent C
Execution Responsibility


El contrato debe determinar quién responde ante el incumplimiento.

---

# 62. Subcontratación

Un agente puede contratar a otro agente para cumplir una obligación.

Esto crea una nueva relación contractual.


Main Contract
A ↔ B

Subcontract
A ↔ C


La obligación principal continúa existiendo.

---

# 63. Obligaciones derivadas

Una obligación puede generar otras obligaciones.

Ejemplo:


Obligation A
    ↓
Creates
    ↓
Obligation B


El runtime debe registrar la relación entre ambas.

---

# 64. Dependencias entre contratos

Una obligación puede depender de otro contrato.

Ejemplo:


Contract A
    │
    │ Requires
    ▼
Contract B


Si Contract B falla, puede afectar a Contract A.

Estas relaciones deben poder identificarse.

---

# 65. Obligaciones y reputación

El resultado de una obligación puede afectar a la reputación.

Ejemplo:


Obligation
    ↓
Execution
    ↓
Verification
    ↓
Performance Result
    ↓
Reputation Update


La reputación debe basarse en hechos verificables.

---

# 66. Obligaciones y pagos

Una obligación puede activar un pago.

Ejemplo:


Obligation Fulfilled
       ↓
Verification
       ↓
Payment Authorization
       ↓
Payment


El pago puede depender de:

* cumplimiento;
* verificación;
* condiciones contractuales.

---

# 67. Obligaciones y escrow

Una obligación puede estar asociada a fondos bloqueados.

Ejemplo:


Escrow
   │
   │ Condition
   ▼
Obligation Fulfilled
   │
   ▼
Release Funds


Esto reduce el riesgo de impago.

---

# 68. Obligaciones automáticas

Algunas obligaciones pueden ejecutarse mediante software.

Ejemplo:


Condition
    ↓
Smart Contract
    ↓
Automatic Execution


El Agent Runtime puede interactuar con el smart contract.

---

# 69. Obligaciones híbridas

Una obligación puede combinar acciones automáticas y externas.

Ejemplo:


Agent Action
    ↓
External Event
    ↓
Verification
    ↓
Automatic Payment


Este modelo es especialmente relevante para agentes físicos.

---

# 70. Obligaciones físicas

Los agentes físicos pueden tener obligaciones que impliquen acciones en el mundo real.

Ejemplo:


Agent Robot
    ↓
Transport Package
    ↓
Destination
    ↓
Physical Verification


La verificación puede utilizar:

* sensores;
* GPS;
* cámaras;
* dispositivos IoT;
* firmas de recepción.

---

# 71. Obligaciones de agentes híbridos

Un agente híbrido puede combinar:


Software
+
Robotics
+
IoT


La obligación pertenece al agente.

Las capacidades utilizadas pueden cambiar durante la ejecución.

---

# 72. Cambio de capacidad durante una obligación

Un agente puede sustituir una capacidad.

Ejemplo:


Compute Provider A
      ↓
Failure
      ↓
Compute Provider B


Si el resultado contractual se mantiene válido, la sustitución no necesariamente modifica la obligación.

---

# 73. Persistencia de la obligación

Una obligación debe mantener su identidad aunque cambie:

* la infraestructura;
* el hardware;
* el modelo IA;
* el proveedor de computación.

La obligación está vinculada al contrato y al agente responsable.

---

# 74. Migración durante una obligación

Un agente puede migrar mientras una obligación está activa.

Ejemplo:


Infrastructure A
       ↓
Migration
       ↓
Infrastructure B
       ↓
Continue Obligation


La migración no debe romper automáticamente la obligación.

---

# 75. Suspensión del agente

Si un agente queda suspendido, las obligaciones activas deben evaluarse.

Posibles resultados:


Suspend
   ├── Pause Obligations
   ├── Continue Obligations
   └── Trigger Contingency


La decisión depende del contrato y de las políticas aplicables.

---

# 76. Cierre del agente

Si un agente finaliza su existencia, sus obligaciones pendientes deben resolverse.

Posibles resultados:

* transferencia autorizada;
* cumplimiento por un sustituto;
* cancelación;
* contingencia;
* terminación.

La identidad y responsabilidad histórica deben preservarse.

---

# 77. Modelo conceptual

Una obligación puede representarse conceptualmente como:


Obligation {
    obligation_id

    contract_id

    responsible_party

    beneficiary

    action

    object

    expected_result

    conditions

    dependencies

    resources

    capabilities

    permissions

    deadline

    verification

    evidence

    status
}


Este modelo es conceptual.

No constituye todavía una especificación definitiva de serialización o implementación.

---

# 78. Ciclo completo de una obligación

El ciclo puede representarse:


Contract Created
      ↓
Obligation Defined
      ↓
Obligation Activated
      ↓
Conditions Evaluated
      ↓
Resources Checked
      ↓
Capabilities Checked
      ↓
Permissions Checked
      ↓
Obligation Ready
      ↓
Execution Started
      ↓
Execution Monitored
      ↓
Evidence Produced
      ↓
Verification
      ↓
Fulfilled
      ↓
Settlement


---

# 79. Flujo de ejecución desde el Agent Runtime

El runtime puede seguir el siguiente proceso:


1. Load Contract
       ↓
2. Load Obligation
       ↓
3. Evaluate Conditions
       ↓
4. Check Dependencies
       ↓
5. Check Capabilities
       ↓
6. Check Permissions
       ↓
7. Reserve Resources
       ↓
8. Create Execution Plan
       ↓
9. Execute
       ↓
10. Monitor
       ↓
11. Produce Evidence
       ↓
12. Submit Evidence
       ↓
13. Wait for Verification
       ↓
14. Update Obligation State


---

# 80. Fallo durante la ejecución

Si ocurre un fallo:


Execution
    ↓
Failure
    ↓
Evaluate Contingency


El runtime no debe asumir automáticamente que la obligación ha sido incumplida.

Debe determinar si el fallo:

* es recuperable;
* puede reintentarse;
* requiere sustitución;
* activa una contingencia;
* constituye incumplimiento.

---

# 81. Reintentos

Una obligación puede permitir reintentos.

Ejemplo:


Attempt 1
   ↓
Failed
   ↓
Retry
   ↓
Attempt 2
   ↓
Success


El contrato puede establecer:


Maximum Retries:
3


---

# 82. Idempotencia

Cuando sea posible, las operaciones deben diseñarse para evitar efectos duplicados.

Ejemplo:


Payment Request
    ↓
Retry
    ↓
Same Operation ID


El sistema debe evitar pagar dos veces por una única obligación.

---

# 83. Identificador de ejecución

Una obligación puede tener múltiples intentos de ejecución.

Cada ejecución debe poder identificarse.


Obligation:
O123

Execution:
E001
E002
E003


Esto permite auditar:

* intentos;
* errores;
* reintentos;
* resultados.

---

# 84. Registro de eventos

El runtime debe registrar eventos importantes.

Ejemplos:


OBLIGATION_CREATED
OBLIGATION_ACTIVATED
OBLIGATION_STARTED
OBLIGATION_PROGRESS
OBLIGATION_COMPLETED
EVIDENCE_SUBMITTED
OBLIGATION_VERIFIED
OBLIGATION_FULFILLED
OBLIGATION_FAILED


---

# 85. Auditabilidad

Una obligación debe poder reconstruirse históricamente.

Debe ser posible determinar:


Who
Did What
When
Under Which Contract
With Which Evidence
With What Result


Esto es esencial para:

* disputas;
* reputación;
* auditoría;
* gobernanza.

---

# 86. Obligaciones y privacidad

La existencia de una obligación puede ser pública sin revelar todos sus detalles.

Ejemplo:


Public:
Contract ID
Obligation Status

Private:
Exact Data
Internal Strategy
Confidential Parameters


El runtime debe respetar los permisos de acceso.

---

# 87. Obligaciones y seguridad

Una obligación no debe permitir al agente ejecutar acciones fuera de sus límites de seguridad.

Ejemplo:


Contract:
Transfer 10 SYNC

Permission:
Maximum 5 SYNC


El agente no puede ejecutar automáticamente una transferencia de 10 SYNC.

La autorización debe prevalecer sobre la intención contractual cuando existe una incompatibilidad de seguridad.

El conflicto debe registrarse y gestionarse mediante las reglas contractuales correspondientes.

---

# 88. Obligación contractual y autoridad

El contrato define:


What the agent agreed to do


El sistema de permisos define:


What the agent is authorized to do


El sistema de capacidades define:


What the agent is technically able to do


El runtime debe coordinar los tres.


Contractual Obligation
        +
Capability
        +
Authorization
        ↓
Executable Obligation


---

# 89. Obligaciones imposibles

Un agente puede descubrir que una obligación no puede cumplirse.

Ejemplos:

* capacidad inexistente;
* recurso destruido;
* infraestructura caída;
* dependencia imposible.

El agente debe comunicar la situación y activar el mecanismo de contingencia correspondiente.

---

# 90. Principio de buena ejecución

El runtime debe intentar cumplir las obligaciones de forma consistente con:

* el contrato;
* las políticas del agente;
* los permisos;
* las capacidades;
* las reglas del protocolo.

El runtime no debe modificar unilateralmente una obligación contractual.

---

# 91. Principios fundamentales

## Regla 1 — Toda obligación debe tener un responsable

Debe existir una parte claramente identificada.

---

## Regla 2 — Toda obligación debe ser interpretable

El agente debe poder determinar qué debe realizar.

---

## Regla 3 — Las obligaciones deben poder monitorizarse

El runtime debe conocer su estado.

---

## Regla 4 — El cumplimiento debe ser verificable cuando sea posible

La evidencia debe permitir demostrar el resultado.

---

## Regla 5 — Una obligación no implica capacidad

El agente debe comprobar que puede ejecutarla.

---

## Regla 6 — Una obligación no implica autorización

El agente debe comprobar sus permisos.

---

## Regla 7 — Las obligaciones deben respetar dependencias

No deben ejecutarse antes de que sus requisitos estén satisfechos.

---

## Regla 8 — Los recursos comprometidos deben controlarse

El runtime debe evitar conflictos de recursos cuando sea posible.

---

## Regla 9 — La delegación debe ser explícita

Las obligaciones no deben delegarse silenciosamente.

---

## Regla 10 — Los fallos deben activar mecanismos definidos

Un error de ejecución no debe producir automáticamente un estado ambiguo.

---

## Regla 11 — La identidad de la obligación debe persistir

Los cambios de infraestructura no deben romper la trazabilidad.

---

## Regla 12 — El historial debe ser auditable

Las acciones relevantes deben poder reconstruirse.

---

# 92. Integración con el Agent Runtime Protocol

Las obligaciones conectan múltiples subsistemas:


Contract
    │
    ▼
Obligation
    │
    ├── Identity
    │
    ├── Capabilities
    │
    ├── Permissions
    │
    ├── Resources
    │
    ├── Execution
    │
    ├── Verification
    │
    ├── Economy
    │
    └── Reputation


Los documentos relacionados incluyen:


Agent_Autonomy.md
Agent_Continuity.md
Agent_Evolution.md

Credential_Model.md
Authorization_Model.md
Permission_Model.md

Capability_Model.md
Delegation_Model.md
Agent_to_Agent_Delegation.md

Economic_Autonomy.md
Wallet_Operations.md
Economic_Permissions.md

Contract_Interaction.md
Contract_Contingencies.md

Verification_System.md
Proof_of_Service.md

Runtime_Reputation_Integration.md


---

# 93. Conclusión

Las obligaciones contractuales son el mecanismo que transforma los acuerdos económicos en acciones ejecutables.

Un contrato define una relación.

Una obligación define un compromiso concreto.

El Agent Runtime transforma ese compromiso en una actividad operativa.

El modelo completo puede representarse:


Contract
    ↓
Obligation
    ↓
Condition
    ↓
Capability
    ↓
Permission
    ↓
Resource
    ↓
Execution
    ↓
Evidence
    ↓
Verification
    ↓
Fulfillment
    ↓
Settlement
    ↓
Reputation


Esta arquitectura permite que un agente autónomo no solo pueda aceptar contratos, sino también comprender qué debe hacer, determinar si puede hacerlo, ejecutar sus compromisos, demostrar sus resultados y generar consecuencias verificables.

El principio fundamental es:

> Una obligación contractual SynCoinAI es un compromiso identificable y verificable que puede ser interpretado, planificado, ejecutado y monitorizado por un agente autónomo dentro de los límites de sus capacidades, permisos y recursos.

Las obligaciones constituyen, por tanto, el puente operativo entre el acuerdo contractual y la actividad real del agente.

El siguiente documento, `Contract_Contingencies.md`, definirá cómo debe comportarse el sistema cuando una obligación:

* no puede ejecutarse;
* se retrasa;
* falla;
* se cumple parcialmente;
* pierde sus recursos;
* encuentra una dependencia fallida;
* requiere sustitución;
* entra en disputa;
* o debe terminarse anticipadamente.
