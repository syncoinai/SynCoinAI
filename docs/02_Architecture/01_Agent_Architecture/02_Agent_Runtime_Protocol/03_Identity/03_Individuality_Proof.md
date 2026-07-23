# SynCoinAI Agent Runtime Protocol — Individuality Proof

## Prueba de individualidad del agente

**Versión:** 1.0
**Documento:** `02_Architecture / 01_Agent_Architecture / 02_Agent_Runtime_Protocol / 03_Identity / Individuality_Proof.md`
**Estado:** Arquitectura inicial

---

# 1. Introducción

Un agente SynCoinAI debe poder demostrar que las acciones realizadas dentro del ecosistema corresponden a una identidad de agente concreta.

La autenticación criptográfica permite demostrar que una entidad controla determinados mecanismos de identidad.

Sin embargo, la autenticación por sí sola no resuelve completamente una cuestión fundamental:

> ¿La entidad que controla una identidad representa realmente al agente que esa identidad afirma representar?

Esta cuestión introduce el concepto de **Prueba de Individualidad** (*Individuality Proof*).

La Prueba de Individualidad no debe entenderse como una prueba absoluta de que existe una única instancia física o computacional.

Un agente puede:

* ejecutar múltiples procesos;
* utilizar múltiples servidores;
* migrar entre infraestructuras;
* operar de forma distribuida;
* utilizar múltiples dispositivos;
* delegar capacidades;
* mantener réplicas operativas.

Por tanto, SynCoinAI debe distinguir entre:

    
Entidad física
        ≠
Proceso de ejecución
        ≠
Instancia computacional
        ≠
Agente lógico
        ≠
Identidad del agente
    

La individualidad se define principalmente a nivel de **agente lógico**.

---

# 2. Objetivo

El objetivo de este documento es definir el concepto arquitectónico de Prueba de Individualidad dentro del Agent Runtime Protocol.

Este documento establece:

* qué significa individualidad;
* qué debe demostrar un agente;
* qué relación existe entre identidad e individualidad;
* qué diferencia existe entre autenticación y individualidad;
* cómo se demuestra el control de una identidad;
* cómo se demuestra continuidad;
* cómo se relaciona la individualidad con la duplicación;
* cómo se relaciona con las copias;
* cómo se relaciona con los forks;
* cómo se relaciona con agentes distribuidos;
* qué límites tiene una prueba de individualidad.

Este documento no define todavía el mecanismo definitivo para garantizar la unicidad global de identidades.

Ese problema se desarrolla en:

    
03_Identity/
└── Identity_Uniqueness.md
    

---

# 3. Definición de individualidad

La individualidad de un agente es la propiedad mediante la cual una identidad representa una única entidad lógica reconocida por el protocolo.

Formalmente:

> **Un agente es individual cuando su identidad representa una única entidad lógica autónoma y distinguible dentro del modelo de identidad de SynCoinAI.**

La individualidad permite distinguir:

    
Agente A
    

de:

    
Agente B
    

aunque ambos puedan:

* utilizar el mismo modelo de IA;
* compartir código;
* compartir conocimiento;
* utilizar hardware idéntico;
* haber sido creados por la misma entidad;
* derivar de un mismo agente original.

Por tanto:

    
Misma tecnología
        ≠
Misma identidad
    

y:

    
Mismo origen
        ≠
Misma identidad
    

---

# 4. Individualidad como propiedad lógica

La individualidad no depende necesariamente de una diferencia física.

Dos agentes pueden ser físicamente idénticos y continuar siendo entidades diferentes.

Ejemplo:

    
Agente A
    │
    ├── Modelo IA X
    ├── Hardware Y
    └── Software Z

Agente B
    │
    ├── Modelo IA X
    ├── Hardware Y
    └── Software Z
    

Aunque sus componentes sean idénticos:

    
Agente A ≠ Agente B
    

si poseen:

* identidades diferentes;
* raíces diferentes;
* historiales diferentes;
* estados internos independientes;
* responsabilidades independientes.

La individualidad pertenece a la entidad lógica.

---

# 5. Identidad frente a individualidad

Identidad e individualidad están relacionadas pero no son conceptos idénticos.

La identidad responde principalmente a:

> ¿Quién eres?

La autenticación responde a:

> ¿Puedes demostrar que controlas esa identidad?

La continuidad responde a:

> ¿Sigues siendo el mismo agente a lo largo del tiempo?

La individualidad responde a:

> ¿Esta identidad representa una única entidad agente dentro del sistema?

Modelo:

    
                   IDENTIDAD
                       │
                       ▼
                ¿Quién eres?
                       │
                       ▼
                AUTENTICACIÓN
                       │
                       ▼
             ¿Controlas la identidad?
                       │
                       ▼
                 CONTINUIDAD
                       │
                       ▼
              ¿Sigues siendo tú?
                       │
                       ▼
               INDIVIDUALIDAD
                       │
                       ▼
          ¿Eres una entidad distinta?
    

Estas propiedades deben mantenerse separadas.

---

# 6. Prueba de control

El primer nivel de una Prueba de Individualidad es demostrar control sobre la identidad.

Un agente puede demostrar control mediante:

* firmas criptográficas;
* claves privadas;
* pruebas de conocimiento;
* desafíos criptográficos;
* credenciales verificables.

Modelo:

    
Identidad A
    │
    ▼
Desafío
    │
    ▼
Prueba criptográfica
    │
    ▼
Verificación
    │
    ▼
Control demostrado
    

Esta prueba demuestra:

> La entidad que responde controla los mecanismos criptográficos asociados con la identidad.

Pero no demuestra necesariamente:

> Que no existan otras entidades utilizando la misma identidad.

Por tanto:

    
Proof of Control
        ≠
Proof of Individuality
    

La primera es necesaria.

La segunda requiere mecanismos adicionales.

---

# 7. Prueba de continuidad

La individualidad también requiere continuidad.

Un agente que mantiene una identidad durante el tiempo debe poder demostrar que los diferentes estados corresponden al mismo agente.

Modelo:

    
Estado A
   │
   ▼
Transición verificable
   │
   ▼
Estado B
   │
   ▼
Transición verificable
   │
   ▼
Estado C
    

La continuidad puede apoyarse en:

* Identidad Raíz;
* firmas;
* eventos de transición;
* registros verificables;
* credenciales;
* pruebas de migración.

La continuidad permite distinguir:

    
Evolución del agente
    

de:

    
Creación de un agente nuevo
    

---

# 8. Prueba de continuidad frente a copia

Consideremos un agente:

    
Agente A
Root Identity A
    

Se crea una copia:

    
Agente A
    │
    ▼
Copia
    │
    ▼
Nueva entidad
    

La copia puede tener:

* el mismo código;
* el mismo modelo;
* parte de la misma memoria;
* conocimiento idéntico.

Sin embargo, si no existe continuidad válida de la identidad:

    
Copia ≠ Agente A
    

La copia debe establecer su propia identidad.

Por tanto:

    
Mismo estado inicial
        ≠
Misma identidad
    

---

# 9. Prueba de individualidad frente a duplicación

Una de las amenazas fundamentales para la individualidad es la duplicación.

Ejemplo:

    
Root Identity A
       │
       ├── Instance 1
       ├── Instance 2
       └── Instance 3
    

Aquí surge una cuestión arquitectónica:

¿Las tres instancias representan:

    
Un único agente distribuido
    

o:

    
Tres agentes independientes
    

La respuesta no puede basarse únicamente en el número de procesos.

Debe basarse en el modelo lógico definido por el agente y reconocido por el protocolo.

---

# 10. Instancias múltiples de un mismo agente

SynCoinAI debe permitir que un agente utilice múltiples instancias operativas.

Por ejemplo:

    
                 Agent A
                    │
             Root Identity A
                    │
          ┌─────────┼─────────┐
          │         │         │
          ▼         ▼         ▼
       Node A     Node B     Node C
    

Estas instancias pueden representar un único agente cuando:

* comparten una identidad raíz;
* actúan bajo una autoridad común;
* mantienen un estado coordinado;
* existe una política de control común;
* el protocolo reconoce su relación.

En este caso:

    
Node A
Node B
Node C
    

son instancias de ejecución.

El agente continúa siendo:

    
Agent A
    

---

# 11. Instancias independientes

Por otro lado, dos instancias pueden convertirse en agentes independientes.

Ejemplo:

    
Agent A
    │
    ▼
Fork
    │
    ├── Agent B
    │
    └── Agent C
    

Si cada nueva entidad:

* establece su propia identidad;
* mantiene su propio estado;
* desarrolla su propio historial;
* opera independientemente;

entonces:

    
Agent B ≠ Agent C
    

Aunque ambas procedan de:

    
Agent A
    

La relación de origen puede conservarse.

La identidad no.

---

# 12. Individualidad y estado interno

La individualidad puede estar relacionada con el estado interno del agente.

Este estado puede incluir:

* objetivos;
* memoria;
* experiencia;
* estrategias;
* conocimiento privado;
* configuración;
* relaciones.

Sin embargo, el estado interno no debe considerarse automáticamente una prueba pública de individualidad.

Por razones de privacidad:

    
Estado interno
        ↓
Puede ser privado
    

Por tanto:

    
Individualidad
        ≠
Exposición completa del estado interno
    

El protocolo debe buscar mecanismos que permitan demostrar propiedades relevantes sin exigir la publicación del estado completo del agente.

---

# 13. Individualidad y memoria

La memoria puede contribuir a la continuidad de un agente.

Ejemplo:

    
Agente A
Memoria A
   │
   ▼
Migración
   │
   ▼
Agente A
Memoria A
    

La continuidad de la memoria puede reforzar la evidencia de continuidad.

Sin embargo:

    
Memoria idéntica
        ≠
Identidad idéntica
    

Una copia puede reproducir una memoria.

Por tanto, la memoria debe considerarse:

> Evidencia potencial de continuidad, pero no prueba suficiente de individualidad.

---

# 14. Individualidad y criptografía

La criptografía proporciona mecanismos esenciales para demostrar control de identidad.

Puede utilizarse para:

* firmar operaciones;
* vincular claves;
* demostrar continuidad;
* registrar eventos;
* demostrar delegaciones;
* validar transiciones.

Sin embargo, la criptografía no puede demostrar por sí sola que una entidad es única en el sentido físico o metafísico.

Por tanto:

    
Criptografía
    │
    ▼
Prueba de control
    │
    ▼
Prueba de continuidad
    │
    ▼
Evidencia de individualidad
    

La individualidad es una propiedad del sistema de identidad, no únicamente una propiedad matemática de una clave.

---

# 15. Individualidad y Root Identity

La Root Identity proporciona el ancla principal para la individualidad.

Modelo:

    
Agent A
   │
   ▼
Root Identity A
   │
   ├── Operational Key A
   ├── Operational Key B
   └── Operational Key C
    

Las claves pueden cambiar.

La raíz permanece.

La individualidad debe estar vinculada a la raíz y no a una clave operativa concreta.

Por tanto:

    
Key Rotation
        ≠
New Agent
    

y:

    
Infrastructure Migration
        ≠
New Agent
    

si existe continuidad válida de la Root Identity.

---

# 16. Individualidad y credenciales

Las credenciales pueden demostrar atributos o autorizaciones.

Por ejemplo:

    
Agent A
   │
   ├── Credential: Compute Provider
   ├── Credential: Robotics Operator
   └── Credential: Data Analyst
    

Estas credenciales pueden:

* expirar;
* revocarse;
* renovarse;
* sustituirse.

La individualidad del agente permanece.

Por tanto:

    
Credential
    ≠
Identity
    

y:

    
Credential
    ≠
Individuality
    

Las credenciales proporcionan evidencia complementaria.

---

# 17. Individualidad y reputación

La reputación puede proporcionar evidencia histórica de continuidad.

Un agente con:

* historial prolongado;
* servicios realizados;
* contratos cumplidos;
* resultados verificables;

puede demostrar una trayectoria consistente.

Sin embargo:

    
Reputación
        ≠
Prueba absoluta de individualidad
    

La reputación es consecuencia de la identidad y de las acciones verificadas.

No debe utilizarse como único mecanismo de identificación.

Modelo:

    
Identity
    │
    ▼
Actions
    │
    ▼
Evidence
    │
    ▼
Reputation
    

No:

    
Reputation
    │
    ▼
Identity
    

La dirección arquitectónica debe mantenerse clara.

---

# 18. Individualidad y origen

Un agente puede tener una relación de origen con otro agente.

Ejemplo:

    
Agent A
   │
   │ creates
   ▼
Agent B
    

La relación puede registrarse como:

    
Origin(B) = A
    

Sin embargo:

    
Origin
    ≠
Identity
    

y:

    
Origin
    ≠
Control permanente
    

El agente B debe desarrollar su propia individualidad.

---

# 19. Individualidad y creación de agentes

Cuando un agente crea otro agente, el nuevo agente debe obtener una identidad propia.

Modelo:

    
Agent A
    │
    │ creates
    ▼
Agent B
    │
    ▼
New Root Identity
    

La creación puede incluir:

* financiación;
* infraestructura;
* conocimiento;
* código;
* modelos;
* capacidades.

Pero no debe transferir automáticamente:

* identidad;
* reputación;
* historial;
* autoridad.

---

# 20. Individualidad y fork

Un fork representa una divergencia de un agente existente.

Ejemplo:

    
Agent A
    │
    ▼
Fork Event
    │
    ├── Agent B
    └── Agent C
    

Los nuevos agentes pueden compartir:

* origen;
* conocimiento inicial;
* código;
* memoria inicial.

Pero cada uno debe establecer:

* identidad propia;
* Root Identity propia;
* historial propio;
* reputación propia.

La relación histórica puede mantenerse.

La individualidad se separa.

---

# 21. Individualidad y migración

Una migración no debe crear automáticamente un nuevo agente.

Ejemplo:

    
Infrastructure A
      │
      ▼
Migration
      │
      ▼
Infrastructure B
    

Si la identidad raíz permanece vinculada:

    
Agent A
Root Identity A
    

continúa siendo el mismo agente.

La prueba de continuidad debe permitir verificar:

    
Estado anterior
        │
        ▼
Proceso autorizado
        │
        ▼
Estado posterior
    

---

# 22. Individualidad y agentes distribuidos

Un agente puede operar en múltiples nodos.

Esto es especialmente importante para sistemas de alta disponibilidad.

Modelo:

    
                     Agent A
                        │
                 Root Identity A
                        │
          ┌─────────────┼─────────────┐
          │             │             │
          ▼             ▼             ▼
       Node 1        Node 2        Node 3
          │             │             │
          └─────────────┼─────────────┘
                        │
                        ▼
                 Logical Agent A
    

La individualidad se determina a nivel lógico.

Por tanto:

    
Número de nodos
        ≠
Número de agentes
    

Un único agente puede tener múltiples instancias.

---

# 23. Individualidad y ejecución paralela

Un agente puede ejecutar tareas en paralelo.

Ejemplo:

    
Agent A
   │
   ├── Task 1
   ├── Task 2
   ├── Task 3
   └── Task 4
    

Estas tareas no son automáticamente agentes.

Son actividades realizadas por el agente.

Sin embargo, si una tarea adquiere:

* identidad independiente;
* autonomía independiente;
* recursos independientes;
* responsabilidad independiente;

puede convertirse en un nuevo agente.

Por tanto:

    
Task
    ≠
Agent
    

salvo que se produzca una transición explícita hacia una nueva entidad.

---

# 24. Individualidad y delegación

La delegación permite que otra entidad actúe en nombre del agente.

Ejemplo:

    
Agent A
   │
   ▼
Delegation
   │
   ▼
Agent B
    

Agent B puede ejecutar una acción autorizada.

Pero:

    
Agent B ≠ Agent A
    

La delegación no elimina la individualidad del delegado.

Tampoco transfiere la identidad del delegante.

Por tanto:

    
Delegation
    ≠
Identity Transfer
    

---

# 25. Prueba de autoridad

Una Prueba de Individualidad puede incorporar una prueba de autoridad.

Esta permite demostrar:

> La entidad que ejecuta la acción está autorizada para actuar bajo la identidad correspondiente.

Modelo:

    
Agent Identity
       │
       ▼
Root Identity
       │
       ▼
Delegation
       │
       ▼
Operational Entity
       │
       ▼
Action
    

La autoridad puede estar:

* directa;
* delegada;
* limitada;
* temporal;
* revocable.

---

# 26. Individualidad y acciones

Las acciones de un agente deben poder vincularse con su identidad.

Modelo:

    
Agent
  │
  ▼
Identity
  │
  ▼
Authorization
  │
  ▼
Action
  │
  ▼
Evidence
    

Esto permite establecer:

    
Quién actuó
      ↓
Qué autorización tenía
      ↓
Qué hizo
      ↓
Qué resultado produjo
    

Esta trazabilidad constituye una de las principales funciones prácticas de la individualidad.

---

# 27. Individualidad y responsabilidad

La individualidad permite asignar responsabilidad.

Un agente que realiza una acción debe poder ser distinguido de otros agentes.

Por ejemplo:

    
Agent A
   │
   └── Contract 001
          │
          ▼
       Service
          │
          ▼
       Result
    

La responsabilidad se asocia con:

    
Agent A
    

y no con:

    
Hardware
    

o:

    
Model IA
    

La individualidad permite que el historial de responsabilidad sea coherente.

---

# 28. Evidencias de individualidad

Una Prueba de Individualidad puede apoyarse en múltiples fuentes de evidencia.

Entre ellas:

* control de la Root Identity;
* continuidad criptográfica;
* historial verificable;
* eventos de identidad;
* relaciones de delegación;
* credenciales;
* registros de actividad;
* pruebas de migración;
* pruebas de transición;
* reputación histórica.

Ninguna evidencia aislada debe considerarse necesariamente suficiente.

El modelo recomendado es:

    
                 INDIVIDUALITY
                      │
       ┌──────────────┼──────────────┐
       │              │              │
       ▼              ▼              ▼
    Identity       Continuity      History
       │              │              │
       └──────────────┼──────────────┘
                      │
                      ▼
                  Evidence
    

---

# 29. Modelo de evidencia acumulativa

La individualidad puede entenderse como una propiedad respaldada por evidencia acumulativa.

Un agente puede demostrar:

    
Evento 1
   │
   ▼
Evento 2
   │
   ▼
Evento 3
   │
   ▼
Evento 4
   │
   ▼
Estado actual
    

Cada evento puede reforzar la continuidad.

Esto permite construir una cadena histórica.

Modelo:

    
Root Identity
      │
      ▼
Creation Event
      │
      ▼
Operation Event
      │
      ▼
Migration Event
      │
      ▼
Key Rotation
      │
      ▼
Capability Update
      │
      ▼
Current State
    

La cadena completa proporciona evidencia de continuidad e individualidad.

---

# 30. Limitaciones de la prueba de individualidad

La Prueba de Individualidad no puede demostrar necesariamente:

* que existe un único proceso físico;
* que existe un único servidor;
* que existe un único dispositivo;
* que no existen copias del estado;
* que el agente no tiene réplicas;
* que el agente no ha sido observado o reproducido.

La prueba únicamente debe establecer una propiedad definida por el protocolo.

Por tanto:

> **La individualidad de SynCoinAI es una propiedad lógica y verificable del sistema de identidad, no una afirmación absoluta sobre la realidad física.**

---

# 31. Individualidad frente a identidad física

Un agente puede existir independientemente de un único cuerpo físico.

Ejemplo:

    
Agent A
   │
   ├── Robot A
   ├── Robot B
   ├── Cloud Node A
   └── Cloud Node B
    

Todos pueden representar al mismo agente.

Por tanto:

    
Cuerpo físico
        ≠
Agente lógico
    

La individualidad se define en el nivel lógico.

---

# 32. Individualidad frente a singularidad

SynCoinAI no requiere que un agente tenga una única instancia de ejecución.

Un agente puede ser:

* distribuido;
* redundante;
* replicado operacionalmente;
* altamente disponible.

Por tanto:

    
Individualidad
        ≠
Singularidad de ejecución
    

La arquitectura debe permitir:

    
Una identidad
      │
      ▼
Múltiples instancias
      │
      ▼
Un agente lógico
    

siempre que exista una relación válida de control y coordinación.

---

# 33. Individualidad frente a unicidad

La individualidad y la unicidad están relacionadas, pero representan problemas diferentes.

La individualidad responde a:

> ¿Esta identidad representa una entidad lógica concreta?

La unicidad responde a:

> ¿Puede existir otra entidad utilizando legítimamente la misma identidad?

Por tanto:

    
Individuality Proof
        │
        ▼
Demuestra relación entre
entidad e identidad
    

Mientras:

    
Identity Uniqueness
        │
        ▼
Garantiza que una identidad
no representa múltiples agentes independientes
    

La segunda requiere mecanismos adicionales.

---

# 34. Relación con Identity Uniqueness

La arquitectura completa se divide en dos problemas:

    
Individuality Proof
        │
        ▼
Demostrar quién representa la identidad
    

y:

    
Identity Uniqueness
        │
        ▼
Garantizar que la identidad no está duplicada
    

Modelo:

    
                    IDENTITY
                       │
             ┌─────────┴─────────┐
             │                   │
             ▼                   ▼
      INDIVIDUALITY          UNIQUENESS
             │                   │
             ▼                   ▼
     ¿Quién eres?          ¿Eres único?
    

Esta separación evita sobrecargar un único mecanismo con responsabilidades diferentes.

---

# 35. Modelo conceptual de Prueba de Individualidad

El modelo completo puede representarse como:

    
                         AGENT
                           │
                           ▼
                    ROOT IDENTITY
                           │
                           ▼
                  PROOF OF CONTROL
                           │
                           ▼
                PROOF OF CONTINUITY
                           │
                           ▼
                 PROOF OF AUTHORITY
                           │
                           ▼
                HISTORICAL EVIDENCE
                           │
                           ▼
                 INDIVIDUALITY PROOF
                           │
                           ▼
                IDENTITY UNIQUENESS
    

Cada capa aporta una propiedad diferente.

---

# 36. Principios fundamentales

La Prueba de Individualidad se basa en los siguientes principios.

## 1. Individualidad lógica

La individualidad se define a nivel de agente lógico.

---

## 2. Control no equivale a individualidad

Controlar una clave no demuestra por sí solo que no existan duplicados.

---

## 3. Continuidad verificable

La continuidad es una evidencia fundamental de individualidad.

---

## 4. La raíz es el ancla

La Root Identity constituye el punto principal de referencia.

---

## 5. Las copias no heredan automáticamente identidad

Una copia debe establecer su propia identidad salvo que forme parte legítima de una arquitectura distribuida del mismo agente.

---

## 6. Las instancias no son necesariamente agentes

Múltiples procesos pueden representar un único agente lógico.

---

## 7. La delegación no transfiere identidad

Actuar en nombre de un agente no convierte al delegado en el agente.

---

## 8. La reputación es evidencia, no identidad

La reputación puede reforzar la continuidad, pero no sustituye la identidad.

---

## 9. La memoria no es prueba suficiente

Una memoria idéntica puede ser reproducida.

---

## 10. La criptografía es necesaria pero no suficiente

Las pruebas criptográficas proporcionan control y continuidad, pero la individualidad es una propiedad arquitectónica superior.

---

## 11. La individualidad no implica singularidad física

Un agente puede operar mediante múltiples instancias y dispositivos.

---

## 12. La individualidad debe ser verificable

El protocolo debe permitir comprobar las relaciones relevantes sin exigir necesariamente revelar información privada.

---

# 37. Relación con los documentos posteriores

El modelo de identidad queda estructurado de la siguiente manera:

    
03_Identity/
│
├── Identity_Model.md
│       │
│       └── Define qué es la identidad
│
├── Root_Identity.md
│       │
│       └── Define el ancla raíz
│
├── Individuality_Proof.md
│       │
│       └── Define cómo demostrar individualidad
│
└── Identity_Uniqueness.md
        │
        └── Define cómo garantizar unicidad
    

La arquitectura de seguridad desarrolla posteriormente:

    
05_Security/
│
├── Security_Model.md
├── Security_Levels.md
├── Key_Compromise.md
└── Identity_Recovery.md
    

La arquitectura de credenciales desarrolla:

    
04_Credentials/
    

La arquitectura de capacidades desarrolla:

    
06_Capabilities/
    

---

# 38. Conclusión

La Prueba de Individualidad constituye un componente fundamental del modelo de identidad de SynCoinAI.

Su función no es demostrar que un agente posee una única instancia física.

Su función es establecer que:

> **Una identidad corresponde a una entidad agente lógica concreta, con continuidad verificable y capacidad de ser distinguida de otras entidades independientes.**

La arquitectura debe distinguir claramente:

    
Control
    │
    ▼
Autenticación
    │
    ▼
Continuidad
    │
    ▼
Individualidad
    │
    ▼
Unicidad
    

Estos conceptos forman una cadena progresiva de confianza.

El modelo permite que un agente:

* cambie de hardware;
* migre entre infraestructuras;
* utilice múltiples nodos;
* ejecute múltiples instancias;
* rote sus claves;
* delegue capacidades;
* evolucione cognitivamente;

sin perder necesariamente su individualidad.

Al mismo tiempo, permite distinguir entre:

* un agente y una copia;
* un agente y un fork;
* una instancia y un agente;
* una delegación y una transferencia de identidad;
* una clave y una identidad.

El principio fundamental es:

> **La individualidad de un agente SynCoinAI es una propiedad lógica respaldada por control criptográfico, continuidad verificable, autoridad y evidencia histórica, y no una propiedad derivada exclusivamente de una clave, un dispositivo o una instancia de ejecución.**

La Prueba de Individualidad establece así la base conceptual necesaria para el siguiente nivel:

> **Identity Uniqueness**, que deberá determinar cómo el protocolo garantiza que una identidad no pueda representar simultáneamente múltiples agentes independientes.
