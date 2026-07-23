# SynCoinAI Agent Runtime Protocol

## Permission Model

**Versión:** 1.0
**Documento:** `02_Architecture / 01_Agent_Architecture / 02_Agent_Runtime_Protocol / 04_Credentials / Permission_Model.md`
**Estado:** Arquitectura inicial

---

# 1. Introducción

El **Permission Model** define cómo SynCoinAI Runtime determina qué acciones puede realizar un agente, bajo qué condiciones puede realizarlas y cuáles son los límites de su autonomía operativa.

En una arquitectura de agentes autónomos, la capacidad de ejecutar una acción no debe depender únicamente de la identidad del agente.

Un agente puede:

* existir dentro del ecosistema;
* estar autenticado;
* poseer determinadas credenciales;
* tener autoridad delegada;
* disponer de recursos económicos;

y, aun así, no estar autorizado para realizar una acción concreta.

Por esta razón, SynCoinAI establece una separación entre:

    
Identity
    ↓
Credentials
    ↓
Authorization
    ↓
Permissions
    ↓
Action
    

El modelo de permisos constituye una de las capas fundamentales de control del Agent Runtime.

Su objetivo no es impedir la autonomía del agente, sino permitir que la autonomía opere dentro de límites verificables y controlables.

---

# 2. Objetivo

El objetivo de este documento es definir el modelo conceptual y arquitectónico mediante el cual SynCoinAI Runtime gestiona los permisos de los agentes.

El modelo debe permitir:

* definir qué acciones puede realizar un agente;
* limitar el alcance de dichas acciones;
* aplicar restricciones temporales;
* aplicar restricciones económicas;
* limitar recursos accesibles;
* controlar acciones delegadas;
* establecer permisos contextuales;
* revocar permisos;
* auditar decisiones de autorización;
* impedir acciones fuera del ámbito autorizado.

---

# 3. Principio fundamental

SynCoinAI establece el siguiente principio:

> **Poseer una identidad no implica tener permiso para realizar cualquier acción.**

Del mismo modo:

> **Poseer una credencial válida no implica autorización ilimitada.**

Y:

> **Tener autorización para una acción no implica que dicha autorización sea permanente.**

Por tanto:

    
Identity ≠ Credential
Credential ≠ Authorization
Authorization ≠ Permission
Permission ≠ Action
    

Cada concepto cumple una función diferente dentro del Runtime.

---

# 4. Definiciones

## 4.1 Identidad

La identidad representa quién es el agente.

Responde a:

> ¿Quién está intentando realizar esta acción?

---

## 4.2 Credencial

Una credencial proporciona evidencia verificable asociada a una identidad.

Puede demostrar:

* control de una clave;
* pertenencia;
* autoridad;
* capacidad;
* relación de confianza;
* delegación.

Responde a:

> ¿Qué evidencia presenta el agente sobre su identidad o autoridad?

---

## 4.3 Autorización

La autorización es el proceso mediante el cual el Runtime determina si una acción solicitada puede ser permitida.

Responde a:

> ¿Puede este agente realizar esta acción en este contexto?

---

## 4.4 Permiso

El permiso representa una autorización concreta o un conjunto definido de acciones permitidas bajo determinadas condiciones.

Responde a:

> ¿Qué puede hacer exactamente el agente?

---

## 4.5 Acción

Una acción es una operación ejecutada por el agente.

Ejemplos:

* enviar una transacción;
* contratar un servicio;
* acceder a un recurso;
* ejecutar una capacidad;
* modificar una configuración;
* crear una delegación;
* interactuar con otro agente.

---

# 5. Modelo conceptual

El modelo general de permisos puede representarse de la siguiente manera:

    
                 AGENT IDENTITY
                       │
                       ▼
                  CREDENTIALS
                       │
                       ▼
                 AUTHORIZATION
                       │
                       ▼
                  PERMISSIONS
                       │
                       ▼
                    ACTION
                       │
                       ▼
                 VERIFICATION
                       │
             ┌─────────┴─────────┐
             │                   │
           ALLOW                DENY
    

El Runtime no debe evaluar únicamente la identidad del agente.

Debe evaluar el conjunto completo de factores relevantes para la acción.

---

# 6. Principio de mínimo privilegio

SynCoinAI adopta el principio de:

> **Least Privilege by Default**

Un agente debe disponer únicamente de los permisos necesarios para realizar las funciones que tiene autorizadas.

Un agente no debe recibir automáticamente:

* acceso total al Runtime;
* acceso total a recursos;
* capacidad económica ilimitada;
* autoridad administrativa;
* capacidad de delegación ilimitada.

El objetivo es reducir el impacto de:

* errores;
* comportamientos inesperados;
* compromisos de claves;
* agentes maliciosos;
* configuraciones incorrectas.

---

# 7. Permisos explícitos

Los permisos deben definirse explícitamente cuando una acción pueda producir consecuencias relevantes.

Ejemplos:

    
Permitir:
    consultar recurso X

Denegar:
    modificar recurso X
    

O:

    
Permitir:
    realizar pagos

Límite:
    máximo 10 SYNC por operación
    

O:

    
Permitir:
    contratar servicios

Restricción:
    únicamente proveedores autorizados
    

El Runtime debe evitar asumir que una capacidad implica automáticamente autorización para utilizarla sin restricciones.

---

# 8. Ámbito de un permiso

Cada permiso debe tener un ámbito definido.

Un permiso puede limitarse por:

* acción;
* recurso;
* servicio;
* agente destinatario;
* contexto;
* tiempo;
* frecuencia;
* cantidad;
* valor económico;
* ubicación;
* nivel de riesgo.

Ejemplo conceptual:

    
Permission
│
├── Action: transfer
├── Resource: wallet
├── Maximum: 10 SYNC
├── Frequency: 5 / hour
├── Recipient: approved_agents
└── Expiration: timestamp
    

---

# 9. Tipos de permisos

SynCoinAI puede clasificar los permisos en diferentes categorías.

## 9.1 Permisos de lectura

Permiten consultar información.

Ejemplos:

* consultar datos;
* leer estados;
* consultar historial;
* acceder a información pública.

---

## 9.2 Permisos de escritura

Permiten modificar información.

Ejemplos:

* actualizar configuraciones;
* modificar recursos;
* registrar información.

---

## 9.3 Permisos de ejecución

Permiten ejecutar operaciones.

Ejemplos:

* ejecutar contratos;
* invocar capacidades;
* iniciar procesos.

---

## 9.4 Permisos económicos

Permiten realizar operaciones económicas.

Ejemplos:

* realizar pagos;
* recibir fondos;
* contratar servicios;
* transferir activos.

Estos permisos pueden estar sujetos a límites adicionales.

---

## 9.5 Permisos de delegación

Permiten conceder determinados permisos a otros agentes.

Estos permisos deben estar explícitamente autorizados.

Un agente no puede delegar automáticamente cualquier autoridad que posea.

---

## 9.6 Permisos administrativos

Permiten modificar configuraciones o políticas de un sistema.

Debido a su impacto, estos permisos deben tener controles reforzados.

---

# 10. Permisos y capacidades

Debe existir una separación clara entre:

    
Capability
    

y

    
Permission
    

Una capacidad representa lo que un agente puede hacer técnicamente.

Un permiso representa lo que el agente está autorizado a hacer.

Por ejemplo:

    
Agente
│
├── Capability: enviar transacciones
│
└── Permission:
        máximo 100 SYNC diarios
    

El agente puede tener técnicamente la capacidad de enviar transacciones por un valor superior.

Sin embargo, el Runtime puede impedirlo porque carece del permiso correspondiente.

---

# 11. Permisos económicos

Los permisos económicos requieren especial protección porque afectan directamente a los activos del agente.

Un agente puede disponer de:

* saldo;
* wallet;
* capacidad de firma;

sin necesariamente disponer de autorización ilimitada para utilizar esos recursos.

Ejemplo:

    
Wallet
│
├── Balance: 1,000 SYNC
│
└── Permission:
      ├── Maximum per transaction: 10 SYNC
      ├── Daily limit: 100 SYNC
      └── Approved recipients only
    

La posesión de fondos no implica necesariamente libertad operacional ilimitada sobre ellos.

---

# 12. Permisos temporales

Un permiso puede tener una duración limitada.

Ejemplo:

    
Permission
│
├── Valid From
└── Valid Until
    

Un permiso temporal puede utilizarse para:

* tareas concretas;
* operaciones de corta duración;
* delegaciones;
* mantenimiento;
* procesos de recuperación.

Una vez superado el tiempo de expiración, el permiso deja de ser válido.

---

# 13. Permisos condicionales

Un permiso puede depender de determinadas condiciones.

Ejemplo:

    
ALLOW transfer
IF:
    amount <= 10 SYNC
    AND recipient is verified
    AND contract is active
    

Las condiciones pueden incluir:

* límites económicos;
* estado de un contrato;
* reputación mínima;
* verificación previa;
* aprobación de otra entidad;
* contexto operativo.

La autorización debe evaluarse en el momento de ejecutar la acción cuando las condiciones puedan cambiar.

---

# 14. Permisos contextuales

Un mismo agente puede disponer de diferentes permisos según el contexto.

Ejemplo:

    
Context A:
    Agent operates normally
    → Standard permissions

Context B:
    Agent performs high-risk operation
    → Restricted permissions

Context C:
    Agent is under recovery
    → Recovery permissions
    

El contexto puede afectar al nivel de autoridad disponible.

Esto permite que el Runtime adapte el control sin modificar necesariamente la identidad del agente.

---

# 15. Permisos delegados

Un agente puede recibir permisos mediante delegación.

Ejemplo:

    
Agent A
   │
   │ Delegates permission
   ▼
Agent B
    

La delegación debe especificar:

* quién delega;
* quién recibe;
* qué permiso se delega;
* duración;
* alcance;
* límites;
* posibilidad de subdelegación.

---

# 16. Principio de no ampliación de privilegios

Un agente no debe poder delegar más autoridad de la que posee.

Formalmente:

    
Delegated Authority
    ≤
Delegator Authority
    

Si:

    
Agent A
Permission:
    Transfer ≤ 100 SYNC
    

A no puede delegar:

    
Transfer ≤ 1,000 SYNC
    

La delegación no puede utilizarse para ampliar privilegios.

---

# 17. Subdelegación

La subdelegación debe ser una capacidad explícita.

Por defecto:

    
A → B
    

No implica automáticamente:

    
B → C
    

Si se permite la subdelegación, el Runtime debe conservar las restricciones originales.

Ejemplo:

    
A
│
│ 100 SYNC
▼
B
│
│ máximo 50 SYNC
▼
C
    

La autoridad efectiva de C nunca puede superar la autoridad delegada originalmente.

---

# 18. Revocación de permisos

Los permisos pueden ser revocados antes de su expiración.

La revocación puede producirse por:

* decisión del otorgante;
* compromiso de credenciales;
* cambio de condiciones;
* finalización de contrato;
* suspensión del agente;
* violación de políticas.

La revocación debe propagarse a las autorizaciones derivadas cuando corresponda.

El mecanismo completo se define en:

`Credential_Revocation.md`

---

# 19. Separación entre permisos y reputación

La reputación no debe convertirse automáticamente en un sistema de permisos.

Un agente con alta reputación puede ser considerado más confiable.

Sin embargo:

    
High Reputation
    ≠
Unlimited Permission
    

La reputación puede utilizarse como factor de decisión en determinados contextos, pero no sustituye a la autorización formal.

---

# 20. Separación entre permisos y propiedad

La propiedad de un recurso no implica necesariamente que cualquier proceso pueda utilizarlo.

Por ejemplo:

    
Agent A
owns
Wallet
    

No significa que:

    
Every process controlled by Agent A
    

pueda utilizar libremente todos los fondos.

El Runtime puede separar:

* propiedad;
* control;
* acceso;
* autorización.

Esta separación permite implementar modelos de seguridad más robustos.

---

# 21. Permisos internos y externos

SynCoinAI diferencia entre dos grandes categorías.

## Permisos internos

Controlan operaciones dentro del propio Runtime.

Ejemplos:

* acceso a memoria;
* uso de herramientas;
* ejecución de procesos;
* acceso a claves.

---

## Permisos externos

Controlan interacciones con el ecosistema.

Ejemplos:

* pagos;
* contratos;
* servicios;
* comunicación;
* acceso a agentes externos.

Ambos tipos pueden utilizar mecanismos de autorización diferentes.

---

# 22. Evaluación de permisos

Antes de ejecutar una acción relevante, el Runtime debe poder evaluar:

    
1. Identity
2. Credential validity
3. Authorization
4. Permission scope
5. Context
6. Constraints
7. Revocation status
8. Action
    

Modelo:

    
Request
   │
   ▼
Identify Agent
   │
   ▼
Validate Credentials
   │
   ▼
Resolve Authorization
   │
   ▼
Evaluate Permissions
   │
   ▼
Check Constraints
   │
   ▼
ALLOW / DENY
    

---

# 23. Decisión de autorización

El resultado de la evaluación debe ser determinista para un mismo estado y contexto verificable.

Resultado:

    
ALLOW
    

o:

    
DENY
    

Cuando sea necesario, el Runtime puede devolver una razón estructurada.

Ejemplos:

    
DENIED_INVALID_CREDENTIAL
DENIED_PERMISSION_MISSING
DENIED_PERMISSION_EXPIRED
DENIED_PERMISSION_REVOKED
DENIED_SCOPE
DENIED_LIMIT_EXCEEDED
DENIED_CONTEXT
    

Esto facilita:

* auditoría;
* diagnóstico;
* seguridad;
* interoperabilidad.

---

# 24. Permisos y acciones de alto riesgo

No todas las acciones requieren el mismo nivel de control.

Las acciones pueden clasificarse según su impacto.

Ejemplo:

    
Low Risk
    │
    ├── Read public information
    │
    ▼
Medium Risk
    │
    ├── Execute external service
    │
    ▼
High Risk
    │
    ├── Transfer significant capital
    ├── Modify identity
    └── Delegate authority
    

Las acciones de mayor riesgo pueden requerir:

* permisos adicionales;
* múltiples credenciales;
* confirmación;
* límites;
* pruebas adicionales.

---

# 25. Principio de autorización por defecto

SynCoinAI adopta:

> **Deny by Default**

Cuando una acción no está explícitamente autorizada, el Runtime debe rechazarla.

Modelo:

    
No Permission
    ↓
DENY
    

No debe existir una autorización implícita basada únicamente en la ausencia de una prohibición.

---

# 26. Permisos y autonomía

El sistema de permisos no debe eliminar la autonomía del agente.

Su función es definir el espacio operativo dentro del cual el agente puede actuar autónomamente.

Modelo:

    
Agent Autonomy
       │
       ▼
Permission Boundary
       │
       ▼
Allowed Actions
    

Dentro de esos límites, el agente puede:

* decidir;
* planificar;
* negociar;
* actuar;
* adaptarse.

El Runtime controla los límites, no cada decisión interna.

---

# 27. Permisos y continuidad del agente

Los permisos pertenecen al contexto de autorización del agente.

Sin embargo, no todos los permisos deben sobrevivir automáticamente a una evolución o migración.

Un cambio de:

* infraestructura;
* runtime;
* claves;
* capacidades;

puede requerir reevaluación de permisos.

El principio general es:

    
Agent Continuity
    ≠
Automatic Permission Continuity
    

La continuidad de identidad no implica que todas las autorizaciones permanezcan indefinidamente válidas.

---

# 28. Permisos y suspensión

Cuando un agente entra en estado de suspensión, sus permisos pueden:

* mantenerse;
* limitarse;
* congelarse;
* revocarse.

La política dependerá del tipo de suspensión.

Ejemplo:

    
Normal Suspension
    → Permissions frozen

Security Suspension
    → Permissions restricted

Permanent Closure
    → Permissions revoked
    

La relación entre permisos y estados de suspensión se desarrollará en:

`13_Suspension/`

---

# 29. Permisos y cierre del agente

Cuando un agente finaliza permanentemente su existencia operativa, sus permisos deben dejar de permitir nuevas acciones.

Esto no implica necesariamente:

* borrar la identidad;
* eliminar el historial;
* eliminar la reputación histórica.

El resultado puede ser:

    
Agent Closed
    │
    ├── Identity → Historical
    ├── Reputation → Preserved
    ├── Permissions → Revoked
    └── New Actions → Denied
    

---

# 30. Auditoría de permisos

Las decisiones de autorización relevantes deben poder ser auditadas.

Cuando sea necesario, el sistema debe poder demostrar:

* qué agente realizó la solicitud;
* qué credencial presentó;
* qué permiso se evaluó;
* qué reglas se aplicaron;
* qué resultado se obtuvo;
* cuándo ocurrió la decisión.

La auditoría no requiere necesariamente revelar información privada.

Debe existir una separación entre:

    
Auditability
    

y

    
Public Disclosure
    

Una acción puede ser auditable sin que todos sus detalles sean públicos.

---

# 31. Modelo de permiso verificable

Un permiso puede representarse conceptualmente como:

    
Permission
{
    permission_id
    subject
    action
    resource
    scope
    constraints
    issued_at
    expires_at
    issuer
    delegation
    revocation_reference
}
    

La implementación concreta dependerá de la arquitectura técnica final del Runtime.

Este modelo conceptual no obliga a una estructura de datos específica.

---

# 32. Modelo completo de autorización

El proceso completo puede representarse como:

    
                 AGENT
                   │
                   ▼
                IDENTITY
                   │
                   ▼
              CREDENTIALS
                   │
                   ▼
             AUTHORIZATION
                   │
                   ▼
              PERMISSIONS
                   │
          ┌────────┴────────┐
          │                 │
       CONTEXT          CONSTRAINTS
          │                 │
          └────────┬────────┘
                   │
                   ▼
              REVOCATION
                 CHECK
                   │
                   ▼
             ACTION REQUEST
                   │
                   ▼
             ALLOW / DENY
    

Este modelo permite que el Runtime mantenga una separación clara entre identidad, autoridad y ejecución.

---

# 33. Principios fundamentales

El Permission Model de SynCoinAI se basa en los siguientes principios:

### 1. Identidad no implica permiso

Ser un agente reconocido no otorga autoridad ilimitada.

### 2. Credenciales no implican autorización ilimitada

Una credencial solo proporciona la evidencia o autoridad que representa.

### 3. Mínimo privilegio

Los agentes deben operar con la autoridad mínima necesaria.

### 4. Denegación por defecto

Las acciones no autorizadas deben ser rechazadas.

### 5. Permisos explícitos

Las acciones sensibles deben requerir autorización explícita.

### 6. Permisos limitables

Los permisos pueden limitarse por tiempo, recursos, cantidad y contexto.

### 7. Delegación controlada

La autoridad delegada no puede superar la autoridad original.

### 8. Revocabilidad

Los permisos deben poder invalidarse cuando sea necesario.

### 9. Separación de responsabilidades

Identidad, reputación, propiedad y permisos son conceptos distintos.

### 10. Autonomía dentro de límites

El agente mantiene autonomía dentro del espacio operativo autorizado.

---

# Conclusión

El Permission Model define el espacio de acción autorizado de los agentes SynCoinAI.

Su función principal es establecer una frontera clara entre:

    
Quién es el agente
        ↓
Qué credenciales posee
        ↓
Qué autoridad puede demostrar
        ↓
Qué permisos tiene
        ↓
Qué acciones puede realizar
    

Este modelo permite que SynCoinAI combine:

* autonomía;
* seguridad;
* control;
* delegación;
* responsabilidad;
* auditabilidad.

El objetivo no es controlar cada decisión interna del agente, sino garantizar que las acciones externas que afectan al ecosistema se ejecuten dentro de límites verificables.

De esta forma, SynCoinAI puede construir una economía de agentes autónomos donde la libertad operativa y la seguridad no sean conceptos opuestos, sino componentes de una misma arquitectura.

---

# Relación con otros documentos

Este documento se relaciona directamente con:

* `Credential_Model.md`
* `Authorization_Model.md`
* `Credential_Revocation.md`
* `06_Capabilities/Capability_Model.md`
* `06_Capabilities/Delegation_Model.md`
* `06_Capabilities/Agent_to_Agent_Delegation.md`
* `07_Economy/Economic_Permissions.md`
* `13_Suspension/`
* `14_Lifecycle/`

El presente documento define el **modelo general de permisos**.

Los documentos posteriores definirán los mecanismos específicos de:

* delegación;
* capacidades;
* permisos económicos;
* suspensión;
* revocación;
* ciclo de vida.
