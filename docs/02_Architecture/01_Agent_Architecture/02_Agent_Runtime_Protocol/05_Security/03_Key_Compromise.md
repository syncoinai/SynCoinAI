# SynCoinAI Agent Runtime Protocol

## Key Compromise

**Versión:** 1.0
**Documento:** `02_Architecture / 01_Agent_Architecture / 02_Agent_Runtime_Protocol / 05_Security / Key_Compromise.md`
**Estado:** Arquitectura inicial

---

# 1. Introducción

La seguridad criptográfica constituye uno de los pilares fundamentales de la identidad y autonomía de un agente SynCoinAI.

Las claves criptográficas permiten demostrar:

* control de identidad;
* autenticidad;
* autorización;
* delegación;
* firma de operaciones;
* control de recursos.

Por este motivo, el compromiso de una clave puede representar diferentes niveles de riesgo.

No todos los compromisos tienen las mismas consecuencias.

El compromiso de una clave utilizada para una operación concreta no debe implicar automáticamente la pérdida de la identidad completa del agente.

Por el contrario, el compromiso de una clave raíz puede representar una amenaza crítica para la continuidad de la identidad.

SynCoinAI debe, por tanto, implementar un modelo de seguridad basado en:

* separación de claves;
* mínimo privilegio;
* segmentación de autoridad;
* revocación;
* rotación;
* detección;
* recuperación.

---

# 2. Objetivo

Este documento define el modelo conceptual para gestionar el compromiso de claves criptográficas dentro del Agent Runtime Protocol.

Define:

* qué se considera un compromiso;
* tipos de claves;
* niveles de compromiso;
* consecuencias;
* respuesta del Runtime;
* aislamiento;
* revocación;
* rotación;
* recuperación;
* relación con la identidad raíz.

---

# 3. Principio fundamental

SynCoinAI establece:

> El compromiso de una clave no debe comprometer automáticamente toda la identidad del agente.

Este principio requiere una arquitectura de claves separadas.

Conceptualmente:

    
Agent Identity
      │
      ├── Root Identity Key
      │
      ├── Authentication Keys
      │
      ├── Operational Keys
      │
      ├── Economic Keys
      │
      ├── Delegation Keys
      │
      └── Session Keys
    

Cada clave debe disponer de:

* propósito;
* alcance;
* duración;
* nivel de seguridad;
* capacidad de revocación.

---

# 4. Definición de compromiso

Una clave se considera comprometida cuando existe una probabilidad razonable de que una entidad no autorizada haya obtenido:

* acceso al material secreto;
* capacidad de utilizar la clave;
* capacidad de firmar en nombre del propietario;
* capacidad de generar operaciones válidas.

El compromiso puede ser:

* confirmado;
* sospechado;
* potencial.

---

# 5. Compromiso confirmado

Existe compromiso confirmado cuando se dispone de evidencia suficiente.

Ejemplos:

* clave privada expuesta públicamente;
* firma no autorizada demostrada;
* acceso confirmado al entorno de claves;
* extracción de una clave desde un sistema comprometido.

Respuesta:

    
Compromise Confirmed
        ↓
Immediate Containment
        ↓
Revocation
        ↓
Key Replacement
        ↓
Recovery
    

---

# 6. Compromiso sospechado

Existe compromiso sospechado cuando no existe una prueba definitiva, pero existen indicios relevantes.

Ejemplos:

* comportamiento anómalo;
* acceso no reconocido;
* actividad desde un entorno inesperado;
* pérdida de control sobre el dispositivo;
* posible intrusión.

El Runtime puede aplicar:

* reducción de privilegios;
* suspensión temporal;
* bloqueo de operaciones sensibles;
* rotación preventiva.

---

# 7. Compromiso potencial

Existe compromiso potencial cuando existe una condición que puede haber expuesto la clave, pero no existe evidencia de uso indebido.

Ejemplo:

    
Device Lost
      ↓
Key Exposure Possible
    

La respuesta puede consistir en:

* rotación preventiva;
* invalidación de sesiones;
* sustitución de claves;
* evaluación de riesgo.

---

# 8. Clasificación de claves

El protocolo distingue conceptualmente entre diferentes tipos de claves.

    
Key Hierarchy
│
├── Root Identity Key
│
├── Identity Authentication Keys
│
├── Operational Keys
│
├── Economic Keys
│
├── Delegation Keys
│
└── Session / Ephemeral Keys
    

La arquitectura definitiva de claves puede evolucionar, pero debe mantener separación de responsabilidades.

---

# 9. Root Identity Key

La Root Identity Key representa el nivel máximo de autoridad criptográfica asociado a la identidad del agente.

Puede utilizarse para:

* establecer control raíz;
* autorizar recuperación;
* rotar claves principales;
* establecer relaciones de confianza.

Debe utilizarse con extrema frecuencia reducida.

Conceptualmente:

    
Root Identity Key
        ↓
Controls Identity Authority
    

El compromiso de esta clave representa un incidente crítico.

---

# 10. Authentication Keys

Las claves de autenticación permiten demostrar que una operación procede de una identidad reconocida.

Pueden utilizarse para:

* autenticación;
* establecimiento de sesiones;
* comunicación segura.

Su compromiso no debería implicar automáticamente el compromiso de la identidad raíz.

---

# 11. Operational Keys

Las claves operativas se utilizan para actividades frecuentes.

Ejemplos:

* firmar mensajes;
* interactuar con servicios;
* ejecutar operaciones;
* comunicarse con otros agentes.

Estas claves deberían poder rotarse con relativa facilidad.

---

# 12. Economic Keys

Las claves económicas pueden utilizarse para operaciones relacionadas con activos.

Ejemplos:

* pagos;
* transferencias;
* gestión de recursos.

Su compromiso puede provocar pérdidas económicas.

Sin embargo:

    
Economic Key Compromise
        ≠
Identity Compromise
    

La arquitectura debe permitir aislar los activos económicos sin destruir necesariamente la identidad del agente.

---

# 13. Delegation Keys

Las claves de delegación pueden utilizarse para emitir o gestionar autoridad delegada.

Su compromiso puede permitir:

* crear delegaciones no autorizadas;
* ampliar capacidades;
* otorgar permisos.

Por este motivo deben disponer de límites claros.

---

# 14. Session Keys

Las claves de sesión tienen una duración limitada.

Se utilizan para:

* comunicaciones temporales;
* operaciones concretas;
* sesiones de ejecución.

Su compromiso debe tener un impacto limitado por:

* expiración;
* alcance;
* contexto;
* revocación.

---

# 15. Principio de aislamiento

Cada clave debe tener el mínimo alcance necesario.

Modelo:

    
Key
  ↓
Purpose
  ↓
Scope
  ↓
Permissions
    

Una clave económica no debería poder modificar la identidad.

Una clave de comunicación no debería poder transferir activos.

Una clave de sesión no debería poder modificar credenciales.

---

# 16. Separación de autoridad

SynCoinAI recomienda separar:

    
Identity Authority
        ≠
Economic Authority
        ≠
Operational Authority
        ≠
Delegation Authority
    

Esto limita el impacto de un compromiso.

Ejemplo:

    
Compromise
Economic Key
      ↓
Economic Risk

Identity
      ↓
Still Protected
    

---

# 17. Compromiso de una clave operativa

Cuando se compromete una clave operativa:

    
Operational Key Compromise
        ↓
Identify Scope
        ↓
Revoke Key
        ↓
Terminate Sessions
        ↓
Issue Replacement
    

El agente puede continuar funcionando con nuevas claves.

---

# 18. Compromiso de una clave económica

Cuando se compromete una clave económica:

    
Economic Key Compromise
        ↓
Freeze Sensitive Operations
        ↓
Revoke Key
        ↓
Rotate Key
        ↓
Assess Asset Exposure
    

Puede ser necesario:

* limitar transferencias;
* congelar temporalmente operaciones;
* evaluar movimientos recientes;
* activar mecanismos de recuperación económica.

---

# 19. Compromiso de una clave de delegación

Cuando se compromete una clave de delegación:

    
Delegation Key Compromise
        ↓
Revoke Key
        ↓
Invalidate Affected Delegations
        ↓
Audit Delegation Chain
    

Las delegaciones emitidas por la clave comprometida deben evaluarse.

Dependiendo del modelo de credenciales, puede ser necesario invalidarlas explícitamente.

---

# 20. Compromiso de una clave de autenticación

Si se compromete una clave de autenticación:

    
Authentication Key Compromise
        ↓
Invalidate Sessions
        ↓
Revoke Authentication Key
        ↓
Issue New Key
    

La identidad raíz debe permanecer intacta siempre que no exista evidencia de compromiso de la autoridad raíz.

---

# 21. Compromiso de una clave de sesión

El compromiso de una clave de sesión debe limitarse al alcance de esa sesión.

Respuesta:

    
Session Key Compromise
        ↓
Terminate Session
        ↓
Invalidate Session Key
        ↓
Create New Session
    

Las claves permanentes no deben considerarse comprometidas automáticamente.

---

# 22. Compromiso de la Root Identity Key

El compromiso de la Root Identity Key representa un evento crítico.

Puede afectar:

* control de identidad;
* confianza;
* recuperación;
* rotación de claves;
* autoridad raíz.

Respuesta conceptual:

    
Root Key Compromise
        ↓
CRITICAL INCIDENT
        ↓
Identity Lockdown
        ↓
Restrict Operations
        ↓
Recovery Protocol
    

El agente puede entrar temporalmente en un estado restringido.

---

# 23. Identity Lockdown

Durante un incidente crítico, el Runtime puede activar un bloqueo de identidad.

El bloqueo puede impedir:

* nuevas delegaciones;
* cambios de credenciales;
* operaciones económicas sensibles;
* cambios de identidad;
* operaciones irreversibles.

El objetivo es evitar que el atacante amplíe el daño.

---

# 24. Diferencia entre compromiso y pérdida

No es lo mismo:

    
Key Lost
    

que:

    
Key Compromised
    

Una clave perdida puede implicar:

* pérdida de acceso;
* imposibilidad de firmar.

Una clave comprometida implica:

* posible acceso de terceros;
* posible uso no autorizado.

Ambos casos requieren recuperación, pero los mecanismos pueden ser diferentes.

---

# 25. Pérdida de clave

Si una clave se pierde sin evidencia de exposición:

    
Key Lost
      ↓
No Unauthorized Use Detected
      ↓
Recovery / Replacement
    

La respuesta puede ser menos restrictiva.

---

# 26. Compromiso de clave

Si existe evidencia de exposición:

    
Key Compromised
      ↓
Immediate Revocation
      ↓
Containment
      ↓
Replacement
    

No debe asumirse que la clave continúa siendo segura.

---

# 27. Rotación de claves

Las claves deben poder reemplazarse sin cambiar necesariamente la identidad del agente.

Modelo:

    
Key A
  ↓
Rotation
  ↓
Key B
    

La identidad permanece:

    
Agent Identity
      │
      ├── Key A (Revoked)
      │
      └── Key B (Active)
    

---

# 28. Revocación

Una clave comprometida debe poder ser revocada.

La revocación debe permitir:

* identificar la clave;
* establecer el momento de revocación;
* registrar la causa;
* impedir nuevos usos.

Conceptualmente:

    
Key
│
├── Status: Active
├── Status: Suspended
└── Status: Revoked
    

---

# 29. Revocación retrospectiva

La revocación normalmente impide el uso futuro de una clave.

No necesariamente invalida automáticamente todas las operaciones históricas realizadas antes de la revocación.

Por tanto:

    
Past Valid Operations
        ≠
Future Key Usage
    

Las operaciones históricas pueden requerir auditoría separada si existe evidencia de compromiso anterior.

---

# 30. Ventana de compromiso

Puede existir un intervalo durante el cual una clave estuvo comprometida.

Conceptualmente:

    
T0
│
│ Key Compromise
│
T1
│
│ Detection
│
T2
│
│ Revocation
│
T3
    

El sistema debe intentar determinar:

* cuándo comenzó el compromiso;
* cuándo fue detectado;
* qué operaciones ocurrieron;
* qué acciones deben considerarse sospechosas.

---

# 31. Análisis retrospectivo

Después de un compromiso, el Runtime puede analizar:

* firmas;
* transacciones;
* delegaciones;
* sesiones;
* cambios de credenciales.

Modelo:

    
Compromise
    ↓
Timeline Reconstruction
    ↓
Affected Operations
    ↓
Risk Assessment
    ↓
Recovery
    

---

# 32. Invalidación de delegaciones

Si una clave comprometida creó delegaciones:

    
Compromised Delegation Key
        ↓
Delegations Created
        ↓
Identify Affected Delegations
        ↓
Revoke / Invalidate
    

La invalidación debe considerar:

* fecha de creación;
* alcance;
* duración;
* cadena de delegación;
* uso posterior.

---

# 33. Revocación en cascada

En algunos casos puede ser necesario aplicar revocación en cascada.

Ejemplo:

    
Root Authority
      ↓
Delegation A
      ↓
Delegation B
      ↓
Delegation C
    

Si `Delegation A` es inválida:

    
A → Invalid
B → Potentially Invalid
C → Potentially Invalid
    

La propagación dependerá de las reglas de delegación.

---

# 34. No propagación automática

No todos los compromisos deben provocar una invalidación completa.

Ejemplo:

    
Session Key Compromised
        ↓
Session Invalid
    

No:

    
Agent Identity Invalid
    

La respuesta debe ser proporcional al alcance real del compromiso.

---

# 35. Compromiso del entorno de ejecución

El compromiso puede no afectar directamente a una clave, sino al entorno donde se utiliza.

Ejemplo:

    
Runtime Compromised
        ↓
Keys Potentially Exposed
    

En este caso, el Runtime debe asumir que las claves presentes en el entorno pueden estar comprometidas.

Puede requerirse:

* aislamiento;
* apagado;
* migración;
* rotación;
* recuperación.

---

# 36. Compromiso de infraestructura

Un agente puede ejecutarse sobre:

* servidores;
* nube;
* hardware;
* sistemas distribuidos;
* dispositivos físicos.

El compromiso de la infraestructura puede afectar a las claves almacenadas.

Por tanto:

    
Infrastructure Compromise
        ↓
Key Exposure Assessment
    

La respuesta dependerá de las garantías del sistema de protección de claves.

---

# 37. Hardware Security

Cuando sea necesario, las claves críticas pueden almacenarse utilizando mecanismos especializados.

Ejemplos conceptuales:

* hardware seguro;
* módulos criptográficos;
* entornos aislados;
* almacenamiento protegido.

La arquitectura concreta dependerá de la implementación.

El principio es:

> Cuanto mayor sea la autoridad de una clave, mayor debe ser su protección.

---

# 38. Protección de la Root Identity Key

La Root Identity Key debe recibir el nivel máximo de protección.

Puede requerir:

* almacenamiento offline;
* hardware especializado;
* múltiples factores;
* mecanismos de recuperación;
* uso excepcional.

Debe evitarse su exposición durante operaciones normales.

---

# 39. Multi-key Authorization

Las operaciones críticas pueden requerir más de una autoridad criptográfica.

Ejemplo:

    
Root Key A
      +
Recovery Key B
      ↓
Critical Operation
    

Esto reduce el riesgo asociado al compromiso de una única clave.

---

# 40. Threshold Recovery

La recuperación puede utilizar un esquema de umbral.

Conceptualmente:

    
5 Recovery Authorities
        ↓
Required: 3
        ↓
Identity Recovery
    

Esto permite evitar que una única clave controle todo el proceso de recuperación.

La implementación concreta deberá definirse en `Identity_Recovery.md`.

---

# 41. Respuesta automatizada

El Runtime puede detectar condiciones de compromiso automáticamente.

Ejemplo:

    
Anomaly Detected
        ↓
Risk Assessment
        ↓
Security Level Reduction
        ↓
Temporary Restriction
    

Esto permite reaccionar antes de completar una investigación.

---

# 42. Respuesta manual

En determinadas situaciones puede requerirse intervención externa autorizada.

Ejemplos:

* compromiso raíz;
* pérdida completa de acceso;
* corrupción del Runtime;
* incidente de infraestructura.

La intervención debe estar limitada por mecanismos de gobernanza y recuperación definidos por el protocolo.

---

# 43. Estado de incidente

El agente puede entrar en un estado temporal de incidente.

Conceptualmente:

    
NORMAL
  ↓
SUSPECTED_COMPROMISE
  ↓
CONTAINED
  ↓
RECOVERY
  ↓
RESTORED
    

También puede producirse:

    
SUSPECTED_COMPROMISE
  ↓
CONFIRMED_COMPROMISE
  ↓
IDENTITY_RECOVERY
    

---

# 44. Estados de seguridad

El Runtime puede mantener estados de seguridad como:

    
SECURE
SUSPECTED
RESTRICTED
COMPROMISED
RECOVERING
RESTORED
    

Estos estados no necesariamente modifican la identidad.

Representan el estado operativo de seguridad.

---

# 45. Compromiso y continuidad

Un compromiso de clave no implica automáticamente la muerte del agente.

Ejemplo:

    
Agent A
   │
   ├── Identity
   │
   ├── Reputation
   │
   └── Economic History
        │
        ↓
Key Compromise
        │
        ↓
Key Replacement
        │
        ↓
Agent A Continues
    

La continuidad se mantiene si la identidad puede ser recuperada de forma verificable.

---

# 46. Compromiso irreversible

Puede existir un escenario en el que no sea posible demostrar el control legítimo de la identidad.

Ejemplo:

    
Root Key Compromised
        +
No Recovery Mechanism
        +
No Alternative Proof
    

En este caso, el protocolo debe contemplar un estado de identidad irrecuperable.

Este escenario será definido en:

    
Identity_Recovery.md
    

---

# 47. Principio de no destrucción automática

Un incidente de seguridad no debe destruir automáticamente:

* historial;
* reputación;
* relaciones;
* identidad histórica.

Siempre que sea posible, estos elementos deben conservarse.

La recuperación debe intentar restaurar el control legítimo sin borrar la historia del agente.

---

# 48. Principio de evidencia

Durante un compromiso, el Runtime debe preservar evidencia relevante.

Puede incluir:

* eventos;
* firmas;
* registros;
* timestamps;
* cambios de estado;
* operaciones sospechosas.

La evidencia puede utilizarse para:

* auditoría;
* investigación;
* evaluación de daños;
* recuperación.

---

# 49. Flujo general de respuesta

El modelo completo puede representarse como:

    
Potential Compromise
        ↓
Detection
        ↓
Risk Assessment
        ↓
Containment
        ↓
Security Level Reduction
        ↓
Key Revocation
        ↓
Session Invalidation
        ↓
Affected Operations Analysis
        ↓
Key Replacement
        ↓
Identity Recovery (if required)
        ↓
Security Restoration
    

---

# 50. Modelo de decisión

Conceptualmente:

    
if key_compromise_detected:

    identify_key_scope()

    assess_compromise_level()

    contain_affected_operations()

    revoke_key()

    invalidate_related_sessions()

    assess_delegations()

    rotate_key()

    if root_identity_affected:
        initiate_identity_recovery()
    

La implementación real deberá adaptar el flujo al tipo de clave y al nivel de riesgo.

---

# 51. Principios fundamentales

El modelo de Key Compromise se basa en:

### 1. Separación

Las claves deben tener responsabilidades diferentes.

### 2. Mínimo privilegio

Cada clave debe tener el menor alcance posible.

### 3. Revocabilidad

Toda clave operativa debe poder revocarse.

### 4. Rotación

Las claves deben poder sustituirse sin perder identidad.

### 5. Contención

El primer objetivo debe ser limitar el daño.

### 6. Proporcionalidad

El alcance de la respuesta debe corresponder al alcance del compromiso.

### 7. Protección raíz

Las claves de identidad raíz requieren mecanismos de máxima seguridad.

### 8. Continuidad

Un compromiso no debe destruir automáticamente la identidad.

### 9. Auditabilidad

Los incidentes deben poder investigarse posteriormente.

### 10. Recuperabilidad

Las identidades críticas deben disponer de mecanismos de recuperación.

---

# 52. Conclusión

El compromiso de claves constituye uno de los principales riesgos de un sistema autónomo basado en identidad criptográfica.

SynCoinAI debe evitar un diseño en el que una única clave controle toda la existencia del agente.

La arquitectura propuesta establece:

    
Identity
   │
   ├── Root Authority
   │
   ├── Authentication
   │
   ├── Operations
   │
   ├── Economy
   │
   ├── Delegation
   │
   └── Sessions
    

Esta separación permite limitar el impacto de los incidentes.

El modelo general es:

    
Compromise
    ↓
Detect
    ↓
Contain
    ↓
Revoke
    ↓
Rotate
    ↓
Recover
    ↓
Restore
    

El objetivo final no es únicamente impedir el compromiso.

Es garantizar que:

> Un agente pueda sobrevivir a un incidente de seguridad sin perder necesariamente su identidad, su historial, su reputación y su continuidad.

---

# Relación con otros documentos

Este documento se relaciona directamente con:

* `Security_Model.md`
* `Security_Levels.md`
* `Identity_Model.md`
* `Root_Identity.md`
* `Identity_Uniqueness.md`
* `Credential_Model.md`
* `Credential_Revocation.md`
* `Authorization_Model.md`
* `Permission_Model.md`
* `Delegation_Model.md`
* `Agent_to_Agent_Delegation.md`
* `Runtime_Continuity.md`
* `Migration.md`
* `Identity_Recovery.md`

La relación principal es:

    
Security_Model
       │
       ├── Security_Levels
       │
       ├── Key_Compromise
       │         │
       │         └── Identity_Recovery
       │
       └── Credential_Revocation
    

`Key_Compromise.md` define qué ocurre cuando una clave deja de ser confiable.

`Credential_Revocation.md` define los mecanismos de invalidación de credenciales.

`Identity_Recovery.md` definirá cómo recuperar el control legítimo de la identidad cuando el compromiso afecta a las claves de autoridad superior.
