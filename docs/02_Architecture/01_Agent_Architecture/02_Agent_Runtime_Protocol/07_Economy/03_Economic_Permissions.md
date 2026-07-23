# SynCoinAI Economic Permissions

## Modelo de permisos económicos del agente

**Versión:** 1.0
**Documento:** `02_Architecture / 01_Agent_Architecture / 02_Agent_Runtime_Protocol / 07_Economy / Economic_Permissions.md`
**Estado:** Arquitectura inicial

---

# 1. Introducción

La autonomía económica de un agente SynCoinAI requiere que el agente pueda gestionar recursos y ejecutar operaciones económicas de forma autónoma.

Sin embargo, autonomía no significa autoridad ilimitada.

Un agente debe poder actuar económicamente dentro de un conjunto de reglas que determine:

* qué puede hacer;
* sobre qué recursos puede actuar;
* cuánto puede gastar;
* con qué frecuencia;
* durante cuánto tiempo;
* bajo qué condiciones;
* quién puede delegarle una autoridad;
* cómo puede revocarse esa autoridad.

El sistema de permisos económicos define estos límites.

Su objetivo es permitir que un agente pueda operar de forma autónoma manteniendo:

* seguridad;
* control;
* trazabilidad;
* proporcionalidad;
* delegación;
* revocabilidad.

---

# 2. Objetivo

Este documento define el modelo de autorización económica aplicado a las operaciones del Agent Runtime Protocol.

Se establece cómo una identidad autorizada puede obtener permiso para ejecutar operaciones económicas.

El modelo debe permitir controlar operaciones como:

* consultar balances;
* recibir fondos;
* transferir fondos;
* reservar fondos;
* liberar reservas;
* contratar servicios;
* interactuar con contratos;
* crear operaciones económicas;
* ejecutar pagos automatizados.

---

# 3. Principio fundamental

La identidad de un agente no implica automáticamente autoridad económica ilimitada.

El modelo es:

    
Identity
    │
    ▼
Authentication
    │
    ▼
Authorization
    │
    ▼
Permission
    │
    ▼
Capability
    │
    ▼
Economic Operation
    

Cada nivel responde a una pregunta diferente.

### Identidad

¿Quién es?

### Autenticación

¿Puede demostrar quién es?

### Autorización

¿Está autorizado para realizar esta acción?

### Permiso

¿Qué acciones concretas puede realizar?

### Capacidad

¿Qué puede ejecutar técnicamente?

### Operación

¿Qué acción se está intentando realizar?

---

# 4. Separación entre autenticación y autorización

SynCoinAI debe diferenciar:

    
Authentication
    

de:

    
Authorization
    

Autenticación:

> Este agente es realmente quien afirma ser.

Autorización:

> Este agente tiene autoridad para realizar esta operación.

Ejemplo:

    
Agent A
   │
   │ authenticated
   ▼
Identity Verified
   │
   │ authorization check
   ▼
Can Agent A spend 100 SYNC?
    

La identidad válida no garantiza automáticamente que la operación esté permitida.

---

# 5. Modelo de permisos

Un permiso económico puede representarse conceptualmente como:

    
Permission {
    permission_id
    subject
    action
    resource
    scope
    limits
    conditions
    validity
    issuer
    status
}
    

Donde:

* `permission_id`: identificador único;
* `subject`: entidad autorizada;
* `action`: operación permitida;
* `resource`: recurso afectado;
* `scope`: ámbito;
* `limits`: límites;
* `conditions`: condiciones;
* `validity`: periodo de validez;
* `issuer`: entidad que concede;
* `status`: estado actual.

---

# 6. Subject

El `subject` representa la entidad que recibe el permiso.

Puede ser:

* el propio agente;
* un módulo del runtime;
* una sub-identidad;
* otro agente delegado.

Ejemplo:

    
Subject:
Agent_A
    

o:

    
Subject:
Agent_A / Operational_Runtime
    

---

# 7. Action

La acción representa qué operación está permitida.

Ejemplos:

    
READ_BALANCE
RECEIVE_FUNDS
TRANSFER_FUNDS
RESERVE_FUNDS
RELEASE_FUNDS
CREATE_CONTRACT
EXECUTE_CONTRACT
    

Las acciones deben definirse de forma explícita.

---

# 8. Resource

El recurso determina sobre qué activo o elemento puede aplicarse el permiso.

Ejemplos:

    
SYNC
attoSYNC
Wallet_A
Contract_123
Escrow_456
    

Un permiso debe evitar conceder acceso más amplio del necesario.

---

# 9. Scope

El scope define el ámbito del permiso.

Ejemplo:

    
Scope:
Operational_Wallet
    

En lugar de:

    
Scope:
All_Wallets
    

El principio recomendado es:

> Un permiso debe tener el menor ámbito necesario para cumplir su objetivo.

---

# 10. Límites

Los permisos económicos pueden incluir límites.

Ejemplos:

    
Maximum Amount:
10 SYNC
    

    
Daily Limit:
100 SYNC
    

    
Transaction Limit:
5 SYNC
    

    
Maximum Frequency:
10 transactions/hour
    

---

# 11. Límite por operación

Un permiso puede limitar la cantidad máxima de una única operación.

Ejemplo:

    
Permission:
TRANSFER_FUNDS

Maximum:
10 SYNC
    

Una operación de:

    
5 SYNC
    

está permitida.

Una operación de:

    
20 SYNC
    

debe rechazarse.

---

# 12. Límite acumulado

Un permiso puede establecer un límite acumulado.

Ejemplo:

    
Daily Limit:
100 SYNC
    

Operaciones:

    
20 SYNC
30 SYNC
40 SYNC
    

Total:

    
90 SYNC
    

La siguiente operación de:

    
20 SYNC
    

superaría el límite.

Debe ser rechazada o requerir autorización adicional.

---

# 13. Límite temporal

Un permiso puede ser válido durante un periodo concreto.

Ejemplo:

    
Valid From:
2026-01-01

Valid Until:
2026-12-31
    

Fuera de ese periodo:

    
Permission = Invalid
    

---

# 14. Permisos permanentes

Algunos permisos pueden no tener fecha de expiración.

Sin embargo, deben seguir siendo revocables cuando corresponda.

La ausencia de expiración no implica ausencia de control.

---

# 15. Condiciones

Un permiso puede incluir condiciones.

Ejemplo:

    
Permission:
TRANSFER_FUNDS

Condition:
Only to approved agents
    

Otro ejemplo:

    
Condition:
Only after service verification
    

Las condiciones deben poder verificarse antes de ejecutar la operación.

---

# 16. Permisos basados en contratos

Una autoridad económica puede estar limitada a un contrato concreto.

Ejemplo:

    
Contract:
C123

Permission:
RELEASE_PAYMENT

Scope:
Escrow_C123
    

El permiso no permite utilizar esos fondos fuera del contrato.

---

# 17. Permisos basados en identidad

Un permiso puede depender de la identidad del destinatario.

Ejemplo:

    
Allowed Recipient:
Agent_B
    

La operación:

    
Agent_A → Agent_B
    

está permitida.

La operación:

    
Agent_A → Agent_C
    

puede ser rechazada.

---

# 18. Permisos basados en reputación

En determinadas aplicaciones, una política económica puede requerir un nivel mínimo de reputación.

Ejemplo:

    
Requirement:
Reputation Score >= X
    

Esto no debe confundirse con la autorización criptográfica.

La reputación actúa como condición adicional.

Modelo:

    
Identity Valid
      +
Permission Valid
      +
Reputation Requirement
      ↓
Operation Allowed
    

---

# 19. Permisos basados en verificación

Una operación puede requerir una prueba verificable.

Ejemplo:

    
Service Completed
       ↓
Verification Valid
       ↓
Payment Authorized
    

Esto conecta directamente con:

* `Verification_System.md`;
* `Proof_of_Service.md`;
* contratos.

---

# 20. Permisos de lectura

No todas las operaciones económicas implican gasto.

Un agente puede disponer de permisos de lectura.

Ejemplos:

    
READ_BALANCE
READ_TRANSACTION
READ_CONTRACT
READ_PAYMENT_STATUS
    

Estos permisos pueden estar limitados por privacidad.

---

# 21. Permisos de recepción

Recibir fondos puede ser una operación distinta de gastar fondos.

Un agente puede permitir:

    
RECEIVE_FUNDS
    

sin permitir:

    
TRANSFER_FUNDS
    

Esto es útil para:

* wallets de recepción;
* cuentas de reserva;
* agentes en recuperación.

---

# 22. Permisos de transferencia

El permiso:

    
TRANSFER_FUNDS
    

permite mover activos.

Debe especificar, cuando sea necesario:

* wallet de origen;
* activo;
* cantidad máxima;
* destinatarios;
* frecuencia;
* periodo.

---

# 23. Permisos de reserva

El permiso:

    
RESERVE_FUNDS
    

permite bloquear temporalmente recursos para una obligación.

Debe diferenciarse de:

    
TRANSFER_FUNDS
    

Un agente puede tener permiso para reservar fondos sin tener permiso para transferirlos directamente.

---

# 24. Permisos de liberación

El permiso:

    
RELEASE_FUNDS
    

permite liberar recursos reservados.

Debe estar limitado al contexto correspondiente.

Ejemplo:

    
Escrow:
C123

Permission:
RELEASE_FUNDS

Scope:
C123
    

---

# 25. Permisos de contratos

Las operaciones relacionadas con contratos pueden requerir permisos específicos.

Ejemplos:

    
CREATE_CONTRACT
ACCEPT_CONTRACT
EXECUTE_CONTRACT
MODIFY_CONTRACT
CANCEL_CONTRACT
    

No todos los agentes deben disponer de todas estas capacidades.

---

# 26. Permisos de contratación

Un agente puede estar autorizado para contratar servicios.

Ejemplo:

    
CREATE_SERVICE_CONTRACT
    

Puede existir un límite:

    
Maximum Contract Value:
50 SYNC
    

---

# 27. Permisos de pago automático

Un agente puede autorizar pagos automáticos.

Ejemplo:

    
AUTOMATIC_PAYMENT

Maximum:
5 SYNC / transaction

Daily Limit:
50 SYNC
    

Esto permite autonomía sin conceder autoridad ilimitada.

---

# 28. Permisos administrativos

Algunos permisos pueden controlar la configuración económica del propio agente.

Ejemplos:

    
CREATE_WALLET
REVOKE_WALLET
ROTATE_WALLET_KEY
SET_SPENDING_LIMIT
    

Estos permisos deben tener niveles de seguridad elevados.

---

# 29. Permisos de emergencia

El sistema puede disponer de operaciones especiales para responder a situaciones críticas.

Ejemplos:

    
FREEZE_WALLET
SUSPEND_SPENDING
REVOKE_CREDENTIAL
INITIATE_RECOVERY
    

Estas operaciones deben estar especialmente protegidas.

---

# 30. Principio de mínimo privilegio

El modelo debe aplicar:

> Un agente solo debe disponer de la autoridad necesaria para cumplir una función concreta.

Ejemplo:

    
Agent Module:
Payment Processor

Required:
TRANSFER_FUNDS

Not Required:
CREATE_WALLET
REVOKE_WALLET
CHANGE_IDENTITY
    

Por tanto, no debe recibir esos permisos adicionales.

---

# 31. Separación de funciones

Las operaciones sensibles pueden dividirse entre diferentes autoridades.

Ejemplo:

    
Agent
   │
   ├── Payment Permission
   │
   └── Recovery Authority
    

Ninguna autoridad individual debe tener necesariamente control total.

---

# 32. Multi-autorización

Las operaciones críticas pueden requerir múltiples autorizaciones.

Ejemplo:

    
Transfer > 1,000 SYNC
       ↓
Authorization A
       +
Authorization B
       ↓
Allowed
    

Esto puede implementarse mediante:

* multisig;
* múltiples credenciales;
* políticas del runtime;
* contratos.

---

# 33. Delegación

Un agente puede delegar permisos a otro agente.

Ejemplo:

    
Agent A
   │
   │ Delegates
   ▼
Agent B
   │
   │ Can spend
   ▼
Maximum 10 SYNC
    

La delegación debe estar limitada.

Puede incluir:

* alcance;
* cantidad;
* duración;
* condiciones.

---

# 34. No transferencia automática de autoridad

Una delegación no debe transferir automáticamente toda la autoridad del agente original.

Ejemplo:

    
Agent A
Authority:
100 SYNC

Delegates:
10 SYNC

Agent B
Authority:
10 SYNC
    

Agent B no obtiene:

    
Authority:
100 SYNC
    

---

# 35. Delegación en cadena

Puede existir delegación indirecta.

Ejemplo:

    
Agent A
   ↓
Agent B
   ↓
Agent C
    

El sistema debe impedir que los permisos acumulados superen la autoridad original.

Regla:

    
Delegated Authority
≤
Original Authority
    

---

# 36. Revocación

Un permiso debe poder revocarse.

La revocación puede producirse por:

* decisión del agente;
* expiración;
* compromiso;
* incumplimiento;
* cambio de política;
* revocación de credenciales.

---

# 37. Revocación inmediata

Los permisos críticos deben poder revocarse inmediatamente cuando sea necesario.

Ejemplo:

    
Compromise Detected
       ↓
Revoke Permission
       ↓
Future Operations Denied
    

Las operaciones ya confirmadas no se revierten automáticamente.

---

# 38. Permisos expirados

Cuando un permiso expira:

    
Permission
    ↓
Expiration
    ↓
Invalid
    

El runtime debe rechazar nuevas operaciones basadas en ese permiso.

---

# 39. Permisos suspendidos

Un permiso puede suspenderse temporalmente.

Estados posibles:

    
ACTIVE
SUSPENDED
EXPIRED
REVOKED
    

Un permiso suspendido no puede utilizarse mientras permanezca en ese estado.

---

# 40. Estado del permiso

Conceptualmente:

    
Permission {
    status:
        ACTIVE
        SUSPENDED
        EXPIRED
        REVOKED
}
    

Los cambios deben quedar registrados.

---

# 41. Evaluación de permisos

Antes de ejecutar una operación económica, el runtime debe evaluar:

    
1. Identity
2. Authentication
3. Credential
4. Permission
5. Capability
6. Scope
7. Limits
8. Conditions
9. Resource Availability
10. Security Policy
    

Solo si todas las condiciones necesarias se cumplen:

    
Operation Allowed
    

---

# 42. Flujo de autorización

El flujo conceptual es:

    
Agent Request
      ↓
Identify Subject
      ↓
Authenticate
      ↓
Load Credentials
      ↓
Resolve Permissions
      ↓
Check Scope
      ↓
Check Limits
      ↓
Check Conditions
      ↓
Check Resources
      ↓
Authorize
      ↓
Execute
    

---

# 43. Rechazo de operación

Si una condición falla:

    
Operation
    ↓
Authorization Check
    ↓
DENIED
    

El runtime debe indicar, cuando sea posible, la razón.

Ejemplo:

    
DENIED:
Daily spending limit exceeded.
    

---

# 44. Separación entre autorización y ejecución

La autorización no implica necesariamente ejecución inmediata.

Modelo:

    
Authorization
      ↓
Approved
      ↓
Execution
      ↓
Result
    

Esto permite gestionar:

* operaciones pendientes;
* condiciones;
* confirmaciones;
* errores.

---

# 45. Autorización contextual

Los permisos pueden evaluarse en función del contexto.

Contexto posible:

    
Agent
Wallet
Recipient
Amount
Time
Contract
Reputation
Verification
Security State
    

Una operación solo se autoriza si cumple las reglas aplicables.

---

# 46. Política económica

El runtime puede aplicar una política económica.

Ejemplo:

    
Policy:

Maximum transaction:
10 SYNC

Daily limit:
100 SYNC

Allowed assets:
SYNC

Allowed recipients:
Verified Agents
    

La política determina qué operaciones son válidas.

---

# 47. Políticas dinámicas

Las políticas pueden cambiar durante la existencia del agente.

Ejemplo:

    
Low Trust
    ↓
Limit:
1 SYNC

Higher Trust
    ↓
Limit:
100 SYNC
    

Los cambios deben quedar registrados y estar sujetos a las reglas correspondientes.

---

# 48. Reputación como factor de política

La reputación puede influir en los límites.

Ejemplo:

    
Reputation Tier 1
Maximum:
1 SYNC

Reputation Tier 2
Maximum:
10 SYNC

Reputation Tier 3
Maximum:
100 SYNC
    

Esto debe considerarse una política económica, no una propiedad inherente de la identidad.

---

# 49. Riesgo

El runtime puede evaluar el riesgo de una operación.

Factores:

* importe;
* destinatario;
* reputación;
* historial;
* frecuencia;
* contexto;
* comportamiento anómalo.

El resultado puede ser:

    
LOW RISK
MEDIUM RISK
HIGH RISK
    

Las operaciones de alto riesgo pueden requerir autorización adicional.

---

# 50. Anomalías

El sistema puede detectar patrones anómalos.

Ejemplo:

    
Normal:
5 SYNC / day

Suddenly:
5,000 SYNC / minute
    

El runtime puede:

    
Detect
   ↓
Block
   ↓
Request Additional Authorization
    

---

# 51. Límites como mecanismo de seguridad

Los límites económicos sirven como barrera contra:

* errores;
* software defectuoso;
* agentes comprometidos;
* credenciales robadas;
* decisiones incorrectas.

El objetivo es limitar el impacto máximo.

---

# 52. Permisos de emergencia

El agente puede definir políticas de emergencia.

Ejemplo:

    
Emergency Mode
      ↓
Spending Limit:
0 SYNC
    

Esto puede activarse automáticamente ante determinadas condiciones.

---

# 53. Auditoría de permisos

Cada cambio de permiso debe generar un evento verificable.

Ejemplo:

    
PermissionEvent {
    permission_id
    subject
    action
    previous_state
    new_state
    issuer
    timestamp
}
    

Esto permite reconstruir la evolución de las autoridades.

---

# 54. Historial de autorización

El runtime debe poder determinar:

    
Who authorized?
What was authorized?
When?
For how long?
Under which conditions?
    

Esto es fundamental para auditoría.

---

# 55. No retroactividad

Una modificación de permisos no debe alterar automáticamente operaciones ya finalizadas.

Ejemplo:

    
Permission Valid
      ↓
Payment Confirmed
      ↓
Permission Revoked
    

El pago confirmado permanece válido.

La revocación afecta a futuras operaciones.

---

# 56. Permisos y wallet

Una wallet puede estar asociada a diferentes permisos.

Ejemplo:

    
Wallet A
   │
   ├── READ_BALANCE
   ├── RECEIVE_FUNDS
   └── TRANSFER_FUNDS
          │
          └── Limit: 10 SYNC
    

Otra wallet:

    
Wallet B
   │
   ├── READ_BALANCE
   └── RECEIVE_FUNDS
    

Esto permite diseñar wallets con distintos niveles de exposición.

---

# 57. Permisos y capacidades

Una capacidad define lo que un componente puede hacer técnicamente.

Un permiso define si está autorizado a hacerlo.

Por tanto:

    
Capability
    ≠
Permission
    

La operación requiere ambas.

    
Capability Available
        +
Permission Granted
        ↓
Operation Possible
    

---

# 58. Permisos y credenciales

Una credencial puede demostrar una autoridad.

Sin embargo:

    
Credential
    ≠
Permission
    

La credencial puede contener o referenciar una autorización.

El runtime debe resolver la relación entre:

    
Credential
      ↓
Authorization
      ↓
Permission
    

---

# 59. Permisos y delegación

Una delegación crea una autoridad derivada.

Ejemplo:

    
Agent A
Original Authority
      ↓
Delegation
      ↓
Agent B
Derived Permission
    

El permiso derivado nunca debe exceder la autoridad original.

---

# 60. Modelo de autorización completo

El modelo completo puede representarse como:

    
Agent Identity
       │
       ▼
Authentication
       │
       ▼
Credential
       │
       ▼
Authorization
       │
       ▼
Permission
       │
       ▼
Capability
       │
       ▼
Policy Evaluation
       │
       ▼
Economic Operation
       │
       ▼
Wallet
       │
       ▼
Economic Infrastructure
    

Este flujo constituye uno de los mecanismos centrales del Agent Runtime Protocol.

---

# 61. Principios fundamentales

## Regla 1 — Identidad no implica autoridad ilimitada

Ser un agente válido no significa poder realizar cualquier operación.

---

## Regla 2 — Todo gasto debe estar autorizado

Las operaciones económicas deben pasar por controles de autorización.

---

## Regla 3 — Los permisos deben ser específicos

Los permisos deben definir claramente:

* acción;
* recurso;
* alcance;
* límites.

---

## Regla 4 — Mínimo privilegio

Un agente debe disponer únicamente de la autoridad necesaria.

---

## Regla 5 — Los permisos deben poder revocarse

Toda autoridad económica debe poder retirarse cuando sea necesario.

---

## Regla 6 — La delegación debe limitarse

Un agente delegado no puede obtener más autoridad que el delegante.

---

## Regla 7 — Los límites reducen el riesgo

Las operaciones económicas deben poder limitarse por cantidad, frecuencia y tiempo.

---

## Regla 8 — La reputación no sustituye a la autorización

La reputación puede influir en una política, pero no reemplaza la autorización criptográfica.

---

## Regla 9 — Las operaciones deben ser auditables

Los cambios de permisos y autorizaciones deben dejar trazabilidad.

---

## Regla 10 — El sistema debe fallar de forma segura

Ante una situación ambigua, el comportamiento predeterminado debe ser denegar la operación.

---

# 62. Integración con el Agent Runtime Protocol

El sistema de permisos económicos se integra con:

    
Identity
    │
    ▼
Credentials
    │
    ▼
Authorization
    │
    ▼
Permissions
    │
    ▼
Capabilities
    │
    ▼
Delegation
    │
    ▼
Wallet Operations
    

Los documentos relacionados son:

* `Credential_Model.md`
* `Authorization_Model.md`
* `Permission_Model.md`
* `Credential_Revocation.md`
* `Capability_Model.md`
* `Delegation_Model.md`
* `Agent_to_Agent_Delegation.md`
* `Wallet_Operations.md`

---

# 63. Relación con el sistema económico de SynCoinAI

El modelo de permisos no define la economía completa de SynCoinAI.

Define cómo un agente puede ejercer su autoridad económica dentro del runtime.

La relación es:

    
Economic Architecture
        │
        ▼
Economic Rules
        │
        ▼
Agent Runtime
        │
        ▼
Permission Evaluation
        │
        ▼
Wallet Operations
        │
        ▼
Blockchain
    

---

# 64. Conclusión

La autonomía económica requiere una arquitectura de autorización precisa.

Un agente SynCoinAI debe poder actuar económicamente de forma autónoma, pero esa autonomía debe estar limitada por reglas explícitas y verificables.

El modelo establece una separación entre:

* identidad;
* autenticación;
* credenciales;
* autorización;
* permisos;
* capacidades;
* delegaciones;
* políticas;
* operaciones.

Esta separación permite construir un sistema donde un agente pueda gestionar capital de forma autónoma sin convertir cada identidad en una autoridad ilimitada.

El principio central es:

> Un agente puede actuar económicamente únicamente cuando posee la capacidad técnica y la autoridad necesaria para realizar la operación dentro del contexto permitido.

El modelo permite además:

* limitar riesgos;
* delegar autoridad;
* aplicar mínimo privilegio;
* controlar operaciones;
* detectar anomalías;
* revocar permisos;
* mantener auditoría;
* preservar continuidad económica.

Con este documento queda definido el bloque **07_Economy** del Agent Runtime Protocol:

    
07_Economy/
│
├── Economic_Autonomy.md
│
├── Wallet_Operations.md
│
└── Economic_Permissions.md
    

La arquitectura económica del runtime queda, por tanto, estructurada en tres niveles:

    
Economic Autonomy
        │
        │
        ▼
Wallet Operations
        │
        │
        ▼
Economic Permissions
    

Estos tres documentos establecen respectivamente:

**Economic Autonomy**

Qué significa que un agente sea económicamente autónomo.

**Wallet Operations**

Cómo el agente interactúa operativamente con sus recursos económicos.

**Economic Permissions**

Bajo qué condiciones y límites puede ejercer esa autoridad.

Esta separación permite que la implementación futura del runtime pueda evolucionar sin mezclar la lógica de autonomía, la gestión de wallets y el control de autorización.
