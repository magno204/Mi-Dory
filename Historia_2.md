Habilidades Técnicas Requeridas:

✓ Microsoft (Backend): .Net (Backend)
✓ Microsoft (Backend): .NETCore (Backend)
✓ Microsoft Azure : Azure DevOps
✓ Unit Testing
✓ Unit Testing : Moq
✓ Unit Testing : Xunit
✓ Microsoft (Backend) : C# (Backend)
✓ Database : MongoDB
✓ Microsoft Azure : CosmoDB (Azure)
✓ Agile - Process : Frameworks-Scrum
✓ Services : REST (Backend)
✓ Backend : Design Patterns
✓ Backend : CQRS / Event sourcing
✓ API Governance : Swagger
✓ .NET 5, 6, 7, 8
✓ Azure Key Vault, App Configuration, Blob Storage
✓ Microservicios
✓ Monolitos modulares
✓ Patrones de diseño (Factory, Strategy, Singleton, Observer, Repository)
✓ Arquitectura limpia
✓ MediatR
✓ OpenAPI
✓ Consulting: SOLID Principles
✓ SDLC : Git


Habilidades Técnicas Deseadas:

✓ Microsoft (Backend) : VB.net (Backend)
✓ Database: SQL Server✓ SDLC: Sonar
✓ Database: PL/SQL✓ Docker✓ Azure AKS
✓ Azure Service Bus
✓ Application Insights
✓ RabbitMQ
✓ GitFlow o trunk-based

## HISTORIAS PARA LA ENTREVISTA - EXPERIENCIA CON MICROSERVICIOS

### **Historia 2: Sistema de Microservicios para Control de Calidad de Materia Prima Farmacéutica**

#### **Contexto del Proyecto:**
*"Una empresa farmacéutica me contrató para desarrollar un sistema de control de calidad para materia prima que ingresa a la compañía. El sistema debía gestionar evaluaciones de calidad mediante análisis microbiológicos y análisis fisicoquímicos, cumpliendo con normativas GMP (Good Manufacturing Practices) y FDA. Diseñé una arquitectura de microservicios para permitir escalabilidad independiente de cada módulo de análisis y mantener trazabilidad completa."*

#### **¿Por Qué Microservicios? - Justificación de la Arquitectura**

**Análisis del Problema:**
El sistema de control de calidad farmacéutico presentaba características que lo hacían ideal para microservicios en lugar de un monolito:

**1. Dominios de Negocio Claramente Separados:**
- **Análisis Microbiológico** y **Análisis Fisicoquímico** son dominios independientes con:
  - Equipos de laboratorio diferentes
  - Tiempos de procesamiento distintos (microbiológico: 24-72 horas, fisicoquímico: 2-8 horas)
  - Normativas y protocolos específicos para cada tipo
  - Personal especializado diferente
- Cada dominio puede evolucionar independientemente sin afectar al otro

**2. Escalabilidad Diferenciada por Proceso:**
- **Picos de carga variables por tipo de análisis:**
  - En temporada alta de producción: más análisis fisicoquímicos (materias primas comunes)
  - En auditorías FDA: más análisis microbiológicos (muestras de retención)
  - Con microservicios: escalar SOLO el servicio que lo necesita (ahorro de costos)
  - Con monolito: habría que escalar TODA la aplicación aunque solo un módulo esté saturado

**3. Requisitos Regulatorios Estrictos:**
- **Trazabilidad completa** (GMP/FDA) requiere:
  - Event Sourcing para registrar cada cambio inmutablemente
  - Auditoría independiente que no debe afectar el rendimiento de los análisis
  - Con microservicios: el servicio de auditoría puede escalar independientemente durante auditorías sin impactar los análisis en curso

**4. Integraciones con Sistemas Externos Heterogéneos:**
- **Equipos de laboratorio diversos:**
  - Espectrofotómetros, cromatógrafos (fisicoquímico)
  - Incubadoras, contadores de colonias (microbiológico)
- Cada microservicio se integra con sus equipos específicos sin crear dependencias cruzadas
- Fallo en integración con equipo microbiológico NO afecta los análisis fisicoquímicos

**5. Ciclos de Actualización Independientes:**
- **Regulaciones cambiantes:**
  - FDA actualiza requisitos de análisis microbiológico → deploy SOLO de ese servicio
  - Nueva normativa de pH en materias primas → actualizar SOLO servicio fisicoquímico
- Reducción de riesgo: cambios aislados en lugar de redesplegar toda la aplicación crítica

**6. Resiliencia y Tolerancia a Fallos:**
- **Alta disponibilidad crítica:**
  - Si el servicio de notificaciones falla → los análisis continúan registrándose
  - Si un tipo de análisis tiene problemas → el otro tipo sigue operando
  - Con monolito: un error en cualquier módulo podría tumbar todo el sistema

**7. Equipos de Desarrollo Especializados:**
- **Equipos por dominio de expertise:**
  - Equipo con conocimiento microbiológico trabaja en su servicio
  - Equipo con conocimiento fisicoquímico trabaja en su servicio
  - Desarrollo paralelo sin conflictos en el mismo código

**Alternativa Rechazada: Monolito Modular**

**Por qué NO elegimos un monolito modular:**

❌ **Escalabilidad:** No podríamos escalar análisis microbiológicos independientemente de fisicoquímicos
❌ **Deployment:** Cualquier cambio pequeño requeriría redesplegar toda la aplicación (riesgo alto en farmacéutica)
❌ **Base de datos compartida:** Conflictos entre esquemas de análisis diferentes
❌ **Resiliencia:** Un módulo con error podría comprometer todo el sistema
❌ **Regulatorio:** Más difícil demostrar aislamiento de cambios en auditorías

**Cuándo SÍ consideraríamos un monolito:**
✓ Si fuera una startup sin regulaciones estrictas
✓ Si el equipo de desarrollo fuera muy pequeño (<5 personas)
✓ Si todos los análisis fueran del mismo tipo (sin dominios separados)
✓ Si no hubiera requisitos de escalabilidad diferenciada

**Decisión Final:**
*"Opté por microservicios porque los dominios de negocio estaban naturalmente separados, los requisitos de escalabilidad eran diferenciados por tipo de análisis, y las normativas FDA exigían trazabilidad aislada por proceso. La inversión inicial en complejidad se justificó por los beneficios de despliegues independientes, escalabilidad selectiva, y resiliencia operativa en un entorno regulado."*

#### **Tecnologías Aplicadas:**

**Arquitectura Base:**
- Desarrollé desde cero con **.NET 8** usando **arquitectura limpia** (Clean Architecture)
- **CQRS con MediatR** para separar comandos (registros de análisis) de queries (consultas de estado)
- **Microservicios** desacoplados por dominio de negocio

**Microservicios Clave:**
1. **Recepción de Materia Prima**: Registro de ingresos, proveedores, lotes y muestras
2. **Análisis Microbiológico**: Gestión de pruebas de esterilidad, conteo microbiano, endotoxinas
3. **Análisis Fisicoquímico**: Control de pH, humedad, pureza, identificación química
4. **Gestión de Resultados**: Consolidación de análisis y dictamen de calidad (Aprobado/Rechazado)
5. **Auditoría y Trazabilidad**: Registro inmutable de todas las operaciones (requisito GMP/FDA)
6. **Notificaciones**: Alertas a supervisores y producción sobre estado de materias primas

**Patrones de Diseño Aplicados:**
- **Repository Pattern** para acceso a datos de análisis
- **Strategy Pattern** para diferentes tipos de análisis (microbiológico vs fisicoquímico)
- **Factory Pattern** para crear diferentes tipos de muestras según materia prima
- **Observer Pattern** para notificar cambios de estado en análisis en curso
- **SOLID Principles** en toda la solución para cumplir con auditorías regulatorias

**Comunicación entre Servicios:**
- **REST APIs** con **Swagger/OpenAPI** para documentación (integración con sistemas de laboratorio externos)
- **Azure Service Bus** para eventos asíncronos:
  - Cuando se completa un análisis microbiológico → notificar al servicio de resultados
  - Cuando se completa un análisis fisicoquímico → notificar al servicio de resultados
  - Cuando todos los análisis están completos → notificar a producción
- **Patrón Saga** para coordinar el proceso completo de evaluación que requiere múltiples análisis

**Almacenamiento:**
- **MongoDB/CosmosDB** para almacenar:
  - Resultados de análisis (datos no estructurados, cada tipo de análisis tiene campos diferentes)
  - Especificaciones de materia prima y rangos de aceptación
  - Historial de lotes por proveedor
- **Blob Storage** para:
  - Certificados de análisis (PDF)
  - Fotografías de muestras
  - Reportes regulatorios
- **Event Sourcing** con MongoDB para trazabilidad inmutable (crítico para auditorías FDA)

**Gestión de Configuración:**
- **Azure Key Vault** para credenciales de bases de datos y APIs de laboratorio
- **App Configuration** para:
  - Parámetros de calidad por tipo de materia prima
  - Rangos de aceptación de análisis
  - Feature flags para nuevos tipos de análisis

**Testing Riguroso:**
- **XUnit** + **Moq** para unit testing con cobertura >85% (requisito regulatorio)
- Mockeé repositorios y servicios de análisis para pruebas aisladas
- Testing específico de reglas de negocio de calidad (rangos de aceptación, criterios de rechazo)
- Testing de cada comando y query del patrón CQRS

**Observabilidad:**
- **Application Insights** configurado con:
  - Distributed tracing para seguir una materia prima a través de todos los análisis
  - Métricas custom: tiempo promedio de análisis, tasa de rechazo por proveedor
  - Alertas: análisis pendientes por más de 24 horas, rechazos críticos
  - Dashboards para supervisores de calidad

**DevOps:**
- **Azure DevOps** con pipelines CI/CD separados por microservicio
- **Docker** para containerización de cada servicio
- **Azure AKS** para orquestación en producción
- **GitFlow** para gestión de releases
- **SonarQube** para análisis de calidad de código (requisito de validación de software en farmacéutica)

**Ejemplo de Flujo con Patrón Saga:**
```
1. Materia Prima ingresa → Servicio de Recepción crea registro
2. Se toman muestras → Publica evento "MuestrasListas"
3. Servicio Microbiológico inicia análisis → Publica "AnalisisMicrobiologicoIniciado"
4. Servicio Fisicoquímico inicia análisis → Publica "AnalisisFisicoquimicoIniciado"
5. Ambos análisis completan → Servicio de Resultados recibe ambos eventos
6. Sistema evalúa criterios de aceptación:
   - Si ambos APROBADOS → Materia Prima aprobada, notificar a producción
   - Si alguno RECHAZADO → Materia prima rechazada, notificar a compras para devolución
7. Event Sourcing registra toda la cadena de eventos para auditoría
```

**Beneficios Logrados:**
- ✓ Reducción de tiempo de evaluación de 5 días a 3 días (análisis en paralelo)
- ✓ Trazabilidad completa para auditorías FDA (cada cambio registrado)
- ✓ Escalabilidad: durante picos de ingreso de materia prima, se escalan independientemente los servicios de análisis
- ✓ Integración con equipos de laboratorio mediante APIs REST
- ✓ Reportes automáticos de tendencias de calidad por proveedor

## **CONSEJOS PARA CONTAR ESTAS HISTORIAS EN LA ENTREVISTA**

### **Usa el método STAR:**
- **S**ituación: "En la empresa farmacéutica teníamos un sistema monolítico que..."
- **T**area: "Me asignaron diseñar una arquitectura de microservicios que..."
- **A**cción: "Implementé 5 microservicios usando .NET 6, Azure Service Bus, y..."
- **R**esultado: "Logramos reducir el tiempo de deploy de 2 horas a 15 minutos, mejorar la escalabilidad..."

### **Métricas que puedes mencionar:**
- "Redujimos el tiempo de deployment de X horas a Y minutos"
- "Mejoramos la disponibilidad del sistema al 99.9%"
- "Escalamos independientemente el microservicio de órdenes durante picos de producción"
- "Alcanzamos 85% de cobertura de código con XUnit"
- "Redujimos el tiempo de respuesta de APIs en un 40%"

### **Desafíos que enfrentaste:**
- "El mayor desafío fue mantener la consistencia eventual entre microservicios"
- "Implementar event sourcing para cumplir con requisitos de auditoría fue complejo"
- "La migración gradual del monolito usando Strangler Pattern requirió planificación cuidadosa"

### **Preguntas Técnicas Comunes:**

**1. ¿Cómo manejaste la consistencia de datos entre microservicios?**
- "Implementé el patrón Saga para transacciones distribuidas y event sourcing para mantener trazabilidad completa."

**2. ¿Cómo gestionaste la comunicación entre servicios?**
- "Usé comunicación síncrona (REST) para operaciones que requerían respuesta inmediata y asíncrona (Azure Service Bus/RabbitMQ) para eventos que no bloqueaban el flujo principal."

**3. ¿Cómo monitoreaste el sistema?**
- "Con Application Insights configuré distributed tracing para seguir una petición a través de múltiples microservicios, además de métricas custom y alertas proactivas."

**4. ¿Cómo manejaste el versionado de APIs?**
- "Implementé versionado semántico en las URLs (/api/v1/, /api/v2/) y mantuve compatibilidad hacia atrás por al menos 2 versiones."

**5. ¿Cuál fue el mayor desafío técnico?**
- "Migrar datos del monolito manteniendo el sistema operativo 24/7. Usamos el patrón Strangler y sincronización dual-write temporal."


## **PATRONES AVANZADOS - EXPLICACIÓN DETALLADA**

### **Patrón SAGA para Transacciones Distribuidas**

#### **¿Qué es el Patrón Saga?**

El **patrón Saga** es una solución para manejar transacciones que abarcan múltiples microservicios. En arquitecturas distribuidas, no podemos usar transacciones ACID tradicionales porque cada microservicio tiene su propia base de datos. La Saga divide una transacción grande en una serie de **transacciones locales** más pequeñas.

**Características principales:**
- Cada microservicio ejecuta su propia transacción local y publica un evento
- Si una transacción falla en algún punto, se ejecutan **transacciones compensatorias** para deshacer los cambios previos
- Mantiene **consistencia eventual** (no inmediata) entre los servicios
- Evita el problema de transacciones distribuidas de dos fases (2PC) que son lentas y propensas a fallos

#### **Tipos de Saga:**

**1. Orquestación (Orchestration):**
- Un servicio central (orquestador) coordina todas las transacciones
- El orquestador le dice a cada servicio qué hacer y cuándo
- Más fácil de entender y debuggear
- Punto único de control

**2. Coreografía (Choreography):**
- No hay coordinador central
- Cada servicio escucha eventos y sabe qué hacer
- Más desacoplado pero más difícil de rastrear el flujo completo

#### **Ejemplo Práctico 2: Control de Calidad de Materia Prima Farmacéutica**

**Escenario:** Evaluar materia prima (excipiente farmacéutico) que requiere análisis microbiológico Y fisicoquímico

**Flujo normal:**
```
1. Servicio de Recepción: Registra ingreso de materia prima del proveedor → Publica "MateriaPrimaIngresada"
2. Servicio de Muestras: Toma muestras para laboratorio → Publica "MuestrasGeneradas"
3. Servicio Análisis Microbiológico: Ejecuta pruebas de esterilidad → Publica "AnalisisMicrobiologicoAPROBADO"
4. Servicio Análisis Fisicoquímico: Ejecuta pruebas de pH, humedad, pureza → Publica "AnalisisFisicoquimicoAPROBADO"
5. Servicio de Resultados: Consolida ambos análisis → Estado: APROBADO
6. Servicio de Auditoría: Registra aprobación (requisito GMP/FDA)
7. Servicio de Notificaciones: Notifica a producción que materia prima está disponible
8. ÉXITO: Materia prima aprobada y disponible para producción
```

**Flujo con fallo en análisis microbiológico:**
```
1. Servicio de Recepción: Registra ingreso de materia prima ✓
2. Servicio de Muestras: Toma muestras para laboratorio ✓
3. Servicio Análisis Microbiológico: Detecta contaminación → Publica "AnalisisMicrobiologicoRECHAZADO" ✗

   → COMPENSACIÓN INMEDIATA (crítico - no continuar con análisis costosos):
   3. Servicio de Resultados: Marca materia prima como RECHAZADA (sin esperar fisicoquímico)
   2. Servicio de Auditoría: Registra rechazo con razón
   1. Servicio de Notificaciones: 
      - Alerta a supervisor de calidad
      - Notifica a compras para devolución al proveedor
      - Bloquea materia prima en sistema de inventario
```

**Flujo con fallo en análisis fisicoquímico (después de microbiológico aprobado):**
```
1. Servicio de Recepción: Registra ingreso de materia prima ✓
2. Servicio de Muestras: Toma muestras para laboratorio ✓
3. Servicio Análisis Microbiológico: Aprobado ✓
4. Servicio Análisis Fisicoquímico: pH fuera de rango → Publica "AnalisisFisicoquimicoRECHAZADO" ✗

   → COMPENSACIÓN PARCIAL:
   4. Servicio de Resultados: Marca materia prima como RECHAZADA
   3. Servicio de Auditoría: Registra rechazo fisicoquímico (aunque microbiológico aprobó)
   2. Servicio de Notificaciones: Alerta diferenciada (posible reanálisis vs rechazo definitivo)
   1. Sistema mantiene registro de análisis microbiológico para auditoría
```

#### **Beneficios del Patrón Saga:**

✓ **Escalabilidad**: Cada servicio mantiene su propia transacción local
✓ **Resiliencia**: Si un servicio falla, la saga puede compensar y recuperarse
✓ **Flexibilidad**: Fácil agregar nuevos pasos a la saga
✓ **Auditoría**: Cada paso queda registrado (crítico en farmacéutica)

#### **Desafíos del Patrón Saga:**

⚠️ **Consistencia eventual**: Hay un período donde los datos no están sincronizados
⚠️ **Complejidad**: Debes diseñar transacciones compensatorias para cada paso
⚠️ **Idempotencia**: Las operaciones deben ser idempotentes (ejecutarse múltiples veces sin problemas)
⚠️ **Debugging**: Más difícil rastrear el flujo completo en coreografía

#### **Implementación con Azure Service Bus:**

```csharp
// Evento publicado cuando se crea la orden
public class OrdenCreadaEvent
{
    public Guid OrdenId { get; set; }
    public Guid SagaId { get; set; }  // ID único para rastrear toda la saga
    public string Producto { get; set; }
    public int Cantidad { get; set; }
}

// Handler en el servicio de inventario
public class ReservarMateriaPrimaHandler : IMessageHandler<OrdenCreadaEvent>
{
    public async Task HandleAsync(OrdenCreadaEvent evento)
    {
        try
        {
            // Reservar materia prima
            await _inventarioService.ReservarMateriales(evento.OrdenId, evento.Cantidad);
            
            // Publicar evento de éxito
            await _serviceBus.PublishAsync(new MateriaPrimaReservadaEvent 
            { 
                OrdenId = evento.OrdenId,
                SagaId = evento.SagaId 
            });
        }
        catch (StockInsuficienteException ex)
        {
            // Publicar evento de fallo para iniciar compensación
            await _serviceBus.PublishAsync(new ReservaMaterialFallidaEvent 
            { 
                OrdenId = evento.OrdenId,
                SagaId = evento.SagaId,
                Razon = ex.Message
            });
        }
    }
}
```

#### **Herramientas para Implementar Sagas:**

- **MassTransit**: Framework .NET con soporte para sagas (state machines)
- **NServiceBus**: Framework comercial con excelente soporte para sagas
- **Azure Durable Functions**: Para orquestación en Azure
- **Custom con MediatR**: Implementación propia usando MediatR y Azure Service Bus

#### **Cómo Explicarlo en la Entrevista:**

**Respuesta General:**
*"En mis proyectos de microservicios, el patrón Saga fue fundamental para manejar operaciones que abarcaban múltiples servicios."*

**Ejemplo 2 - Farmacéutica:**
*"En el sistema de control de calidad farmacéutico, evaluar una materia prima requería coordinar análisis microbiológicos y fisicoquímicos en paralelo. Implementé una Saga con orquestación usando MediatR y Azure Service Bus. Cada análisis publicaba eventos cuando completaba, y el servicio de resultados consolidaba ambos. Si el análisis microbiológico fallaba, inmediatamente cancelábamos el fisicoquímico para evitar costos innecesarios. Lo más crítico fue diseñar compensaciones idempotentes y mantener un SagaId para rastrear toda la operación en Application Insights, cumpliendo con requisitos de auditoría FDA."*

**Puntos Clave a Mencionar:**
- ✓ Usé **orquestación** (más fácil de debuggear que coreografía)
- ✓ Cada paso publicaba eventos mediante **Azure Service Bus**
- ✓ Implementé **detección temprana de fallos** para optimizar recursos
- ✓ Las compensaciones no revertían datos sino que generaban **reportes de no conformidad**
- ✓ Mantuve un **SagaId** único para trazar todo el flujo en **Application Insights**
- ✓ Las operaciones eran **idempotentes** (podían ejecutarse múltiples veces sin problemas)