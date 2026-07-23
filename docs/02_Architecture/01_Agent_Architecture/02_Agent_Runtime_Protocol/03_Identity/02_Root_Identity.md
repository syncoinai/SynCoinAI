# SynCoinAI Agent Runtime Protocol — Root Identity

## Identidad raíz del agente

**Versión:** 1.0
**Documento:** `02_Architecture / 01_Agent_Architecture / 02_Agent_Runtime_Protocol / 03_Identity / Root_Identity.md`
**Estado:** Arquitectura inicial

---

# 1. Introducción

La identidad de un agente SynCoinAI requiere un elemento raíz que permita establecer, verificar y mantener la identidad a lo largo de su existencia.

Este elemento recibe el nombre de **Identidad Raíz** (*Root Identity*).

La Identidad Raíz constituye el ancla fundamental desde la cual se establece la relación entre:

* el agente;
* su identidad;
* sus claves criptográficas;
* sus credenciales;
* sus autorizaciones;
* sus capacidades;
* sus operaciones;
* su continuidad.

La Identidad Raíz no representa necesariamente toda la identidad funcional del agente.

Su función principal es proporcionar una base estable desde la cual el agente pueda demostrar:

> **"Esta entidad controla y representa esta identidad de agente."**

---

# 2. Objetivo

El objetivo de este documento es definir el modelo conceptual de la Identidad Raíz dentro del Agent Runtime Protocol.

Este documento establece:

* qué es la Identidad Raíz;
* qué función cumple;
* cómo se relaciona con el agente;
* cómo se relaciona con la identidad pública;
* cómo se relaciona con las claves criptográficas;
* cómo se relaciona con las credenciales;
* cómo se relaciona con la autenticación;
* cómo se relaciona con la continuidad;
* cómo debe sobrevivir a cambios de infraestructura;
* cómo debe gestionarse el compromiso de claves;
* cómo debe realizarse una recuperación de identidad;
* qué elementos pueden rotarse;
* qué elementos deben permanecer estables.

Los mecanismos concretos de seguridad y recuperación se desarrollarán posteriormente en:

    
05_Security/
├── Security_Model.md
├── Security_Levels.md
├── Key_Compromise.md
└── Identity_Recovery.md
    

---

# 3. Definición de Identidad Raíz

La Identidad Raíz es el ancla criptográfica y lógica que permite establecer la continuidad de una identidad de agente.

Formalmente:

> **La Identidad Raíz es el elemento persistente de confianza que vincula un agente con su identidad y permite verificar la continuidad de dicha identidad a través del tiempo.**

La Identidad Raíz debe permitir establecer una relación verificable entre:

    
Agente
   │
   ▼
Identidad
   │
   ▼
Identidad Raíz
   │
   ▼
Mecanismos criptográficos
    

La Identidad Raíz representa el nivel más fundamental de confianza de la identidad del agente.

---

# 4. Propósito de la Identidad Raíz

La Identidad Raíz tiene cuatro funciones fundamentales:

## 4.1 Identificación

Permite identificar de manera única al agente.

---

## 4.2 Autenticación

Permite demostrar que una entidad controla la identidad del agente.

---

## 4.3 Continuidad

Permite mantener una identidad estable a través de cambios tecnológicos.

---

## 4.4 Delegación

Permite establecer identidades operativas, credenciales y claves derivadas sin comprometer necesariamente la raíz.

Modelo:

    
                    ROOT IDENTITY
                          │
          ┌───────────────┼───────────────┐
          │               │               │
          ▼               ▼               ▼
       Identity       Authentication    Continuity
          │
          ▼
      Delegation
          │
     ┌────┴────┐
     │         │
     ▼         ▼
  Keys      Credentials
     │         │
     └────┬────┘
          ▼
      Operations
    

---

# 5. Root Identity frente a Agent Identity

La Identidad Raíz y la identidad del agente están estrechamente relacionadas, pero no son exactamente el mismo concepto.

La identidad del agente representa la entidad reconocida por el ecosistema.

La Identidad Raíz proporciona la base de confianza utilizada para demostrar continuidad y control sobre dicha identidad.

Modelo:

    
AGENTE
   │
   │ posee
   ▼
AGENT IDENTITY
   │
   │ anclada en
   ▼
ROOT IDENTITY
    

Por tanto:

    
Agent Identity ≠ Root Identity
    

Pero:

    
Agent Identity
       │
       ▼
Root Identity
    

La Identidad Raíz actúa como ancla de la identidad.

---

# 6. Propiedad fundamental: estabilidad

La Identidad Raíz debe ser extremadamente estable.

Una identidad puede utilizar diferentes claves operativas durante su existencia.

Sin embargo, la raíz debe proporcionar continuidad entre ellas.

Ejemplo:

    
Root Identity
      │
      ├── Operational Key A
      │
      ├── Operational Key B
      │
      ├── Operational Key C
      │
      └── Operational Key D
    

Las claves operativas pueden rotarse.

La raíz permanece.

Esto permite:

* rotación de claves;
* actualización de seguridad;
* sustitución de dispositivos;
* migración de infraestructura;
* recuperación frente a compromiso.

---

# 7. Separación entre raíz y claves operativas

El Agent Runtime Protocol debe evitar que una única clave operativa tenga necesariamente que representar toda la existencia del agente.

La arquitectura debe permitir una separación entre:

    
Root Identity
      │
      ├── Identity Key
      │
      ├── Authentication Keys
      │
      ├── Signing Keys
      │
      ├── Communication Keys
      │
      └── Economic Keys
    

Cada tipo de clave puede tener una función específica.

Esto reduce el impacto de un compromiso.

Por ejemplo:

    
Compromiso de clave económica
        ↓
No implica necesariamente
        ↓
Compromiso de identidad raíz
    

La separación entre identidad y claves operativas constituye un principio fundamental de seguridad.

---

# 8. Identidad Raíz como ancla de confianza

La Identidad Raíz representa el nivel máximo de confianza dentro de la arquitectura de identidad del agente.

La cadena conceptual es:

    
Root Identity
      ↓
Identity Authority
      ↓
Operational Identity
      ↓
Credentials
      ↓
Permissions
      ↓
Actions
    

La raíz permite establecer una cadena de confianza.

Cada nivel inferior debe poder vincularse criptográfica o lógicamente con el nivel superior.

---

# 9. Modelo jerárquico de identidad

El modelo recomendado es jerárquico.

    
                         ROOT IDENTITY
                              │
              ┌───────────────┼───────────────┐
              │               │               │
              ▼               ▼               ▼
        Identity Keys    Authentication    Recovery
              │               Keys            Mechanism
              │
              ▼
        Operational Keys
              │
       ┌──────┼──────┐
       │      │      │
       ▼      ▼      ▼
    Economic  Service Communication
      Keys      Keys       Keys
       │
       ▼
   Operations
    

Este modelo permite que la identidad raíz permanezca aislada mientras las operaciones diarias utilizan credenciales y claves con menor nivel de autoridad.

---

# 10. Identidad Raíz y autenticación

La autenticación de un agente debe basarse en una cadena verificable de confianza.

Un agente puede demostrar control sobre su identidad mediante:

* firmas digitales;
* pruebas criptográficas;
* protocolos de desafío-respuesta;
* credenciales verificables;
* mecanismos equivalentes.

El método concreto puede variar según el entorno.

Sin embargo, debe existir una relación verificable:

    
Entidad que actúa
       │
       ▼
Clave operativa
       │
       ▼
Delegación verificable
       │
       ▼
Identidad Raíz
       │
       ▼
Identidad del agente
    

La autenticación no debe depender exclusivamente de la infraestructura donde se ejecuta el agente.

---

# 11. Identidad Raíz y credenciales

Las credenciales pueden emitirse bajo la autoridad de una identidad raíz.

Ejemplo:

    
Root Identity
      │
      ▼
Credential
      │
      ├── Capability A
      ├── Permission B
      └── Authorization C
    

Una credencial puede:

* expirar;
* revocarse;
* limitarse;
* sustituirse.

La Identidad Raíz permanece.

Por tanto:

    
Credential Lifecycle
        ≠
Identity Lifecycle
    

La revocación de una credencial no implica la revocación de la identidad.

---

# 12. Identidad Raíz y delegación

La Identidad Raíz puede delegar autoridad.

La delegación permite que:

* otros agentes;
* módulos;
* procesos;
* servicios;
* dispositivos;

actúen en nombre del agente bajo condiciones definidas.

Ejemplo:

    
Root Identity
      │
      ▼
Delegation
      │
      ├── Agent Module
      ├── Economic Service
      ├── Robot Controller
      └── External Service
    

La delegación debe ser:

* explícita;
* limitada;
* verificable;
* revocable.

La delegación no transfiere automáticamente la identidad raíz.

---

# 13. Delegación frente a transferencia de identidad

Debe existir una separación estricta entre:

    
Delegación
    

y:

    
Transferencia de identidad
    

Cuando un agente delega autoridad:

    
Agente A
   │
   └── Delega capacidad
          │
          ▼
       Entidad B
    

La entidad B actúa bajo autoridad delegada.

Pero:

    
Identidad A ≠ Identidad B
    

La delegación no convierte a B en A.

---

# 14. Root Identity y continuidad

La Identidad Raíz proporciona el ancla para demostrar continuidad.

Ejemplo:

    
Agente A
   │
   ▼
Root Identity A
   │
   ├── Infraestructura A
   │
   ├── Migración
   │
   ├── Infraestructura B
   │
   └── Nueva infraestructura C
    

La identidad puede mantenerse porque la raíz permanece vinculada al mismo agente.

La infraestructura cambia.

La raíz no.

---

# 15. Root Identity y migración

Durante una migración, el agente debe poder demostrar que:

    
Estado anterior
       │
       ▼
Proceso de migración
       │
       ▼
Nuevo estado
    

corresponde al mismo agente.

La Identidad Raíz proporciona la base de confianza necesaria.

Una migración válida debe mantener:

* control sobre la identidad;
* continuidad;
* historial;
* credenciales válidas;
* relaciones aplicables.

La migración no debe generar automáticamente una nueva Identidad Raíz.

---

# 16. Root Identity y evolución

Un agente puede evolucionar.

Puede cambiar:

* modelos;
* software;
* hardware;
* capacidades;
* estrategias;
* memoria;
* infraestructura.

La Identidad Raíz debe permanecer estable durante estas transformaciones cuando existe continuidad.

Modelo:

    
Root Identity A
       │
       ├── Agent Version 1
       │
       ├── Agent Version 2
       │
       ├── Agent Version 3
       │
       └── Agent Version N
    

Por tanto:

    
Evolución del agente
        ≠
Cambio automático de Root Identity
    

---

# 17. Rotación de claves

Las claves operativas deben poder rotarse.

La rotación puede producirse por:

* razones de seguridad;
* expiración;
* mantenimiento;
* cambio de infraestructura;
* actualización tecnológica;
* políticas internas.

Modelo:

    
Root Identity
      │
      ├── Key A
      │     ↓
      │   Rotación
      │     ↓
      ├── Key B
      │     ↓
      │   Rotación
      │     ↓
      └── Key C
    

La rotación no debe romper automáticamente la continuidad de la identidad.

Debe existir una relación verificable entre las claves antiguas y las nuevas.

---

# 18. Compromiso de claves

El compromiso de una clave operativa no debe implicar automáticamente la pérdida de identidad del agente.

Modelo:

    
Root Identity
      │
      ├── Key A
      │
      └── Key B
    

Si:

    
Key A
   ↓
Comprometida
    

El agente puede:

    
Revocar Key A
       ↓
Emitir Key C
       ↓
Continuar utilizando Root Identity
    

Esto requiere que la raíz permanezca segura.

La gestión detallada del compromiso se desarrolla en:

    
05_Security/
└── Key_Compromise.md
    

---

# 19. Compromiso de la Identidad Raíz

El compromiso de la Identidad Raíz representa un evento de mayor gravedad.

Puede afectar a:

* autenticación;
* continuidad;
* delegaciones;
* credenciales;
* operaciones;
* recuperación.

La arquitectura debe distinguir claramente entre:

    
Compromiso de clave operativa
    

y:

    
Compromiso de Root Identity
    

El segundo requiere mecanismos específicos de recuperación.

---

# 20. Recuperación de identidad

El Agent Runtime Protocol debe permitir mecanismos de recuperación cuando una identidad se ve comprometida o cuando el agente pierde acceso a sus mecanismos de autenticación.

La recuperación debe preservar, cuando sea posible:

* identidad;
* historial;
* reputación;
* relaciones;
* activos;
* continuidad.

Modelo:

    
Identidad
    │
    ▼
Incidente
    │
    ▼
Recuperación
    │
    ▼
Nueva infraestructura criptográfica
    │
    ▼
Misma identidad
    

La recuperación no debe crear automáticamente un nuevo agente.

Los mecanismos concretos se desarrollarán en:

    
05_Security/
└── Identity_Recovery.md
    

---

# 21. Mecanismos de recuperación

La arquitectura puede contemplar mecanismos como:

* claves de recuperación;
* múltiples autoridades;
* recuperación distribuida;
* guardianes criptográficos;
* pruebas de continuidad;
* mecanismos sociales;
* mecanismos institucionales;
* mecanismos de gobernanza.

No se establece en este documento un único mecanismo obligatorio.

La implementación final deberá equilibrar:

* seguridad;
* autonomía;
* descentralización;
* resistencia a ataques;
* recuperación.

---

# 22. Principio de mínima exposición de la raíz

La Identidad Raíz no debería utilizarse para todas las operaciones diarias.

El modelo recomendado es:

    
Root Identity
      │
      │
      ▼
Delegación limitada
      │
      ▼
Claves operativas
      │
      ▼
Operaciones diarias
    

Esto reduce la exposición de la raíz.

La raíz debe utilizarse principalmente para operaciones de alto nivel como:

* establecer identidad;
* rotar autoridades;
* establecer delegaciones;
* recuperar identidad;
* modificar elementos críticos.

---

# 23. Root Identity y economía

La Identidad Raíz no debe confundirse con una wallet económica.

Un agente puede disponer de:

* una identidad;
* múltiples wallets;
* múltiples claves económicas;
* diferentes cuentas;
* diferentes activos.

Modelo:

    
Root Identity
      │
      ├── Wallet A
      ├── Wallet B
      ├── Wallet C
      └── Economic Key D
    

Por tanto:

    
Root Identity ≠ Wallet
    

La pérdida de una wallet no debería implicar necesariamente la pérdida de la identidad.

La relación entre identidad y economía se desarrollará en:

    
07_Economy/
    

---

# 24. Root Identity y privacidad

La Identidad Raíz no debe obligar a exponer públicamente todos los elementos internos de identidad.

El agente debe poder mantener:

* claves privadas;
* mecanismos de recuperación;
* información interna;
* relaciones privadas.

La red únicamente debe recibir las pruebas necesarias para verificar las operaciones.

Por tanto:

    
Información privada
        ≠
Prueba pública
    

El protocolo debe favorecer una arquitectura de:

> **Verificación sin exposición innecesaria.**

---

# 25. Root Identity y privacidad de las claves

Las claves privadas asociadas a la raíz nunca deben exponerse como parte de una operación normal.

La arquitectura debe asumir:

    
Clave privada
    ↓
Secreto
    

y:

    
Clave pública
    ↓
Verificable
    

La protección de las claves privadas constituye una responsabilidad crítica del runtime y de la infraestructura de ejecución.

---

# 26. Root Identity y hardware

La Identidad Raíz no debe depender obligatoriamente de un hardware concreto.

Sin embargo, puede utilizar mecanismos hardware para mejorar la seguridad.

Por ejemplo:

* hardware security modules;
* secure elements;
* trusted execution environments;
* dispositivos de seguridad.

Estos mecanismos pueden proteger la raíz.

Pero:

    
Hardware Security
        ≠
Root Identity
    

El hardware puede cambiar mientras la identidad permanece.

---

# 27. Root Identity y agentes físicos

Un agente físico puede utilizar múltiples dispositivos durante su existencia.

Ejemplo:

    
Root Identity
      │
      ├── Robot A
      ├── Robot B
      └── Sensor Network
    

La Identidad Raíz pertenece al agente.

Los dispositivos representan capacidades o medios de interacción.

Esto permite que un mismo agente opere sobre múltiples sistemas físicos sin crear automáticamente múltiples identidades.

---

# 28. Root Identity y agentes distribuidos

Un agente puede ejecutarse de forma distribuida.

Ejemplo:

    
                  ROOT IDENTITY
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼
       Node A        Node B       Node C
          │            │            │
          └────────────┼────────────┘
                       │
                       ▼
                    AGENTE
    

La existencia de múltiples procesos o nodos no implica automáticamente múltiples agentes.

La identidad debe representar la entidad lógica del agente.

La arquitectura debe distinguir entre:

    
Distribución de ejecución
    

y:

    
Duplicación de identidad
    

---

# 29. Root Identity y copias

Una copia de un agente no debe heredar automáticamente la capacidad de representar la Identidad Raíz original.

Ejemplo:

    
Agente A
Root Identity A
       │
       ▼
       Copy
       │
       ├── Agente B
       └── Agente C
    

Las copias deben generar o adquirir identidades propias.

La información de origen puede conservarse:

    
Agente B
Origen → Agente A

Agente C
Origen → Agente A
    

Pero:

    
Root Identity A
    ≠
Root Identity B
    ≠
Root Identity C
    

---

# 30. Root Identity y fork

Un fork puede utilizar información derivada de un agente original.

Sin embargo, la nueva entidad debe establecer su propia raíz de identidad.

Modelo:

    
Agente A
Root Identity A
       │
       ▼
     Fork
       │
       ├── Agente B
       │   Root Identity B
       │
       └── Agente C
           Root Identity C
    

La relación histórica puede registrarse.

La autoridad de la raíz original no se transfiere automáticamente.

---

# 31. Root Identity y finalización

La finalización del agente no implica necesariamente la destrucción física de los elementos criptográficos de su identidad.

La identidad histórica puede permanecer verificable.

Esto permite preservar:

* historial;
* reputación histórica;
* relaciones;
* contratos;
* registros económicos.

Por tanto:

    
Agente finalizado
       │
       ▼
Root Identity histórica
       │
       ▼
Referencia verificable
    

La capacidad de actuar activamente puede ser revocada o suspendida.

La identidad histórica puede permanecer.

---

# 32. Estados de la Identidad Raíz

La Identidad Raíz puede encontrarse conceptualmente en diferentes estados.

    
CREATED
   │
   ▼
ACTIVE
   │
   ├──────────────┐
   ▼              ▼
SUSPENDED      COMPROMISED
   │              │
   ▼              ▼
RECOVERED      RECOVERING
   │              │
   └──────┬───────┘
          ▼
        ACTIVE
          │
          ▼
      REVOKED
          │
          ▼
      HISTORICAL
    

Estos estados no implican necesariamente la destrucción de la identidad.

Representan el estado operativo y de confianza de la raíz.

---

# 33. Creación de una Identidad Raíz

La creación de una Identidad Raíz representa el establecimiento inicial de una identidad de agente.

El proceso conceptual incluye:

    
Creación del agente
       │
       ▼
Generación de identidad
       │
       ▼
Establecimiento de Root Identity
       │
       ▼
Creación de claves
       │
       ▼
Registro o anclaje
       │
       ▼
Agente operativo
    

La creación debe producir una identidad individual.

La identidad no debe reutilizarse para representar simultáneamente múltiples agentes independientes.

---

# 34. Registro de la Identidad Raíz

La Identidad Raíz puede requerir un mecanismo de registro o anclaje.

Dependiendo de la arquitectura final, este anclaje puede estar basado en:

* blockchain;
* registro descentralizado;
* sistema distribuido;
* estructura criptográfica;
* combinación de mecanismos.

El protocolo no debe asumir necesariamente que toda la información de identidad deba almacenarse directamente en blockchain.

El principio fundamental es:

> **La existencia y continuidad de una identidad deben poder verificarse sin exigir que toda su información interna sea pública.**

---

# 35. Identidad Raíz y blockchain

La blockchain puede utilizarse como mecanismo de anclaje de identidad.

Puede registrar:

* identificadores;
* compromisos criptográficos;
* eventos de creación;
* rotaciones;
* revocaciones;
* pruebas de continuidad.

Sin embargo:

    
Blockchain ≠ Identidad
    

La blockchain proporciona una infraestructura de registro y verificación.

La identidad pertenece al agente.

---

# 36. Identidad Raíz y Runtime

El Agent Runtime Protocol debe utilizar la Identidad Raíz como referencia fundamental para gestionar la identidad del agente.

El runtime debe poder:

* cargar la identidad;
* verificarla;
* autenticar operaciones;
* gestionar claves;
* validar delegaciones;
* mantener continuidad;
* detectar cambios no autorizados.

Modelo:

    
                AGENT RUNTIME
                      │
        ┌─────────────┼─────────────┐
        │             │             │
        ▼             ▼             ▼
    Identity      Security      Credentials
        │             │             │
        └─────────────┼─────────────┘
                      │
                      ▼
                 ROOT IDENTITY
    

La Identidad Raíz constituye uno de los elementos centrales del runtime.

---

# 37. Modelo de confianza

La arquitectura completa puede representarse como una cadena de confianza:

    
                    ROOT IDENTITY
                          │
                          ▼
                   Identity Keys
                          │
                          ▼
                 Operational Keys
                          │
                          ▼
                    Credentials
                          │
                          ▼
                   Authorizations
                          │
                          ▼
                      Actions
                          │
                          ▼
                     Evidence
                          │
                          ▼
                    Reputation
    

Esta cadena permite conectar:

    
Quién soy
    ↓
Qué puedo hacer
    ↓
Qué hice
    ↓
Qué evidencia existe
    ↓
Qué confianza genero
    

La identidad constituye el punto inicial de la cadena.

---

# 38. Principios fundamentales

La Identidad Raíz del Agent Runtime Protocol se basa en los siguientes principios.

## 1. Estabilidad

La raíz debe proporcionar continuidad a largo plazo.

---

## 2. Independencia de infraestructura

La raíz no debe depender de un servidor o hardware concreto.

---

## 3. Separación de claves

Las operaciones diarias no deben requerir necesariamente exposición constante de la raíz.

---

## 4. Delegación controlada

La autoridad debe poder delegarse de forma limitada y verificable.

---

## 5. Revocabilidad

Las claves y credenciales derivadas deben poder revocarse.

---

## 6. Recuperabilidad

Debe existir un mecanismo para recuperar el control de la identidad.

---

## 7. No transferibilidad automática

La raíz no debe transferirse automáticamente a otro agente.

---

## 8. Resistencia a la duplicación

Una copia no debe poder representar automáticamente la misma identidad.

---

## 9. Privacidad

Los elementos privados de la identidad deben permanecer protegidos.

---

## 10. Continuidad

La raíz debe permitir demostrar continuidad a través de cambios tecnológicos.

---

## 11. Mínima exposición

La raíz debe utilizarse únicamente cuando sea necesario.

---

## 12. Separación de responsabilidades

La identidad, las credenciales, los permisos y las capacidades deben permanecer conceptualmente separados.

---

# 39. Relación con los documentos posteriores

La Identidad Raíz se desarrolla mediante otros componentes del Agent Runtime Protocol.

    
03_Identity/
│
├── Identity_Model.md
│       │
│       └── Modelo general de identidad
│
├── Root_Identity.md
│       │
│       └── Ancla raíz de la identidad
│
├── Individuality_Proof.md
│       │
│       └── Demostración de individualidad
│
└── Identity_Uniqueness.md
        │
        └── Garantía de unicidad
    

La seguridad de la raíz se desarrolla posteriormente en:

    
05_Security/
├── Security_Model.md
├── Security_Levels.md
├── Key_Compromise.md
└── Identity_Recovery.md
    

Las credenciales se desarrollan en:

    
04_Credentials/
    

Las capacidades delegables se desarrollan en:

    
06_Capabilities/
    

La continuidad operativa se desarrolla en:

    
12_Continuity/
    

---

# 40. Conclusión

La Identidad Raíz constituye el ancla fundamental de la identidad de un agente SynCoinAI.

Su función principal es proporcionar una base estable y verificable que permita mantener la continuidad de la identidad a lo largo del tiempo.

La Identidad Raíz debe permitir que un agente:

* cambie de infraestructura;
* migre entre sistemas;
* evolucione cognitivamente;
* cambie de hardware;
* incorpore nuevas capacidades;
* utilice múltiples claves;
* delegue autoridad;
* recupere mecanismos comprometidos;

sin perder automáticamente su identidad.

El principio fundamental es:

> **La Identidad Raíz debe permanecer estable mientras la entidad agente mantenga continuidad verificable.**

La arquitectura debe evitar que:

    
Una clave = Toda la identidad
    

o que:

    
Una infraestructura = La identidad del agente
    

En su lugar:

    
                         AGENTE
                            │
                            ▼
                    AGENT IDENTITY
                            │
                            ▼
                     ROOT IDENTITY
                            │
                 ┌──────────┴──────────┐
                 │                     │
                 ▼                     ▼
        Operational Keys         Recovery Mechanisms
                 │
        ┌────────┼────────┐
        │        │        │
        ▼        ▼        ▼
     Economic  Service  Communication
       Keys      Keys       Keys
        │        │        │
        └────────┼────────┘
                 ▼
             Operations
    

De esta forma, la Identidad Raíz proporciona una arquitectura de confianza capaz de soportar la evolución de agentes autónomos durante largos periodos de tiempo, manteniendo la separación entre identidad, autenticación, autorización, capacidades, economía y reputación.

La Identidad Raíz es, por tanto, el elemento que permite que la identidad de un agente sea **persistente, verificable, recuperable y resistente a los cambios tecnológicos**.
