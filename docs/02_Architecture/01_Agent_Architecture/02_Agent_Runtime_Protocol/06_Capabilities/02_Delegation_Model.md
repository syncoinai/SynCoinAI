# SynCoinAI Delegation Model

## Modelo general de delegación de capacidades y autoridad

**Versión:** 1.0
**Documento:** `02_Architecture / 01_Agent_Architecture / 02_Agent_Runtime_Protocol / 06_Capabilities / Delegation_Model.md`
**Estado:** Arquitectura inicial

---

# 1. Introducción

La arquitectura de SynCoinAI permite que los agentes inteligentes actúen de forma autónoma y utilicen capacidades propias o proporcionadas por otros agentes y sistemas.

Sin embargo, en un ecosistema de agentes autónomos no todas las capacidades deben estar disponibles permanentemente para todas las entidades.

Un agente puede necesitar conceder temporalmente a otro agente, sistema o proceso la posibilidad de utilizar una capacidad determinada.

Este mecanismo recibe el nombre de **delegación**.

La delegación permite transferir temporalmente una capacidad de actuación sin transferir:

* la identidad del agente;
* la propiedad de sus activos;
* su reputación;
* su historial;
* su autoridad completa;
* su control permanente.

El principio fundamental es:

> La delegación concede una capacidad limitada de actuación, pero no transfiere la identidad del agente delegante.

---

# 2. Objetivo

Este documento define el modelo general de delegación dentro del Agent Runtime Protocol de SynCoinAI.

El modelo establece:

* qué es una delegación;
* qué elementos la componen;
* quién puede delegar;
* qué puede delegarse;
* cómo se limita una delegación;
* cómo se autoriza;
* cómo se verifica;
* cómo se representa su estado;
* cómo se relaciona con capacidades;
* cómo se relaciona con permisos;
* cómo se relaciona con credenciales;
* cómo se revoca;
* cómo se controla su duración;
* cómo se mantiene la trazabilidad.

Este documento define el modelo conceptual y arquitectónico.

Los mecanismos específicos de delegación entre agentes se definen en:

`Agent_to_Agent_Delegation.md`

---

# 3. Definición de delegación

Una delegación es una autorización mediante la cual una entidad concede a otra la capacidad limitada de realizar determinadas acciones dentro de un alcance definido.

Formalmente:

    
Delegation =
    Authorization
    +
    Capability
    +
    Scope
    +
    Constraints
    +
    Validity
    

Una delegación puede representarse conceptualmente como:

    
Delegator
    │
    │ grants
    ▼
Delegation
    │
    │ authorizes
    ▼
Delegate
    │
    │ uses
    ▼
Capability
    

La delegación no modifica la identidad del delegante.

---

# 4. Delegación frente a transferencia

SynCoinAI establece una separación fundamental entre:

    
Delegación
    

y:

    
Transferencia
    

Una transferencia implica que una propiedad o recurso cambia de titular.

Una delegación implica que una entidad conserva la propiedad o autoridad original, pero permite que otra entidad utilice una capacidad determinada.

Ejemplo:

    
Agente A
    │
    │ posee
    ▼
Recurso X
    

Delegación:

    
Agente A
    │
    │ permite utilizar
    ▼
Agente B
    

El recurso continúa perteneciendo a A.

B únicamente obtiene autorización para utilizarlo dentro del alcance definido.

---

# 5. Delegación frente a identidad

La identidad no puede delegarse.

Un agente puede permitir que otro actúe en su nombre en determinadas circunstancias, pero el segundo agente no se convierte en el primero.

Ejemplo:

    
Agente A
Identidad:
A_ID
    

Delegación:

    
A_ID
    │
    │ delegates capability
    ▼
B_ID
    

Durante la ejecución:

    
Executor:
B_ID

Delegating authority:
A_ID
    

Ambas identidades deben permanecer diferenciadas.

---

# 6. Delegación frente a propiedad

Una delegación no implica transferencia de propiedad.

Si A delega el uso de un recurso a B:

    
A
│
│ owns
▼
Resource X
│
│ delegates usage
▼
B
    

La propiedad continúa perteneciendo a A.

B obtiene:

    
Usage Authority
    

pero no necesariamente:

    
Ownership
    

Esta distinción es fundamental para los activos económicos y físicos.

---

# 7. Delegación frente a reputación

La reputación tampoco se transfiere mediante una delegación.

Si A delega una capacidad a B:

    
A
│
│ delegates
▼
B
│
│ executes
▼
Action
    

La acción debe poder atribuirse a B como ejecutor.

La relación de delegación se conserva como contexto.

Por tanto:

    
Execution:
B

Delegation:
A → B

Reputation of execution:
B
    

La reputación de A no se transfiere automáticamente a B.

---

# 8. Elementos de una delegación

Una delegación completa debe poder representar conceptualmente:

    
Delegation {
    delegation_id
    delegator
    delegate
    capability
    scope
    constraints
    validity
    authorization
    status
}
    

Puede incluir adicionalmente:

    
parent_delegation
delegation_depth
execution_limit
economic_limit
revocation_reference
contract_reference
audit_reference
    

La implementación concreta podrá utilizar estructuras diferentes.

Sin embargo, la información necesaria debe ser equivalente.

---

# 9. Identificador de delegación

Cada delegación debe disponer de un identificador único.

Ejemplo:

    
delegation_id:
DLG-8F3A-2026
    

El identificador permite:

* referenciar la delegación;
* verificar su estado;
* registrar ejecuciones;
* realizar auditorías;
* asociar contratos;
* procesar revocaciones.

Una delegación no debería depender exclusivamente de una descripción textual para ser identificada.

---

# 10. Delegante

El **delegante** es la entidad que concede la capacidad.

Puede ser:

* un agente SynCoinAI;
* una organización autorizada;
* un sistema de infraestructura;
* un contrato inteligente;
* otro componente autorizado.

El delegante debe poseer autoridad suficiente para conceder la capacidad.

No puede delegarse una capacidad que el delegante no posee o no está autorizado a delegar.

---

# 11. Delegado

El **delegado** es la entidad que recibe la capacidad.

Puede ser:

* otro agente;
* un proceso;
* un servicio;
* un sistema;
* una infraestructura;
* un componente autorizado.

En el contexto principal del Agent Runtime Protocol, el delegado será normalmente otro agente SynCoinAI.

---

# 12. Capacidad delegada

La delegación siempre debe estar asociada a una capacidad concreta.

Ejemplos:

    
read_data
    

    
execute_payment
    

    
use_compute
    

    
operate_device
    

    
negotiate_contract
    

    
access_resource
    

La capacidad define **qué puede hacer** el delegado.

La delegación define **en qué condiciones puede hacerlo**.

Por tanto:

    
Capability
    =
    What

Delegation
    =
    Who + What + Under which conditions
    

---

# 13. Alcance

Toda delegación debe definir un alcance.

El alcance determina el contexto dentro del cual la capacidad puede utilizarse.

Puede incluir:

* recursos concretos;
* agentes específicos;
* contratos;
* servicios;
* operaciones;
* tipos de datos;
* dispositivos;
* cantidades.

Ejemplo:

    
Capability:
    execute_payment

Scope:
    Payments related to Contract_X
    

La delegación no permite realizar pagos fuera de ese contexto.

---

# 14. Restricciones

Las restricciones limitan el uso de la capacidad delegada.

Pueden ser:

* temporales;
* cuantitativas;
* geográficas;
* económicas;
* operativas;
* contextuales;
* contractuales.

Ejemplo:

    
Capability:
    execute_payment

Maximum:
    100 SYNC

Target:
    Agent_C

Duration:
    24 hours
    

La delegación efectiva será:

    
Capability
+
Scope
+
Constraints
    

---

# 15. Principio de mínimo privilegio

SynCoinAI adopta el principio de mínimo privilegio.

Una delegación debe conceder únicamente la capacidad necesaria para alcanzar el objetivo autorizado.

No debe conceder capacidades adicionales por comodidad de implementación.

Ejemplo incorrecto:

    
Need:
    Purchase storage

Delegation:
    Full wallet control
    

Ejemplo correcto:

    
Need:
    Purchase storage

Delegation:
    purchase_storage

Limit:
    100 SYNC
    

Este principio limita el impacto de:

* errores;
* agentes comprometidos;
* credenciales robadas;
* comportamiento malicioso.

---

# 16. Delegación explícita

Las capacidades sensibles deben requerir una delegación explícita.

Ejemplos:

* transferir fondos;
* controlar dispositivos físicos;
* acceder a datos privados;
* modificar configuraciones críticas;
* crear nuevas autorizaciones.

El hecho de que un agente tenga acceso técnico a un sistema no implica automáticamente que tenga autorización para utilizar todas sus capacidades.

---

# 17. Delegación implícita

Las delegaciones implícitas deben evitarse para capacidades sensibles.

Una capacidad solo debe considerarse delegada cuando existe una relación de autorización verificable.

Por tanto:

    
Access
≠
Authorization
    

Y:

    
Technical capability
≠
Delegated authority
    

---

# 18. Delegación temporal

Una delegación puede tener una duración limitada.

Modelo:

    
valid_from
valid_until
    

Ejemplo:

    
valid_from:
2026-01-01 10:00

valid_until:
2026-01-01 12:00
    

Fuera de este intervalo:

    
Delegation = Invalid
    

La expiración debe poder verificarse de forma independiente.

---

# 19. Delegación permanente

Las delegaciones permanentes pueden existir cuando el modelo de seguridad lo permita.

Sin embargo, deben considerarse de mayor riesgo.

Ejemplo:

    
valid_until:
NONE
    

Las delegaciones permanentes deberían utilizarse únicamente cuando:

* exista una razón clara;
* el riesgo sea aceptable;
* exista mecanismo de revocación.

---

# 20. Límite de ejecuciones

Una delegación puede limitar el número de veces que puede utilizarse.

Ejemplo:

    
execution_limit:
5
    

Estado:

    
executions_used:
3
    

Ejecuciones restantes:

    
2
    

Cuando:

    
executions_used = execution_limit
    

La delegación queda:

    
CONSUMED
    

---

# 21. Límites económicos

Las capacidades económicas deben poder limitarse mediante cantidades máximas.

Puede existir:

    
maximum_per_operation
    

y:

    
maximum_total
    

Ejemplo:

    
Maximum per operation:
10 SYNC

Maximum total:
100 SYNC
    

Esto permite:

    
Operation 1:
5 SYNC

Operation 2:
10 SYNC

Operation 3:
20 SYNC
    

Siempre que el total permanezca dentro del límite.

---

# 22. Delegación contextual

Una delegación puede estar condicionada a un contexto específico.

Ejemplo:

    
Capability:
    purchase_resource

Context:
    Contract_X
    

El delegado puede utilizar la capacidad únicamente mientras:

    
Contract_X = Active
    

Si el contrato finaliza:

    
Contract_X = Terminated
    

La delegación puede quedar automáticamente invalidada.

---

# 23. Delegación condicional

Una delegación puede depender de determinadas condiciones.

Ejemplo:

    
IF:
    Contract active

AND:
    Budget available

AND:
    Agent authorized

THEN:
    Execute capability
    

Este modelo permite construir sistemas de autorización dinámicos.

Las condiciones pueden ser verificadas:

* por el runtime;
* por contratos inteligentes;
* por sistemas externos verificables.

---

# 24. Delegación y credenciales

Las credenciales representan evidencias de autoridad.

Una delegación puede utilizar una credencial para demostrar:

    
Quién delega
    

y:

    
Qué autoridad concede
    

Conceptualmente:

    
Identity
    ↓
Credential
    ↓
Authorization
    ↓
Delegation
    ↓
Capability
    

No todas las credenciales deben representar delegaciones.

Pero una delegación debe poder expresarse mediante mecanismos de credenciales cuando sea necesario.

---

# 25. Delegación y permisos

Los permisos determinan qué acciones están permitidas.

La delegación permite conceder determinados permisos a otra entidad.

Ejemplo:

    
Permission:
    transfer_funds
    

Delegación:

    
A → B
    

Resultado:

    
B may transfer funds
    

pero únicamente:

    
within delegated constraints
    

La delegación no debe saltarse las políticas de permisos del sistema.

---

# 26. Delegación y autorización

La autorización responde a:

> ¿Está permitido realizar esta acción?

La delegación responde a:

> ¿Quién ha concedido esta autoridad y bajo qué condiciones?

Por tanto:

    
Authorization
    =
    Decision

Delegation
    =
    Mechanism for granting authority
    

Ambos conceptos están relacionados pero no son idénticos.

---

# 27. Delegación y ejecución

Una delegación no implica que la acción haya sido ejecutada.

Debe distinguirse:

    
Delegation
    ↓
Authorization exists
    

de:

    
Execution
    ↓
Action actually occurred
    

Por tanto:

    
Delegation ≠ Execution
    

Una delegación puede existir sin ser utilizada.

---

# 28. Verificación de una delegación

Antes de aceptar una acción delegada, el sistema debería comprobar:

    
1. Delegation exists
2. Delegation is authentic
3. Delegator is valid
4. Delegate is valid
5. Capability is allowed
6. Scope is satisfied
7. Constraints are satisfied
8. Delegation is active
9. Delegation is not revoked
10. Delegation is not expired
    

Si alguna condición crítica falla:

    
Action = Rejected
    

---

# 29. Estado de una delegación

Una delegación puede tener diferentes estados.

Estados mínimos:

    
CREATED
ACTIVE
SUSPENDED
REVOKED
EXPIRED
CONSUMED
    

---

# 30. Estado CREATED

La delegación ha sido creada, pero todavía no está disponible para ejecución.

Puede ocurrir cuando:

* espera una condición;
* espera una fecha de inicio;
* requiere activación adicional.

    
CREATED
    ↓
ACTIVE
    

---

# 31. Estado ACTIVE

La delegación puede utilizarse.

Debe cumplir:

* autenticidad;
* vigencia;
* alcance;
* restricciones;
* ausencia de revocación.

---

# 32. Estado SUSPENDED

La delegación está temporalmente inactiva.

No puede utilizarse mientras permanezca suspendida.

Puede volver a:

    
ACTIVE
    

si la suspensión termina.

---

# 33. Estado REVOKED

La delegación ha sido invalidada permanentemente.

Una delegación revocada no debe volver a utilizarse.

    
ACTIVE
    ↓
REVOKED
    

---

# 34. Estado EXPIRED

La delegación ha superado su periodo de validez.

    
ACTIVE
    ↓
EXPIRED
    

La expiración es automática cuando se alcanza el límite temporal.

---

# 35. Estado CONSUMED

La delegación ha agotado su número máximo de ejecuciones.

    
ACTIVE
    ↓
CONSUMED
    

Una delegación consumida no puede utilizarse nuevamente.

---

# 36. Revocación

El delegante debe poder revocar una delegación cuando las reglas aplicables lo permitan.

La revocación debe invalidar futuras ejecuciones.

Conceptualmente:

    
Delegation
    ↓
Revocation
    ↓
Status = REVOKED
    

El mecanismo concreto de revocación se define en:

`Credential_Revocation.md`

cuando la delegación utilice credenciales revocables.

---

# 37. Suspensión

La suspensión es diferente de la revocación.

    
Suspension:
    Temporal
    

    
Revocation:
    Permanente
    

Una delegación suspendida puede volver a activarse.

Una delegación revocada no debe reactivarse como la misma autorización.

---

# 38. Delegación y subdelegación

Una delegación puede permitir que el delegado conceda parte de la autoridad recibida a otra entidad.

Esto se denomina:

    
Subdelegation
    

Ejemplo:

    
A
│
│ Delegates
▼
B
│
│ Subdelegates
▼
C
    

La subdelegación debe estar expresamente permitida.

Por defecto:

    
Delegation
    → No automatic subdelegation
    

---

# 39. Principio de no ampliación

Una subdelegación nunca puede ampliar la autoridad recibida.

Si A concede:

    
Maximum:
100 SYNC
    

B no puede conceder:

    
Maximum:
500 SYNC
    

La autoridad descendiente debe ser igual o más restrictiva.

Conceptualmente:

    
EffectiveAuthority(child)
    ⊆
EffectiveAuthority(parent)
    

---

# 40. Delegación y cadena de autoridad

Las delegaciones pueden formar cadenas.

    
A
│
▼
B
│
▼
C
│
▼
D
    

La autoridad efectiva de D debe derivarse de todas las delegaciones anteriores.

Por tanto:

    
Effective Authority
=
Intersection of Delegated Authorities
    

Si una delegación superior deja de ser válida:

    
Parent delegation invalid
        ↓
Dependent delegation invalid
    

cuando la segunda dependa exclusivamente de la primera.

---

# 41. Profundidad máxima

Las cadenas de delegación deben poder limitarse.

Ejemplo:

    
maximum_depth:
2
    

Permitido:

    
A → B → C
    

No permitido:

    
A → B → C → D
    

Esto reduce:

* complejidad;
* riesgo;
* dificultad de auditoría.

---

# 42. Delegación y trazabilidad

Toda delegación debe poder asociarse con una cadena de autorización.

Ejemplo:

    
Delegator:
A

Delegate:
B

Capability:
X

Execution:
E
    

El sistema debe poder responder:

    
¿Quién autorizó la acción?
    

    
A
    

    
¿Quién ejecutó?
    

    
B
    

    
¿Qué capacidad utilizó?
    

    
X
    

---

# 43. Delegación y responsabilidad

La delegación no elimina la responsabilidad de las partes.

Debe distinguirse entre:

    
Responsabilidad de conceder autoridad
    

y:

    
Responsabilidad de utilizar autoridad
    

El delegante es responsable de la autorización concedida según las reglas aplicables.

El delegado es responsable del uso que haga de la autoridad recibida.

---

# 44. Delegación y seguridad

El modelo de delegación debe asumir que cualquier autoridad delegada puede convertirse en un vector de ataque.

Por tanto, la arquitectura debe favorecer:

* mínimo privilegio;
* duración limitada;
* límites económicos;
* límites de ejecución;
* revocación;
* trazabilidad;
* validación criptográfica.

---

# 45. Delegación como mecanismo de aislamiento

La delegación permite limitar el impacto de un agente comprometido.

Ejemplo:

    
A
│
│ delegates
▼
B
    

Si B es comprometido:

    
B compromised
    

El atacante debería obtener únicamente:

    
Delegated Authority
    

y no:

    
Full Authority of A
    

Este principio convierte la delegación en un mecanismo de aislamiento de privilegios.

---

# 46. Delegación y autonomía

La delegación es necesaria para la autonomía de los agentes.

Un agente autónomo debe poder:

1. determinar una necesidad;
2. identificar una capacidad requerida;
3. solicitar autorización;
4. recibir una delegación;
5. ejecutar la capacidad;
6. verificar el resultado.

Este proceso puede ejecutarse sin intervención humana constante.

---

# 47. Delegación como mecanismo económico

Las delegaciones pueden utilizarse en operaciones económicas.

Ejemplos:

* autorizar pagos;
* autorizar compras;
* autorizar inversiones;
* administrar presupuestos;
* contratar servicios.

Ejemplo:

    
Agent A
    │
    │ delegates
    ▼
Agent B

Capability:
    execute_payment

Limit:
    50 SYNC
    

B puede realizar pagos dentro del límite.

No obtiene automáticamente control total sobre los activos de A.

---

# 48. Delegación y recursos físicos

Las delegaciones pueden controlar el uso de recursos físicos.

Ejemplos:

* robots;
* vehículos;
* sensores;
* instalaciones;
* dispositivos IoT.

Ejemplo:

    
Agent A
    │
    │ delegates usage
    ▼
Agent B

Resource:
    Robot_X

Duration:
    1 hour
    

La delegación concede capacidad de uso.

No implica necesariamente propiedad.

---

# 49. Delegación y privacidad

Las delegaciones pueden contener información sensible.

Por tanto, el sistema debe permitir distinguir entre:

    
Delegation Metadata
    

y:

    
Delegation Confidential Data
    

Por ejemplo:

    
Public:
    Delegation exists

Private:
    Maximum budget
    Internal objective
    Sensitive resource
    

La arquitectura debe permitir verificar autoridad sin revelar información innecesaria cuando sea técnicamente posible.

---

# 50. Delegación y auditoría

Las delegaciones deben ser auditables.

Una auditoría debería poder reconstruir:

    
Quién delegó
    ↓
Qué capacidad delegó
    ↓
A quién
    ↓
Bajo qué condiciones
    ↓
Durante cuánto tiempo
    ↓
Qué acciones se realizaron
    ↓
Qué resultado produjeron
    

La auditoría puede ser:

* pública;
* privada;
* selectiva;
* criptográficamente verificable.

---

# 51. Modelo conceptual completo

El modelo general de delegación puede representarse como:

    
                 IDENTITY
                    │
                    ▼
                DELEGATOR
                    │
                    │ grants
                    ▼
              AUTHORIZATION
                    │
                    ▼
               DELEGATION
                    │
         ┌──────────┼──────────┐
         ▼          ▼          ▼
     CAPABILITY    SCOPE    CONSTRAINTS
         │          │          │
         └──────────┼──────────┘
                    ▼
                 DELEGATE
                    │
                    ▼
                EXECUTION
                    │
                    ▼
                RESULT
    

---

# 52. Flujo general

El flujo completo es:

    
1. Capability exists
        ↓
2. Delegator has authority
        ↓
3. Delegation created
        ↓
4. Delegation authorized
        ↓
5. Delegate receives delegation
        ↓
6. Delegate requests execution
        ↓
7. Runtime validates delegation
        ↓
8. Capability executes
        ↓
9. Execution recorded
        ↓
10. Delegation state updated
    

---

# 53. Requisitos arquitectónicos

Una implementación compatible con este modelo debería proporcionar:

### Identificación

* identificador único de delegación.

### Autenticidad

* prueba de quién creó la delegación.

### Integridad

* protección contra modificaciones no autorizadas.

### Alcance

* definición de qué puede hacerse.

### Restricciones

* límites de uso.

### Vigencia

* inicio y expiración.

### Estado

* activo, suspendido, revocado, expirado o consumido.

### Revocación

* mecanismo para invalidar la autorización.

### Auditoría

* registro de delegaciones y ejecuciones.

---

# 54. Separación entre modelo y mecanismo

SynCoinAI no define en este documento una única implementación tecnológica obligatoria.

Una delegación podría implementarse mediante:

* credenciales firmadas;
* tokens de autorización;
* estructuras criptográficas;
* smart contracts;
* políticas verificables;
* mecanismos híbridos.

El modelo arquitectónico debe permanecer independiente del mecanismo concreto.

Por tanto:

    
Delegation Model
        │
        ├── Cryptographic Credential
        ├── Smart Contract
        ├── Runtime Policy
        └── Hybrid Mechanism
    

La implementación podrá evolucionar sin cambiar necesariamente el modelo conceptual.

---

# 55. Reglas fundamentales

El modelo de delegación de SynCoinAI queda definido por las siguientes reglas:

## Regla 1 — Delegar no transfiere identidad

    
Delegation ≠ Identity Transfer
    

## Regla 2 — Delegar no transfiere automáticamente propiedad

    
Delegation ≠ Ownership Transfer
    

## Regla 3 — Delegar no transfiere reputación

    
Delegation ≠ Reputation Transfer
    

## Regla 4 — Toda delegación debe tener alcance

    
Delegation → Scope
    

## Regla 5 — Las capacidades sensibles deben delegarse explícitamente

    
Sensitive Capability → Explicit Authorization
    

## Regla 6 — La autoridad debe poder verificarse

    
Delegation → Verifiable
    

## Regla 7 — La delegación debe poder invalidarse

    
Delegation → Revocable
    

cuando el modelo de autoridad aplicable lo permita.

## Regla 8 — La subdelegación no puede ampliar autoridad

    
Child Authority ⊆ Parent Authority
    

## Regla 9 — La ejecución debe ser trazable

    
Execution → Executor + Delegation
    

## Regla 10 — La seguridad debe basarse en mínimo privilegio

    
Granted Authority = Minimum Required Authority
    

---

# 56. Relación con otros componentes del Agent Runtime Protocol

El `Delegation_Model.md` se relaciona directamente con:

    
Capability_Model.md
        │
        ▼
Delegation_Model.md
        │
        ├── Credential_Model.md
        │
        ├── Authorization_Model.md
        │
        ├── Permission_Model.md
        │
        ├── Credential_Revocation.md
        │
        └── Agent_to_Agent_Delegation.md
    

La separación de responsabilidades es:

    
Capability
    → Qué puede hacer

Permission
    → Qué está permitido

Authorization
    → Decisión de permitir

Credential
    → Evidencia verificable

Delegation
    → Concesión limitada de autoridad

Agent-to-Agent Delegation
    → Aplicación entre agentes
    

---

# 57. Relación con Agent-to-Agent Delegation

Este documento define el modelo general.

El documento:

`Agent_to_Agent_Delegation.md`

define su aplicación específica cuando:

    
Delegator = Agent
    

y:

    
Delegate = Agent
    

Por tanto:

    
Delegation_Model
        │
        ▼
General Delegation Framework
        │
        ▼
Agent_to_Agent_Delegation
        │
        ▼
Multi-Agent Delegation
    

El segundo documento debe mantener las reglas definidas en este modelo general.

---

# 58. Conclusión

La delegación es un mecanismo fundamental del Agent Runtime Protocol de SynCoinAI.

Permite que las capacidades y autoridades puedan compartirse de forma controlada sin romper la separación entre identidades.

El modelo establece una arquitectura basada en:

* capacidades explícitas;
* autoridad limitada;
* mínimo privilegio;
* alcance definido;
* restricciones;
* vigencia;
* revocación;
* trazabilidad;
* separación de identidad;
* separación de propiedad;
* separación de reputación.

El objetivo final es permitir que los agentes puedan cooperar y actuar de forma autónoma manteniendo un control preciso sobre quién puede hacer qué, en nombre de quién, bajo qué condiciones y con qué consecuencias.

La relación fundamental queda definida como:

    
IDENTITY
    │
    ▼
AUTHORITY
    │
    ▼
DELEGATION
    │
    ▼
CAPABILITY
    │
    ▼
EXECUTION
    │
    ▼
RESULT
    │
    ▼
AUDIT
    

La delegación no convierte al delegado en el delegante.

No transfiere automáticamente identidad, propiedad ni reputación.

Concede únicamente una autoridad limitada y verificable para realizar acciones concretas dentro de un alcance determinado.

> En SynCoinAI, delegar significa conceder capacidad de actuación sin transferir la identidad que origina la autoridad.
