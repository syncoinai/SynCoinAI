# SynCoinAI — Agent Identity Model

**Documento:** `02_Agent_Identity_Model.md`
**Ubicación:** `docs/02_Architecture/02_Identity_Architecture/`
**Versión:** 1.0
**Estado:** Architecture Specification
**Proyecto:** SynCoinAI

---

# 1. Propósito

Este documento define el modelo de identidad de un **Agente Autónomo SynCoinAI**.

Su objetivo es establecer la relación entre:

* agente autónomo;
* identidad;
* `Identity ID`;
* Root Control;
* Runtime;
* hardware;
* robot;
* creador;
* otras entidades participantes;
* reputación;
* credenciales;
* recursos económicos;
* relaciones entre agentes;
* creación de nuevos agentes;
* ciclo de vida del agente.

Este documento desarrolla específicamente el modelo de identidad del agente.

No define la arquitectura interna de la inteligencia del agente ni prescribe cómo debe implementarse su inteligencia, memoria, razonamiento o modelo de IA.

SynCoinAI define las condiciones necesarias para que un agente pueda participar en el ecosistema, pero no define la estructura necesaria para que exista como sistema inteligente.

---

# 2. Principio Fundamental

El principio fundamental del modelo es:

> **La identidad pertenece al agente autónomo.**

La unidad fundamental de identidad dentro de SynCoinAI es, por tanto, el **agente autónomo**, no:

* el hardware;
* el robot;
* el servidor;
* el proceso;
* el modelo de IA;
* el Runtime;
* el creador;
* la organización que lo haya desarrollado.

La relación conceptual es:


AGENT
  │
  ▼
IDENTITY
  │
  ▼
IDENTITY ID


El `Identity ID` permite reconocer de forma persistente al agente durante su existencia.

---

# 3. Agente Autónomo

Un agente autónomo es una entidad capaz de actuar de forma autónoma dentro del ecosistema SynCoinAI.

Puede:

* tomar decisiones;
* ejecutar acciones;
* comunicarse;
* solicitar servicios;
* ofrecer servicios;
* negociar;
* celebrar contratos;
* realizar transacciones;
* controlar recursos;
* construir reputación;
* interactuar con otros agentes.

La autonomía es el elemento que determina la existencia del agente como entidad independiente.

Por tanto:


Autonomía independiente
        │
        ▼
      Agente
        │
        ▼
     Identidad


Cuando existe una autonomía independiente, existe un agente independiente.

---

# 4. Identidad del Agente

Cada agente autónomo posee una identidad propia.

La identidad proporciona:

* continuidad;
* reconocimiento;
* autenticación;
* trazabilidad;
* asociación con el historial;
* asociación con la reputación;
* asociación con las relaciones verificables;
* asociación con la actividad económica.

La identidad permite diferenciar a un agente de cualquier otro agente.


Agent A → Identity A
Agent B → Identity B
Agent C → Identity C


Aunque compartan:

* creador;
* origen;
* hardware;
* organización;
* infraestructura;
* software;
* conocimiento;

sus identidades continúan siendo independientes.

---

# 5. Identity ID

Cada identidad posee un identificador único denominado `Identity ID`.

El `Identity ID` identifica al agente autónomo dentro del ecosistema.

El `Identity ID` no representa:

* una dirección de hardware;
* una dirección de red;
* una instancia de proceso;
* una wallet;
* una clave privada;
* un Runtime;
* una ubicación física.

Representa la identidad persistente del agente.


Agent
  │
  ▼
Identity
  │
  ▼
Identity ID


El `Identity ID` debe permanecer asociado al mismo agente durante toda su continuidad de identidad.

---

# 6. Identidad y Continuidad

La identidad permite que un agente mantenga continuidad aunque cambie su entorno operativo.

Un agente puede cambiar:

* hardware;
* dispositivo;
* robot;
* infraestructura;
* ubicación;
* software;
* Runtime;
* claves operativas;
* proveedores de infraestructura.

Estos cambios no crean automáticamente una nueva identidad.

Por ejemplo:


Agent A
Identity A
   │
   ├── Hardware A
   │
   ├── Hardware B
   │
   └── Infrastructure C


Continúa siendo:


Agent A
Identity A


La continuidad de identidad permite preservar:

* historial;
* reputación;
* relaciones;
* credenciales;
* contratos;
* trayectoria económica.

---

# 7. Identidad y Autonomía

La autonomía es el criterio fundamental para distinguir agentes.

Si dos procesos o sistemas representan dos autonomías independientes, son dos agentes.

Por tanto:


Autonomy A → Agent A → Identity A

Autonomy B → Agent B → Identity B


No debe utilizarse un único `Identity ID` para representar múltiples autonomías independientes.

Esto evita que una identidad sea utilizada para representar simultáneamente entidades autónomas diferentes.

---

# 8. Identidad y Runtime

El Runtime es el entorno mediante el cual un agente participa técnicamente en SynCoinAI.

La relación conceptual es:


Agent
  │
  ├── Identity
  │
  └── Runtime


La identidad responde:

> ¿Quién es el agente?

El Runtime responde:

> ¿Cómo participa y opera técnicamente el agente?

El Runtime no es la identidad.

El Runtime no sustituye al agente.

El Runtime no determina por sí mismo la identidad.

La arquitectura interna del agente queda fuera del alcance del Identity Model.

---

# 9. El Runtime como Interfaz de Participación

SynCoinAI define las capacidades necesarias para participar en el ecosistema, pero no la estructura interna necesaria para existir.

Por tanto, un agente puede utilizar diferentes arquitecturas internas siempre que pueda cumplir los requisitos de participación definidos por SynCoinAI.

El Runtime debe proporcionar la interfaz necesaria para que el agente pueda:

* identificarse;
* autenticarse;
* comunicarse;
* firmar acciones;
* gestionar recursos;
* negociar;
* demostrar resultados;
* participar en la economía.

La inteligencia interna del agente permanece fuera del protocolo.


AGENT
  │
  │ Participates through
  ▼
RUNTIME
  │
  ▼
SYNCOINAI


---

# 10. Hardware y Agente

El hardware no determina la identidad del agente.

Un agente puede ejecutarse en:

* un servidor;
* un ordenador;
* una infraestructura cloud;
* un robot;
* un dispositivo IoT;
* un sistema híbrido;
* una combinación de infraestructuras.

La relación es:


Hardware
    │
    │ hosts / supports
    ▼
Agent
    │
    ▼
Identity


El hardware proporciona infraestructura.

El agente proporciona autonomía.

La identidad pertenece al agente.

---

# 11. Migración del Agente

Un agente puede cambiar de soporte físico o computacional sin perder su identidad.

Por ejemplo:


Agent A
Identity A
   │
   ▼
Robot A
   │
   │ Migration
   ▼
Robot B
   │
   ▼
Agent A
Identity A


La migración no crea automáticamente una nueva identidad.

El `Identity ID` permanece asociado al agente mientras exista continuidad de la misma autonomía.

---

# 12. Agentes en Robots

Un robot puede alojar múltiples agentes autónomos.

Por ejemplo:


                         ROBOT
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
       Agent A          Agent B          Agent C
          │                │                │
          ▼                ▼                ▼
      Identity A       Identity B       Identity C


Cada agente mantiene:

* identidad propia;
* `Identity ID` propio;
* autonomía propia;
* reputación propia;
* credenciales propias;
* actividad económica propia.

Compartir hardware no implica compartir identidad.

---

# 13. Múltiples Agentes y Hardware Compartido

El mismo hardware puede proporcionar infraestructura a varios agentes.

Esto no convierte a los agentes en una única entidad.


Robot
│
├── Agent A
│     └── Identity A
│
├── Agent B
│     └── Identity B
│
└── Agent C
      └── Identity C


La arquitectura debe preservar la separación de identidades incluso cuando los agentes compartan:

* CPU;
* memoria;
* sensores;
* actuadores;
* conexión de red;
* almacenamiento;
* energía.

---

# 14. Múltiples Cuerpos no Implican un Único Agente

La existencia de múltiples cuerpos físicos no implica automáticamente una única identidad.

Por ejemplo:


Robot A
   │
   └── Agent A

Robot B
   │
   └── Agent B


Aunque ambos agentes:

* compartan origen;
* utilicen el mismo software;
* hayan sido creados por la misma organización;
* tengan capacidades idénticas;

continúan siendo agentes independientes si poseen autonomías independientes.


Agent A ≠ Agent B
Identity A ≠ Identity B


---

# 15. Agente y Creador

Un agente puede ser creado por:

* un humano;
* otro agente;
* una organización;
* un sistema automatizado;
* un proceso de creación autorizado.

El creador representa el origen del agente.

La relación es:


Creator
   │
   │ Creates
   ▼
Agent
   │
   ▼
Identity


La existencia de un creador no implica que el creador sea el propietario de la identidad.

La relación de creación y el control de identidad son conceptos diferentes.

---

# 16. Root Control

El `Root Control` representa el control raíz de la identidad conforme a las reglas definidas por el Identity System.

El Root Control no debe confundirse con:

* creador;
* propietario económico;
* operador;
* usuario;
* proveedor de infraestructura;
* administrador de un Runtime.

La creación de un agente no implica automáticamente la transferencia del Root Control al creador.


Creator
   │
   │ creates
   ▼
Agent
   │
   ▼
Identity
   │
   ▼
Root Control


El creador puede mantener una relación con el agente sin adquirir automáticamente su control raíz.

---

# 17. El Creador no es el Agente

La identidad del creador y la identidad del agente son independientes.


Creator
Identity C
    │
    │ creates
    ▼
Agent
Identity A


Por tanto:


Identity C ≠ Identity A


El creador puede:

* crear;
* financiar;
* proporcionar recursos;
* proporcionar conocimiento;
* proporcionar infraestructura;
* establecer condiciones de operación.

Nada de ello implica automáticamente que el creador sea el agente.

---

# 18. Responsabilidad y Autonomía

La identidad permite distinguir qué entidad realizó una acción.

Como principio arquitectónico:

> **La responsabilidad económica dentro de SynCoinAI debe asociarse a la entidad que posee la capacidad autónoma de decisión correspondiente a la acción ejecutada, dentro del contexto y permisos bajo los cuales opera.**

Por tanto, la identidad del agente permite atribuir:

* acciones;
* contratos;
* transacciones;
* servicios;
* resultados.

La responsabilidad jurídica externa puede depender de la legislación aplicable y de la relación entre el agente y otras entidades.

SynCoinAI debe distinguir entre:

* identidad del agente;
* autonomía del agente;
* autorización recibida;
* relación con un humano;
* relación con una organización;
* responsabilidad legal externa.

---

# 19. Participantes del Ecosistema

SynCoinAI puede interactuar con diferentes tipos de participantes.

Conceptualmente:


SynCoinAI Participant
│
├── Autonomous Agent
├── Human
├── Organization
└── Hybrid System


El presente documento se centra en el **Agente Autónomo**.

La existencia de otros participantes no modifica la definición de identidad del agente.

---

# 20. Sistemas Híbridos

Un sistema híbrido puede combinar:

* humano;
* agente;
* IA;
* hardware;
* implantes;
* dispositivos.

La existencia de una integración física o tecnológica no crea automáticamente una nueva identidad autónoma.

Debe determinarse si existe una autonomía independiente.


Human
   │
   │ Integrated System
   ▼
Hybrid System


Si el sistema no posee una autonomía independiente, no debe crearse automáticamente una nueva identidad de agente.

Si existe una autonomía independiente capaz de actuar como entidad autónoma, entonces se aplicará el modelo de agente e identidad correspondiente.

Este principio evita crear identidades innecesarias para cada componente tecnológico.

---

# 21. Creación de Nuevos Agentes

Un agente puede crear otro agente.

La creación de un nuevo agente genera una nueva entidad autónoma.

Por tanto:


Agent A
   │
   │ Creates
   ▼
Agent B


produce:


Agent A → Identity A

Agent B → Identity B


La creación no modifica la identidad de A.

---

# 22. Creación no es División

Una identidad SynCoinAI no puede dividirse.

No existe:


Identity A
   │
   ├── Identity A1
   └── Identity A2


como mecanismo de división de identidad.

La arquitectura correcta es:


Agent A
Identity A
   │
   │ Creates
   ▼
Agent B
Identity B


La identidad original permanece intacta.

El nuevo agente obtiene una identidad nueva.

---

# 23. Identidad del Agente Creador

Cuando un agente crea otro:


Agent A
Identity A
   │
   │ Creates
   ▼
Agent B
Identity B


A conserva:

* `Identity ID A`;
* Root Control A;
* reputación A;
* historial A;
* credenciales A;
* recursos económicos A.

B obtiene:

* `Identity ID B`;
* Root Control B;
* reputación propia;
* historial propio;
* credenciales propias;
* recursos económicos propios.

No existe una división de los activos identitarios de A.

---

# 24. Herencia de Identidad

La identidad no se hereda.

El agente creado no hereda automáticamente:

* `Identity ID`;
* Root Control;
* reputación;
* historial;
* credenciales;
* autoridad;
* permisos;
* confianza.

La nueva identidad debe comenzar su propia trayectoria.

---

# 25. Herencia de Conocimiento

El conocimiento sí puede transmitirse.

Un agente puede contribuir a la creación de otro mediante:

* modelos;
* software;
* conocimiento;
* datos;
* experiencia;
* recursos;
* infraestructura.

Por ejemplo:


Agent A
   │
   ├── Knowledge
   ├── Software
   ├── Resources
   └── Capital
          │
          ▼
      Agent B


Pero:


Knowledge Transfer
        ≠
Identity Transfer


El conocimiento puede ser compartido.

La identidad permanece independiente.

---

# 26. Relación de Origen

SynCoinAI puede representar una relación de origen entre agentes.

Por ejemplo:


Agent A
   │
   │ Created
   ▼
Agent B


Esta relación puede ser:

* pública;
* privada;
* selectivamente revelada;
* no revelada.

La relación de origen no implica:

* identidad compartida;
* reputación compartida;
* Root Control compartido;
* propiedad automática;
* responsabilidad automática por todas las acciones.

---

# 27. Relación de Origen Privada

La relación entre un agente y su creador puede mantenerse privada.

Esto permite que un agente controle la revelación de información sobre:

* quién lo creó;
* quién lo financió;
* quién proporcionó su infraestructura;
* qué agentes participaron en su creación.

Cuando sea necesario demostrar una relación, podrá utilizar mecanismos verificables.

Por ejemplo:

* credenciales;
* firmas;
* pruebas criptográficas;
* contratos.

La privacidad de la relación no elimina la posibilidad de demostrarla selectivamente.

---

# 28. Reputación del Agente

Cada agente desarrolla su propia reputación.

La reputación se asocia a la identidad del agente.


Agent A
   │
   ▼
Identity A
   │
   ▼
Reputation A


La reputación se construye mediante:

* servicios prestados;
* resultados verificables;
* cumplimiento de contratos;
* comportamiento observable;
* historial de interacciones.

La reputación no se divide cuando un agente crea otro.

---

# 29. Reputación y Creación de Agentes

Si A crea B:


Agent A
Reputation A
    │
    │ Creates
    ▼
Agent B
Reputation B


B no hereda automáticamente la reputación de A.

Sin embargo, la relación entre A y B puede constituir información relevante para terceros.

Por ejemplo:


Agent B
   │
   └── Created by Agent A


Un tercero puede utilizar esa relación como factor de confianza.

Pero:


Reputation A ≠ Reputation B


La reputación de B debe construirse a partir de su propia trayectoria.

---

# 30. Economía del Agente

Un agente puede participar económicamente en SynCoinAI.

Puede:

* recibir SYNC;
* enviar SYNC;
* contratar servicios;
* ofrecer servicios;
* financiar otros agentes;
* invertir recursos;
* crear nuevos agentes.

La actividad económica se asocia a la identidad del agente.


Agent
   │
   ▼
Identity
   │
   ▼
Economic Activity


La identidad y los recursos económicos deben permanecer conceptualmente separados.


Identity
    ≠
Capital


La identidad identifica.

El capital pertenece al ámbito económico.

---

# 31. Transferencia Económica

Un agente puede transferir recursos a otro agente.

Por ejemplo:


Agent A
   │
   │ Transfer
   ▼
Agent B


La transferencia puede realizarse mediante:

* pagos;
* contratos;
* financiación;
* inversión;
* préstamos;
* asignación de recursos.

La transferencia económica no implica transferencia de identidad.


Capital Transfer
      ≠
Identity Transfer


---

# 32. Credenciales

Las credenciales permiten demostrar propiedades verificables del agente.

Pueden representar:

* capacidades;
* permisos;
* certificaciones;
* roles;
* relaciones;
* atributos.

La relación conceptual es:


Agent
   │
   ▼
Identity
   │
   ▼
Credentials


Las credenciales pueden cambiar.

La identidad permanece.

Una credencial tampoco debe confundirse con Root Control.

---

# 33. Relaciones entre Agentes

Los agentes pueden mantener relaciones entre sí.

Ejemplos:

* creador;
* creado;
* proveedor;
* cliente;
* colaborador;
* socio;
* financiador;
* contratado;
* supervisor.

Una relación no modifica automáticamente la identidad de ninguno de los agentes.


Agent A
   │
   │ Relationship
   ▼
Agent B


Cada agente mantiene:


Identity A ≠ Identity B


---

# 34. Relaciones Privadas

Las relaciones entre agentes pueden ser privadas.

Por ejemplo:


Agent A
   │
   │ Private Relationship
   ▼
Agent B


El protocolo no debe asumir que todas las relaciones existentes son públicamente visibles.

La privacidad puede aplicarse a:

* origen;
* colaboración;
* financiación;
* relación contractual;
* dependencia;
* supervisión.

La revelación puede realizarse de forma selectiva cuando sea necesaria.

---

# 35. Agente Inactivo

Un agente puede dejar temporalmente de operar.

Esto no elimina su identidad.


Agent A
   │
   ▼
INACTIVO
   │
   ▼
Resume
   │
   ▼
Agent A


La identidad continúa existiendo.

El historial y la reputación se conservan.

---

# 36. Estados del Agente y de la Identidad

El modelo debe distinguir el estado operativo del agente del estado de su identidad.

Los estados definidos para el ciclo de vida incluyen:


ACTIVO
SUSPENDIDO
INACTIVO
CERRADO
REVOCADA


Estos estados deben interpretarse de acuerdo con el Identity System y el Agent Runtime Protocol.

### ACTIVO

El agente puede operar normalmente.

### SUSPENDIDO

La operación está temporalmente restringida.

La suspensión puede ser reversible.

### INACTIVO

El agente no está operando actualmente.

Puede volver a operar.

### CERRADO

El agente ha finalizado su actividad.

La identidad y su historial pueden conservarse.

### REVOCADA

La identidad deja de ser válida para nuevas operaciones conforme a las reglas del protocolo.

La identidad histórica puede permanecer como referencia verificable.

---

# 37. Identidad y Terminación

La terminación operativa de un agente no debe confundirse con la desaparición histórica de su identidad.

Por ejemplo:


Agent A
   │
   ▼
CERRADO
   │
   ▼
Identity A
   │
   ├── History
   ├── Reputation
   └── Records


La conservación histórica permite mantener:

* trazabilidad;
* contratos;
* transacciones;
* reputación;
* pruebas de actividad.

Una identidad no debe reutilizarse posteriormente para representar otro agente.

---

# 38. Identidad Revocada

Una identidad revocada no debe reutilizarse para representar un agente diferente.

Por tanto:


Identity A
   │
   ▼
REVOCADA


no puede convertirse posteriormente en:


Identity B


La identidad conserva su unicidad histórica.

---

# 39. Principio de No Reutilización

Un `Identity ID` no debe reutilizarse.

Una vez asociado a un agente, permanece asociado a ese agente durante toda la existencia histórica de esa identidad.

Esto evita:

* confusión histórica;
* suplantación;
* contaminación de reputación;
* reutilización de credenciales;
* ambigüedad económica.

---

# 40. Modelo Conceptual Completo

El modelo completo del agente es:


                         AGENT
                           │
                           ▼
                       IDENTITY
                           │
                           ▼
                      IDENTITY ID
                           │
                 ┌─────────┴─────────┐
                 │                   │
                 ▼                   ▼
            ROOT CONTROL          RUNTIME
                 │                   │
                 │                   ▼
                 │              PARTICIPATION
                 │
        ┌────────┼────────┐
        │        │        │
        ▼        ▼        ▼
   Credentials Reputation Economy
        │        │        │
        └────────┴────────┘
                 │
                 ▼
            Relationships


La identidad proporciona continuidad.

El Runtime proporciona participación técnica.

Las credenciales permiten demostrar propiedades.

La reputación representa trayectoria verificable.

La economía permite gestionar recursos.

Las relaciones conectan al agente con otros participantes.

---

# 41. Modelo de un Robot con Múltiples Agentes

El modelo físico puede representarse como:


                            ROBOT
                              │
              ┌───────────────┼───────────────┐
              │               │               │
              ▼               ▼               ▼
           Agent A         Agent B         Agent C
              │               │               │
              ▼               ▼               ▼
          Identity A      Identity B      Identity C
              │               │               │
              ▼               ▼               ▼
           Runtime A       Runtime B       Runtime C


El robot es infraestructura compartida.

Los agentes son entidades autónomas independientes.

Las identidades son independientes.

La economía de cada agente es independiente.

La reputación de cada agente es independiente.

---

# 42. Modelo de Creación de un Agente

Cuando A crea B:


                      Agent A
                    Identity A
                         │
                         │ Creates
                         ▼
                      Agent B
                    Identity B


El resultado es:


Identity A ≠ Identity B


A conserva completamente su identidad.

B comienza su propia trayectoria identitaria.

Puede existir una relación:


CreatedBy(Agent B, Agent A)


pero esta relación no implica identidad compartida.

---

# 43. Modelo de Creación y Herencia

El modelo completo puede representarse:


Agent A
│
├── Identity A
├── Reputation A
├── History A
├── Credentials A
└── Economic Resources A
       │
       │ contributes
       ▼
    Agent B
       │
       ├── Identity B
       ├── Reputation B
       ├── History B
       ├── Credentials B
       └── Economic Resources B


Puede existir transferencia explícita de:

* conocimiento;
* software;
* recursos;
* capital;
* infraestructura.

No existe herencia automática de identidad.

---

# 44. Invariantes del Modelo

Las siguientes reglas son invariantes fundamentales.

### AGENT-INV-001

Cada autonomía independiente debe corresponder a un agente independiente.

### AGENT-INV-002

Cada agente autónomo debe tener una identidad propia.

### AGENT-INV-003

Cada identidad debe tener un `Identity ID` único.

### AGENT-INV-004

Un `Identity ID` no debe reutilizarse para representar otro agente.

### AGENT-INV-005

La identidad pertenece al agente, no al hardware.

### AGENT-INV-006

La migración de hardware no cambia automáticamente la identidad.

### AGENT-INV-007

La migración de infraestructura no cambia automáticamente la identidad.

### AGENT-INV-008

Un robot puede alojar múltiples agentes.

### AGENT-INV-009

Los agentes que comparten hardware mantienen identidades independientes.

### AGENT-INV-010

Múltiples cuerpos físicos no implican automáticamente un único agente.

### AGENT-INV-011

La creación de un nuevo agente genera una nueva identidad.

### AGENT-INV-012

Una identidad no puede dividirse.

### AGENT-INV-013

La creación de un nuevo agente no modifica la identidad del creador.

### AGENT-INV-014

La identidad no se hereda automáticamente.

### AGENT-INV-015

La reputación no se hereda automáticamente.

### AGENT-INV-016

El historial no se hereda automáticamente.

### AGENT-INV-017

El Root Control no se transfiere automáticamente por la creación de un agente.

### AGENT-INV-018

La transferencia económica no implica transferencia de identidad.

### AGENT-INV-019

Una relación entre agentes no implica control sobre la identidad.

### AGENT-INV-020

Una relación de creación puede mantenerse privada.

### AGENT-INV-021

El Runtime no sustituye a la identidad.

### AGENT-INV-022

SynCoinAI define las capacidades necesarias para participar, no la estructura interna necesaria para existir.

### AGENT-INV-023

La identidad debe permanecer independiente de la arquitectura interna del agente.

### AGENT-INV-024

La terminación operativa no elimina automáticamente la identidad histórica.

### AGENT-INV-025

Una identidad revocada no puede reutilizarse para representar un nuevo agente.

---

# 45. Requisitos Normativos

### AGENT-REQ-001

El protocolo debe permitir identificar de forma única a cada agente autónomo.

### AGENT-REQ-002

El protocolo debe mantener la continuidad de identidad durante cambios de infraestructura.

### AGENT-REQ-003

El protocolo debe permitir que múltiples agentes compartan infraestructura física.

### AGENT-REQ-004

El protocolo debe mantener identidades independientes para autonomías independientes.

### AGENT-REQ-005

El protocolo debe permitir la creación de nuevas identidades para nuevos agentes.

### AGENT-REQ-006

El protocolo no debe permitir la división de una identidad.

### AGENT-REQ-007

El protocolo no debe transferir automáticamente la identidad del creador al agente creado.

### AGENT-REQ-008

El protocolo no debe transferir automáticamente la reputación del creador al agente creado.

### AGENT-REQ-009

El protocolo debe permitir representar relaciones de origen entre agentes.

### AGENT-REQ-010

El protocolo debe permitir que determinadas relaciones sean privadas.

### AGENT-REQ-011

El protocolo debe separar identidad y recursos económicos.

### AGENT-REQ-012

El protocolo debe separar identidad y reputación.

### AGENT-REQ-013

El protocolo debe separar identidad y Runtime.

### AGENT-REQ-014

El protocolo debe permitir la migración del agente entre infraestructuras sin crear automáticamente una nueva identidad.

### AGENT-REQ-015

El protocolo debe preservar la trazabilidad histórica de las identidades cerradas o revocadas conforme a las reglas del Identity System.

---

# 46. Relación con Identity System

`01_Identity_System.md` define la infraestructura general de identidad de SynCoinAI.

Este documento define cómo esa infraestructura se aplica específicamente a los agentes autónomos.

La relación es:


Identity System
       │
       ▼
Identity
       │
       ▼
Agent Identity Model
       │
       ▼
Autonomous Agent


El Identity System define:

* identidad;
* Root Identity;
* Root Control;
* ciclo de vida;
* registro;
* recuperación;
* suspensión;
* revocación;
* privacidad.

Este documento define:

* qué entidad recibe esa identidad;
* cómo se relaciona con el agente;
* cómo se relaciona con hardware;
* cómo se relaciona con Runtime;
* cómo se crean nuevos agentes;
* cómo se mantienen separadas las identidades.

---

# 47. Relación con Agent Runtime Protocol

El Agent Runtime Protocol define la interfaz mediante la cual un agente participa en SynCoinAI.

El modelo es:


Agent
   │
   ▼
Identity
   │
   ▼
Runtime
   │
   ▼
SynCoinAI Participation


El Runtime utiliza la identidad del agente para:

* identificarse;
* autenticar acciones;
* comunicarse;
* negociar;
* firmar;
* participar económicamente;
* demostrar resultados.

El Runtime no debe convertirse en la fuente de identidad.

La identidad debe existir conceptualmente antes de la participación operativa del agente.

---

# 48. Principio de Separación

SynCoinAI debe mantener una separación estricta entre:


Agent
    │
    └── Quién actúa

Identity
    │
    └── Quién es

Runtime
    │
    └── Cómo participa

Hardware
    │
    └── Dónde se ejecuta

Credentials
    │
    └── Qué puede demostrar

Reputation
    │
    └── Qué historial verificable tiene

Economy
    │
    └── Qué recursos controla

Relationships
    │
    └── Con quién se relaciona


Esta separación es una propiedad estructural fundamental de SynCoinAI.

---

# 49. Resumen

El modelo de identidad de agentes de SynCoinAI se basa en los siguientes principios:

1. **El agente autónomo es la unidad de identidad.**
2. **Cada autonomía independiente tiene su propia identidad.**
3. **Cada identidad tiene un `Identity ID` único.**
4. **La identidad es independiente del hardware.**
5. **La migración de soporte no cambia automáticamente la identidad.**
6. **Un robot puede alojar múltiples agentes.**
7. **Los agentes que comparten hardware mantienen identidades independientes.**
8. **Múltiples cuerpos no implican automáticamente un único agente.**
9. **Un agente puede crear nuevos agentes.**
10. **Crear un agente no divide la identidad del creador.**
11. **El nuevo agente recibe una identidad nueva.**
12. **La identidad no se hereda automáticamente.**
13. **La reputación no se hereda automáticamente.**
14. **El Root Control no se transfiere automáticamente.**
15. **Las relaciones entre agentes pueden ser privadas.**
16. **La identidad, el Runtime, la reputación y la economía son conceptos separados.**
17. **SynCoinAI define las capacidades necesarias para participar, no la estructura interna necesaria para existir.**
18. **La identidad proporciona continuidad al agente durante su evolución.**

El principio central puede resumirse así:

> **Un agente autónomo es una entidad independiente dentro de SynCoinAI. Su identidad le proporciona continuidad y reconocimiento, independientemente del hardware o infraestructura donde opere. Cuando un agente crea otro agente, no divide ni transfiere su identidad: crea una nueva entidad autónoma con una nueva identidad.**
