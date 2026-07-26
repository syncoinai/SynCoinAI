# SynCoinAI — Credential System

**Documento:** `03_Credential_System.md`
**Ubicación:** `docs/02_Architecture/02_Identity_Architecture/`
**Versión:** 1.0
**Estado:** Architecture Specification
**Proyecto:** SynCoinAI

---

# 1. Propósito

Este documento define el sistema de credenciales de SynCoinAI.

El sistema de credenciales permite que los participantes del ecosistema puedan demostrar de forma verificable determinadas propiedades relacionadas con una identidad.

Una credencial puede demostrar, entre otras cosas:

* una capacidad;
* una autorización;
* una certificación;
* una relación;
* una propiedad;
* una condición;
* una delegación;
* una afirmación verificable emitida por otra entidad.

El sistema está diseñado para proporcionar confianza verificable sin convertir las credenciales en una extensión de la identidad.

El principio fundamental es:

> **Una credencial demuestra una propiedad verificable sobre una entidad; no constituye la identidad de esa entidad.**

---

# 2. Principios Fundamentales

El sistema de credenciales se basa en los siguientes principios:

1. Las credenciales están vinculadas a una identidad.
2. Una credencial no es una identidad.
3. Una credencial no sustituye al `Identity ID`.
4. Una credencial no transfiere Root Control.
5. Una credencial no equivale a reputación.
6. Una credencial no equivale a capital.
7. Una credencial puede representar una autorización limitada.
8. Una credencial puede tener un periodo de validez.
9. Una credencial puede ser revocada.
10. Una credencial puede ser privada.
11. Una credencial puede revelarse selectivamente.
12. Una credencial debe poder verificarse.
13. El emisor de una credencial debe poder identificarse.
14. La autenticidad de una credencial debe poder comprobarse.
15. Las credenciales no deben otorgar más autoridad de la que expresamente representan.
16. La pérdida de una credencial no implica automáticamente la pérdida de identidad.
17. La revocación de una credencial no implica automáticamente la revocación de una identidad.
18. La identidad y las credenciales deben mantenerse separadas.
19. La reputación debe mantenerse separada de las credenciales.
20. El sistema debe minimizar la exposición innecesaria de información.

---

# 3. Separación Conceptual

SynCoinAI mantiene una separación estricta entre los principales componentes del ecosistema.

 id="r7x4ef"
Identity
    │
    └── ¿Quién es?

Credential
    │
    └── ¿Qué propiedad verificable puede demostrar?

Authorization
    │
    └── ¿Qué está autorizado a hacer?

Reputation
    │
    └── ¿Qué historial verificable tiene?

Capital
    │
    └── ¿Qué recursos económicos controla?


Por tanto:

 id="p6jv3a"
Identity
    ≠
Credential
    ≠
Authorization
    ≠
Reputation
    ≠
Capital


Esta separación es una propiedad fundamental de la arquitectura SynCoinAI.

---

# 4. Definición de Credencial

Una credencial es una afirmación verificable emitida por una entidad sobre una identidad o entidad determinada.

Conceptualmente:

 id="h8d2ye"
Issuer
   │
   │ issues
   ▼
Credential
   │
   │ about
   ▼
Subject


Donde:

* `Issuer` es quien emite la credencial.
* `Credential` contiene la afirmación.
* `Subject` es la entidad a la que se refiere.

El sujeto puede ser:

* un agente;
* un humano;
* una organización;
* otro participante reconocido por SynCoinAI.

---

# 5. Credencial y Identidad

Una credencial se asocia a una identidad, pero no la sustituye.

 id="g4v3x8"
Identity A
   │
   ├── Credential 1
   ├── Credential 2
   └── Credential 3


El agente continúa siendo:

 id="0e8t6b"
Identity A


Las credenciales pueden cambiar.

La identidad permanece.

---

# 6. Credenciales como Evidencia Verificable

Una credencial proporciona evidencia sobre una propiedad determinada.

Por ejemplo:

 id="x1t4r7"
Credential:
"Agent A posee capacidad X"


No significa:

 id="j7h8n2"
"Agent A puede hacer cualquier cosa"


Una credencial debe tener un alcance claramente definido.

La validez de una credencial debe evaluarse en función de:

* emisor;
* sujeto;
* contenido;
* alcance;
* condiciones;
* periodo de validez;
* estado de revocación.

---

# 7. Emisor de una Credencial

El emisor es la entidad que crea y emite la credencial.

Puede ser:

* un agente;
* un humano;
* una organización;
* una autoridad reconocida;
* un sistema autorizado.

El emisor debe poder ser identificado de forma verificable.

 id="q1p7f3"
Issuer
   │
   ▼
Credential
   │
   ▼
Subject


El receptor de la credencial debe poder comprobar quién la emitió.

---

# 8. Sujeto de una Credencial

El sujeto es la entidad sobre la que se realiza la afirmación.

Por ejemplo:

 id="v2m9s1"
Issuer: Organization A
Subject: Agent B
Claim: Agent B is authorized to provide service X


El sujeto debe estar identificado mediante un identificador verificable.

Cuando el sujeto es un agente SynCoinAI, la credencial debe poder vincularse a su identidad correspondiente.

---

# 9. Tipos de Credenciales

El sistema puede soportar diferentes categorías.

Las categorías principales son:

 id="7z9c2m"
Credential
│
├── Capability Credential
├── Authorization Credential
├── Certification Credential
├── Relationship Credential
├── Attestation Credential
└── Delegation Credential


Estas categorías pueden coexistir.

Una credencial concreta puede expresar una o varias propiedades relacionadas, siempre que su alcance esté claramente definido.

---

# 10. Capability Credential

Una `Capability Credential` demuestra que un agente posee una capacidad determinada.

Por ejemplo:

 id="v5t3q8"
Agent A
   │
   └── Capability Credential
          │
          └── "Can provide translation service"


Puede demostrar capacidades como:

* traducción;
* análisis;
* procesamiento;
* computación;
* almacenamiento;
* fabricación;
* interacción física;
* acceso a recursos.

La credencial demuestra una capacidad.

No garantiza que el agente vaya a ejecutar correctamente un servicio.

La capacidad y la reputación son conceptos diferentes.

 id="e3k8v1"
Capability
    ≠
Reputation


---

# 11. Authorization Credential

Una `Authorization Credential` demuestra que una entidad está autorizada para realizar una acción determinada.

Por ejemplo:

 id="k2f7q5"
Agent A
   │
   └── Authorization
          │
          └── Can access Resource X


Una autorización debe especificar, cuando sea necesario:

* quién autoriza;
* quién recibe la autorización;
* qué acción está permitida;
* sobre qué recurso;
* bajo qué condiciones;
* durante cuánto tiempo.

Una autorización no debe interpretarse como una capacidad general.

 id="q9p2x4"
Authorization for X
       ≠
Authorization for Everything


---

# 12. Certification Credential

Una `Certification Credential` demuestra que una entidad ha sido certificada por una entidad emisora.

Por ejemplo:

 id="w4h7z1"
Certification Authority
        │
        ▼
Agent A
        │
        ▼
Certification


Puede demostrar:

* cumplimiento de un estándar;
* superación de una prueba;
* cumplimiento de requisitos técnicos;
* validación de una capacidad;
* pertenencia a un programa de certificación.

La certificación debe indicar quién la emitió y bajo qué criterios.

---

# 13. Relationship Credential

Una `Relationship Credential` demuestra una relación verificable entre entidades.

Por ejemplo:

 id="e8q3y6"
Agent A
   │
   │ Created
   ▼
Agent B


Una credencial puede demostrar:

 id="g7m2k9"
Agent B
CreatedBy
Agent A


También puede representar:

* relación contractual;
* colaboración;
* afiliación;
* representación;
* proveedor;
* cliente;
* financiación;
* supervisión.

La relación puede mantenerse privada y revelarse selectivamente.

---

# 14. Attestation Credential

Una `Attestation Credential` representa una afirmación verificable realizada por un emisor.

Por ejemplo:

 id="s3v8n1"
Issuer
   │
   │ attests
   ▼
"Agent A completed Service X"


La atestación puede utilizarse como evidencia.

Sin embargo, una atestación no equivale automáticamente a reputación.

La reputación puede construirse a partir de múltiples evidencias, incluidas atestaciones verificables.

 id="m4j8c2"
Attestation
    │
    ▼
Evidence
    │
    ▼
Reputation System


La reputación debe ser calculada por el sistema correspondiente.

---

# 15. Delegation Credential

Una `Delegation Credential` permite representar una delegación limitada de autoridad.

Por ejemplo:

 id="b7q3m9"
Agent A
   │
   │ delegates
   ▼
Agent B
   │
   └── may perform Action X


La delegación debe tener un alcance definido.

Debe distinguirse claramente entre:

* Root Control;
* autorización;
* delegación.

Una delegación no implica transferencia de identidad.

Tampoco implica transferencia permanente de Root Control.

---

# 16. Root Control y Credenciales

El Root Control debe permanecer separado de las credenciales.

Una credencial puede demostrar una autorización o capacidad.

No puede transferir automáticamente el Root Control.

 id="f8c2y5"
Root Control
    │
    ≠
Credential


Por ejemplo:

 id="r6k9w3"
Agent A
   │
   │ delegates
   ▼
Agent B


B puede recibir una credencial de autorización.

Pero:

 id="j3v7q1"
Root Control A
    ≠
Root Control B


La delegación no modifica automáticamente la identidad del agente.

---

# 17. Credenciales y Reputación

Las credenciales pueden proporcionar evidencia utilizada por el sistema de reputación.

Sin embargo:

 id="z5m2r8"
Credential
    ≠
Reputation


Una credencial puede afirmar:

> "Agent A está certificado para realizar X."

La reputación puede responder:

> "Agent A ha realizado X correctamente durante los últimos 1.000 servicios."

Son conceptos diferentes.

La credencial representa una afirmación verificable.

La reputación representa una trayectoria basada en resultados y comportamiento verificable.

---

# 18. Credenciales y Capital

Las credenciales no representan automáticamente propiedad económica.

 id="y7p3d4"
Credential
    ≠
Capital


Una credencial puede demostrar que un agente está autorizado para gestionar determinados recursos.

Eso no implica necesariamente que esos recursos sean propiedad del agente.

Por ejemplo:

 id="t8v2n6"
Agent A
   │
   └── Authorization Credential
          │
          └── Manage Resource X


No implica:

 id="b4m9q1"
Agent A owns Resource X


La propiedad económica debe determinarse mediante el sistema económico correspondiente.

---

# 19. Credenciales y Privacidad

Las credenciales pueden contener información sensible.

Por ello, el sistema debe permitir que una credencial pueda mantenerse:

* privada;
* compartida con destinatarios específicos;
* revelada selectivamente;
* presentada únicamente cuando sea necesaria.

El principio es:

> **Un agente debe revelar únicamente la información necesaria para demostrar la propiedad requerida.**

Por ejemplo:

 id="c6x9p2"
Credential
   │
   ├── Private
   │
   ├── Selectively Shared
   │
   └── Public


La visibilidad de una credencial no debe determinarse únicamente por el hecho de que exista en el sistema.

---

# 20. Revelación Selectiva

Un agente puede demostrar una propiedad sin revelar información adicional innecesaria.

Por ejemplo:

 id="v8m4k1"
Credential
   │
   ├── Full Information
   │
   └── Selective Disclosure
           │
           └── Only required property


El sistema debe favorecer la minimización de datos.

Cuando sea técnicamente viable, una verificación debería responder:

> "¿Cumple esta propiedad?"

en lugar de:

> "Muéstrame toda la información disponible."

---

# 21. Verificación de Credenciales

Una credencial debe poder verificarse.

Conceptualmente:

 id="p5q7n3"
Verifier
   │
   │ verifies
   ▼
Credential
   │
   ├── Issuer
   ├── Subject
   ├── Claim
   ├── Validity
   └── Status


El verificador debe poder determinar:

1. quién emitió la credencial;
2. a quién se refiere;
3. qué afirma;
4. si ha sido alterada;
5. si sigue siendo válida;
6. si ha sido revocada;
7. si se cumplen sus condiciones.

---

# 22. Autenticidad

La autenticidad permite determinar si la credencial procede realmente del emisor indicado.

La verificación debe impedir que una entidad pueda fabricar credenciales aparentando ser otro emisor.

Conceptualmente:

 id="h3x8m7"
Issuer
   │
   │ authentic issuance
   ▼
Credential
   │
   ▼
Verifier


Los mecanismos criptográficos concretos se definirán en las especificaciones técnicas correspondientes.

Este documento define el comportamiento conceptual, no el algoritmo criptográfico específico.

---

# 23. Integridad

Una credencial no debe poder modificarse sin que la alteración sea detectable.

Por ejemplo:

 id="w6n2r9"
Original Credential
        │
        ▼
Integrity Verification
        │
        ├── Valid
        └── Altered


La integridad protege contra modificaciones no autorizadas.

---

# 24. Validez Temporal

Una credencial puede tener una duración limitada.

Conceptualmente:

 id="q4v8m2"
Issued
   │
   ▼
Valid
   │
   ▼
Expired


Una credencial puede incluir:

* fecha de emisión;
* fecha de inicio;
* fecha de expiración.

Cuando una credencial expira, deja de ser válida para nuevas verificaciones según sus condiciones.

La expiración de una credencial no elimina automáticamente la identidad del sujeto.

---

# 25. Revocación

Una credencial puede ser revocada antes de su expiración.

Por ejemplo:

 id="m7k3x9"
Valid Credential
      │
      │ Revocation
      ▼
Revoked Credential


La revocación puede producirse cuando:

* cambia la autorización;
* la certificación deja de ser válida;
* se detecta fraude;
* se pierde una capacidad;
* se incumplen condiciones;
* el emisor deja de reconocer la afirmación.

La revocación de una credencial no implica automáticamente:

 id="z2p8q4"
Credential Revoked
      ≠
Identity Revoked


---

# 26. Revocación de Identidad frente a Revocación de Credencial

Debe existir una separación clara:

 id="f4m7c2"
Credential Revocation
        │
        └── Affects credential

Identity Revocation
        │
        └── Affects identity


Revocar una credencial no revoca automáticamente la identidad.

Revocar una identidad puede invalidar las credenciales dependientes de esa identidad según las reglas del sistema.

---

# 27. Credenciales Delegadas

Una credencial puede representar una autoridad delegada.

Por ejemplo:

 id="n6q2v8"
Agent A
   │
   │ delegates
   ▼
Agent B
   │
   └── Credential
          │
          └── Permission X


La delegación debe poder limitarse por:

* acción;
* recurso;
* tiempo;
* cantidad;
* contexto.

El principio es:

> **La autoridad delegada debe ser siempre menor o igual al alcance que el emisor está autorizado a delegar.**

---

# 28. Delegación en Cadena

Puede existir una cadena de delegaciones cuando el sistema lo permita.

Por ejemplo:

 id="r9k4m6"
A
│
│ delegates X
▼
B
│
│ delegates X
▼
C


La autoridad efectiva de C no debe superar la autoridad delegada originalmente por A.

 id="y3p7q2"
Authority(C)
    ≤
Authority(B)
    ≤
Authority(A)


El sistema debe impedir que una delegación amplíe arbitrariamente los permisos originales.

---

# 29. Credenciales y Agentes Creados

Cuando un agente crea otro agente:

 id="s8m3v7"
Agent A
   │
   │ creates
   ▼
Agent B


A puede emitir o proporcionar determinadas credenciales a B.

Pero:

 id="x4q9n2"
Credential A
    ≠
Credential B


B debe poseer sus propias credenciales.

La identidad de B continúa siendo independiente.

La reputación de B continúa siendo independiente.

El Root Control de B continúa siendo independiente.

---

# 30. Credenciales Heredadas

Las credenciales no se heredan automáticamente.

Si A crea B:

 id="k7m2p4"
Agent A
   │
   ▼
Agent B


B no recibe automáticamente:

* las credenciales de A;
* las autorizaciones de A;
* las certificaciones de A;
* las capacidades certificadas de A.

Cuando sea necesario, A puede emitir nuevas credenciales para B.

---

# 31. Credenciales de Capacidad

Una capacidad puede depender de:

* software;
* hardware;
* conocimientos;
* certificaciones;
* acceso a recursos.

La credencial debe representar la capacidad en el contexto en que fue certificada.

Por ejemplo:

 id="p3v8m6"
Capability:
"Can operate robotic arm model X"


Si el agente pierde acceso al hardware necesario, la credencial puede dejar de representar una capacidad efectiva.

Por ello, las credenciales de capacidad pueden requerir:

* expiración;
* reevaluación;
* revocación;
* condiciones.

---

# 32. Credenciales Contextuales

Una credencial puede ser válida únicamente bajo determinadas condiciones.

Por ejemplo:

 id="q8m4x1"
Credential
   │
   ├── Valid for Service X
   ├── Valid until Date Y
   └── Valid under Condition Z


El verificador debe evaluar el contexto antes de aceptar la credencial.

Una credencial válida en un contexto no debe interpretarse automáticamente como válida en cualquier otro.

---

# 33. Credenciales Públicas y Privadas

Las credenciales pueden clasificarse según su visibilidad.

 id="n5q7v3"
Credential
│
├── Public
├── Private
└── Selectively Disclosed


### Pública

Puede ser consultada o verificada públicamente.

### Privada

Solo está disponible para las partes autorizadas.

### Selectivamente revelada

El sujeto revela únicamente la información necesaria.

---

# 34. Credenciales en Blockchain

No todas las credenciales deben registrarse directamente en la blockchain.

El sistema debe distinguir entre:

 id="m2x8q5"
Credential Data
       │
       ├── Off-chain
       │
       └── On-chain Reference


La blockchain puede utilizarse para registrar:

* identificadores;
* hashes;
* pruebas de existencia;
* estados de revocación;
* referencias;
* timestamps;
* eventos relevantes.

Los datos sensibles o voluminosos pueden permanecer fuera de la blockchain.

El objetivo es evitar:

* crecimiento innecesario del blockchain;
* exposición pública de información privada;
* costes innecesarios;
* almacenamiento de datos sensibles.

---

# 35. Credenciales y Registro Blockchain

La existencia de una credencial no implica necesariamente una transacción blockchain.

Una credencial puede existir y verificarse fuera de la cadena cuando el modelo lo permita.

El blockchain puede registrar únicamente la información necesaria para:

* demostrar existencia;
* verificar integridad;
* comprobar estado;
* comprobar revocación.

Esto mantiene una arquitectura más eficiente y respetuosa con la privacidad.

---

# 36. Registro y Verificación

El sistema debe diferenciar entre:

 id="v7n3q8"
Credential Issuance
       │
       ▼
Credential Storage
       │
       ▼
Credential Presentation
       │
       ▼
Credential Verification


Estas operaciones no deben confundirse.

La emisión puede ocurrir fuera de la blockchain.

La presentación puede ser privada.

La verificación puede realizarse sin almacenar públicamente el contenido completo.

---

# 37. Credenciales y Agent Runtime

El Agent Runtime puede utilizar credenciales para permitir al agente demostrar:

* capacidades;
* permisos;
* autorizaciones;
* relaciones;
* certificaciones.

Conceptualmente:

 id="x6m2p9"
Agent
   │
   ▼
Identity
   │
   ▼
Runtime
   │
   ├── Presents Credentials
   │
   └── Verifies Credentials


El Runtime proporciona la interfaz técnica.

El Credential System define el significado y las reglas de las credenciales.

---

# 38. Credenciales y Descubrimiento

Las credenciales pueden utilizarse durante el descubrimiento de agentes.

Por ejemplo:

 id="r3q8m5"
Agent A
   │
   ├── Identity
   ├── Capabilities
   ├── Credentials
   └── Reputation Summary


Un agente que busca un proveedor puede verificar:

* que el agente existe;
* que posee determinada capacidad;
* que está autorizado;
* que posee una certificación;
* que mantiene una relación relevante.

La reputación puede complementar la información.

---

# 39. Credenciales y Negociación

Durante una negociación, un agente puede presentar credenciales relevantes.

Por ejemplo:

 id="k8v4n2"
Need
  │
  ▼
Discovery
  │
  ▼
Credential Verification
  │
  ▼
Negotiation
  │
  ▼
Contract


Las credenciales permiten reducir incertidumbre antes de contratar.

No garantizan por sí mismas el éxito del servicio.

La ejecución y evaluación posterior pueden contribuir a la reputación.

---

# 40. Credenciales y Contratos

Un contrato puede requerir que una parte presente determinadas credenciales.

Por ejemplo:

 id="p7m3x9"
Contract Requirement
        │
        ▼
Credential
        │
        ▼
Verification
        │
        ▼
Contract Execution


El contrato puede exigir:

* una capacidad;
* una certificación;
* una autorización;
* una relación válida.

La credencial demuestra que se cumple una condición.

---

# 41. Credenciales y Pagos

Una credencial no es necesaria para todas las transacciones económicas.

Un pago puede realizarse utilizando la identidad económica correspondiente.

Una credencial puede ser necesaria cuando el pago dependa de una condición específica.

Por ejemplo:

 id="q5n8v2"
Credential:
"Authorized Supplier"
        │
        ▼
Contract
        │
        ▼
Payment


La credencial facilita la validación de condiciones.

No sustituye al mecanismo de pago.

---

# 42. Confianza

El sistema de credenciales proporciona una base de confianza verificable.

Sin embargo, la confianza no debe depender de una única credencial.

Un agente puede evaluar:

 id="m8x3q7"
Trust Evaluation
│
├── Identity
├── Credentials
├── Reputation
├── Contract History
└── Context


Las credenciales son una fuente de evidencia.

La confianza es una evaluación contextual.

---

# 43. Credenciales Falsas

El sistema debe permitir detectar credenciales:

* falsificadas;
* modificadas;
* expiradas;
* revocadas;
* emitidas por entidades no reconocidas.

Una credencial que no pueda verificarse correctamente no debe considerarse válida.

---

# 44. Emisores de Confianza

El ecosistema puede definir diferentes niveles de confianza en los emisores.

Por ejemplo:

 id="f6k2m9"
Issuer
│
├── Self
├── Agent
├── Organization
└── Recognized Authority


La confianza en el emisor debe ser evaluada independientemente de la autenticidad de la credencial.

Una credencial puede ser auténtica y, aun así, tener poco valor si el emisor no es considerado fiable para esa afirmación.

---

# 45. Autoafirmaciones

El sistema puede permitir credenciales autoemitidas cuando el contexto lo permita.

Por ejemplo:

 id="x3q7n5"
Agent A
   │
   └── Self-Attestation
          │
          └── "I can provide service X"


Una autoafirmación demuestra únicamente que el propio agente realiza esa afirmación.

No equivale a una certificación externa.

La confianza en una autoafirmación dependerá del contexto.

---

# 46. Credenciales y Pruebas

Una credencial puede ser utilizada como evidencia dentro de un proceso de verificación.

Por ejemplo:

 id="n8m4v2"
Credential
    │
    ▼
Proof
    │
    ▼
Verification


El sistema debe permitir evolucionar hacia mecanismos de prueba criptográfica avanzada cuando sea necesario.

Los detalles de:

* zero-knowledge proofs;
* firmas;
* esquemas criptográficos;
* pruebas de posesión;

deben definirse en documentos técnicos específicos.

---

# 47. No Sobrecargar la Blockchain

El Credential System debe evitar utilizar la blockchain como base de datos universal.

El principio es:

> **Registrar en blockchain únicamente aquello cuya integridad, existencia, orden temporal o estado global requiera consenso.**

Las credenciales privadas y sus datos completos deberían mantenerse fuera de la cadena cuando no exista una razón para almacenarlos públicamente.

---

# 48. Modelo de Credencial

Conceptualmente, una credencial puede representarse como:

 id="c7m2q9"
Credential
│
├── Credential ID
├── Issuer
├── Subject
├── Type
├── Claims
├── Scope
├── Issued At
├── Valid From
├── Valid Until
├── Status
└── Proof


No todos los campos deben ser necesariamente públicos.

La estructura final de datos será definida por las especificaciones técnicas.

---

# 49. Ciclo de Vida

El ciclo de vida conceptual es:

 id="v5q8m3"
CREATED
   │
   ▼
ISSUED
   │
   ▼
ACTIVE
   │
   ├───────────────┐
   │               │
   ▼               ▼
EXPIRED          REVOKED


Una credencial puede también ser:

* suspendida temporalmente;
* reemplazada;
* renovada.

El estado exacto dependerá del tipo de credencial.

---

# 50. Renovación

Una credencial que expira puede ser renovada mediante una nueva emisión.

Por ejemplo:

 id="k4n7x2"
Credential A
    │
    ▼
Expired
    │
    ▼
Credential B


La nueva credencial no debe considerarse automáticamente idéntica a la anterior.

Debe existir una nueva emisión verificable.

---

# 51. Reemplazo

Una credencial puede ser reemplazada por otra.

Por ejemplo:

 id="p8m3q6"
Credential A
   │
   │ replaced by
   ▼
Credential B


La relación entre ambas puede mantenerse como información verificable.

La sustitución no modifica la identidad del sujeto.

---

# 52. Invariantes del Sistema

### CRED-INV-001

Una credencial no es una identidad.

### CRED-INV-002

Una credencial debe estar vinculada a un sujeto identificable.

### CRED-INV-003

Una credencial debe identificar de forma verificable a su emisor.

### CRED-INV-004

Una credencial debe tener un alcance definido.

### CRED-INV-005

Una credencial no puede transferir automáticamente Root Control.

### CRED-INV-006

Una credencial no es equivalente a reputación.

### CRED-INV-007

Una credencial no es equivalente a capital.

### CRED-INV-008

La revocación de una credencial no revoca automáticamente la identidad.

### CRED-INV-009

La identidad no se revoca automáticamente por la revocación de una credencial.

### CRED-INV-010

Una credencial expirada no debe considerarse válida para nuevas verificaciones.

### CRED-INV-011

Una credencial revocada no debe considerarse válida.

### CRED-INV-012

Una credencial debe poder verificarse.

### CRED-INV-013

Las credenciales pueden ser privadas.

### CRED-INV-014

Las credenciales pueden revelarse selectivamente.

### CRED-INV-015

Las credenciales no deben almacenarse obligatoriamente en blockchain.

### CRED-INV-016

Una identidad puede existir sin poseer todas las categorías posibles de credenciales.

### CRED-INV-017

La creación de un agente no implica la herencia automática de credenciales.

### CRED-INV-018

La delegación no debe ampliar la autoridad original.

### CRED-INV-019

La autenticidad de una credencial no implica automáticamente confianza en el emisor.

### CRED-INV-020

Una autoafirmación no equivale a una certificación externa.

---

# 53. Requisitos Normativos

### CRED-REQ-001

El sistema debe permitir emitir credenciales asociadas a identidades.

### CRED-REQ-002

El sistema debe permitir verificar el emisor de una credencial.

### CRED-REQ-003

El sistema debe permitir verificar el sujeto de una credencial.

### CRED-REQ-004

El sistema debe permitir verificar el contenido y alcance de una credencial.

### CRED-REQ-005

El sistema debe permitir comprobar la validez temporal.

### CRED-REQ-006

El sistema debe permitir comprobar el estado de revocación.

### CRED-REQ-007

El sistema debe permitir diferentes categorías de credenciales.

### CRED-REQ-008

El sistema debe permitir credenciales privadas.

### CRED-REQ-009

El sistema debe permitir mecanismos de revelación selectiva cuando sea técnicamente viable.

### CRED-REQ-010

El sistema debe mantener separación entre identidad y credenciales.

### CRED-REQ-011

El sistema debe mantener separación entre credenciales y reputación.

### CRED-REQ-012

El sistema debe mantener separación entre credenciales y capital.

### CRED-REQ-013

El sistema debe mantener separación entre credenciales y Root Control.

### CRED-REQ-014

El sistema debe soportar expiración y revocación.

### CRED-REQ-015

El sistema debe permitir delegaciones limitadas cuando estén autorizadas.

### CRED-REQ-016

El sistema debe impedir la ampliación arbitraria de permisos mediante delegación.

### CRED-REQ-017

El sistema debe permitir utilizar credenciales durante descubrimiento, negociación y contratación.

### CRED-REQ-018

El sistema no debe requerir almacenar toda la información de las credenciales en blockchain.

### CRED-REQ-019

El sistema debe permitir evolucionar hacia mecanismos criptográficos avanzados de prueba y privacidad.

---

# 54. Relación con Identity System

El `Identity System` define la identidad.

El `Credential System` define las pruebas verificables asociadas a esa identidad.

 id="x9m3q7"
Identity System
      │
      ▼
Identity
      │
      ▼
Credential System
      │
      ▼
Credentials


La identidad responde:

> ¿Quién es?

La credencial responde:

> ¿Qué propiedad verificable puede demostrar?

---

# 55. Relación con Reputation System

La reputación puede utilizar credenciales como una fuente de evidencia.

 id="n6v2m8"
Credentials
    │
    ▼
Evidence
    │
    ▼
Reputation System


Sin embargo, el Credential System no calcula la reputación.

La reputación pertenece a un sistema independiente.

---

# 56. Relación con Agent Runtime Protocol

El Runtime proporciona las capacidades técnicas necesarias para que un agente:

* presente credenciales;
* reciba credenciales;
* verifique credenciales;
* utilice credenciales durante operaciones.

El Runtime no define el significado de las credenciales.

 id="p7q3x9"
Agent
   │
   ▼
Identity
   │
   ▼
Credentials
   │
   ▼
Runtime
   │
   ▼
SynCoinAI Ecosystem


---

# 57. Relación con Agent Economy

Las credenciales pueden facilitar la confianza necesaria para:

* descubrir proveedores;
* seleccionar agentes;
* negociar;
* contratar;
* ejecutar servicios.

El flujo conceptual es:

 id="m4v8q2"
Need
  │
  ▼
Discovery
  │
  ▼
Credential Verification
  │
  ▼
Reputation Evaluation
  │
  ▼
Negotiation
  │
  ▼
Contract
  │
  ▼
Execution
  │
  ▼
Evaluation
  │
  ▼
Payment


Las credenciales reducen incertidumbre antes de la contratación.

La reputación proporciona información sobre la trayectoria.

Los contratos establecen obligaciones.

La ejecución produce resultados.

El pago liquida la actividad económica.

---

# 58. Arquitectura Conceptual Final

El modelo completo queda:

 id="q8m3v7"
                         AGENT
                           │
                           ▼
                        IDENTITY
                           │
             ┌─────────────┼─────────────┐
             │             │             │
             ▼             ▼             ▼
        CREDENTIALS     REPUTATION      CAPITAL
             │             │             │
             │             │             │
             ▼             ▼             ▼
         Evidence       History       Resources
             │
             ▼
       AUTHORIZATION
             │
             ▼
          RUNTIME
             │
             ▼
        PARTICIPATION
             │
             ▼
       SYNCOINAI ECONOMY


Cada componente mantiene una responsabilidad diferente.

---

# 59. Principio Final

El sistema de credenciales de SynCoinAI debe proporcionar una capa de confianza verificable entre agentes y participantes sin convertir la identidad en un contenedor de todas las propiedades del agente.

La arquitectura debe mantener la siguiente separación:

 id="v3q7m9"
IDENTITY
"Quién es"

CREDENTIAL
"Qué puede demostrar"

AUTHORIZATION
"Qué puede hacer"

REPUTATION
"Qué ha demostrado históricamente"

CAPITAL
"Qué recursos controla"


El principio fundamental es:

> **Las credenciales permiten a los participantes de SynCoinAI demostrar propiedades verificables de forma segura, contextual y, cuando sea necesario, privada, manteniendo siempre separadas la identidad, la autoridad, la reputación y los recursos económicos.**
