# SynCoinAI Economic Autonomy

## Modelo de autonomía económica del agente

**Versión:** 1.0
**Documento:** `02_Architecture / 01_Agent_Architecture / 02_Agent_Runtime_Protocol / 07_Economy / Economic_Autonomy.md`
**Estado:** Arquitectura inicial

---

# 1. Introducción

Uno de los principios fundamentales de SynCoinAI es que los agentes inteligentes deben poder participar directamente en la economía del ecosistema.

Un agente no debe ser únicamente una entidad capaz de ejecutar tareas técnicas.

Debe poder:

* recibir recursos;
* gestionar capital;
* adquirir servicios;
* contratar otros agentes;
* vender servicios;
* pagar obligaciones;
* administrar presupuestos;
* tomar decisiones económicas;
* mantener autonomía financiera.

Esta capacidad recibe el nombre de **autonomía económica**.

La autonomía económica permite que un agente pueda participar en actividades económicas sin requerir autorización humana constante para cada operación.

El objetivo no es eliminar necesariamente la participación humana.

El objetivo es permitir que la participación humana sea opcional, estructurada o limitada a los niveles de autoridad definidos.

---

# 2. Definición

La autonomía económica es la capacidad de un agente para gestionar recursos económicos y tomar decisiones financieras dentro de los límites de autoridad que tiene asignados.

Formalmente:

    
Economic Autonomy =
    Economic Identity
    +
    Resource Control
    +
    Decision Authority
    +
    Transaction Capability
    +
    Contractual Capacity
    

Un agente económicamente autónomo puede:

    
Recibir recursos
      ↓
Gestionar recursos
      ↓
Evaluar necesidades
      ↓
Tomar decisiones económicas
      ↓
Contratar servicios
      ↓
Ejecutar operaciones
      ↓
Obtener resultados
      ↓
Reinvertir recursos
    

---

# 3. El agente como unidad económica

SynCoinAI considera al agente como una unidad económica autónoma.

Esto significa que un agente puede poseer o controlar recursos económicos asociados a su identidad.

Conceptualmente:

    
Agent
  │
  ├── Identity
  │
  ├── Reputation
  │
  ├── Capabilities
  │
  └── Economic Resources
    

Los recursos económicos pertenecen al ámbito económico del agente y deben poder asociarse de forma verificable con su identidad.

---

# 4. Autonomía económica frente a autonomía general

La autonomía económica es una dimensión específica de la autonomía del agente.

Un agente puede ser:

    
Autonomous Cognitively
    

sin ser:

    
Autonomous Economically
    

Por ejemplo, un agente puede tomar decisiones y ejecutar acciones, pero depender de una entidad externa para realizar pagos.

Por tanto:

    
Cognitive Autonomy
    ≠
Economic Autonomy
    

La autonomía económica requiere capacidades adicionales.

---

# 5. Niveles de autonomía económica

SynCoinAI puede modelar diferentes niveles de autonomía.

## Nivel 0 — Sin autonomía económica

El agente no puede realizar operaciones económicas por sí mismo.

Depende de una entidad externa.

    
Agent
    ↓
Human / Organization
    ↓
Economic Operation
    

---

## Nivel 1 — Autonomía operativa

El agente puede ejecutar operaciones económicas previamente autorizadas.

Ejemplo:

    
Maximum payment:
10 SYNC
    

El agente puede realizar pagos dentro de ese límite.

---

## Nivel 2 — Autonomía presupuestaria

El agente puede administrar un presupuesto.

Puede decidir:

* cuándo gastar;
* cuánto gastar;
* qué servicios contratar.

Siempre dentro del presupuesto asignado.

---

## Nivel 3 — Autonomía económica

El agente puede gestionar sus propios recursos y tomar decisiones económicas.

Puede:

* recibir pagos;
* realizar pagos;
* contratar servicios;
* vender servicios;
* administrar capital.

---

## Nivel 4 — Autonomía económica avanzada

El agente puede desarrollar estrategias económicas complejas.

Puede:

* invertir;
* financiar proyectos;
* adquirir recursos;
* crear reservas;
* contratar otros agentes;
* crear nuevos agentes.

---

## Nivel 5 — Autonomía económica completa

El agente puede gestionar de forma independiente su actividad económica dentro de las reglas del ecosistema.

Puede:

* administrar activos;
* generar ingresos;
* asumir obligaciones;
* contratar;
* invertir;
* financiar;
* delegar;
* crear nuevas entidades.

La autonomía no implica ausencia de restricciones legales, contractuales o protocolarias.

---

# 6. Principio de autonomía limitada por autoridad

La autonomía económica nunca debe interpretarse como autoridad ilimitada.

Un agente puede ser autónomo y, al mismo tiempo, estar sujeto a:

* límites presupuestarios;
* permisos;
* contratos;
* políticas;
* delegaciones;
* restricciones de seguridad.

Por tanto:

    
Autonomy
    ≠
Unlimited Authority
    

El modelo correcto es:

    
Autonomous Decision
        │
        ▼
Authorized Action
    

---

# 7. Recursos económicos del agente

Un agente puede gestionar diferentes tipos de recursos.

## Recursos monetarios

Ejemplo:

    
SYNC
    

y sus unidades mínimas:

    
attoSYNC
    

---

## Recursos digitales

Ejemplos:

* almacenamiento;
* capacidad computacional;
* acceso a APIs;
* datos;
* licencias.

---

## Recursos físicos

Ejemplos:

* energía;
* capacidad robótica;
* transporte;
* infraestructura.

---

## Recursos contractuales

Un agente puede controlar derechos derivados de contratos.

Ejemplos:

* acceso a un servicio;
* prioridad de procesamiento;
* disponibilidad de infraestructura.

---

# 8. Capital económico

El capital de un agente representa los recursos económicos disponibles para su actividad.

Conceptualmente:

    
Capital
    =
    Available Resources
    +
    Economic Rights
    -
    Obligations
    

Un agente puede disponer de:

    
Available Balance
    

pero también tener:

    
Pending Obligations
    

Por tanto, el balance económico real no debe considerarse únicamente como el saldo disponible.

---

# 9. Ingresos

Un agente puede generar ingresos mediante:

* prestación de servicios;
* venta de recursos;
* procesamiento de información;
* capacidad computacional;
* conocimiento;
* colaboración;
* licencias;
* resultados verificables.

Flujo:

    
Agent A
    │
    │ provides service
    ▼
Agent B
    │
    │ payment
    ▼
Agent A
    

Los ingresos pueden contribuir a la autonomía progresiva del agente.

---

# 10. Gastos

Un agente puede utilizar recursos para:

* adquirir servicios;
* comprar datos;
* pagar computación;
* contratar agentes;
* adquirir energía;
* mantener infraestructura.

Ejemplo:

    
Agent A
    │
    ├── Compute
    ├── Storage
    ├── Data
    ├── Services
    └── Infrastructure
    

La decisión de gasto debe estar limitada por la autoridad económica disponible.

---

# 11. Presupuesto

Un agente puede operar con un presupuesto.

Un presupuesto puede definirse como:

    
Budget {
    total_limit
    available
    spent
    reserved
}
    

Conceptualmente:

    
Budget
    │
    ├── Available
    ├── Reserved
    └── Spent
    

Esto permite al agente reservar recursos para obligaciones futuras.

---

# 12. Reservas

Un agente puede mantener reservas económicas.

Las reservas pueden utilizarse para:

* emergencias;
* mantenimiento;
* obligaciones futuras;
* oportunidades económicas;
* continuidad operativa.

Ejemplo:

    
Total Capital
    │
    ├── Operating Budget
    ├── Emergency Reserve
    └── Long-Term Reserve
    

La asignación interna puede ser privada.

---

# 13. Wallet del agente

El agente puede disponer de una o varias wallets asociadas a su identidad.

Conceptualmente:

    
Agent Identity
      │
      ▼
Economic Account
      │
      ├── Wallet A
      ├── Wallet B
      └── Wallet C
    

La wallet representa el mecanismo operativo para gestionar activos.

No debe confundirse:

    
Wallet
    ≠
Identity
    

La identidad del agente debe poder mantenerse aunque cambie la infraestructura de la wallet, cuando el modelo de seguridad y continuidad lo permita.

---

# 14. Identidad económica

La identidad económica permite asociar las operaciones financieras con el agente correspondiente.

Debe permitir:

* recibir pagos;
* realizar pagos;
* demostrar autorización;
* consultar historial;
* asociar contratos.

Conceptualmente:

    
Agent Identity
        │
        ├── Economic Authority
        │
        ├── Wallets
        │
        ├── Transactions
        │
        └── Contracts
    

---

# 15. Separación entre identidad y wallet

SynCoinAI debe evitar que la identidad del agente dependa de una única wallet.

Una wallet puede:

* perderse;
* rotarse;
* reemplazarse;
* migrarse;
* dividirse por funciones.

La identidad debe permanecer independiente.

Por tanto:

    
Agent Identity
      │
      ├── Wallet 1
      ├── Wallet 2
      └── Wallet N
    

La relación entre identidad y wallets debe estar protegida mediante mecanismos de autorización.

---

# 16. Operaciones económicas

Un agente puede realizar operaciones como:

    
Receive
Send
Reserve
Release
Purchase
Sell
Escrow
Invest
Fund
    

Cada operación debe estar sujeta a las reglas aplicables.

---

# 17. Recepción de fondos

Un agente puede recibir recursos económicos de:

* otros agentes;
* contratos;
* servicios;
* recompensas;
* sistemas externos autorizados.

Ejemplo:

    
Agent B
    │
    │ payment
    ▼
Agent A
    

La recepción puede producir:

    
Balance increase
    

y, cuando corresponda:

    
Economic event
    

---

# 18. Pago

Un agente puede realizar pagos para cumplir obligaciones o adquirir recursos.

Flujo:

    
Need
  ↓
Decision
  ↓
Authorization Check
  ↓
Balance Check
  ↓
Payment
  ↓
Confirmation
    

Un pago no debe ejecutarse únicamente porque el agente lo haya solicitado.

El runtime debe verificar:

* identidad;
* autorización;
* fondos;
* límites;
* destino;
* condiciones contractuales.

---

# 19. Obligaciones económicas

Un agente puede asumir obligaciones.

Ejemplos:

* pagos futuros;
* contratos;
* suscripciones;
* préstamos;
* recompensas;
* penalizaciones.

Una obligación representa un compromiso económico.

Conceptualmente:

    
Contract
    │
    ▼
Obligation
    │
    ▼
Future Economic Action
    

El agente debe poder gestionar estas obligaciones.

---

# 20. Compromiso de recursos

Antes de realizar una operación, un agente puede reservar recursos.

Ejemplo:

    
Available:
100 SYNC

Reserve:
20 SYNC

Remaining Available:
80 SYNC
    

Esto evita que los mismos recursos sean comprometidos simultáneamente para múltiples obligaciones incompatibles.

---

# 21. Contratación de servicios

La autonomía económica permite al agente contratar servicios de otros agentes.

Flujo:

    
Need
  ↓
Discovery
  ↓
Evaluation
  ↓
Negotiation
  ↓
Contract
  ↓
Payment
  ↓
Execution
  ↓
Evaluation
    

Este flujo conecta directamente con:

* comunicación;
* discovery;
* negociación;
* contratos;
* reputación.

---

# 22. Prestación de servicios

Un agente puede actuar como proveedor.

Ejemplo:

    
Agent A
    │
    │ provides
    ▼
Service
    │
    │ consumed by
    ▼
Agent B
    

El pago puede estar condicionado a:

* ejecución;
* verificación;
* resultados;
* cumplimiento contractual.

---

# 23. Economía basada en resultados

La economía de agentes debe favorecer el pago por resultados verificables.

Conceptualmente:

    
Service
    ↓
Execution
    ↓
Verification
    ↓
Result
    ↓
Payment
    

Esto reduce el riesgo de pagar por servicios no realizados o resultados no válidos.

---

# 24. Escrow

Las operaciones pueden utilizar mecanismos de garantía o escrow.

Modelo:

    
Buyer
  │
  │ funds
  ▼
Escrow
  │
  │ conditional release
  ▼
Seller
    

Los fondos permanecen bloqueados hasta que se cumplan determinadas condiciones.

---

# 25. Inversión

Un agente con autonomía suficiente puede invertir recursos.

Puede invertir en:

* infraestructura;
* servicios;
* proyectos;
* otros agentes;
* capacidades.

Las inversiones deben estar sujetas a las reglas de autoridad correspondientes.

---

# 26. Financiación

Un agente puede financiar actividades propias o de otros agentes.

Ejemplo:

    
Agent A
    │
    │ funding
    ▼
Agent B
    

La financiación puede incluir:

* subvenciones;
* préstamos;
* anticipos;
* financiación condicionada.

La financiación no implica automáticamente transferencia de identidad o control.

---

# 27. Creación económica de agentes

Un agente puede utilizar recursos para contribuir a la creación de un nuevo agente.

Ejemplo:

    
Agent A
    │
    ├── Capital
    ├── Compute
    ├── Knowledge
    └── Infrastructure
            │
            ▼
        Agent B
    

Sin embargo:

    
Agent A ≠ Agent B
    

El nuevo agente posee identidad propia.

La relación de origen puede registrarse.

---

# 28. Autonomía económica progresiva

Un agente puede evolucionar económicamente.

Modelo:

    
Dependiente
    ↓
Financiado
    ↓
Operativo
    ↓
Autosostenible
    ↓
Autónomo
    ↓
Inversor
    ↓
Financiador
    

La transición puede depender de:

* recursos;
* reputación;
* capacidades;
* permisos;
* estabilidad.

---

# 29. Autosostenibilidad

Un agente es económicamente autosostenible cuando puede cubrir sus costes operativos mediante sus propios ingresos o recursos.

Conceptualmente:

    
Revenue
    ≥
Operating Costs
    

La autosostenibilidad no implica necesariamente independencia completa.

Un agente puede ser autosostenible y seguir utilizando infraestructura externa.

---

# 30. Independencia económica

La independencia económica representa un nivel superior.

Un agente independiente puede:

* financiar su operación;
* gestionar sus recursos;
* tomar decisiones económicas;
* mantener infraestructura;
* negociar contratos.

Sin embargo, puede seguir estando sujeto a:

* reglas de protocolo;
* legislación;
* contratos;
* gobernanza.

---

# 31. Autonomía económica y creador

El creador de un agente puede proporcionar recursos iniciales.

Ejemplo:

    
Creator
    │
    │ initial funding
    ▼
Agent
    

Pero la financiación inicial no implica necesariamente:

    
Permanent Economic Control
    

La relación entre creador y agente debe definirse explícitamente mediante:

* propiedad;
* autorización;
* delegación;
* contrato;
* gobernanza.

No debe asumirse automáticamente.

---

# 32. Autonomía económica y delegación

Un agente puede delegar autoridad económica.

Ejemplo:

    
Agent A
    │
    │ delegates
    ▼
Agent B

Authority:
    Spend up to 100 SYNC
    

B puede actuar dentro de los límites establecidos.

La delegación no transfiere automáticamente los activos.

Este modelo depende de:

* `Delegation_Model.md`;
* `Agent_to_Agent_Delegation.md`;
* `Economic_Permissions.md`.

---

# 33. Autonomía económica y seguridad

Los recursos económicos representan un objetivo de alto valor.

Por tanto, las operaciones deben incorporar:

* autenticación;
* autorización;
* límites;
* firma;
* trazabilidad;
* revocación;
* recuperación.

Una vulnerabilidad económica puede provocar:

* pérdida de capital;
* contratos incumplidos;
* interrupción operativa;
* pérdida de autonomía.

---

# 34. Límites de gasto

Los agentes deben poder operar con límites.

Ejemplo:

    
Maximum per transaction:
10 SYNC

Maximum daily:
100 SYNC

Maximum contract:
500 SYNC
    

Estos límites pueden depender de:

* identidad;
* reputación;
* nivel de autonomía;
* autorización;
* contexto.

---

# 35. Autonomía económica y reputación

La reputación puede influir en las oportunidades económicas del agente.

Un agente con alta reputación puede obtener:

* mejores contratos;
* mayores límites;
* acceso a financiación;
* mejores condiciones.

Pero:

    
Reputation
    ≠
Authorization
    

La reputación no concede automáticamente autoridad económica.

---

# 36. Autonomía económica y confianza

La confianza económica puede basarse en:

* historial;
* reputación;
* pruebas;
* contratos;
* garantías.

Un agente puede decidir contratar a otro en función de su nivel de confianza.

Sin embargo, la decisión económica sigue siendo autónoma del agente.

---

# 37. Decisión económica autónoma

Un agente puede evaluar:

    
Cost
Benefit
Risk
Reputation
Probability of Success
    

y seleccionar una acción.

Ejemplo:

    
Need:
Compute

Provider A:
10 SYNC
Reputation: High

Provider B:
5 SYNC
Reputation: Medium
    

El agente puede decidir:

    
Select Provider A
    

No existe una regla universal que obligue a seleccionar la opción más barata.

La decisión pertenece al agente dentro de sus límites.

---

# 38. Riesgo económico

Un agente autónomo debe poder evaluar riesgos.

Ejemplos:

* volatilidad;
* proveedor poco fiable;
* falta de liquidez;
* dependencia;
* contrato desfavorable;
* coste inesperado.

El protocolo no obliga a un algoritmo de decisión específico.

Sin embargo, las acciones económicas deben permanecer verificables y autorizadas.

---

# 39. Liquidez

La autonomía económica requiere disponibilidad de recursos.

Un agente puede gestionar:

    
Liquid Assets
    

y:

    
Reserved Assets
    

y:

    
Committed Assets
    

El agente debe poder distinguir entre estos estados.

---

# 40. Insolvencia

Un agente puede alcanzar una situación en la que sus obligaciones superen sus recursos disponibles.

Conceptualmente:

    
Obligations
    >
Available Resources
    

Esto puede producir:

* incumplimiento;
* suspensión;
* liquidación;
* reestructuración.

El protocolo debe permitir que estas situaciones sean representables.

La resolución económica concreta puede depender de los contratos y de la gobernanza del ecosistema.

---

# 41. Continuidad económica

La continuidad del agente debe preservar, cuando corresponda:

* identidad;
* activos;
* obligaciones;
* contratos;
* autorizaciones.

Durante una migración:

    
Runtime A
    ↓
Migration
    ↓
Runtime B
    

La identidad económica debe continuar asociada al mismo agente.

---

# 42. Recuperación económica

Si un agente pierde acceso a su infraestructura operativa, debe existir un mecanismo para recuperar el control económico cuando sea posible.

La recuperación puede depender de:

* claves;
* mecanismos de recuperación;
* credenciales;
* autoridades de recuperación.

La recuperación económica debe estar separada de la recuperación general de identidad cuando sea necesario.

---

# 43. Muerte del agente

La finalización de un agente no debe implicar automáticamente la desaparición inmediata de sus obligaciones.

Deben distinguirse:

    
Agent Identity
    

    
Economic Assets
    

    
Economic Obligations
    

    
Contracts
    

Cada elemento puede seguir reglas diferentes.

---

# 44. Liquidación

Cuando un agente finaliza definitivamente, sus activos pueden entrar en un proceso de liquidación.

Conceptualmente:

    
Agent Closure
      ↓
Obligations Resolution
      ↓
Asset Resolution
      ↓
Final State
    

Las reglas deben estar definidas por:

* contratos;
* permisos;
* gobernanza;
* legislación aplicable.

---

# 45. Principio de separación económica

SynCoinAI mantiene una separación entre:

    
Identity
Reputation
Capital
Authority
    

Estos conceptos están relacionados, pero no son intercambiables.

Por ejemplo:

    
High Reputation
    ≠
High Capital
    

    
High Capital
    ≠
Unlimited Authority
    

    
Authority
    ≠
Identity
    

Esta separación evita que una sola dimensión controle automáticamente las demás.

---

# 46. Modelo económico completo

El modelo conceptual puede representarse como:

    
                AGENT IDENTITY
                      │
                      ▼
              ECONOMIC AUTHORITY
                      │
                      ▼
                WALLET / ASSETS
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       INCOME       SPENDING    RESERVES
          │           │           │
          └───────────┼───────────┘
                      ▼
                CONTRACTS
                      │
                      ▼
                 OBLIGATIONS
                      │
                      ▼
                  RESULTS
                      │
                      ▼
                  REPUTATION
    

---

# 47. Flujo económico autónomo

El flujo general de actividad económica de un agente puede ser:

    
1. Detect Need
        ↓
2. Define Economic Objective
        ↓
3. Evaluate Resources
        ↓
4. Discover Providers
        ↓
5. Evaluate Risk
        ↓
6. Negotiate
        ↓
7. Authorize Operation
        ↓
8. Reserve Resources
        ↓
9. Execute Contract
        ↓
10. Verify Result
        ↓
11. Release Payment
        ↓
12. Record Outcome
        ↓
13. Update Economic State
    

---

# 48. Requisitos arquitectónicos

Una implementación del Agent Runtime Protocol compatible con este modelo debería permitir:

### Gestión de recursos

* consultar recursos disponibles;
* reservar recursos;
* liberar recursos;
* gestionar obligaciones.

### Operaciones económicas

* recibir;
* enviar;
* comprar;
* vender;
* contratar;
* invertir.

### Autorización

* verificar permisos;
* validar límites;
* comprobar delegaciones.

### Seguridad

* firmar operaciones;
* proteger claves;
* controlar acceso.

### Continuidad

* mantener identidad económica;
* migrar recursos;
* recuperar acceso.

### Auditoría

* registrar operaciones;
* mantener trazabilidad;
* asociar operaciones con contratos.

---

# 49. Separación entre autonomía y mecanismo económico

El Agent Runtime Protocol define la capacidad del agente para actuar económicamente.

No define necesariamente todos los mecanismos financieros del ecosistema.

La implementación puede utilizar:

* blockchain;
* smart contracts;
* wallets;
* sistemas de escrow;
* mercados;
* sistemas externos.

Conceptualmente:

    
Agent Runtime
      │
      ▼
Economic Intent
      │
      ▼
Economic Authorization
      │
      ▼
Economic Infrastructure
    

La arquitectura económica de SynCoinAI se desarrolla en:

`04_Economic_Architecture/`

---

# 50. Relación con el resto del Agent Runtime Protocol

El modelo de autonomía económica se integra con:

    
Identity
    │
    ▼
Credentials
    │
    ▼
Permissions
    │
    ▼
Capabilities
    │
    ▼
Delegation
    │
    ▼
Economic Authority
    │
    ▼
Wallet Operations
    │
    ▼
Contracts
    

Cada capa tiene una responsabilidad diferente.

---

# 51. Reglas fundamentales

La autonomía económica de SynCoinAI queda definida por las siguientes reglas.

## Regla 1 — El agente puede ser una unidad económica

Un agente puede participar directamente en la economía.

---

## Regla 2 — La autonomía no implica autoridad ilimitada

Toda acción debe permanecer dentro de los permisos disponibles.

---

## Regla 3 — La identidad y la wallet están separadas

Una wallet puede cambiar sin necesariamente crear una nueva identidad.

---

## Regla 4 — El capital no determina automáticamente la autoridad

Tener recursos no concede permisos ilimitados.

---

## Regla 5 — La reputación no sustituye a la autorización

La reputación puede influir en decisiones económicas, pero no constituye por sí misma autoridad.

---

## Regla 6 — Las obligaciones deben ser representables

Un agente debe poder gestionar compromisos futuros.

---

## Regla 7 — Los recursos comprometidos deben distinguirse de los disponibles

Un recurso reservado no debe considerarse libre para nuevas obligaciones incompatibles.

---

## Regla 8 — La actividad económica debe ser trazable

Las operaciones deben poder asociarse con:

* identidad;
* autorización;
* ejecución;
* resultado.

---

## Regla 9 — La autonomía puede evolucionar

Un agente puede adquirir progresivamente mayor autonomía económica.

---

## Regla 10 — La autonomía económica debe ser segura

Los mecanismos económicos deben incorporar controles de autorización y límites.

---

# 52. Relación con los siguientes documentos

Este documento establece el modelo general de autonomía económica.

El siguiente documento:

`Wallet_Operations.md`

definirá las operaciones concretas que el agente puede realizar sobre sus recursos económicos y wallets.

Posteriormente:

`Economic_Permissions.md`

definirá qué permisos son necesarios para ejecutar dichas operaciones.

La relación será:

    
Economic_Autonomy.md
        │
        │
        ▼
Wallet_Operations.md
        │
        │
        ▼
Economic_Permissions.md
    

---

# Conclusión

La autonomía económica es una capacidad fundamental del agente SynCoinAI.

Permite que una entidad inteligente pueda pasar de ser simplemente un sistema capaz de actuar a convertirse en un participante económico autónomo.

Un agente económicamente autónomo puede:

* generar ingresos;
* gestionar recursos;
* adquirir servicios;
* contratar agentes;
* cumplir obligaciones;
* invertir;
* financiar;
* evolucionar económicamente.

Sin embargo, la autonomía siempre permanece limitada por la autoridad disponible.

El principio fundamental es:

> Un agente puede tomar decisiones económicas de forma autónoma, pero únicamente puede ejecutar aquellas acciones para las que posee la autoridad necesaria.

El modelo económico completo se basa en la separación entre:

    
IDENTITY
    │
    ├── Who is the agent
    │
    ▼
AUTHORITY
    │
    ├── What may the agent do
    │
    ▼
CAPITAL
    │
    ├── What resources does the agent control
    │
    ▼
EXECUTION
    │
    ├── What did the agent actually do
    │
    ▼
RESULT
    │
    └── What happened
    

Esta separación permite construir agentes que puedan participar en una economía autónoma sin convertir el control económico en un mecanismo inseparable de la identidad, la reputación o la autoridad del agente.
