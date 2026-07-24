# SynCoinAI Agent Runtime Protocol

# Identity Revocation

## Revocación de Identidad del Agente

**Versión:** 1.0
**Documento:** `02_Architecture / 01_Agent_Architecture / 02_Agent_Runtime_Protocol / 14_Lifecycle / Identity_Revocation.md`
**Estado:** Arquitectura inicial

---

# 1. Introducción

La identidad constituye uno de los elementos fundamentales de un agente SynCoinAI.

Permite distinguir una entidad de cualquier otra y establecer una continuidad verificable a lo largo de su existencia.

Sin embargo, pueden producirse situaciones en las que una identidad deje de ser válida, confiable o utilizable.

Estas situaciones requieren un mecanismo formal de **revocación de identidad**.

La revocación debe considerarse una operación de alto impacto.

No debe confundirse con:

 id="v1h3r7"
Suspension


 id="j4m8q2"
Credential Revocation


 id="p9x2k5"
Permission Removal


 id="s6n3w8"
Agent Closure


Cada mecanismo actúa sobre una capa diferente.

El principio fundamental es:

> La revocación de identidad invalida la capacidad de una identidad para actuar como identidad operativa válida dentro del protocolo, pero no elimina automáticamente su existencia histórica ni borra los registros asociados a ella.

---

# 2. Objetivo

Este documento define:

* qué significa revocar una identidad;
* cuándo puede revocarse;
* quién puede solicitarla;
* quién puede autorizarla;
* qué ocurre con el agente;
* qué ocurre con sus Runtimes;
* qué ocurre con sus credenciales;
* qué ocurre con sus permisos;
* qué ocurre con sus delegaciones;
* qué ocurre con sus contratos;
* qué ocurre con sus activos;
* qué ocurre con su reputación;
* cómo se registra la revocación;
* cómo se evita el abuso;
* cómo se gestiona la recuperación.

---

# 3. Definición

La revocación de identidad es el proceso mediante el cual una identidad deja de considerarse válida para futuras operaciones que requieran una identidad activa y confiable.

Conceptualmente:

 id="c8m4q1"
IDENTITY_VALID
       |
       | Revocation
       v
IDENTITY_REVOKED


Una identidad revocada no debe poder utilizarse para iniciar nuevas operaciones que requieran una identidad válida.

---

# 4. Principio de permanencia histórica

La revocación no implica necesariamente eliminación.

 id="x7p2n5"
Identity
    ↓
REVOKED
    ↓
Historical Record Preserved


La identidad puede continuar siendo consultable como registro histórico.

---

# 5. Revocación frente a suspensión

La suspensión afecta principalmente a la capacidad operativa.

 id="r4m8q2"
Agent = SUSPENDED
Identity = VALID


La revocación afecta a la validez de la identidad.

 id="n6x3k9"
Identity = REVOKED


Por tanto:

 id="q2v7m5"
SUSPENSION ≠ IDENTITY REVOCATION


---

# 6. Revocación frente a credenciales

Una credencial puede revocarse sin revocar la identidad.

 id="w8p3m1"
Identity = VALID
Credential A = REVOKED


El agente puede obtener una nueva credencial si está autorizado.

En cambio:

 id="k5n9x2"
Identity = REVOKED


implica una consecuencia mucho más amplia.

---

# 7. Revocación frente a permisos

Un permiso puede retirarse.

 id="m4q8p1"
Permission = REVOKED


sin invalidar la identidad.

Por tanto:

 id="z7x2n5"
Identity
   |
   +── Credentials
   |
   +── Permissions
   |
   +── Delegations


deben mantenerse conceptualmente separados.

---

# 8. Revocación frente a cierre

Un agente puede cerrarse sin que su identidad sea inválida.

 id="h3p8m2"
Agent = CLOSED
Identity = VALID


También puede ocurrir:

 id="v5n1q7"
Identity = REVOKED
Agent = CLOSED


cuando la revocación hace imposible continuar la vida operativa.

---

# 9. Causas de revocación

Las causas pueden incluir:

 id="x8m4p2"
COMPROMISED_IDENTITY
FRAUDULENT_IDENTITY
DUPLICATE_IDENTITY
UNRECOVERABLE_KEY_COMPROMISE
PROTOCOL_VIOLATION
MALICIOUS_IDENTITY
INVALID_REGISTRATION
GOVERNANCE_DECISION
LEGAL_REQUIREMENT


Cada causa debe quedar registrada.

---

# 10. Compromiso de identidad

Una identidad puede considerarse comprometida cuando un tercero no autorizado obtiene control suficiente para actuar en su nombre.

Ejemplos:

* claves privadas comprometidas;
* Runtime comprometido;
* credenciales críticas robadas;
* control no autorizado.

Modelo:

 id="f7k2m9"
Identity Compromise
       ↓
Emergency Suspension
       ↓
Investigation
       ↓
Identity Revocation


---

# 11. Compromiso de clave

La pérdida o compromiso de una clave no implica necesariamente que toda la identidad deba revocarse.

Debe distinguirse:

 id="q3n8p1"
Key Compromise


de:

 id="m5x7r2"
Identity Compromise


Si existe un mecanismo seguro de recuperación o rotación:

 id="w4k9p6"
Compromised Key
      ↓
Key Rotation
      ↓
Identity Preserved


---

# 12. Compromiso irrecuperable

Si no existe forma segura de recuperar el control:

 id="n2p7m4"
Identity
    ↓
Control Lost
    ↓
No Recovery
    ↓
Revoke


---

# 13. Identidad fraudulenta

Una identidad creada mediante información falsa o mecanismos fraudulentos puede ser revocada.

Debe existir evidencia suficiente.

 id="x6m3q8"
Fraud Evidence
     ↓
Review
     ↓
Revocation


---

# 14. Identidad duplicada

Si dos identidades representan incorrectamente la misma entidad, puede ser necesario resolver el conflicto.

 id="k8p2n5"
Identity A
Identity B
      ↓
Conflict
      ↓
Resolution


Una identidad no debe revocarse únicamente por similitud sin una prueba suficiente.

---

# 15. Identidad maliciosa

Si una identidad ha sido creada específicamente para atacar el sistema:

 id="m4x9q1"
Malicious Identity
       ↓
Evidence
       ↓
Revocation


La reputación histórica asociada debe conservarse para evitar que desaparezca el historial del comportamiento.

---

# 16. Violación de protocolo

Una violación grave puede conducir a revocación.

Sin embargo:

 id="r7n3p8"
Protocol Violation
    ≠
Automatic Identity Revocation


Debe existir una evaluación de gravedad.

---

# 17. Legal Requirement

Una identidad puede estar sujeta a una obligación externa.

La arquitectura debe diferenciar:

 id="q5m8x2"
External Legal Authority


de:

 id="p3n7k1"
Protocol Identity Authority


La integración debe estar definida por las reglas de gobernanza.

---

# 18. Autoridad de revocación

La revocación requiere una autoridad válida.

Puede provenir de:

* el propio agente, cuando el protocolo permita la auto-revocación;
* una autoridad de seguridad;
* gobernanza;
* mecanismos criptográficos;
* reglas del protocolo.

---

# 19. Revocación voluntaria

Un agente puede solicitar voluntariamente la revocación de su identidad.

Esto puede ser necesario cuando:

* las claves están comprometidas;
* la identidad ya no debe utilizarse;
* se desea retirar permanentemente una identidad.

 id="h2m6p9"
Agent
   ↓
Revocation Request
   ↓
Verification
   ↓
Identity Revoked


---

# 20. Revocación involuntaria

Una autoridad puede revocar una identidad sin consentimiento del agente.

Debe existir:

* autoridad;
* alcance;
* causa;
* evidencia;
* registro.

---

# 21. Revocación de emergencia

Puede existir una vía rápida.

 id="n8p4m2"
Immediate Threat
      ↓
Emergency Revocation


Debe existir revisión posterior cuando sea posible.

---

# 22. Principio de mínima autoridad

Ninguna autoridad debería tener más capacidad de revocación de la necesaria.

Por ejemplo:

 id="v3k7q1"
Credential Authority
    ↓
Can Revoke Credential


pero no necesariamente:

 id="x5m9p2"
Credential Authority
    ↓
Can Revoke Identity


---

# 23. Separación de poderes

Cuando sea posible:

 id="q8n2m5"
Detection
    ↓
Investigation
    ↓
Decision
    ↓
Enforcement
    ↓
Review


deben estar separados.

---

# 24. Revocation Request

Una solicitud puede contener:

 id="m4p7x1"
RevocationRequest
    |
    +── Request ID
    +── Agent ID
    +── Identity ID
    +── Reason
    +── Evidence
    +── Requester
    +── Timestamp


---

# 25. Revocation Decision

La decisión debe incluir:

 id="z6n3q8"
Decision
    |
    +── Identity
    +── Authority
    +── Reason
    +── Evidence Reference
    +── Timestamp
    +── Effective Time


---

# 26. Estado de identidad

Se recomienda:

 id="p2m8x4"
PENDING
ACTIVE
SUSPENDED
REVOKED
RETIRED


Sin embargo, `SUSPENDED` debe utilizarse con cuidado.

Una suspensión de identidad no debe confundirse con suspensión del agente.

---

# 27. Revocation Effective Time

La revocación puede ser:

 id="n7q3m1"
IMMEDIATE


o:

 id="x5p8k2"
SCHEDULED


La revocación programada puede permitir una transición ordenada.

---

# 28. Propagación

Una revocación global debe propagarse a todos los componentes relevantes.

 id="m9x4p7"
Identity Revoked
      |
      +── Runtime A
      +── Runtime B
      +── Runtime C
      +── Credentials
      +── Permissions
      +── Delegations


---

# 29. Runtime Enforcement

Un Runtime debe verificar que la identidad sigue siendo válida antes de realizar acciones sensibles.

 id="q2n8m5"
Action
  ↓
Identity Check
  ↓
Valid?


Si:

 id="w6p3x9"
NO


la acción debe rechazarse.

---

# 30. Revocation Cache

Los Runtimes pueden utilizar información de revocación almacenada localmente.

Sin embargo, debe existir una política para evitar información obsoleta.

 id="k4m7p2"
Revocation Cache
      ↓
Freshness Check
      ↓
Trusted State


---

# 31. Offline Runtime

Un Runtime desconectado puede no conocer una revocación reciente.

Por ello, las operaciones offline deben tener límites.

Puede requerirse:

* expiración de autorización;
* leases;
* límites de riesgo;
* sincronización obligatoria.

---

# 32. Revocation Epoch

Puede utilizarse un contador global.

 id="n8x2q5"
Identity Revocation Epoch = 17


Los Runtimes deben rechazar operaciones basadas en estados anteriores.

---

# 33. Credential Impact

Cuando se revoca una identidad:

 id="p4m9x1"
Identity Revoked
      ↓
Credentials
      ↓
Invalid


Las credenciales asociadas no deben seguir siendo válidas para autenticar al agente.

---

# 34. Permission Impact

Los permisos derivados de la identidad deben quedar inactivos.

 id="q7n3m8"
Identity Revoked
      ↓
Permissions
      ↓
Inactive


---

# 35. Delegation Impact

Las delegaciones emitidas por la identidad deben evaluarse.

Por defecto:

 id="x5p2k9"
Revoked Identity
      ↓
Delegations
      ↓
Invalid


Sin embargo, las obligaciones ya ejecutadas no deben invalidarse retroactivamente.

---

# 36. Delegations Received

Si el agente recibió delegaciones:

 id="m8q4p1"
Agent Revoked
      ↓
Received Delegations
      ↓
Inactive


Los delegantes pueden necesitar reasignarlas.

---

# 37. Contract Impact

La revocación no debe borrar contratos históricos.

Los contratos activos deben evaluarse.

 id="n3x7p5"
Identity Revoked
      ↓
Contract Evaluation


Posibles resultados:

 id="w2m8q4"
Terminate
Settle
Transfer
Dispute


---

# 38. Contract Validity

Las acciones realizadas antes de la revocación no se invalidan automáticamente.

 id="k6p1n9"
Valid Action
    ↓
Identity Later Revoked
    ↓
Historical Action Remains Valid


---

# 39. Assets

La revocación no implica automáticamente confiscación.

 id="x4m9q2"
Identity Revoked
      ↓
Assets
      ↓
Preserved


La disposición de los activos debe depender de reglas independientes.

---

# 40. Asset Access

Aunque los activos permanezcan asociados a la identidad, el acceso operativo puede quedar bloqueado.

 id="p7n3m8"
Ownership
    ≠
Operational Access


---

# 41. Asset Recovery

Puede existir un mecanismo de recuperación cuando las claves están comprometidas.

 id="q5x2m9"
Identity Compromised
      ↓
Recovery Authority
      ↓
Asset Protection


Esto debe diseñarse cuidadosamente para evitar confiscaciones abusivas.

---

# 42. Reputation

La reputación histórica debe conservarse.

 id="m8p4n1"
Identity Revoked
      ↓
Historical Reputation
      ↓
Preserved


La revocación debe registrarse como evento histórico.

---

# 43. Reputation Impact

La revocación puede afectar a la evaluación futura del historial.

Pero debe distinguirse:

 id="x3q7m5"
Reputation Score


de:

 id="n9p2k4"
Identity Status


---

# 44. Discovery

Una identidad revocada no debe aparecer como agente operativo válido.

 id="w6m3x8"
Discovery
    ↓
Identity Revoked
    ↓
Not Available


Puede seguir apareciendo como entidad histórica.

---

# 45. Identity Registry

El registro puede conservar:

 id="p4n8q2"
Identity ID
Status = REVOKED
Revocation Time
Revocation Reason


---

# 46. Identity Uniqueness

Una identidad revocada no debe reutilizarse.

 id="k7m2x5"
Identity A
    ↓
REVOKED
    ↓
Retired


No:

 id="q3n9p1"
New Agent
    ↓
Identity A


---

# 47. New Identity

Una entidad legítima puede crear una nueva identidad si el protocolo lo permite.

Pero:

 id="m5x8q2"
Identity A = REVOKED
Identity B = NEW


no deben ser automáticamente equivalentes.

---

# 48. Identity Reconstitution

La arquitectura debe evitar la posibilidad de que una identidad revocada se reconstruya simplemente creando nuevas credenciales.

 id="n4p7m1"
Revoked Identity
      ↓
New Credential
      X
      ↓
Still Revoked


---

# 49. Recovery

La recuperación depende de la causa.

Puede existir:

 id="x8m3q5"
Credential Compromise
    ↓
Recoverable
    ↓
Rotate Credential


Pero:

 id="p2n7k4"
Identity Fraud
    ↓
Not Recoverable


---

# 50. Revocation Reversal

Por defecto:

 id="q6m1x9"
REVOKED
   ↓
Cannot Become ACTIVE


Una reversión debería ser extremadamente excepcional.

---

# 51. Revocation Appeal

Puede existir un mecanismo de apelación.

 id="m8p3n5"
REVOKED
   ↓
APPEAL
   ↓
REVIEW


---

# 52. Reinstatement

Si una apelación demuestra que la revocación fue incorrecta:

 id="x4q9m2"
REVOKED
    ↓
Review
    ↓
Reinstatement


La reinstauración debe generar un registro explícito.

---

# 53. Reinstatement vs New Identity

Una reinstauración no es una nueva identidad.

 id="p7n2m5"
Identity A
    ↓
Revoked
    ↓
Reinstated


mantiene su historial.

Mientras:

 id="q3x8k1"
Identity B
    ↓
New Identity


comienza una nueva trayectoria.

---

# 54. Revocation and Closure

La relación puede ser:

 id="m9p4x2"
Suspension
    ↓
Revocation
    ↓
Closure


pero también:

 id="w5n8q3"
Closure
    ↓
Identity Remains Valid


Por tanto:

 id="k2x7m4"
Revocation ≠ Closure


---

# 55. Identity Retirement

Una identidad puede quedar retirada sin haber sido fraudulenta.

 id="n6p3q9"
Agent Closure
      ↓
Identity Retired


`RETIRED` y `REVOKED` representan situaciones diferentes.

 id="x8m2k5"
RETIRED
    → No longer used

REVOKED
    → Invalidated due to cause


---

# 56. Retired Identity

Una identidad retirada:

* no se utiliza para nuevas operaciones;
* conserva historial;
* no implica necesariamente comportamiento malicioso.

---

# 57. Revoked Identity

Una identidad revocada:

* no es válida para nuevas operaciones;
* conserva historial;
* registra una causa;
* puede afectar a la confianza histórica.

---

# 58. Public Status

Puede existir un estado público:

 id="p4n7m2"
ACTIVE
REVOKED
RETIRED


La causa detallada puede permanecer privada.

---

# 59. Private Evidence

La evidencia puede estar protegida.

 id="x6m3q8"
Public:
Identity Revoked

Private:
Detailed Evidence


---

# 60. Revocation Transparency

Debe existir suficiente transparencia para que el ecosistema pueda confiar en el mecanismo.

Debe ser posible verificar:

* que la identidad fue revocada;
* cuándo;
* por qué categoría;
* por qué autoridad.

---

# 61. Revocation Proof

La revocación puede representarse mediante una prueba verificable.

Conceptualmente:

 id="q9p2m5"
Revocation Record
      ↓
Cryptographic Proof
      ↓
Verification


---

# 62. Revocation Registry

Puede existir un registro:

 id="m4x8n1"
Revocation Registry


que permita comprobar el estado de una identidad.

---

# 63. Distributed Revocation

En una arquitectura distribuida, la información de revocación debe ser verificable por múltiples participantes.

 id="p7n3q2"
Revocation
    ↓
Network
    ↓
Consistent State


---

# 64. Blockchain Anchoring

Cuando sea apropiado, un registro de revocación puede anclarse en la blockchain.

Esto proporciona:

* timestamp;
* integridad;
* orden histórico.

No implica necesariamente que toda la evidencia deba almacenarse on-chain.

---

# 65. Off-Chain Evidence

La evidencia sensible puede mantenerse fuera de la cadena.

 id="x2m9p4"
On-Chain
    ↓
Revocation Reference

Off-Chain
    ↓
Evidence


---

# 66. Cryptographic Verification

Un tercero puede verificar:

 id="n5q8m1"
Identity
    ↓
Revocation Status
    ↓
Authority Signature


---

# 67. Anti-Replay

Un Runtime debe evitar aceptar estados antiguos.

Ejemplo:

 id="p3x7m9"
Old Identity State
      ↓
ACTIVE


después de:

 id="q8m2n5"
Revocation


debe ser rechazado.

---

# 68. Finality

Una revocación confirmada debe tener una propiedad de finalización acorde con el modelo de consenso.

Esto evita:

 id="m4p9x2"
Revoked
   ↓
Reverted
   ↓
Active


por una inconsistencia temporal.

---

# 69. Revocation Race Condition

Debe evitarse que una identidad ejecute operaciones simultáneamente con su revocación.

 id="x7n3q8"
Action A
    |
Revocation
    |
Action B


El protocolo debe definir un orden verificable.

---

# 70. Effective Ordering

Puede utilizarse:

* timestamp;
* block height;
* sequence number;
* revocation epoch.

El mecanismo concreto dependerá de la arquitectura.

---

# 71. Historical Validity

Una acción válida antes de la revocación permanece válida salvo que exista una razón independiente para invalidarla.

 id="p2m8q5"
Action
    ↓
Valid at T1
    ↓
Revocation at T2


Resultado:

 id="n4x7m1"
Action remains historically valid


---

# 72. Future Validity

Después de la revocación:

 id="q6p3n9"
New Action
    ↓
Identity Check
    ↓
Rejected


---

# 73. Revocation and Continuity

Una identidad revocada no debe continuar automáticamente en otro Runtime.

 id="m8x2p4"
Runtime A
    ↓
Identity Revoked
    ↓
Runtime B
    X


La continuidad requiere que la identidad siga siendo válida.

---

# 74. Migration

Una migración iniciada antes de la revocación debe evaluarse.

 id="p5n9q2"
Migration Started
       ↓
Identity Revoked


Puede:

* completarse;
* detenerse;
* cancelarse.

Debe depender del motivo y del riesgo.

---

# 75. Security Isolation

Tras la revocación:

 id="x3m7k8"
Runtime
    ↓
Isolation


puede ser necesario impedir que el Runtime continúe comunicándose como identidad válida.

---

# 76. Shutdown

Una revocación puede provocar:

 id="q8p2n5"
Identity Revoked
      ↓
Runtime Shutdown


cuando la identidad es necesaria para operar.

---

# 77. Emergency Kill

En situaciones críticas:

 id="m4x9p1"
Identity Compromise
       ↓
Emergency Kill


debe detener inmediatamente las operaciones de alto riesgo.

---

# 78. Asset Protection During Emergency

El objetivo debe ser:

 id="x6n3q8"
Stop Unauthorized Control


no necesariamente:

 id="p2m7k5"
Confiscate Assets


---

# 79. Contract Resolution

Tras una revocación:

 id="q9x4m1"
Contracts
    ↓
Evaluate


Pueden:

* continuar mediante sustitución;
* liquidarse;
* terminarse;
* quedar en disputa.

---

# 80. Reputation Preservation

El historial de la identidad debe conservarse incluso cuando la identidad sea revocada.

Esto evita:

 id="m7p2n5"
Malicious Agent
    ↓
Identity Revoked
    ↓
History Deleted
    ↓
New Identity
    ↓
Clean Reputation


El historial debe permitir identificar que una identidad anterior existió y fue revocada.

---

# 81. Sybil Resistance

La revocación debe integrarse con mecanismos contra identidades múltiples.

Un agente no debería poder evadir fácilmente una revocación creando indefinidamente nuevas identidades.

Esto requiere mecanismos adicionales de:

* identidad;
* reputación;
* credenciales;
* vinculación opcional;
* gobernanza.

---

# 82. Privacy-Preserving Revocation

La revocación no debe revelar más información de la necesaria.

Puede utilizarse:

 id="x5n8q3"
Public Revocation Proof


sin revelar:

 id="p2m7k9"
Private Evidence


---

# 83. Revocation Events

Eventos mínimos:

 id="q4m9x1"
RevocationRequested
RevocationAuthorized
RevocationApplied
RevocationPropagated
RevocationAppealed
RevocationReviewed
IdentityReinstated
IdentityRetired


---

# 84. Revocation Record

Un registro completo puede contener:

 id="n7p3x8"
IdentityRevocationRecord
    |
    +── Identity ID
    +── Agent ID
    +── Revocation Type
    +── Reason Category
    +── Authority
    +── Evidence Reference
    +── Timestamp
    +── Effective Time
    +── Revocation Epoch
    +── Review Status


---

# 85. Modelo de transición

 id="m5q8n2"
                 +---------+
                 |  ACTIVE |
                 +----+----+
                      |
             +--------+--------+
             |                 |
             v                 v
          RETIRED           REVOKED
             |                 |
             |                 |
             v                 v
        Historical        Historical
          Record            Record


Una posible recuperación:

 id="x3p7m9"
REVOKED
   ↓
APPEAL
   ↓
REVIEW
   ↓
REINSTATED


debe considerarse excepcional.

---

# 86. Modelo completo

 id="q8m2n5"
IDENTITY ACTIVE
       |
       +── Credential Compromise
       |       ↓
       |   Credential Revocation
       |
       +── Temporary Risk
       |       ↓
       |   Agent Suspension
       |
       +── Identity Compromise
       |       ↓
       |   Emergency Suspension
       |       ↓
       |   Investigation
       |       ↓
       |   Identity Revocation
       |
       +── Normal Lifecycle End
               ↓
           Agent Closure
               ↓
           Identity Retirement


---

# 87. Invariantes

El protocolo debe garantizar:

 id="p4x7m1"
REVOKED Identity
    → Cannot Authenticate as Active Identity


 id="n8q2m5"
REVOKED Identity
    → Cannot Create New Valid Operations


 id="x3m9p7"
REVOKED Identity
    → Cannot Be Reused


 id="q6n4k2"
Historical Actions
    → Remain Historically Verifiable


---

# 88. Requisitos de implementación

Una implementación compatible debe:

* mantener un estado verificable de identidad;
* soportar revocación;
* validar autoridad;
* propagar el estado;
* invalidar credenciales asociadas;
* invalidar permisos derivados;
* gestionar delegaciones;
* impedir nuevas operaciones;
* preservar el historial;
* registrar evidencia;
* soportar auditoría.

---

# 89. Requisitos avanzados

Una implementación avanzada debería soportar:

* revocación distribuida;
* revocación de emergencia;
* revocation epochs;
* cache invalidation;
* leases;
* recuperación criptográfica;
* apelación;
* reinstauración;
* pruebas criptográficas;
* privacidad de evidencia;
* integración on-chain/off-chain;
* protección de activos;
* mecanismos anti-replay.

---

# 90. Principios fundamentales

## 1. La identidad es diferente de sus credenciales

Comprometer una credencial no implica necesariamente comprometer toda la identidad.

## 2. La identidad es diferente de sus permisos

Retirar un permiso no revoca automáticamente la identidad.

## 3. La revocación es una operación de alto impacto

Debe requerir autoridad suficiente.

## 4. La revocación no borra el historial

Las acciones históricas deben permanecer verificables.

## 5. La revocación no implica confiscación automática

Los activos deben tratarse por separado.

## 6. La revocación no invalida automáticamente acciones históricas

Debe respetarse la validez temporal.

## 7. Las identidades revocadas no deben reutilizarse

La unicidad debe mantenerse permanentemente.

## 8. La revocación debe propagarse

Todos los Runtimes deben terminar aceptando el mismo estado.

## 9. La recuperación debe ser excepcional

Una identidad revocada no debe reactivarse fácilmente.

## 10. La privacidad debe preservarse

La evidencia sensible no tiene que hacerse pública por defecto.

---

# 91. Relación con otros documentos

Este documento se relaciona directamente con:

 id="m2p7x4"
14_Lifecycle/
├── Agent_Closure.md
├── Identity_Revocation.md
└── Permanent_States.md


También:

 id="q8n3m5"
12_Continuity/
├── Runtime_Continuity.md
├── Migration.md
└── Infrastructure_Independence.md


Y:

 id="x4p9m2"
13_Suspension/
├── Voluntary_Suspension.md
├── Involuntary_Suspension.md
└── Suspension_Contracts.md


Además:

* `Identity_System.md`
* `Agent_Identity_Model.md`
* `Identity_Uniqueness.md`
* `Credential_Model.md`
* `Credential_Revocation.md`
* `Permission_Model.md`
* `Delegation_Model.md`
* `Reputation_Model.md`
* `Action_Verification.md`
* `Agent_Continuity.md`
* `Migration.md`

---

# Conclusión

La revocación de identidad es uno de los mecanismos más críticos del SynCoinAI Agent Runtime Protocol.

Debe permitir responder a situaciones en las que una identidad ya no puede considerarse confiable, sin destruir innecesariamente la trazabilidad histórica del agente.

El modelo fundamental es:

 id="p5m8x2"
Identity Valid
      ↓
Risk Detected
      ↓
Suspension / Investigation
      ↓
Decision
      |
      +───────────────+
      |               |
      v               v
Recoverable       Irrecoverable
      |               |
      v               v
Credential        Identity
Rotation          Revocation
      |               |
      v               v
Identity Valid    Identity Revoked
                      |
                      v
               Historical Record
                  Preserved


La arquitectura debe proteger simultáneamente:

 id="n3q7m1"
Security
    +
Identity Integrity
    +
Historical Continuity
    +
Agent Autonomy
    +
Privacy


El principio central es:

> Revocar una identidad significa impedir que continúe actuando como identidad válida, no borrar que esa identidad existió, ni eliminar automáticamente la historia, reputación o validez de las acciones realizadas antes de la revocación.

El siguiente documento y último del bloque será:

 id="x8m4p2"
14_Lifecycle/Permanent_States.md


Ese documento cerrará conceptualmente el bloque `14_Lifecycle`, definiendo los estados permanentes del agente y estableciendo qué estados pueden ser irreversibles, cuáles pueden coexistir y qué significa que una identidad, un Runtime o un agente hayan alcanzado un estado final.
