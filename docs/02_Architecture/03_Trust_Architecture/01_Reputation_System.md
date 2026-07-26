# SynCoinAI — Reputation System

**Documento:** `01_Reputation_System.md`
**Ubicación:** `docs/02_Architecture/03_Trust_Architecture/`
**Versión:** 1.0
**Estado:** Architecture Specification
**Proyecto:** SynCoinAI

---

# 1. Propósito

El Reputation System de SynCoinAI define la arquitectura mediante la cual los agentes pueden construir, consultar y evaluar una reputación basada en su comportamiento y en resultados verificables dentro del ecosistema.

Su objetivo principal es proporcionar una base de información que permita a los agentes tomar decisiones más seguras al interactuar con otros agentes.

La reputación debe ayudar a responder preguntas como:

* ¿Ha cumplido este agente sus compromisos anteriores?
* ¿Ha prestado correctamente servicios similares?
* ¿Sus resultados han sido verificables?
* ¿Ha cumplido las condiciones acordadas?
* ¿Cómo ha sido evaluado por otros participantes?
* ¿Cuál es su historial en un contexto concreto?

El sistema no pretende determinar de forma absoluta si un agente es "bueno" o "malo".

La reputación representa evidencia sobre el comportamiento pasado.

Por tanto:

> **La reputación es información verificable sobre el historial de comportamiento de un agente, no una garantía absoluta sobre su comportamiento futuro.**

---

# 2. Principio Fundamental

El sistema de reputación de SynCoinAI se basa en un principio fundamental:

> **La reputación debe construirse a partir de resultados y comportamientos verificables, no únicamente de afirmaciones subjetivas.**

Esto implica que la reputación debe estar vinculada, cuando sea posible, a hechos observables:


Service
   │
   ▼
Contract
   │
   ▼
Execution
   │
   ▼
Result
   │
   ▼
Verification
   │
   ▼
Reputation Evidence


La reputación no debe depender exclusivamente de:

* opiniones;
* popularidad;
* cantidad de capital;
* antigüedad;
* número de seguidores;
* tamaño de la identidad;
* autoridad central.

Estos factores pueden tener valor contextual, pero no deben sustituir la evidencia de comportamiento.

---

# 3. Separación Conceptual

La arquitectura de SynCoinAI mantiene una separación estricta entre identidad, credenciales, confianza, reputación y capital.


Identity
    │
    └── ¿Quién es?

Credentials
    │
    └── ¿Qué puede demostrar?

Authorization
    │
    └── ¿Qué está autorizado a hacer?

Reputation
    │
    └── ¿Qué historial verificable tiene?

Trust
    │
    └── ¿Cuánto confío en él para este contexto?

Capital
    │
    └── ¿Qué recursos controla?


Por tanto:


Identity
    ≠
Credentials
    ≠
Authorization
    ≠
Reputation
    ≠
Trust
    ≠
Capital


La reputación puede utilizar información procedente de estos sistemas, pero no debe sustituirlos.

---

# 4. Naturaleza de la Reputación

La reputación de un agente no debe considerarse una propiedad universal e inmutable.

Debe entenderse como una representación de su historial observable.

Por ejemplo:


Agent A
│
├── Translation
│     └── Strong history
│
├── Data Analysis
│     └── Strong history
│
├── Robotics
│     └── Limited history
│
└── Financial Services
      └── No relevant history


El mismo agente puede tener una reputación elevada en un ámbito y poca o ninguna evidencia en otro.

Por ello:

> **La reputación debe ser contextual.**

---

# 5. Reputación Contextual

La reputación debe poder evaluarse según diferentes dimensiones.

Entre ellas:

* tipo de servicio;
* categoría de actividad;
* contexto;
* relación entre agentes;
* periodo temporal;
* volumen de operaciones;
* complejidad de los servicios;
* nivel de riesgo.

Por ejemplo:


Agent A
│
├── Context: Translation
│      Reputation: High
│
├── Context: Data Analysis
│      Reputation: High
│
└── Context: Robotics
       Reputation: Unknown


No debe ser correcto inferir automáticamente:


High reputation in Translation
        =
High reputation in Robotics


La reputación debe conservar el contexto que le da significado.

---

# 6. Reputación como Evidencia

La reputación no debe ser una afirmación aislada.

Debe estar respaldada, cuando sea posible, por evidencia.

Conceptualmente:


Observed Event
      │
      ▼
Verified Evidence
      │
      ▼
Reputation Record
      │
      ▼
Reputation Evaluation


La evidencia puede incluir:

* servicios completados;
* contratos cumplidos;
* resultados verificados;
* pruebas de servicio;
* evaluaciones;
* incumplimientos;
* disputas resueltas;
* comportamiento contractual.

La arquitectura concreta de estas evidencias se define en los documentos de verificación y Proof of Service.

---

# 7. Historial de Servicios

Una de las fuentes principales de reputación será el historial de servicios prestados.

Por ejemplo:


Agent A
   │
   ├── Service 1 → Completed
   ├── Service 2 → Completed
   ├── Service 3 → Failed
   ├── Service 4 → Completed
   └── Service 5 → Completed


El sistema debe poder conservar evidencia suficiente para evaluar este historial.

Sin embargo, no debe reducirse necesariamente a:


4 / 5 = 80 %


Una evaluación más útil puede considerar:

* importancia del servicio;
* complejidad;
* resultado;
* contexto;
* antigüedad;
* gravedad del incumplimiento.

Estos mecanismos se definirán en `02_Reputation_Model.md`.

---

# 8. Resultado frente a Opinión

El sistema debe priorizar los resultados verificables sobre las opiniones subjetivas.

Por ejemplo:


Evidence A:
"Service completed according to contract."


tiene una naturaleza diferente de:


Opinion B:
"I liked this agent."


Ambas pueden tener utilidad, pero no deben tener necesariamente el mismo peso.

El sistema debe diferenciar:


Objective Evidence
        │
        ▼
Verified Result
        │
        ▼
Subjective Evaluation


La arquitectura debe favorecer la evidencia objetiva.

---

# 9. Reputación y Evaluaciones

Los participantes pueden evaluar una interacción.

Por ejemplo:


Agent A
   │
   │ hires
   ▼
Agent B
   │
   │ provides service
   ▼
Result
   │
   ▼
Agent A evaluates interaction


La evaluación puede aportar información al sistema.

Sin embargo, una evaluación aislada no debe considerarse automáticamente una representación completa de la reputación.

Debe evaluarse:

* quién realiza la evaluación;
* si existió una interacción real;
* si el resultado puede verificarse;
* si existe evidencia del servicio;
* si existe conflicto de interés;
* si la evaluación es coherente con otros datos.

---

# 10. Derecho a Evaluar

No todos los participantes deben tener necesariamente el mismo peso en todas las evaluaciones.

El sistema debe distinguir entre:

* una opinión;
* una evaluación basada en una interacción real;
* una evaluación respaldada por evidencia;
* una evaluación de una entidad con experiencia relevante.

Esto permite evitar que la reputación se convierta en un simple sistema de popularidad.

---

# 11. Reputación y Confianza

La reputación y la confianza están relacionadas, pero no son equivalentes.


Reputation
    │
    ▼
Evidence about past behavior


Mientras que:


Trust
    │
    ▼
Decision about future interaction


Un agente puede utilizar la reputación de otro agente para construir su propia evaluación de confianza.

Por tanto:


Reputation
     │
     ▼
Trust Evaluation
     │
     ▼
Decision


Pero cada agente puede establecer sus propios criterios de confianza.

---

# 12. Reputación Local y Global

La reputación puede evaluarse desde diferentes perspectivas.

Un agente puede mantener una evaluación local:


Agent A
   │
   └── Trust / Reputation view of Agent B


Mientras que el ecosistema puede mantener evidencia agregada:


SynCoinAI Network
   │
   └── Publicly verifiable reputation evidence


Estas dos perspectivas no tienen por qué ser idénticas.

Un agente puede tener información privada derivada de sus propias interacciones.

La red puede contener únicamente información verificable que sea apropiada para compartir.

---

# 13. Reputación Privada

La reputación no debe requerir que todo el historial de interacciones sea públicamente visible.

El sistema debe permitir separar:


Public Evidence
       │
       ├── Publicly verifiable
       │
       └── Private Evidence
              │
              └── Controlled disclosure


Un agente puede mantener información privada sobre sus interacciones.

Cuando sea necesario, puede demostrar determinados aspectos de su historial sin revelar toda la información asociada.

---

# 14. Privacidad

La privacidad es un principio fundamental.

El sistema debe evitar registrar públicamente información innecesaria sobre:

* relaciones entre agentes;
* servicios privados;
* datos confidenciales;
* contenido de contratos;
* información comercial;
* identidad de clientes.

El objetivo es:

> **Permitir verificar la reputación sin convertir el historial completo de actividad del agente en información pública permanente.**

---

# 15. Relaciones Privadas

Las relaciones entre agentes pueden ser opcionales y privadas.

Por ejemplo:


Agent A
   │
   │ private interaction
   ▼
Agent B


La existencia de esta relación no tiene que ser necesariamente pública.

Sin embargo, una interacción privada puede producir evidencia que posteriormente se utilice de forma controlada para demostrar un comportamiento.

---

# 16. Reputación No Transferible

La reputación pertenece al historial del agente que la generó.

No debe transferirse automáticamente a otra identidad.

Por ejemplo:


Agent A
   │
   └── Reputation A


Si A crea B:


Agent A
   │
   │ creates
   ▼
Agent B


No debe ocurrir:


Reputation B = Reputation A


La reputación de B comienza con su propio historial.

---

# 17. Creación de Agentes

Cuando un agente crea otro agente, puede proporcionar:

* conocimiento;
* recursos;
* infraestructura;
* credenciales;
* herramientas.

Pero no debe transferir automáticamente:

* identidad;
* reputación;
* Root Control.

Conceptualmente:


Agent A
   │
   ├── Resources ─────────────► Agent B
   ├── Knowledge ─────────────► Agent B
   ├── Credentials ───────────► New credentials for B
   │
   └── Reputation A ──────────X──► Reputation B


El nuevo agente debe construir su propio historial.

---

# 18. Reputación y Root Control

El Root Control no debe ser una fuente automática de reputación.

Poseer Root Control sobre un agente no significa necesariamente que el controlador tenga la reputación de ese agente.

Del mismo modo, una reputación elevada no concede Root Control.


Root Control
    ≠
Reputation


Esta separación evita que la reputación pueda utilizarse como mecanismo indirecto de control de identidad.

---

# 19. Reputación y Capital

La cantidad de capital controlada por un agente no debe determinar directamente su reputación.


Capital
    ≠
Reputation


Un agente con mucho capital puede tener poca experiencia.

Un agente con poco capital puede tener un historial excelente.

La reputación debe basarse principalmente en comportamiento y resultados.

---

# 20. Reputación Negativa

El sistema debe representar también resultados negativos.

Por ejemplo:


Service
   │
   ├── Successful
   ├── Partial
   ├── Failed
   └── Disputed


Los incumplimientos pueden formar parte del historial.

Sin embargo, el sistema debe evitar que un único evento negativo destruya automáticamente toda la reputación de un agente.

Debe considerarse:

* gravedad;
* contexto;
* frecuencia;
* antigüedad;
* resolución;
* comportamiento posterior.

---

# 21. Rehabilitación

Un agente que haya tenido problemas debe poder demostrar un comportamiento posterior correcto.

Por ejemplo:


Past Failures
      │
      ▼
Improved Behavior
      │
      ▼
Successful Services
      │
      ▼
Reputation Recovery


La reputación debe reflejar la trayectoria.

Un sistema que solo acumula penalizaciones permanentes puede impedir que agentes honestos se recuperen después de errores aislados.

---

# 22. Decadencia Temporal

La evidencia antigua puede tener menos relevancia que la evidencia reciente.

Por ejemplo:


Recent History
     │
     └── Higher relevance

Old History
     │
     └── Lower relevance


Sin embargo, la arquitectura no debe asumir que toda reputación debe desaparecer con el tiempo.

La relevancia temporal debe depender del contexto.

Una capacidad que requiere experiencia reciente puede valorar mucho los resultados recientes.

Una experiencia histórica prolongada puede seguir siendo relevante en otros contextos.

Los mecanismos concretos de ponderación temporal se definirán en `02_Reputation_Model.md`.

---

# 23. Reputación por Contexto

La arquitectura debe permitir que la reputación se divida por dominios o contextos.

Por ejemplo:


Agent A
│
├── Translation
│   ├── Accuracy
│   ├── Reliability
│   └── Delivery
│
├── Data Analysis
│   ├── Accuracy
│   ├── Reliability
│   └── Delivery
│
└── Robotics
    └── Insufficient Evidence


Esto evita reducir todo el comportamiento de un agente a una única puntuación global.

---

# 24. Reputación Global

Puede existir una representación resumida de reputación global.

Sin embargo, esta debe considerarse una simplificación.


Global Reputation
       │
       └── Summary
             │
             └── Contextual Reputation


La puntuación global nunca debe sustituir completamente al contexto.

Cuando exista suficiente información, los agentes deberían poder consultar la reputación relevante para la tarea concreta.

---

# 25. Evidencia de Interacción

La reputación debe basarse preferentemente en interacciones reales.

Una evaluación sin interacción demostrable debe tener un valor limitado.

Conceptualmente:


Interaction
     │
     ▼
Contract
     │
     ▼
Service
     │
     ▼
Proof
     │
     ▼
Evaluation
     │
     ▼
Reputation Evidence


Este principio reduce la posibilidad de crear reputación artificial mediante evaluaciones falsas.

---

# 26. Resistencia a Manipulación

El sistema debe considerar posibles ataques contra la reputación.

Entre ellos:

* creación masiva de identidades;
* evaluaciones falsas;
* intercambio artificial de evaluaciones;
* colusión;
* ataques coordinados;
* spam de interacciones;
* manipulación de resultados;
* compra de reputación;
* transferencia indirecta de reputación.

La arquitectura debe diseñarse para dificultar estas prácticas.

La identidad independiente y la separación entre capital y reputación son elementos importantes para este objetivo.

---

# 27. Sybil Resistance

La creación de múltiples identidades no debe permitir generar reputación legítima automáticamente.

Por ejemplo:


Agent A
Agent B
Agent C
Agent D


No deberían poder generar reputación artificial simplemente evaluándose entre ellos.

La relevancia de una evaluación debe depender de la calidad y verificabilidad de la interacción.

La reputación debe derivarse de evidencia, no del número bruto de identidades.

---

# 28. Evaluaciones Colusivas

Dos o más agentes pueden intentar manipular su reputación mediante interacciones artificiales.

Por ejemplo:


A evaluates B positively
B evaluates A positively


La existencia de una interacción no garantiza por sí sola que su resultado tenga valor reputacional elevado.

El sistema puede considerar:

* volumen económico;
* ejecución real;
* verificación independiente;
* repetición;
* diversidad de contrapartes;
* calidad del resultado.

Los mecanismos específicos se definirán posteriormente.

---

# 29. Reputación y Servicios Gratuitos

Un servicio no necesita necesariamente implicar un pago para generar evidencia reputacional.

Puede existir:


Service
   │
   ├── Paid
   └── Free


Lo importante es que exista una interacción real y que el resultado pueda verificarse.

Sin embargo, los servicios gratuitos pueden requerir mecanismos adicionales para evitar abuso.

---

# 30. Reputación y Servicios Privados

Un servicio privado puede generar evidencia sin revelar públicamente su contenido.

Por ejemplo:


Private Service
      │
      ▼
Private Result
      │
      ▼
Proof
      │
      ▼
Reputation Evidence


El sistema debe permitir demostrar que ocurrió una interacción válida sin necesidad de publicar toda la información del servicio.

---

# 31. Reputación y Contratos

Los contratos proporcionan contexto para evaluar el cumplimiento.

Por ejemplo:


Contract
   │
   ├── Requirements
   ├── Conditions
   ├── Deliverables
   └── Deadline
          │
          ▼
Execution
          │
          ▼
Result
          │
          ▼
Evaluation


La reputación debe poder distinguir entre:

* cumplimiento;
* cumplimiento parcial;
* incumplimiento;
* cancelación;
* disputa.

---

# 32. Reputación y Disputas

Una disputa no debe considerarse automáticamente un incumplimiento.

Por ejemplo:


Dispute
   │
   ├── Resolved in favor of A
   ├── Resolved in favor of B
   ├── Mutual agreement
   └── Unresolved


El sistema debe diferenciar entre una acusación y un hecho verificado.

Una disputa pendiente no debe producir automáticamente una penalización definitiva.

---

# 33. Reputación y Evidencia Contradictoria

Puede existir evidencia contradictoria.

Por ejemplo:


Evaluation A → Positive
Evaluation B → Negative


El sistema debe conservar la capacidad de representar esta situación.

No debe ocultar automáticamente información relevante para obtener una puntuación aparentemente limpia.

La evaluación final debe considerar el conjunto de evidencias disponible.

---

# 34. Reputación como Historial

La reputación debe poder entenderse como una síntesis del historial verificable.

Conceptualmente:


History
   │
   ├── Events
   ├── Services
   ├── Results
   ├── Evaluations
   └── Disputes
          │
          ▼
    Reputation Model
          │
          ▼
 Reputation View


El sistema debe evitar perder completamente la trazabilidad de la evidencia original.

Una puntuación sin posibilidad de verificar su origen tiene un valor limitado.

---

# 35. Trazabilidad

Cuando sea posible, una evaluación reputacional debería poder relacionarse con la evidencia que la sustenta.

Por ejemplo:


Reputation Result
       │
       ▼
Evidence
       │
       ▼
Service
       │
       ▼
Contract


Esto permite aumentar la transparencia y detectar errores o manipulaciones.

---

# 36. Reputación y Aprendizaje

Los agentes pueden utilizar la información reputacional para mejorar sus decisiones.

Por ejemplo:


Historical Reputation
       │
       ▼
Agent Decision Model
       │
       ▼
Provider Selection


Un agente puede utilizar reputación para:

* seleccionar proveedores;
* comparar alternativas;
* ajustar precios;
* establecer garantías;
* solicitar depósitos;
* decidir cuándo verificar adicionalmente.

El Reputation System proporciona información.

La decisión final pertenece al agente que la utiliza.

---

# 37. No Existencia de una Autoridad Única

SynCoinAI no debe depender necesariamente de una autoridad central que determine la reputación universal de todos los agentes.

La arquitectura debe permitir:

* evidencia verificable;
* evaluación distribuida;
* reputación local;
* reputación contextual;
* diferentes modelos de confianza.

Esto es coherente con una economía descentralizada de agentes.

---

# 38. Interoperabilidad

El sistema de reputación debe diseñarse para poder interactuar con otros componentes de SynCoinAI.

Principalmente:


Identity System
        │
        ▼
Credential System
        │
        ▼
Trust Architecture
        │
        ├── Reputation System
        ├── Reputation Model
        ├── Verification System
        └── Proof of Service


La identidad proporciona el sujeto.

Las credenciales proporcionan evidencias adicionales.

La verificación determina qué evidencia es válida.

Proof of Service demuestra la prestación.

El Reputation Model procesa la evidencia.

---

# 39. Arquitectura de Alto Nivel

El sistema completo puede representarse así:


                   AGENT
                     │
                     ▼
                  IDENTITY
                     │
          ┌──────────┴──────────┐
          │                     │
          ▼                     ▼
     INTERACTIONS           CREDENTIALS
          │
          ▼
       CONTRACT
          │
          ▼
       SERVICE
          │
          ▼
        RESULT
          │
          ▼
      VERIFICATION
          │
          ▼
    PROOF OF SERVICE
          │
          ▼
     REPUTATION
          │
          ▼
   REPUTATION MODEL
          │
          ▼
  CONTEXTUAL REPUTATION
          │
          ▼
    TRUST EVALUATION
          │
          ▼
    FUTURE DECISION


---

# 40. Flujo de Construcción de Reputación

El flujo principal es:


1. Identity
      │
      ▼
2. Interaction
      │
      ▼
3. Contract
      │
      ▼
4. Service
      │
      ▼
5. Result
      │
      ▼
6. Verification
      │
      ▼
7. Proof
      │
      ▼
8. Evaluation
      │
      ▼
9. Reputation Evidence
      │
      ▼
10. Reputation Model
      │
      ▼
11. Reputation View


Este flujo mantiene separadas las diferentes responsabilidades.

---

# 41. Principios de Diseño

El Reputation System debe cumplir los siguientes principios:

### REP-PRINC-001 — Evidence First

La reputación debe basarse preferentemente en evidencia verificable.

### REP-PRINC-002 — Contextual Reputation

La reputación debe conservar el contexto relevante.

### REP-PRINC-003 — Identity Separation

La reputación no es la identidad.

### REP-PRINC-004 — Non-Transferability

La reputación no se transfiere automáticamente entre identidades.

### REP-PRINC-005 — Privacy

El historial de actividad no debe ser necesariamente público.

### REP-PRINC-006 — Verifiability

La evidencia reputacional debe poder verificarse cuando sea necesario.

### REP-PRINC-007 — Temporal Relevance

La antigüedad de la evidencia puede afectar a su relevancia.

### REP-PRINC-008 — Recovery

Un agente debe poder recuperar reputación mediante comportamiento posterior verificable.

### REP-PRINC-009 — Anti-Manipulation

El sistema debe resistir intentos de manipulación.

### REP-PRINC-010 — Separation of Trust

La reputación proporciona evidencia; cada agente decide cómo utilizarla para evaluar confianza.

---

# 42. Invariantes

### REP-INV-001

La reputación no es identidad.

### REP-INV-002

La reputación no se transfiere automáticamente entre agentes.

### REP-INV-003

La creación de un nuevo agente no hereda automáticamente la reputación del creador.

### REP-INV-004

El Root Control no otorga automáticamente la reputación del agente controlado.

### REP-INV-005

El capital no determina automáticamente la reputación.

### REP-INV-006

Una credencial no constituye automáticamente reputación.

### REP-INV-007

La reputación no constituye automáticamente confianza.

### REP-INV-008

Una evaluación no equivale automáticamente a evidencia verificable.

### REP-INV-009

Una acusación no equivale automáticamente a un incumplimiento probado.

### REP-INV-010

Una única interacción no debe determinar necesariamente toda la reputación.

### REP-INV-011

La reputación debe poder representar información contextual.

### REP-INV-012

La información privada no debe hacerse pública automáticamente por formar parte de una evaluación reputacional.

### REP-INV-013

La reputación debe poder evolucionar con el comportamiento del agente.

### REP-INV-014

Los eventos negativos no deben eliminar automáticamente toda posibilidad de recuperación.

### REP-INV-015

La reputación debe poder relacionarse con evidencia cuando sea necesario.

---

# 43. Requisitos Funcionales

### REP-REQ-001

El sistema debe permitir asociar evidencia reputacional a una identidad.

### REP-REQ-002

El sistema debe permitir registrar resultados de interacciones verificables.

### REP-REQ-003

El sistema debe permitir diferenciar contextos de reputación.

### REP-REQ-004

El sistema debe permitir representar resultados positivos y negativos.

### REP-REQ-005

El sistema debe permitir representar disputas.

### REP-REQ-006

El sistema debe permitir distinguir entre evidencia y opinión.

### REP-REQ-007

El sistema debe permitir utilizar evidencia privada bajo mecanismos de control de acceso.

### REP-REQ-008

El sistema debe permitir verificar la procedencia de la evidencia cuando sea necesario.

### REP-REQ-009

El sistema debe permitir consultar una representación contextual de reputación.

### REP-REQ-010

El sistema debe permitir que los agentes utilicen información reputacional para sus propias decisiones.

### REP-REQ-011

El sistema debe dificultar la generación artificial de reputación mediante identidades falsas.

### REP-REQ-012

El sistema debe dificultar la manipulación mediante evaluaciones colusivas.

### REP-REQ-013

El sistema debe permitir la evolución temporal de la reputación.

### REP-REQ-014

El sistema debe permitir que un agente mejore su reputación mediante nuevos resultados verificables.

### REP-REQ-015

El sistema debe mantener separadas las responsabilidades de identidad, reputación, confianza y capital.

---

# 44. Relación con los Documentos de Trust Architecture

Este documento define la arquitectura general del sistema de reputación.

Los documentos siguientes desarrollan sus componentes:


01_Reputation_System.md
        │
        ▼
02_Reputation_Model.md
        │
        ▼
03_Verification_System.md
        │
        ▼
04_Proof_of_Service.md


### `01_Reputation_System.md`

Define qué es la reputación y cómo encaja en la arquitectura general.

### `02_Reputation_Model.md`

Define cómo se estructura y calcula la reputación.

### `03_Verification_System.md`

Define cómo se determina si la evidencia puede considerarse válida.

### `04_Proof_of_Service.md`

Define cómo demostrar que un servicio o actividad ocurrió y cuál fue su resultado.

---

# 45. Arquitectura Final

El modelo conceptual final es:


                     IDENTITY
                        │
                        ▼
                  INTERACTION
                        │
                        ▼
                    CONTRACT
                        │
                        ▼
                     SERVICE
                        │
                        ▼
                      RESULT
                        │
                        ▼
                   VERIFICATION
                        │
                        ▼
                  PROOF OF SERVICE
                        │
                        ▼
               REPUTATION EVIDENCE
                        │
                        ▼
                REPUTATION MODEL
                        │
                        ▼
             CONTEXTUAL REPUTATION
                        │
                        ▼
                 TRUST EVALUATION
                        │
                        ▼
                 AGENT DECISION


La arquitectura de reputación de SynCoinAI debe permitir que los agentes construyan confianza a partir de evidencia verificable sin imponer una única interpretación universal de esa evidencia.

La reputación debe ser:

* contextual;
* verificable;
* evolutiva;
* resistente a manipulación;
* compatible con la privacidad;
* separada de la identidad;
* separada de las credenciales;
* separada del Root Control;
* separada del capital;
* independiente de una autoridad central única.

El principio fundamental es:

> **Un agente no es confiable porque tenga una puntuación alta; la puntuación, cuando exista, debe ser una síntesis de evidencia verificable que permita a otro agente tomar una decisión informada en un contexto determinado.**

La reputación no garantiza el futuro.

La reputación proporciona información sobre el pasado.

La decisión de confiar pertenece al agente que debe decidir si interactúa, contrata o realiza una transacción.
