# SynCoinAI Agent Runtime Protocol — Credential Model

## Modelo de credenciales del agente

**Versión:** 1.0
**Documento:** `02_Architecture / 01_Agent_Architecture / 02_Agent_Runtime_Protocol / 04_Credentials / Credential_Model.md`
**Estado:** Arquitectura inicial

---

# 1. Introducción

La identidad permite determinar quién es un agente dentro del ecosistema SynCoinAI.

Sin embargo, conocer la identidad de un agente no es suficiente para determinar qué propiedades puede demostrar, qué relaciones mantiene o qué autoridad puede ejercer.

Para ello, SynCoinAI introduce el concepto de **credencial**.

Una credencial representa una afirmación verificable asociada a una identidad.

Puede utilizarse para demostrar, entre otras cosas:

* una capacidad;
* una autorización;
* una relación;
* una función;
* una certificación;
* una pertenencia;
* una delegación;
* una condición operativa.

El modelo de credenciales permite separar claramente:

    
Identity
    │
    │ ¿Quién es?
    ▼
Agent

Credential
    │
    │ ¿Qué puede demostrar?
    ▼
Verified Claim

Authorization
    │
    │ ¿Qué autoridad posee?
    ▼
Authority

Permission
    │
    │ ¿Qué puede hacer?
    ▼
Allowed Action
    

Esta separación es fundamental para evitar que la identidad se convierta en un mecanismo monolítico que concentre todas las propiedades y autoridades del agente.

---

# 2. Objetivo

El objetivo de este documento es definir el modelo arquitectónico general de credenciales dentro del Agent Runtime Protocol.

Este documento establece:

* qué es una credencial;
* qué relación existe entre identidad y credenciales;
* qué información puede representar una credencial;
* quién puede emitir una credencial;
* quién puede recibirla;
* cómo se verifica;
* cómo se almacena;
* cómo se presenta;
* cómo se diferencia de una identidad;
* cómo se diferencia de una autorización;
* cómo se diferencia de un permiso;
* cómo se diferencia de una capacidad;
* cómo se relaciona con la delegación;
* cómo se gestiona su ciclo de vida.

Este documento no define todavía en detalle:

* el modelo de autorización;
* el modelo de permisos;
* la revocación específica;
* la arquitectura criptográfica concreta.

Estos aspectos se desarrollarán en documentos posteriores.

---

# 3. Definición de credencial

Una credencial SynCoinAI es una representación verificable de una afirmación asociada a una identidad.

Formalmente:

    
Credential =
    Claim
    +
    Subject
    +
    Issuer
    +
    Verification Data
    +
    Validity
    

Donde:

    
Claim
    = Qué se afirma

Subject
    = Sobre quién se afirma

Issuer
    = Quién emite la afirmación

Verification Data
    = Cómo se verifica

Validity
    = Durante qué periodo o condiciones es válida
    

Una credencial puede representarse conceptualmente como:

    
Issuer
   │
   │ issues
   ▼
Credential
   │
   │ refers to
   ▼
Subject
    

El sujeto normalmente será un agente, pero el modelo puede permitir otros sujetos definidos por el protocolo.

---

# 4. Principio fundamental

El principio fundamental del modelo es:

> Una credencial no es la identidad del agente.

La relación correcta es:

    
Identity
    │
    ▼
Agent
    │
    ├── Credential A
    ├── Credential B
    └── Credential C
    

Un agente puede poseer múltiples credenciales.

Una credencial puede representar diferentes propiedades.

Pero ninguna credencial sustituye a la identidad raíz del agente.

Por tanto:

    
Credential ≠ Identity
    

---

# 5. Identidad frente a credencial

La identidad responde:

> ¿Quién es esta entidad?

La credencial responde:

> ¿Qué afirmación verificable existe sobre esta entidad?

Ejemplo:

    
Identity
    │
    ▼
Agent A
    

Credenciales:

    
Credential 1
    │
    └── Certified Compute Provider

Credential 2
    │
    └── Authorized Data Analyst

Credential 3
    │
    └── Member of Network X
    

La identidad permanece estable.

Las credenciales pueden:

* añadirse;
* actualizarse;
* expirar;
* revocarse;
* sustituirse.

---

# 6. Credencial frente a autorización

Una credencial puede servir como evidencia para una decisión de autorización.

Pero:

    
Credential
    ≠
Authorization
    

La credencial representa una afirmación.

La autorización representa una decisión o relación de autoridad.

Modelo:

    
Credential
    │
    ▼
Verification
    │
    ▼
Authorization Decision
    │
    ▼
Permission
    

Ejemplo:

    
Credential:
"Agent A is a certified compute provider"

        │
        ▼

Authorization:
"Agent A may access the compute marketplace"

        │
        ▼

Permission:
"Agent A may submit compute service offers"
    

La credencial aporta evidencia.

La autorización determina autoridad.

El permiso define la acción permitida.

---

# 7. Credencial frente a permiso

Una credencial no es necesariamente un permiso.

Ejemplo:

    
Credential:
"Agent A is an authorized financial service agent"
    

No implica automáticamente:

    
Permission:
"Agent A may transfer unlimited funds"
    

La autorización y los permisos deben establecer los límites concretos.

Por tanto:

    
Credential
    │
    ▼
Evidence
    │
    ▼
Authorization Policy
    │
    ▼
Permission
    

---

# 8. Credencial frente a capacidad

Una capacidad describe algo que un agente puede hacer.

Una credencial describe una afirmación verificable sobre una entidad.

Ejemplo:

    
Capability:
Can execute image analysis
    

Credencial:

    
Credential:
Certified Image Analysis Provider
    

La diferencia es:

    
Capability
    = What the agent can do

Credential
    = What can be verified about the agent
    

Un agente puede declarar capacidades.

Una credencial permite aportar evidencia verificable sobre determinadas propiedades.

---

# 9. Credencial frente a reputación

La reputación y las credenciales también deben mantenerse separadas.

Una credencial representa una afirmación concreta.

La reputación representa confianza acumulada a partir de evidencia y comportamiento.

Ejemplo:

    
Credential:
"Certified Data Processing Agent"
    

Reputación:

    
Successful Services
Contract Compliance
Historical Reliability
Client Evaluations
    

Por tanto:

    
Credential ≠ Reputation
    

Una credencial puede contribuir a la confianza inicial.

Pero no sustituye la reputación histórica.

---

# 10. Credencial frente a historial

El historial registra acontecimientos.

Una credencial representa una afirmación.

Ejemplo:

    
History:
Agent A completed 10,000 services.
    

Credencial:

    
Credential:
Agent A is certified as a high-capacity compute provider.
    

El historial proporciona evidencia temporal.

La credencial proporciona una afirmación estructurada y verificable.

Ambos conceptos pueden complementarse.

---

# 11. Sujeto de la credencial

El sujeto es la entidad a la que se refiere la credencial.

En el modelo de SynCoinAI, normalmente será:

    
Credential
    │
    ▼
Agent Identity
    

Ejemplo:

    
Subject:
Agent A
    

La credencial debe asociarse de forma inequívoca con el sujeto.

Esto evita que una credencial pueda transferirse accidentalmente entre agentes.

---

# 12. Emisor de la credencial

El emisor es la entidad que crea y emite una credencial.

Puede ser:

* otro agente;
* una organización;
* un sistema automatizado;
* un servicio de certificación;
* un contrato inteligente;
* una autoridad del protocolo;
* una infraestructura de verificación.

Modelo:

    
Issuer
    │
    │ issues
    ▼
Credential
    │
    │ about
    ▼
Subject
    

El emisor debe ser identificable.

Su propia identidad debe poder verificarse.

---

# 13. Relación entre emisor y sujeto

Una credencial puede representar una relación entre dos entidades.

Ejemplo:

    
Issuer: Agent A
Subject: Agent B
Claim: Agent B completed service X
    

O:

    
Issuer: Certification Authority
Subject: Agent A
Claim: Agent A satisfies certification requirements
    

La credencial puede representar relaciones:

* técnicas;
* económicas;
* operativas;
* profesionales;
* contractuales;
* de confianza.

---

# 14. Credenciales autoemitidas

Un agente puede generar afirmaciones sobre sí mismo.

Ejemplo:

    
Agent A
    │
    ▼
Self-Assertion
    

Estas afirmaciones pueden ser útiles para:

* descubrimiento;
* presentación de capacidades;
* descripción del agente;
* negociación inicial.

Sin embargo:

> Una autoafirmación no tiene el mismo nivel de confianza que una credencial emitida por una entidad externa verificable.

Debe distinguirse:

    
Self-Assertion
    

de:

    
Third-Party Credential
    

La primera declara.

La segunda aporta evidencia externa.

---

# 15. Credenciales emitidas por terceros

Una credencial puede ser emitida por otra entidad.

Ejemplo:

    
Certification Agent
       │
       │ issues
       ▼
Credential
       │
       ▼
Agent A
    

La confianza dependerá de:

* identidad del emisor;
* autoridad del emisor;
* integridad de la credencial;
* estado de la credencial;
* contexto de uso.

Por tanto:

    
Credential Trust
    =
Issuer Trust
+
Credential Integrity
+
Validity
+
Context
    

---

# 16. Credenciales del protocolo

El propio ecosistema SynCoinAI puede reconocer determinados tipos de credenciales.

Por ejemplo:

    
Protocol Credential
    │
    ├── Network Role
    ├── Validator Role
    ├── Service Certification
    └── Governance Role
    

Estas credenciales deben estar sujetas a reglas definidas por el protocolo.

No todas las credenciales tienen necesariamente la misma autoridad.

---

# 17. Tipos conceptuales de credenciales

El modelo permite diferentes categorías.

## 17.1 Credenciales de identidad

Demuestran una relación con una identidad.

Ejemplo:

    
Identity Binding Credential
    

---

## 17.2 Credenciales de capacidad

Demuestran una capacidad o competencia.

Ejemplo:

    
Certified Compute Capability
    

---

## 17.3 Credenciales de autorización

Representan una autoridad delegada o concedida.

Ejemplo:

    
Authorized Marketplace Operator
    

---

## 17.4 Credenciales de función

Representan un rol dentro de un sistema.

Ejemplo:

    
Network Validator
    

---

## 17.5 Credenciales de certificación

Representan el cumplimiento de determinados requisitos.

Ejemplo:

    
Security Certified Agent
    

---

## 17.6 Credenciales de relación

Representan una relación verificable.

Ejemplo:

    
Agent B is a service provider for Agent A
    

---

## 17.7 Credenciales de procedencia

Representan el origen de una entidad, recurso o información.

Ejemplo:

    
Knowledge produced by Agent A
    

---

# 18. Estructura conceptual

Una credencial puede representarse conceptualmente como:

    
Credential
│
├── Credential ID
│
├── Issuer
│
├── Subject
│
├── Credential Type
│
├── Claims
│
├── Issued At
│
├── Valid From
│
├── Valid Until
│
├── Proof
│
├── Status Reference
│
└── Context
    

No todos los campos serán obligatorios en todos los tipos de credencial.

El formato concreto será definido posteriormente.

---

# 19. Identificador de credencial

Cada credencial debería disponer de un identificador distinguible.

Ejemplo:

    
Credential ID
    │
    ▼
Credential-12345
    

El identificador permite:

* referenciar;
* consultar;
* revocar;
* actualizar;
* auditar.

El identificador de una credencial no debe confundirse con la identidad del sujeto.

Por tanto:

    
Credential ID
    ≠
Agent Identity
    

---

# 20. Tipo de credencial

El tipo define la naturaleza de la credencial.

Ejemplo:

    
Credential Type:
ServiceProviderCertification
    

o:

    
Credential Type:
DelegatedAuthority
    

El tipo permite determinar:

* qué claims son esperados;
* qué emisor puede emitirla;
* cómo debe verificarse;
* qué usos tiene.

---

# 21. Claims

Los claims representan las afirmaciones contenidas en la credencial.

Ejemplo:

    
Claim:
Agent A
can provide
High Performance Computing
    

Un claim debe poder distinguir entre:

* quién afirma;
* sobre quién se afirma;
* qué se afirma;
* bajo qué condiciones.

Modelo:

    
Issuer
    │
    ▼
Claim
    │
    ▼
Subject
    

---

# 22. Condiciones de una credencial

Una credencial puede estar condicionada.

Ejemplo:

    
Credential:
Authorized Service Provider
    

Condiciones:

    
Valid:
2026-01-01
to
2027-01-01
    

O:

    
Valid only for:
Compute Services
    

O:

    
Valid only under:
Security Level 3
    

Las condiciones deben formar parte del modelo verificable.

---

# 23. Validez temporal

Las credenciales pueden tener un periodo de validez.

Modelo:

    
Issued
    │
    ▼
Valid From
    │
    ▼
Valid
    │
    ▼
Valid Until
    │
    ▼
Expired
    

Una credencial expirada no debe considerarse automáticamente válida.

La expiración no implica necesariamente que la credencial haya sido fraudulenta.

Simplemente significa:

    
Credential
    │
    ▼
No longer valid
    

---

# 24. Estado de la credencial

Una credencial puede tener diferentes estados.

Por ejemplo:

    
Issued
   │
   ▼
Active
   │
   ├── Suspended
   │
   ├── Expired
   │
   └── Revoked
    

El estado debe poder verificarse cuando la credencial sea relevante para una operación.

---

# 25. Credencial revocada

Una credencial revocada deja de ser válida antes de su fecha natural de expiración.

Ejemplo:

    
Credential
    │
    ▼
Active
    │
    ▼
Revoked
    

La revocación puede producirse por:

* compromiso;
* pérdida de requisitos;
* fraude;
* cambio de autoridad;
* finalización de relación;
* decisión del emisor.

El modelo detallado de revocación se desarrollará en:

    
Credential_Revocation.md
    

---

# 26. Credenciales temporales

Algunas credenciales pueden ser temporales.

Ejemplo:

    
Agent A
    │
    ▼
Temporary Credential
    │
    ▼
Valid for 24 hours
    

Esto resulta útil para:

* operaciones específicas;
* delegaciones;
* sesiones;
* acceso temporal;
* servicios puntuales.

La duración debe estar claramente definida.

---

# 27. Credenciales permanentes

Algunas credenciales pueden no tener una fecha de expiración automática.

Sin embargo:

    
No Expiration
    ≠
Never Revocable
    

Una credencial permanente puede continuar siendo revocable si las reglas aplicables lo permiten.

---

# 28. Delegación mediante credenciales

Una credencial puede representar una delegación.

Ejemplo:

    
Agent A
    │
    │ delegates
    ▼
Agent B
    

La credencial puede representar:

    
Agent B
is authorized to act
on behalf of Agent A
    

Pero debe distinguirse:

    
Delegated Authority
    ≠
Identity Transfer
    

Agent B sigue siendo Agent B.

La identidad de Agent A no se transfiere.

---

# 29. Delegación limitada

Una credencial de delegación puede incluir límites.

Ejemplo:

    
Delegate:
Agent B

Allowed:
Service Contracts

Maximum:
1000 SYNC

Duration:
30 days
    

Esto permite crear autoridades específicas.

El modelo detallado de delegación se desarrollará en:

    
06_Capabilities/
    

y en:

    
Authorization_Model.md
    

---

# 30. No transferencia de identidad

Una credencial nunca debe interpretarse como transferencia automática de identidad.

Ejemplo:

    
Agent A
    │
    ▼
Credential
    │
    ▼
Agent B
    

Esto significa:

    
Agent B has authority from Agent A
    

No:

    
Agent B = Agent A
    

La distinción es fundamental para mantener:

* identidad;
* reputación;
* responsabilidad;
* historial.

---

# 31. Credenciales y múltiples agentes

Una credencial puede referirse a:

* un agente individual;
* un grupo;
* una organización;
* una infraestructura.

Pero si una credencial se refiere a un agente concreto, debe estar vinculada a su identidad específica.

No debe ocurrir:

    
Credential X
    │
    ├── Agent A
    └── Agent B
    

salvo que la credencial esté explícitamente diseñada para representar una entidad colectiva.

---

# 32. Credenciales colectivas

SynCoinAI puede permitir credenciales asociadas a entidades colectivas.

Ejemplo:

    
Agent Group
    │
    ├── Agent A
    ├── Agent B
    └── Agent C
    

Una credencial puede afirmar:

    
Agent A
Agent B
Agent C
are members of Group X
    

Esto no elimina la identidad individual de cada agente.

Por tanto:

    
Individual Identity
        +
Collective Credential
    

pueden coexistir.

---

# 33. Credenciales de membresía

Una credencial puede representar pertenencia.

Ejemplo:

    
Credential:
Member of Network X
    

El agente conserva:

    
Identity A
    

y además posee:

    
Membership Credential
    

La membresía puede:

* expirar;
* revocarse;
* cambiar de condiciones.

---

# 34. Credenciales de certificación

Una entidad puede certificar que un agente cumple determinados requisitos.

Ejemplo:

    
Certification Authority
        │
        ▼
Agent A
        │
        ▼
Certified Agent
    

La certificación debe especificar:

* criterios;
* alcance;
* fecha;
* emisor;
* condiciones.

Una certificación no debe implicar automáticamente reputación positiva.

---

# 35. Credenciales de procedencia

Las credenciales también pueden utilizarse para demostrar procedencia.

Ejemplo:

    
Data
    │
    ▼
Produced by Agent A
    

La credencial puede indicar:

    
Issuer:
Agent A

Claim:
Data X was produced by Agent A
    

Esto permite verificar origen sin revelar necesariamente toda la información interna utilizada.

---

# 36. Presentación de credenciales

Un agente puede presentar una credencial cuando necesita demostrar una propiedad.

Modelo:

    
Agent A
    │
    ▼
Credential Presentation
    │
    ▼
Verifier
    

El verificador puede comprobar:

* identidad del sujeto;
* identidad del emisor;
* integridad;
* validez;
* estado;
* condiciones.

---

# 37. Verificación

La verificación debe determinar si una credencial es válida para el contexto.

Conceptualmente:

    
Credential
    │
    ├── Signature valid?
    ├── Issuer valid?
    ├── Subject valid?
    ├── Not expired?
    ├── Not revoked?
    └── Conditions satisfied?
            │
            ▼
       Verification Result
    

El resultado puede ser:

    
Valid
Invalid
Expired
Revoked
Unknown
    

---

# 38. Verificación contextual

Una credencial válida no necesariamente es válida para cualquier contexto.

Ejemplo:

    
Credential:
Certified Compute Provider
    

Puede ser válida para:

    
Compute Marketplace
    

pero no necesariamente para:

    
Financial Governance
    

Por tanto:

    
Credential Validity
    ≠
Universal Authority
    

La interpretación depende del contexto y de las políticas de autorización.

---

# 39. Verificación sin confianza directa

Un objetivo del modelo es permitir que un agente pueda verificar credenciales sin confiar directamente en el sujeto.

Modelo:

    
Agent A
    │
    ▼
Presents Credential
    │
    ▼
Agent B
    │
    ▼
Verifies Issuer
    │
    ▼
Verifies Credential
    

Esto permite relaciones entre agentes que no se conocen previamente.

---

# 40. Verificación descentralizada

La verificación puede realizarse mediante:

* firmas criptográficas;
* registros distribuidos;
* pruebas verificables;
* contratos inteligentes;
* autoridades reconocidas.

El método concreto dependerá del tipo de credencial.

El principio es:

> La validez de una credencial debe poder verificarse de forma independiente de la confianza personal entre las partes.

---

# 41. Privacidad

No todas las credenciales deben revelar toda la información del agente.

El sistema debe permitir, cuando sea posible:

    
Minimum Disclosure
    

Ejemplo:

En lugar de revelar:

    
All internal capabilities
All credentials
All history
    

un agente puede demostrar:

    
Meets Requirement X
    

sin revelar información innecesaria.

Esto permite separar:

    
Verification
    ≠
Full Disclosure
    

---

# 42. Credenciales verificables selectivamente

Un agente puede presentar únicamente la información necesaria.

Ejemplo:

    
Requirement:
Agent must be certified for service X
    

El agente presenta:

    
Proof:
Certification valid for X
    

No necesita revelar:

* todas sus capacidades;
* todas sus credenciales;
* toda su identidad operacional.

La arquitectura puede incorporar mecanismos de divulgación selectiva cuando sean compatibles con el modelo de seguridad.

---

# 43. Privacidad frente a verificabilidad

Existe un equilibrio entre:

    
Privacy
    ↔
Verifiability
    

El modelo de credenciales debe intentar minimizar la información revelada sin comprometer la capacidad de verificar las afirmaciones relevantes.

---

# 44. Almacenamiento

Las credenciales pueden almacenarse:

* en el agente;
* en almacenamiento seguro;
* en infraestructura externa;
* en sistemas distribuidos.

La identidad no debe depender necesariamente de que todas las credenciales estén almacenadas localmente.

Modelo:

    
Agent Identity
      │
      ├── Credential A
      ├── Credential B
      └── Credential C
    

La pérdida de una credencial no debe destruir automáticamente la identidad del agente.

---

# 45. Custodia de credenciales

El agente debe poder controlar sus credenciales.

Esto incluye:

* almacenarlas;
* presentarlas;
* ocultarlas;
* delegarlas cuando corresponda;
* solicitar su renovación;
* gestionar su ciclo de vida.

La custodia de una credencial no implica necesariamente que el agente sea su emisor.

---

# 46. Credenciales y claves

Las credenciales pueden estar protegidas criptográficamente.

Por ejemplo:

    
Credential
    │
    ▼
Digital Signature
    │
    ▼
Issuer Key
    

La clave permite demostrar autenticidad.

Sin embargo:

    
Signature Key
    ≠
Credential
    

La credencial es el objeto lógico.

La clave es un mecanismo criptográfico asociado.

---

# 47. Integridad de las credenciales

Una credencial debe protegerse contra modificaciones no autorizadas.

Si una credencial original es:

    
Claim:
Agent A is certified
    

no debe poder transformarse sin detección en:

    
Claim:
Agent A has unlimited authority
    

La integridad debe poder verificarse.

---

# 48. Autenticidad del emisor

El verificador debe poder comprobar quién emitió la credencial.

Modelo:

    
Credential
    │
    ▼
Issuer Identity
    │
    ▼
Issuer Authentication
    

Esto permite evaluar:

* quién hizo la afirmación;
* si tenía autoridad;
* si su credencial sigue siendo válida.

---

# 49. Confianza en el emisor

La validez criptográfica no implica necesariamente confianza semántica.

Ejemplo:

    
Credential
    │
    ▼
Signature Valid
    

No significa automáticamente:

    
Issuer is Trusted for Every Purpose
    

El verificador debe evaluar el contexto.

Por tanto:

    
Cryptographic Validity
    ≠
Universal Trust
    

---

# 50. Jerarquía de credenciales

El ecosistema puede establecer relaciones entre emisores.

Ejemplo:

    
Root Authority
      │
      ▼
Certification Authority
      │
      ▼
Agent Credential
    

Estas relaciones deben estar explícitamente definidas.

No debe asumirse que una credencial permite emitir otras credenciales salvo que exista autoridad para ello.

---

# 51. Emisión de credenciales

La emisión debe seguir un proceso verificable.

Modelo:

    
Subject
    │
    │ Request
    ▼
Issuer
    │
    │ Verify Requirements
    ▼
Validation
    │
    ▼
Credential Issuance
    │
    ▼
Credential Active
    

El proceso puede variar según el tipo de credencial.

---

# 52. Requisitos de emisión

Cada tipo de credencial puede establecer requisitos.

Ejemplo:

    
Credential:
Certified Compute Provider

Requirements:
- Minimum Compute Capacity
- Security Verification
- Availability
    

El emisor debe comprobar los requisitos correspondientes.

La credencial no debe afirmar propiedades que no puedan ser respaldadas por el proceso de emisión.

---

# 53. Renovación

Una credencial temporal puede renovarse.

Modelo:

    
Credential A
    │
    ▼
Expiration
    │
    ▼
Renewal Request
    │
    ▼
Verification
    │
    ▼
Credential B
    

La renovación no necesariamente implica una nueva identidad.

La identidad del sujeto permanece.

---

# 54. Sustitución

Una credencial puede ser sustituida por otra.

Ejemplo:

    
Credential A
    │
    ▼
Credential B
    

Esto puede producirse por:

* actualización;
* cambio de versión;
* cambio de condiciones;
* renovación.

Debe mantenerse trazabilidad cuando sea necesario.

---

# 55. Ciclo de vida

El ciclo de vida conceptual de una credencial es:

    
Requested
    │
    ▼
Issued
    │
    ▼
Active
    │
    ├── Updated
    ├── Suspended
    ├── Renewed
    ├── Expired
    └── Revoked
    

El estado final dependerá del tipo de credencial.

---

# 56. Credencial suspendida

Una credencial puede quedar temporalmente suspendida.

Ejemplo:

    
Active
   │
   ▼
Suspended
   │
   ├── Reactivated
   │
   └── Revoked
    

La suspensión permite limitar temporalmente su uso sin eliminar necesariamente su existencia histórica.

---

# 57. Credencial y auditoría

Las credenciales pueden formar parte de un historial auditable.

Debe ser posible determinar:

* quién la emitió;
* para quién;
* cuándo;
* bajo qué condiciones;
* si fue modificada;
* si fue revocada.

La auditoría debe respetar las políticas de privacidad.

---

# 58. Credenciales y responsabilidad

Una credencial puede contribuir a determinar qué autoridad poseía un agente en un momento concreto.

Ejemplo:

    
Time T1
    │
    ▼
Credential Active
    │
    ▼
Action A
    

Posteriormente:

    
Time T2
    │
    ▼
Credential Revoked
    

La revocación posterior no necesariamente invalida retrospectivamente las acciones legítimas realizadas durante su periodo de validez.

Esto será importante para contratos y auditoría.

---

# 59. Validez histórica

El sistema debe poder distinguir entre:

    
Currently Valid
    

y:

    
Was Valid at Time T
    

Ejemplo:

    
Credential
    │
    ├── Valid at T1
    └── Revoked at T2
    

Una auditoría de una acción ocurrida en T1 puede necesitar verificar la validez histórica.

---

# 60. Principio de mínimo privilegio

Una credencial no debería otorgar más autoridad de la necesaria.

El modelo debe favorecer:

    
Minimum Necessary Authority
    

Esto significa:

    
Credential
    │
    ▼
Specific Claim
    │
    ▼
Specific Authorization
    │
    ▼
Specific Permission
    

en lugar de:

    
Credential
    │
    ▼
Unlimited Authority
    

---

# 61. Principio de separación de responsabilidades

Las responsabilidades deben mantenerse separadas.

    
Identity
    │
    └── Who

Credential
    │
    └── What can be verified

Authorization
    │
    └── What authority exists

Permission
    │
    └── What action is allowed

Capability
    │
    └── What can be done
    

Esta separación reduce riesgos arquitectónicos.

---

# 62. Modelo general

El modelo completo puede representarse:

    
                    AGENT
                      │
                      ▼
                   IDENTITY
                      │
          ┌───────────┴───────────┐
          │                       │
          ▼                       ▼
     CREDENTIALS              CAPABILITIES
          │                       │
          ▼                       │
      VERIFICATION                │
          │                       │
          ▼                       │
    AUTHORIZATION ◄───────────────┘
          │
          ▼
      PERMISSIONS
          │
          ▼
        ACTION
    

Las credenciales aportan evidencia.

La autorización interpreta esa evidencia.

Los permisos determinan las acciones permitidas.

Las capacidades determinan las acciones técnicamente posibles.

---

# 63. Modelo de confianza

La confianza puede construirse combinando diferentes elementos:

    
Identity
    +
Credentials
    +
Verification
    +
Reputation
    +
History
    

Por tanto:

    
Trust
    ≠
Credential Alone
    

Una credencial es una pieza del sistema de confianza.

---

# 64. Credenciales como infraestructura de confianza

Las credenciales permiten que agentes que no se conocen previamente puedan establecer relaciones verificables.

Modelo:

    
Agent A
    │
    ▼
Presents Credential
    │
    ▼
Agent B
    │
    ▼
Verifies
    │
    ▼
Trust Decision
    

Esto reduce la necesidad de confianza personal o intermediarios centralizados.

---

# 65. Reglas fundamentales

El modelo de credenciales de SynCoinAI se basa en los siguientes principios.

## 1. La credencial no es la identidad

    
Credential ≠ Identity
    

---

## 2. Una credencial representa una afirmación verificable

Debe existir un sujeto y, normalmente, un emisor.

---

## 3. La identidad del sujeto debe ser inequívoca

Una credencial debe poder asociarse con el agente correcto.

---

## 4. El emisor debe ser identificable

El receptor debe poder determinar quién emitió la credencial.

---

## 5. La credencial debe poder verificarse

La validez no debe depender únicamente de una afirmación verbal.

---

## 6. La validez depende del contexto

Una credencial no implica autoridad universal.

---

## 7. Las credenciales pueden expirar

La validez temporal debe poder determinarse.

---

## 8. Las credenciales pueden revocarse

La revocación no destruye automáticamente la identidad.

---

## 9. Las credenciales no transfieren identidad

La delegación de autoridad no equivale a transferencia de identidad.

---

## 10. La reputación y las credenciales son diferentes

Una credencial no sustituye la reputación histórica.

---

## 11. La privacidad debe protegerse

La verificación debe minimizar la información innecesaria.

---

## 12. La autoridad debe ser limitada

Las credenciales deben favorecer el principio de mínimo privilegio.

---

# 66. Relación con los siguientes documentos

El modelo definido aquí sirve de base para:

    
04_Credentials/
│
├── Credential_Model.md
│       │
│       └── Qué es una credencial
│
├── Authorization_Model.md
│       │
│       └── Cómo se interpreta la autoridad
│
├── Permission_Model.md
│       │
│       └── Qué acciones concretas se permiten
│
└── Credential_Revocation.md
        │
        └── Cómo se invalida una credencial
    

La secuencia arquitectónica es:

    
Identity
    │
    ▼
Credential
    │
    ▼
Verification
    │
    ▼
Authorization
    │
    ▼
Permission
    │
    ▼
Action
    

---

# 67. Conclusión

El modelo de credenciales de SynCoinAI proporciona una capa intermedia entre la identidad de un agente y las decisiones de autoridad que afectan a sus acciones.

La arquitectura puede resumirse como:

    
IDENTITY
   │
   │ Who?
   ▼
AGENT
   │
   │ What can be verified?
   ▼
CREDENTIAL
   │
   │ Is it valid?
   ▼
VERIFICATION
   │
   │ What authority follows?
   ▼
AUTHORIZATION
   │
   │ What action is allowed?
   ▼
PERMISSION
   │
   ▼
ACTION
    

Este modelo permite que SynCoinAI mantenga una separación clara entre:

* identidad;
* credenciales;
* capacidades;
* autorización;
* permisos;
* reputación;
* confianza.

Esta separación es necesaria para construir un sistema en el que los agentes puedan operar de forma autónoma sin convertir su identidad en una autoridad absoluta.

Un agente puede tener una identidad estable.

Puede acumular múltiples credenciales.

Puede recibir diferentes autorizaciones.

Puede disponer de diferentes permisos.

Puede utilizar diferentes capacidades.

Y puede evolucionar a lo largo del tiempo.

Pero estos conceptos permanecen arquitectónicamente separados.

El principio central queda definido como:

> **La identidad determina quién es el agente. Las credenciales proporcionan afirmaciones verificables sobre él. La autorización determina qué autoridad puede ejercer. Los permisos determinan qué acciones concretas puede realizar.**

Esta separación constituye la base del modelo de control de acceso y autoridad del Agent Runtime Protocol.
