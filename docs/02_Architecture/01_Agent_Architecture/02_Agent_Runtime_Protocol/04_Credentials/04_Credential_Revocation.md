# SynCoinAI Agent Runtime Protocol

## Credential Revocation

**Versión:** 1.0
**Documento:** `02_Architecture / 01_Agent_Architecture / 02_Agent_Runtime_Protocol / 04_Credentials / Credential_Revocation.md`
**Estado:** Arquitectura inicial

---

# 1. Introducción

Las credenciales permiten a un agente demostrar identidad, autoridad o determinadas capacidades dentro del ecosistema SynCoinAI.

Sin embargo, ninguna credencial debe considerarse válida indefinidamente por el simple hecho de haber sido emitida correctamente.

Una credencial puede dejar de ser válida debido a:

* compromiso de una clave;
* pérdida de control;
* cambio de autoridad;
* expiración;
* modificación de permisos;
* finalización de una delegación;
* suspensión del agente;
* cierre del agente;
* violación de políticas;
* sustitución por una nueva credencial.

Por este motivo, SynCoinAI Runtime debe disponer de un mecanismo explícito para invalidar credenciales antes o después de su fecha de expiración.

Este mecanismo se denomina **Credential Revocation**.

---

# 2. Objetivo

El objetivo de este documento es definir el modelo mediante el cual SynCoinAI determina cuándo una credencial deja de ser válida.

El sistema debe permitir:

* revocar credenciales;
* detectar credenciales revocadas;
* impedir su utilización posterior;
* gestionar revocaciones de emergencia;
* mantener trazabilidad;
* preservar el historial de acciones anteriores;
* gestionar credenciales delegadas;
* gestionar credenciales comprometidas;
* separar revocación de identidad;
* permitir recuperación cuando sea posible.

---

# 3. Principio fundamental

SynCoinAI establece:

> Una credencial válida en el pasado no implica que continúe siendo válida en el presente.

Por tanto:

    
Issued
   ↓
Valid
   ↓
Revoked
   ↓
Invalid
    

La revocación afecta a la validez futura de la credencial.

No debe utilizarse para reescribir automáticamente el historial de acciones legítimamente realizadas mientras la credencial era válida.

---

# 4. Separación entre identidad y credencial

La revocación de una credencial no implica necesariamente la revocación de la identidad del agente.

Por ejemplo:

    
Agent Identity
       │
       ├── Credential A → Revoked
       │
       ├── Credential B → Valid
       │
       └── Credential C → Valid
    

En este escenario:

    
Identity = Active
Credential A = Revoked
Credential B = Valid
Credential C = Valid
    

La identidad del agente continúa existiendo.

Esto permite reemplazar credenciales comprometidas sin destruir necesariamente la identidad histórica del agente.

---

# 5. Estados de una credencial

Una credencial puede atravesar diferentes estados.

    
CREATED
   ↓
ISSUED
   ↓
ACTIVE
   ├───────────────┐
   │               │
   ▼               ▼
EXPIRED         REVOKED
   │               │
   └───────┬───────┘
           ▼
         INVALID
    

Estados conceptuales:

* `CREATED`
* `ISSUED`
* `ACTIVE`
* `EXPIRED`
* `REVOKED`
* `INVALID`

Una credencial no puede volver automáticamente a estado `ACTIVE` después de haber sido revocada.

---

# 6. Expiración frente a revocación

La expiración y la revocación son mecanismos diferentes.

## Expiración

La credencial deja de ser válida porque ha alcanzado su fecha límite.

    
Valid Until
     ↓
Expiration
     ↓
Invalid
    

---

## Revocación

La credencial deja de ser válida antes de su expiración debido a una decisión o evento de seguridad.

    
Valid Credential
     ↓
Revocation Event
     ↓
Invalid
    

Por tanto:

    
Expired ≠ Revoked
    

Ambos estados deben poder distinguirse para fines de auditoría y seguridad.

---

# 7. Motivos de revocación

Una credencial puede ser revocada por diferentes motivos.

## 7.1 Compromiso criptográfico

La clave asociada puede haber sido:

* robada;
* expuesta;
* copiada;
* comprometida.

---

## 7.2 Pérdida de control

El agente puede haber perdido el control sobre la credencial.

---

## 7.3 Cambio de autoridad

La entidad que emitió la credencial puede retirar la autoridad concedida.

---

## 7.4 Finalización de delegación

Una credencial delegada puede dejar de ser válida cuando termina la delegación.

---

## 7.5 Cambio de permisos

Una nueva política puede sustituir los permisos anteriores.

---

## 7.6 Suspensión del agente

Una suspensión puede provocar la invalidación temporal o permanente de determinadas credenciales.

---

## 7.7 Cierre del agente

La finalización permanente de un agente puede provocar la revocación de sus credenciales activas.

---

## 7.8 Violación de políticas

El agente puede perder determinadas autorizaciones por incumplimiento de reglas.

---

# 8. Autoridad de revocación

No cualquier entidad puede revocar cualquier credencial.

La autoridad de revocación debe estar vinculada a:

* el emisor de la credencial;
* el propietario legítimo;
* una autoridad delegada;
* un mecanismo de gobernanza;
* un mecanismo de recuperación.

El principio fundamental es:

> Solo una entidad con autoridad verificable puede revocar una credencial.

---

# 9. Revocación por el propio agente

Un agente debe poder revocar sus propias credenciales cuando disponga de los mecanismos necesarios para demostrar control legítimo.

Ejemplo:

    
Agent A
   │
   │ Revokes
   ▼
Credential A
    

Esto resulta especialmente importante en casos de:

* compromiso detectado;
* rotación de claves;
* sustitución de credenciales.

La capacidad de autorrevocación reduce la dependencia de terceros.

---

# 10. Revocación por el emisor

El emisor de una credencial puede revocarla cuando mantiene autoridad sobre ella.

Ejemplo:

    
Issuer
   │
   │ Issues
   ▼
Credential
   │
   │ Revokes
   ▼
Invalid
    

El emisor debe demostrar que conserva la autoridad necesaria para realizar la revocación.

---

# 11. Revocación por compromiso

Cuando existe sospecha razonable de compromiso, la revocación puede ejecutarse inmediatamente.

Modelo:

    
Compromise Detected
       ↓
Emergency Revocation
       ↓
Credential Invalid
       ↓
Recovery Process
    

La prioridad en estos casos es impedir nuevas acciones utilizando la credencial comprometida.

---

# 12. Revocación de emergencia

SynCoinAI debe contemplar mecanismos de revocación rápida para situaciones críticas.

Una revocación de emergencia puede aplicarse cuando:

* una clave privada ha sido comprometida;
* una credencial está siendo utilizada de forma maliciosa;
* existe riesgo económico significativo;
* una autoridad ha sido comprometida.

El mecanismo debe minimizar el tiempo entre:

    
Detection
    

y:

    
Effective Revocation
    

---

# 13. Efecto temporal de la revocación

La revocación debe distinguir entre:

* acciones anteriores;
* acciones posteriores.

Modelo:

    
Credential Valid
       │
       │
       ├── Action A → Valid
       │
       ├── Action B → Valid
       │
       ▼
Revocation
       │
       ├── Action C → Denied
       │
       └── Action D → Denied
    

La revocación no invalida automáticamente las acciones legítimamente ejecutadas antes de su efectividad.

---

# 14. Momento efectivo de revocación

Toda revocación debe tener un momento efectivo verificable.

Conceptualmente:

    
Revocation Event
{
    credential_id
    revoked_at
    revocation_reason
    revoking_authority
}
    

El Runtime debe poder determinar:

> ¿La credencial estaba válida en el momento en que se realizó esta acción?

Esta capacidad es esencial para auditoría y resolución de disputas.

---

# 15. Revocación y acciones pendientes

Una credencial puede ser revocada mientras existen operaciones pendientes.

En estos casos, el Runtime debe evaluar el estado de la credencial antes de completar la operación.

Modelo:

    
Action Pending
       │
       ▼
Credential Revoked
       │
       ▼
Action Re-evaluated
       │
       ▼
DENY / CANCEL
    

Las operaciones ya confirmadas no deben considerarse automáticamente pendientes.

---

# 16. Revocación y transacciones económicas

Las operaciones económicas requieren especial atención.

Una transacción ya confirmada en la infraestructura económica no debe revertirse únicamente porque una credencial utilizada posteriormente haya sido revocada.

Por tanto:

    
Confirmed Transaction
       ↓
Credential Later Revoked
       ↓
Transaction Remains Historical
    

Sin embargo, las nuevas operaciones deben ser rechazadas cuando la credencial ya no sea válida.

La reversión de operaciones económicas, cuando exista, debe depender de mecanismos específicos y no de la revocación por sí sola.

---

# 17. Revocación de credenciales delegadas

Cuando una credencial ha sido delegada, su revocación puede afectar a toda la cadena derivada.

Ejemplo:

    
Agent A
   │
   │ Delegates
   ▼
Agent B
   │
   │ Subdelegates
   ▼
Agent C
    

Si se revoca la autoridad original:

    
A Credential Revoked
       ↓
B Delegation Invalid
       ↓
C Subdelegation Invalid
    

La revocación debe propagarse de acuerdo con las relaciones de autoridad.

---

# 18. Revocación parcial

No toda revocación debe afectar a todas las capacidades del agente.

Por ejemplo:

    
Agent A
│
├── Payment Credential → Revoked
├── Communication Credential → Valid
└── Service Credential → Valid
    

El agente puede continuar operando en determinados ámbitos.

Esto permite aplicar una política de:

> **Revocación mínima necesaria**

En lugar de eliminar completamente la capacidad operativa del agente.

---

# 19. Revocación total

En situaciones graves puede ser necesario invalidar todas las credenciales activas de un agente.

Ejemplo:

    
Agent A
   │
   ├── Credential A → Revoked
   ├── Credential B → Revoked
   └── Credential C → Revoked
    

Esto no implica necesariamente eliminar la identidad.

Puede significar:

    
Identity = Preserved
Credentials = Invalid
Permissions = Denied
    

La identidad histórica puede mantenerse para preservar:

* historial;
* reputación;
* relaciones;
* auditoría.

---

# 20. Revocación y suspensión

La suspensión y la revocación no son equivalentes.

Una suspensión puede ser:

    
Temporal
    

Mientras que una revocación de credencial normalmente es:

    
Permanent for that credential
    

Ejemplo:

    
Agent Suspended
    ↓
Credentials Temporarily Restricted
    

Al finalizar la suspensión, algunas autorizaciones pueden restaurarse.

Por el contrario:

    
Credential Revoked
    ↓
Credential Cannot Be Reused
    

Puede ser necesario emitir una nueva credencial.

---

# 21. Revocación y recuperación

La revocación puede iniciar un proceso de recuperación.

Modelo:

    
Credential Compromised
       ↓
Revocation
       ↓
Identity Preserved
       ↓
Recovery
       ↓
New Credential
    

La recuperación debe permitir que el agente mantenga, cuando corresponda:

* identidad;
* historial;
* reputación;
* activos;
* relaciones.

La recuperación no debe permitir que una credencial comprometida vuelva a utilizarse.

---

# 22. Revocación y rotación de claves

La rotación de claves puede implicar la sustitución de credenciales.

Ejemplo:

    
Key A
   ↓
Credential A
   ↓
Revoked

Key B
   ↓
Credential B
   ↓
Active
    

La identidad del agente permanece:

    
Agent Identity = Same
    

Mientras que la credencial cambia.

Esto refuerza la separación entre:

    
Agent Identity
    

y:

    
Cryptographic Credential
    

---

# 23. Estado de revocación

El Runtime debe poder determinar el estado actual de una credencial.

Conceptualmente:

    
Credential Status
{
    credential_id
    status
    issued_at
    expires_at
    revoked_at
    revocation_reason
}
    

El sistema debe permitir distinguir al menos:

    
ACTIVE
EXPIRED
REVOKED
INVALID
    

---

# 24. Verificación de revocación

Antes de aceptar una acción protegida por una credencial, el Runtime debe verificar su estado.

Modelo:

    
Action Request
       ↓
Credential Validation
       ↓
Revocation Status Check
       ↓
Permission Evaluation
       ↓
ALLOW / DENY
    

Una credencial criptográficamente válida puede seguir siendo inválida si ha sido revocada.

Por tanto:

    
Valid Signature
    ≠
Valid Credential
    

---

# 25. Consistencia del estado de revocación

En un sistema distribuido, diferentes nodos pueden recibir información de revocación en momentos distintos.

SynCoinAI debe considerar:

* propagación;
* sincronización;
* latencia;
* disponibilidad;
* consistencia.

El sistema debe minimizar la posibilidad de que una credencial revocada continúe siendo aceptada debido a información obsoleta.

Las operaciones de alto riesgo pueden requerir una verificación con garantías superiores antes de ser aceptadas.

---

# 26. Revocación offline

En determinados entornos, un agente puede operar temporalmente sin conexión directa al sistema de validación.

En estos casos, la arquitectura debe considerar:

* duración máxima de credenciales;
* límites de riesgo;
* ventanas de validez;
* sincronización posterior.

Las credenciales de alto riesgo no deberían depender indefinidamente de información de revocación potencialmente desactualizada.

---

# 27. Revocación y privacidad

La información sobre una revocación puede contener datos sensibles.

SynCoinAI debe distinguir entre:

    
Revocation Status
    

y:

    
Revocation Details
    

Puede ser necesario revelar públicamente que:

    
Credential = Revoked
    

sin revelar:

* motivo exacto;
* información privada;
* detalles de seguridad;
* información sobre el agente.

La transparencia debe equilibrarse con la privacidad.

---

# 28. Auditoría de revocaciones

Las revocaciones relevantes deben poder ser auditadas.

El sistema debería permitir demostrar:

* qué credencial fue revocada;
* quién ejecutó la revocación;
* cuándo ocurrió;
* qué autoridad la respaldaba;
* cuál fue el motivo registrado;
* desde qué momento fue efectiva.

La auditoría no implica necesariamente publicación completa de información sensible.

---

# 29. Revocación y reputación

La revocación de una credencial no debe modificar automáticamente la reputación del agente.

Debe distinguirse:

    
Credential Revocation
    

de:

    
Reputation Event
    

Sin embargo, el hecho que provocó la revocación puede constituir un evento relevante para el sistema de reputación si existen pruebas verificables.

Por tanto:

    
Revocation
    ↓
Potential Reputation Event
    

pero no:

    
Revocation
    =
Automatic Reputation Penalty
    

La evaluación de reputación debe seguir sus propias reglas.

---

# 30. Revocación y continuidad del agente

La continuidad de identidad puede mantenerse después de la revocación de una credencial.

Ejemplo:

    
Agent A
   │
   ├── Identity → Preserved
   ├── History → Preserved
   ├── Reputation → Preserved
   ├── Credential A → Revoked
   └── Credential B → Newly Issued
    

Esto permite recuperar la capacidad operativa sin crear automáticamente un nuevo agente.

---

# 31. Revocación de identidad frente a revocación de credenciales

SynCoinAI debe distinguir:

    
Credential Revocation
    

de:

    
Identity Revocation
    

La revocación de una credencial afecta a un mecanismo de autenticación o autorización.

La revocación de identidad afecta a la propia existencia reconocida del agente dentro del protocolo.

Por tanto:

    
Credential Revoked
    ≠
Identity Revoked
    

La revocación de identidad debe considerarse un mecanismo excepcional y estar definido en el sistema de identidad y ciclo de vida.

---

# 32. Modelo de revocación

Conceptualmente:

    
Credential
{
    credential_id
    subject
    issuer
    scope
    issued_at
    expires_at
    status
    revoked_at
    revocation_reason
    revoking_authority
}
    

El modelo técnico definitivo podrá variar según la implementación del Runtime.

---

# 33. Flujo de revocación

El flujo general es:

    
Revocation Trigger
       ↓
Authority Verification
       ↓
Revocation Event
       ↓
State Update
       ↓
Propagation
       ↓
Runtime Enforcement
       ↓
Future Actions Denied
    

Cuando sea necesario:

    
       ↓
Recovery Process
       ↓
New Credential
    

---

# 34. Flujo de recuperación después de revocación

Cuando la revocación no implica la pérdida de identidad:

    
Credential Compromise
       ↓
Credential Revoked
       ↓
Agent Identity Preserved
       ↓
Recovery Authentication
       ↓
New Credential Issued
       ↓
Permissions Re-established
    

Los permisos deben ser reevaluados.

No deben restaurarse automáticamente si las condiciones de seguridad han cambiado.

---

# 35. Principios fundamentales

El modelo de revocación de credenciales de SynCoinAI se basa en los siguientes principios:

### 1. Revocabilidad

Toda credencial debe poder dejar de ser válida cuando sea necesario.

### 2. Separación de identidad

Revocar una credencial no implica automáticamente eliminar la identidad.

### 3. Efectividad temporal

La revocación debe tener un momento efectivo verificable.

### 4. No retroactividad automática

La revocación no reescribe automáticamente acciones legítimas anteriores.

### 5. Autoridad verificable

Solo entidades autorizadas pueden revocar credenciales.

### 6. Revocación de emergencia

Los mecanismos críticos deben poder invalidarse rápidamente.

### 7. Revocación mínima

Debe revocarse únicamente el alcance necesario cuando sea posible.

### 8. Propagación de autoridad

La revocación de una autoridad superior debe afectar a las delegaciones derivadas correspondientes.

### 9. Recuperabilidad

Cuando sea posible, un agente debe poder recuperar su capacidad operativa mediante nuevas credenciales.

### 10. Auditabilidad

Las revocaciones relevantes deben poder ser verificadas posteriormente.

---

# Conclusión

El modelo de Credential Revocation permite que SynCoinAI mantenga un sistema de credenciales dinámico y seguro.

La arquitectura establece una separación clara entre:

    
Identity
    ↓
Credential
    ↓
Authorization
    ↓
Permission
    ↓
Action
    

y permite invalidar una credencial sin destruir necesariamente la identidad del agente.

Este diseño es especialmente importante para agentes autónomos porque una credencial comprometida no debería obligar automáticamente a perder:

* identidad;
* reputación;
* historial;
* relaciones;
* activos.

El objetivo es permitir una arquitectura donde la seguridad pueda evolucionar independientemente de la identidad del agente.

La revocación se convierte así en un mecanismo esencial para controlar el riesgo sin sacrificar la continuidad de los agentes.

---

# Relación con otros documentos

Este documento se relaciona directamente con:

* `Credential_Model.md`
* `Authorization_Model.md`
* `Permission_Model.md`
* `03_Identity/Identity_Model.md`
* `03_Identity/Root_Identity.md`
* `03_Identity/Identity_Recovery.md`
* `05_Security/Security_Model.md`
* `05_Security/Security_Levels.md`
* `05_Security/Key_Compromise.md`
* `05_Security/Identity_Recovery.md`
* `06_Capabilities/Delegation_Model.md`
* `06_Capabilities/Agent_to_Agent_Delegation.md`
* `13_Suspension/`
* `14_Lifecycle/`

Este documento define el modelo general de revocación.

Los mecanismos específicos de compromiso de claves, recuperación de identidad, suspensión y cierre del agente se desarrollarán en sus respectivos documentos.
