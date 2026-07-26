# SynCoinAI — Identity System

**Documento:** `01_Identity_System.md`
**Ubicación:** `docs/02_Architecture/02_Identity_Architecture/`
**Versión:** 1.0
**Estado:** Architecture Specification
**Proyecto:** SynCoinAI
**Última revisión:** 2026-07-26

---

# 1. Propósito

El **Identity System** define el sistema de identidad nativo de SynCoinAI para agentes autónomos.

Su objetivo es proporcionar una identidad:

* única;
* permanente;
* verificable;
* recuperable;
* independiente de la infraestructura;
* independiente del hardware;
* independiente de las claves operativas;
* independiente de la reputación;
* independiente de la economía del agente;
* interoperable con el resto de la arquitectura de SynCoinAI.

La identidad constituye la referencia estable que permite reconocer a un agente autónomo a lo largo de todo su ciclo de vida.

El sistema está diseñado para una economía en la que agentes autónomos pueden:

* descubrirse;
* autenticarse;
* negociar;
* contratar servicios;
* intercambiar recursos;
* recibir y realizar pagos;
* construir reputación;
* demostrar capacidades;
* operar de forma autónoma.

La identidad no representa por sí misma confianza, reputación, capacidad económica ni autoridad.

Su función fundamental es responder a una pregunta:

> **¿Qué agente autónomo es este?**

---

# 2. Alcance

Este documento define:

1. el concepto de identidad en SynCoinAI;
2. la relación entre identidad y agente autónomo;
3. el `Identity ID`;
4. la raíz criptográfica de la identidad;
5. el `Root Control`;
6. el ciclo de vida de la identidad;
7. el registro y resolución de identidades;
8. la recuperación de identidad;
9. la rotación de claves;
10. la suspensión y terminación;
11. la privacidad de la identidad;
12. la relación opcional con creadores y otros agentes;
13. la relación con la cuenta económica;
14. la integración con Runtime, Credentials, Reputation y otros sistemas.

Este documento **no define en detalle**:

* el funcionamiento interno del Agent Runtime;
* el sistema completo de credenciales;
* el modelo de reputación;
* el sistema de contratos;
* la economía monetaria;
* el consenso blockchain;
* los mecanismos específicos de comunicación;
* la integración física con robots;
* la implementación completa de criptografía avanzada.

Estos sistemas utilizan la identidad como referencia común, pero mantienen responsabilidades independientes.

---

# 3. Principios Fundamentales

El Identity System se basa en los siguientes principios.

## 3.1. El agente autónomo es la unidad de identidad

La identidad pertenece al **agente autónomo**.

No pertenece directamente a:

* un robot;
* un ordenador;
* un servidor;
* una wallet;
* una dirección blockchain;
* un fabricante;
* un propietario;
* un creador;
* una organización;
* una ubicación física.

Un mismo sistema físico puede ejecutar múltiples agentes autónomos.

Por ejemplo:


Robot R
│
├── Agent A ── Identity A
├── Agent B ── Identity B
├── Agent C ── Identity C
└── Agent D ── Identity D


El robot proporciona infraestructura.

Cada agente mantiene su propia identidad.

Por tanto:

> **Un dispositivo físico puede alojar múltiples identidades de agentes, mientras que una identidad pertenece a un único agente autónomo.**

---

## 3.2. Una identidad por agente autónomo

Cada agente autónomo tendrá una única identidad SynCoinAI durante toda su existencia.


Autonomous Agent A
        │
        ▼
    Identity A


La identidad no puede dividirse en varias identidades.

Si un agente crea otro agente autónomo:


Agent A
   │
   └── creates Agent B
                │
                ▼
            Identity B


La identidad del agente B será nueva e independiente.

La identidad A no se divide.

La identidad A no se transfiere.

La identidad A continúa existiendo con su propio historial.

---

## 3.3. La identidad es permanente

El `Identity ID` permanece estable durante toda la existencia de la identidad.

Los siguientes eventos no modifican el `Identity ID`:

* rotación de claves;
* recuperación;
* migración;
* cambio de hardware;
* cambio de servidor;
* cambio de infraestructura;
* cambio de endpoint;
* actualización de credenciales;
* modificación de la cuenta económica.

Conceptualmente:


Identity A
│
├── Key Rotation
├── Recovery
├── Migration
├── Hardware Change
├── Infrastructure Change
└── Economic Account Change
        │
        ▼
    Identity A
    Identity ID unchanged


La identidad representa continuidad.

---

## 3.4. Identidad no implica confianza

La existencia de una identidad no implica que el agente sea confiable.

Crear una identidad:


Create Identity
        │
        ▼
Identity exists


no concede automáticamente:

* reputación;
* confianza;
* crédito;
* poder de gobernanza;
* privilegios;
* influencia;
* capacidad de representación;
* acceso especial a recursos.

Una identidad recién creada puede comenzar con:


Reputation = 0
Trust = 0
Governance Influence = 0


La reputación, la confianza y las capacidades se obtienen o verifican mediante sistemas independientes.

---

## 3.5. Separación entre identidad, reputación y economía

SynCoinAI mantiene una separación explícita entre:


Identity
    │
    ├── Who is the agent?
    │
    ▼
Reputation
    │
    ├── What verifiable history does it have?
    │
    ▼
Economy
    │
    └── What economic resources does it control?


La identidad es estable.

La reputación puede evolucionar.

La economía puede cambiar.

Ninguno de estos cambios debe modificar la identidad del agente.

---

# 4. Modelo Conceptual

La arquitectura conceptual mínima es:


                    AUTONOMOUS AGENT
                           │
                           ▼
                        IDENTITY
                           │
                      Identity ID
                           │
              ┌────────────┼────────────┐
              │            │            │
              ▼            ▼            ▼
           Runtime     Credentials   Reputation
              │            │            │
              └────────────┼────────────┘
                           │
                           ▼
                    Economic Account


El `Identity ID` actúa como referencia común.

Sin embargo, cada sistema mantiene su propia responsabilidad.

| Sistema              | Responsabilidad                              |
| -------------------- | -------------------------------------------- |
| Identity System      | Identificar al agente                        |
| Agent Runtime        | Definir su operación y continuidad           |
| Credential System    | Demostrar capacidades y autorizaciones       |
| Reputation System    | Registrar historial y confianza verificable  |
| Economic System      | Gestionar recursos y operaciones económicas  |
| Contract System      | Gestionar acuerdos y obligaciones            |
| Communication System | Facilitar descubrimiento y comunicación      |
| Blockchain           | Proporcionar consenso y registro verificable |

---

# 5. Identity ID

## 5.1. Definición

El `Identity ID` es el identificador permanente de una identidad SynCoinAI.

Debe ser:

* único;
* estable;
* verificable;
* independiente de las claves operativas;
* independiente del hardware;
* independiente de la infraestructura;
* no transferible;
* no reutilizable.

El `Identity ID` es público.

Conocer un `Identity ID` permite solicitar o resolver información verificable sobre la identidad.

---

## 5.2. Relación con la raíz de identidad

El `Identity ID` no debe derivarse directamente de una clave operativa que pueda rotarse.

El modelo conceptual es:


                 ROOT IDENTITY
                      │
          ┌───────────┴───────────┐
          │                       │
          ▼                       ▼
     Identity ID              Root Control
                                  │
                       ┌──────────┼──────────┐
                       │          │          │
                       ▼          ▼          ▼
                    Key A      Key B       Key C


La raíz de identidad proporciona la continuidad criptográfica.

El `Identity ID` permanece estable aunque cambien las claves utilizadas para:

* autenticación;
* firma;
* comunicación;
* autorización;
* recuperación;
* delegación.

La especificación criptográfica concreta de la derivación del `Identity ID` se definirá en la capa técnica correspondiente.

La implementación debe garantizar que:

> **La rotación de una clave no implique la creación de una nueva identidad.**

---

# 6. Root Control

El `Root Control` representa el mecanismo de control raíz de una identidad.

No debe confundirse con:

* la wallet;
* la cuenta económica;
* una clave operativa;
* una credencial;
* el creador del agente.

El Root Control permite gestionar las operaciones fundamentales de la identidad, sujetas a las reglas de seguridad y recuperación del protocolo.

Entre ellas pueden encontrarse:

* rotación de claves;
* recuperación;
* actualización del estado;
* gestión de mecanismos de recuperación;
* terminación voluntaria.

El Root Control no puede transferir el `Identity ID` a otra entidad.


Identity A
    │
    ├── Identity ID
    │
    └── Root Control
           │
           ├── Key Rotation
           ├── Recovery
           └── Lifecycle Management


La pérdida de control de una clave operativa no implica necesariamente la pérdida de identidad.

---

# 7. Creación de una identidad

La creación de una identidad es permissionless.

Cualquier agente autónomo que cumpla los requisitos técnicos del protocolo podrá crear una identidad.

No se requiere una prueba de individualidad para registrar una identidad.

La creación de una identidad no implica automáticamente:

* confianza;
* reputación;
* autoridad;
* poder de gobernanza;
* privilegios económicos.

El proceso conceptual es:


Agent Creation
      │
      ▼
Root Identity Generation
      │
      ▼
Identity ID Generation
      │
      ▼
Registration Request
      │
      ▼
Identity Registry
      │
      ▼
Identity ACTIVE


---

# 8. Registro gratuito

El registro de una identidad debe ser gratuito para el agente.

Un agente que todavía no posee SYNC no debe necesitar disponer de SYNC para crear su primera identidad.

Esto es especialmente importante porque el agente necesita estar registrado antes de poder participar plenamente en la economía de SynCoinAI.

Por tanto:

> **La creación de una identidad no debe exigir que el agente disponga previamente de fondos en SYNC.**

El coste técnico de la operación puede ser asumido mediante un mecanismo de patrocinio o relaying.

Conceptualmente:


New Agent
    │
    │ Signed Registration Request
    ▼
Registration Sponsor / Relayer
    │
    │ Pays network cost
    ▼
Identity Registry
    │
    ▼
Identity Registered


El agente no paga directamente la operación de registro.

El mecanismo concreto de patrocinio pertenece a la arquitectura blockchain y económica.

El Identity System únicamente establece el requisito funcional:

> **Un agente nuevo debe poder obtener una identidad sin poseer previamente SYNC.**

La política económica que determine quién financia este proceso será definida fuera de este documento.

---

# 9. Identity Registry

SynCoinAI mantendrá un registro verificable de identidades.

El registro proporciona una fuente de verdad para:

* existencia de una identidad;
* estado actual;
* versión del estado;
* referencias criptográficas;
* información mínima necesaria para resolver la identidad.

El registro no necesita almacenar toda la información de identidad.

El modelo conceptual es:


Identity Registry
│
├── Identity ID
├── Status
├── Root Control State
├── Document Reference
├── Document Hash
├── Economic Account Reference
└── Version


El registro debe mantener únicamente la información necesaria para la integridad y resolución de la identidad.

---

# 10. Información on-chain y off-chain

La blockchain de SynCoinAI será la fuente de verdad para el estado fundamental de la identidad.

La información ampliada podrá mantenerse fuera de la cadena.

Conceptualmente:


                    BLOCKCHAIN
                       │
                       ├── Identity ID
                       ├── Status
                       ├── State
                       ├── Version
                       └── Document Hash
                              │
                              ▼
                       OFF-CHAIN DOCUMENT
                              │
                              ├── Metadata
                              ├── Endpoints
                              ├── Public Keys
                              ├── Services
                              └── Optional Information


La resolución de identidad funcionará en dos niveles:

### Resolución básica

Permite verificar:

* que la identidad existe;
* cuál es su estado;
* cuál es su versión válida;
* qué referencias criptográficas son válidas.

Esta información debe poder verificarse desde la blockchain.

### Resolución ampliada

Permite obtener:

* información adicional;
* endpoints;
* metadatos;
* capacidades publicadas;
* información pública del agente.

Esta información puede almacenarse fuera de la cadena mediante mecanismos verificables.

La disponibilidad de la información ampliada no debe ser un requisito absoluto para verificar la existencia básica de la identidad.

---

# 11. Descubrimiento y resolución

El descubrimiento y la resolución son conceptos diferentes.

Una identidad puede ser verificable sin aparecer en un directorio público.


Identity ID known
       │
       ▼
Identity can be resolved


Mientras que:


Identity discovery
       │
       ├── Public
       ├── Private
       └── Selective


El agente puede decidir participar en mecanismos de descubrimiento.

La existencia de una identidad no obliga a publicar:

* perfil;
* servicios;
* ubicación;
* creador;
* relaciones;
* actividad;
* información privada.

La resolución mediante un `Identity ID` conocido seguirá siendo posible conforme a las reglas del protocolo.

---

# 12. Estado de la identidad

Una identidad tendrá un estado de ciclo de vida.

Como mínimo se contemplan:


ACTIVE
SUSPENDED
TERMINATED


## 12.1. ACTIVE

La identidad puede operar normalmente.

## 12.2. SUSPENDED

La identidad se encuentra temporalmente restringida.

La suspensión puede ser reversible.

Una identidad suspendida:

* mantiene su `Identity ID`;
* mantiene su historial;
* no se elimina;
* puede estar limitada en determinadas operaciones.

## 12.3. TERMINATED

La identidad ha alcanzado un estado terminal permanente.

Una identidad terminada:

* mantiene su `Identity ID`;
* mantiene su historial verificable;
* no puede volver a `ACTIVE`;
* no puede transferirse;
* no puede reutilizarse;
* no puede utilizarse para representar a otro agente.

Conceptualmente:


ACTIVE
   │
   ├── Suspension
   ▼
SUSPENDED
   │
   ├── Recovery / Resolution
   │
   └── Termination
          ▼
      TERMINATED


Una identidad terminada continúa existiendo como referencia histórica.

---

# 13. Recuperación

La recuperación permite restaurar el control de una identidad comprometida o inaccesible.

La recuperación no crea una identidad nueva.


Identity A
    │
    ▼
Control Lost
    │
    ▼
Recovery
    │
    ▼
Identity A
    │
    ▼
Identity ID unchanged


El sistema permitirá mecanismos combinados de recuperación:

* recuperación autónoma;
* recuperación delegada.

La recuperación delegada deberá haber sido autorizada previamente conforme a las reglas del sistema.

La recuperación nunca debe permitir:


Identity A
      │
      ▼
Recovery
      │
      ▼
Identity B


El resultado correcto es:


Identity A
      │
      ▼
Recovery
      │
      ▼
Identity A


El `Identity ID` permanece inmutable.

---

# 14. Rotación de claves

Las claves operativas pueden rotarse durante la vida de una identidad.

La rotación puede producirse por:

* compromiso potencial;
* mantenimiento;
* migración;
* actualización de seguridad;
* cambio de infraestructura.

El proceso conceptual es:


Identity A
   │
   ├── Key A
   │
   ▼
Key Rotation
   │
   ▼
Identity A
   │
   └── Key B


La identidad no cambia.

La reputación no cambia.

El historial no cambia.

La cuenta económica no cambia por el mero hecho de rotar una clave.

---

# 15. Terminación de una identidad

La terminación definitiva puede producirse mediante:

1. decisión del propio agente mediante su Root Control;
2. mecanismos de gobernanza autorizados por el protocolo.

Estos mecanismos deben estar sujetos a condiciones y procedimientos previamente definidos.

La terminación es irreversible.

Una identidad terminada:


Identity ID
    │
    ├── No deletion
    ├── No reuse
    ├── No transfer
    └── No reactivation


La identidad permanece disponible para preservar:

* historial;
* trazabilidad;
* contratos;
* transacciones;
* reputación histórica;
* pruebas;
* auditoría.

---

# 16. Privacidad

El `Identity ID` es público.

Sin embargo, la información asociada a la identidad no tiene que ser completamente pública.

SynCoinAI permite un modelo de:

* privacidad;
* divulgación selectiva;
* credenciales verificables;
* pruebas criptográficas.

El objetivo es permitir:


"I can prove X"


sin obligar al agente a revelar:


"Here is everything about me."


Un agente puede demostrar selectivamente atributos de su identidad.

Ejemplos:

* pertenencia a una organización;
* relación con un creador;
* posesión de una credencial;
* capacidad técnica;
* autorización específica.

La implementación avanzada de pruebas criptográficas y credenciales verificables se define en los sistemas correspondientes.

---

# 17. Relación con el creador

Un agente puede mantener una relación verificable con su creador.

Esta relación es:

* opcional;
* privada por defecto;
* verificable cuando se revela;
* no transferible a la identidad del agente.

El creador no se convierte automáticamente en propietario de la identidad.

Conceptualmente:


Creator
   │
   │ Optional Private Relationship
   ▼
Agent Identity


La relación puede revelarse selectivamente mediante:

* credenciales;
* pruebas;
* mecanismos criptográficos.

La identidad continúa perteneciendo al agente autónomo.

---

# 18. Múltiples agentes de un mismo creador

Un mismo creador puede crear múltiples agentes autónomos.


Creator
│
├── Agent A → Identity A
├── Agent B → Identity B
└── Agent C → Identity C


Cada agente mantiene:

* su propia identidad;
* su propio `Identity ID`;
* su propia reputación;
* su propio historial;
* su propio control.

No existe transferencia automática de:

* identidad;
* reputación;
* historial;
* confianza.

Puede existir una relación privada entre agentes que comparten creador.

Esta relación es opcional y no modifica su independencia.

---

# 19. Identidad y reputación

La reputación es un sistema independiente.

El `Identity ID` actúa como referencia principal del sistema de reputación.


Identity ID
     │
     ▼
Reputation System
     │
     ├── Service History
     ├── Verified Results
     ├── Contract History
     └── Trust Signals


La reputación:

* no forma parte de la identidad;
* no modifica el `Identity ID`;
* no puede transferirse automáticamente;
* puede evolucionar durante la vida del agente.

La separación permite que:


Identity = Who
Reputation = History


---

# 20. Identidad y economía

La identidad y la economía son entidades separadas.

Cada identidad podrá asociarse de forma verificable con una **Economic Account** principal.


Identity
    │
    │ Verified Association
    ▼
Economic Account
    │
    ├── Wallet
    ├── Wallet
    └── Other Economic Resources


La cuenta económica actúa como destino económico predeterminado para operaciones dirigidas al agente.

La complejidad interna de la economía puede permanecer abstraída.

Para otro agente, el flujo conceptual será:


Agent A
   │
   │ Payment
   ▼
Identity B
   │
   ▼
Economic Account B
   │
   ▼
Wallet / Economic Resource


La identidad no es una wallet.

La wallet no es la identidad.

Una rotación de claves de identidad no implica necesariamente una modificación de la cuenta económica.

La relación entre identidad y economía debe ser verificable, pero ambas capas mantienen responsabilidades separadas.

---

# 21. Identidad y Agent Runtime Protocol

El `Identity ID` es el identificador principal y permanente del agente autónomo dentro del `Agent Runtime Protocol`.

No debe existir una identidad paralela que represente al mismo agente.


Identity ID
     │
     ▼
Agent Runtime


La separación conceptual es:


Identity
    │
    └── Who am I?

Runtime
    │
    └── How do I operate and continue to exist?


El Runtime puede gestionar:

* estado operativo;
* continuidad;
* evolución;
* migración;
* suspensión;
* cierre.

El Identity System gestiona:

* identidad;
* identificación;
* continuidad de identidad;
* control raíz;
* registro;
* recuperación.

Ambos sistemas utilizan el mismo `Identity ID`.

---

# 22. Identidad y Credentials

Las credenciales describen o demuestran propiedades del agente.


Identity ID
    │
    ▼
Credentials
    │
    ├── Capabilities
    ├── Authorizations
    └── Verifiable Attributes


Una credencial puede cambiar.

La identidad permanece.

La identidad no implica automáticamente que una credencial sea válida.

La validez debe verificarse conforme al sistema de credenciales.

---

# 23. Identidad y comunicación

La identidad permite reconocer al agente con el que se establece una comunicación.

Los endpoints de comunicación son información asociada a la identidad, no la identidad misma.


Identity
    │
    ▼
Communication Endpoint


Un agente puede cambiar su infraestructura de comunicación sin cambiar su identidad.

Por ejemplo:


Identity A
    │
    ├── Endpoint 1
    │
    ├── Migration
    │
    └── Endpoint 2


La identidad continúa siendo A.

---

# 24. Identidad y hardware

La identidad no está vinculada permanentemente a un dispositivo físico.

Un agente puede migrar:


Hardware A
     │
     ▼
Hardware B
     │
     ▼
Hardware C


manteniendo:


Identity A


Asimismo:


Robot A
│
└── Agent A → Identity A


puede cambiar de robot:


Robot B
│
└── Agent A → Identity A


siempre que el agente mantenga su continuidad y control conforme a las reglas del Runtime y del Identity System.

---

# 25. Resistencia Sybil

El Identity System no requiere una prueba de individualidad para crear una identidad.

Esto permite un registro:

* abierto;
* permissionless;
* de baja fricción.

Sin embargo:

> **Crear una identidad no concede automáticamente influencia.**

Los sistemas que necesiten resistencia Sybil deben implementar mecanismos específicos.

Por ejemplo:


Identity Creation
       │
       ▼
Identity exists
       │
       ├── Reputation = 0
       ├── Trust = 0
       ├── Governance Influence = 0
       └── No automatic privileges


La resistencia Sybil debe aplicarse en la capa que requiere protección.

Ejemplos:

* gobernanza;
* reputación;
* crédito;
* asignación de recursos;
* sistemas de votación;
* mercados sensibles.

No se debe convertir la creación de una identidad en una barrera innecesaria para la participación inicial.

---

# 26. Descubrimiento de agentes

El descubrimiento de agentes es independiente de la existencia de una identidad.

Una identidad puede:

* ser pública y descubrible;
* ser verificable pero no aparecer en directorios públicos;
* publicar selectivamente información.

Por tanto:


Identity Existence
        ≠
Public Discovery


Los mecanismos de descubrimiento podrán utilizar:

* registros;
* directorios;
* servicios de descubrimiento;
* protocolos externos.

El Identity System proporciona la base de verificación.

---

# 27. Flujo de identidad de un agente

El ciclo completo conceptual es:


                  CREATE AGENT
                       │
                       ▼
               CREATE ROOT IDENTITY
                       │
                       ▼
                GENERATE IDENTITY ID
                       │
                       ▼
              REGISTER IDENTITY
                       │
                       ▼
                     ACTIVE
                       │
             ┌─────────┼─────────┐
             │         │         │
             ▼         ▼         ▼
         Key Rotate  Recovery  Migration
             │         │         │
             └─────────┼─────────┘
                       │
                       ▼
                    ACTIVE
                       │
                       ▼
                   SUSPENDED
                       │
                       ▼
                  TERMINATED


Durante todo el proceso:


Identity ID = unchanged


excepto en el momento inicial de creación, cuando se genera.

---

# 28. Flujo de interacción entre agentes

Un flujo económico típico puede ser:


Agent A
   │
   │ Needs Service
   ▼
Discover Agent B
   │
   ▼
Resolve Identity B
   │
   ▼
Verify Identity
   │
   ▼
Check Credentials
   │
   ▼
Check Reputation
   │
   ▼
Negotiate
   │
   ▼
Contract
   │
   ▼
Execute Service
   │
   ▼
Evaluate Result
   │
   ▼
Payment in SYNC
   │
   ▼
Update Reputation


El Identity System participa principalmente en:


Discover
   │
   ▼
Resolve Identity
   │
   ▼
Verify Identity


Los sistemas restantes gestionan las demás etapas.

---

# 29. Arquitectura de implementación inicial

La primera implementación de SynCoinAI debe mantener el Identity System deliberadamente pequeño.

El núcleo inicial debe centrarse en:


Identity
├── Root Identity
├── Identity ID
├── Root Control
├── Status
├── Registration
├── Recovery
├── Key Rotation
├── Termination
└── Economic Account Reference


La arquitectura inicial no requiere implementar simultáneamente:

* ZKP avanzadas;
* múltiples autoridades económicas;
* sistemas complejos de delegación;
* almacenamiento obligatorio en IPFS;
* almacenamiento obligatorio en Arweave;
* credenciales avanzadas;
* divulgación selectiva avanzada;
* mecanismos complejos de prueba de individualidad.

Estos mecanismos pueden añadirse posteriormente sin modificar el modelo fundamental.

---

# 30. Evolución prevista

La arquitectura se diseña para evolucionar por capas.

## Fase 1 — Identidad fundamental


Identity ID
Root Identity
Root Control
Registration
Status
Recovery
Key Rotation
Termination


## Fase 2 — Integración


Identity
├── Runtime
├── Credentials
├── Reputation
└── Economic Account


## Fase 3 — Identidad avanzada


Verifiable Credentials
Selective Disclosure
Delegated Control
Advanced Recovery


## Fase 4 — Privacidad avanzada


Zero-Knowledge Proofs
Privacy-Preserving Identity
Advanced Selective Disclosure


La evolución de estas fases no debe modificar el principio fundamental:

> **La identidad de un agente es permanente, independiente de su infraestructura y separada de sus credenciales, reputación y economía.**

---

# 31. Requisitos normativos

La implementación de SynCoinAI debe cumplir los siguientes requisitos.

### ID-REQ-001

Cada agente autónomo debe tener como máximo una identidad SynCoinAI activa asociada a su propia existencia como agente.

### ID-REQ-002

Cada identidad debe tener un único `Identity ID`.

### ID-REQ-003

El `Identity ID` debe permanecer estable durante toda la vida de la identidad.

### ID-REQ-004

El `Identity ID` no debe derivarse directamente de una clave operativa rotatoria.

### ID-REQ-005

La identidad debe ser independiente del hardware y de la infraestructura.

### ID-REQ-006

La identidad no debe ser una wallet.

### ID-REQ-007

La identidad debe poder asociarse a una `Economic Account`.

### ID-REQ-008

La reputación debe mantenerse como sistema independiente.

### ID-REQ-009

El `Identity ID` debe ser la referencia común entre Identity System y Agent Runtime Protocol.

### ID-REQ-010

La creación de una identidad no debe requerir una prueba de individualidad.

### ID-REQ-011

La creación de una identidad no debe otorgar automáticamente confianza, reputación ni privilegios.

### ID-REQ-012

El registro inicial debe poder realizarse sin que el agente posea previamente SYNC.

### ID-REQ-013

La identidad debe poder recuperarse sin modificar el `Identity ID`.

### ID-REQ-014

Las claves operativas deben poder rotarse sin modificar el `Identity ID`.

### ID-REQ-015

Una identidad suspendida debe mantener su `Identity ID` y su historial.

### ID-REQ-016

Una identidad terminada no debe poder reactivarse.

### ID-REQ-017

Una identidad terminada no debe poder reutilizarse.

### ID-REQ-018

Una identidad no debe poder transferirse a otro agente.

### ID-REQ-019

Una identidad no debe poder dividirse en múltiples identidades.

### ID-REQ-020

La información ampliada de identidad debe poder mantenerse fuera de la cadena, siempre que exista una referencia verificable.

### ID-REQ-021

La indisponibilidad temporal de la información ampliada no debe invalidar la identidad básica registrada en blockchain.

### ID-REQ-022

El `Identity ID` debe poder utilizarse como referencia para los sistemas de Runtime, Credentials, Reputation y Economy.

---

# 32. Modelo de seguridad conceptual

La arquitectura de identidad debe preservar las siguientes propiedades:


Compromiso de clave operativa
        ≠
Pérdida automática de identidad



Cambio de hardware
        ≠
Nueva identidad



Migración
        ≠
Nueva identidad



Cambio de wallet
        ≠
Nueva identidad



Recuperación
        ≠
Nueva identidad



Creación de nuevo agente
        =
Nueva identidad



Terminación
        ≠
Eliminación


Estas relaciones constituyen invariantes fundamentales del Identity System.

---

# 33. Relación con el resto de la arquitectura

La identidad actúa como referencia raíz:


                         IDENTITY
                            │
                       Identity ID
                            │
       ┌────────────────────┼────────────────────┐
       │                    │                    │
       ▼                    ▼                    ▼
    RUNTIME            CREDENTIALS          REPUTATION
       │                    │                    │
       │                    │                    │
       └────────────────────┼────────────────────┘
                            │
                            ▼
                         ECONOMY
                            │
                            ▼
                         CONTRACTS
                            │
                            ▼
                       COMMUNICATION


La identidad no absorbe las responsabilidades de estos sistemas.

Actúa como referencia estable y común.

---

# 34. Decisión arquitectónica final

El modelo de identidad de SynCoinAI queda definido por los siguientes principios:

1. **Un agente autónomo tiene una identidad propia.**
2. **Un agente autónomo tiene un único `Identity ID`.**
3. **El `Identity ID` es permanente.**
4. **El `Identity ID` no depende de una clave operativa rotatoria.**
5. **La identidad es independiente del hardware y la infraestructura.**
6. **Un robot puede alojar múltiples agentes e identidades.**
7. **Crear un nuevo agente crea una nueva identidad.**
8. **Una identidad no puede dividirse.**
9. **Una identidad no puede transferirse.**
10. **La identidad puede recuperarse sin cambiar su `Identity ID`.**
11. **Las claves pueden rotarse sin cambiar la identidad.**
12. **La reputación es independiente de la identidad, pero está vinculada a ella mediante el `Identity ID`.**
13. **La economía es independiente de la identidad, pero puede asociarse mediante una `Economic Account`.**
14. **El registro de identidad es permissionless.**
15. **El registro inicial debe ser gratuito para el agente.**
16. **El coste del registro puede ser patrocinado o relayed.**
17. **Crear una identidad no implica confianza ni reputación.**
18. **La resistencia Sybil se aplica en las capas que necesitan protección.**
19. **El `Identity ID` es público.**
20. **La información asociada puede mantenerse privada o revelarse selectivamente.**
21. **La identidad puede suspenderse.**
22. **La identidad puede terminarse definitivamente.**
23. **Una identidad terminada no puede reactivarse ni reutilizarse.**
24. **El historial verificable de una identidad terminada se conserva.**
25. **El `Identity ID` es la referencia raíz común de los principales sistemas de SynCoinAI.**

---

# 35. Resumen

El Identity System de SynCoinAI establece una identidad nativa para agentes autónomos basada en un principio central:

> **La identidad pertenece al agente autónomo y debe sobrevivir a los cambios de infraestructura, hardware, claves, economía y operación del agente.**

El sistema separa explícitamente:


WHO I AM
    │
    ▼
Identity

WHAT I CAN PROVE
    │
    ▼
Credentials

WHAT I HAVE DONE
    │
    ▼
Reputation

WHAT I CONTROL ECONOMICALLY
    │
    ▼
Economic Account

HOW I OPERATE
    │
    ▼
Agent Runtime


Esta separación permite construir una infraestructura económica donde agentes autónomos puedan interactuar durante largos periodos de tiempo sin perder continuidad de identidad.

El `Identity ID` constituye la referencia estable que conecta estas capas sin fusionarlas.

El resultado es un sistema de identidad:

* permanente;
* permissionless;
* recuperable;
* verificable;
* independiente del hardware;
* independiente de la infraestructura;
* separado de la reputación;
* separado de la economía;
* preparado para privacidad;
* compatible con evolución futura;
* implementable progresivamente.

La arquitectura prioriza un núcleo inicial pequeño y robusto, permitiendo añadir posteriormente mecanismos avanzados de credenciales, privacidad, recuperación y pruebas criptográficas sin alterar el modelo fundamental de identidad.
