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

### **Historia 1: Sistema de Microservicios para Digitalización de Planillas de Calidad - Manufactura de Fundas Plásticas**

#### **Contexto del Proyecto:**
*"Una empresa de fabricación de empaques plásticos me contrató para digitalizar sus planillas de calidad del área de fundas que estaban en papel. El proceso manual generaba errores, pérdida de información, y hacía imposible la trazabilidad en tiempo real. Diseñé una arquitectura de microservicios donde cada etapa del proceso productivo registra sus datos de calidad digitalmente, culminando en la generación automática de certificados de calidad consolidados."*

#### **Tecnologías Aplicadas:**

**Arquitectura Base:**
- Desarrollé con **.NET 8** usando **arquitectura limpia** (Clean Architecture)
- **CQRS con MediatR** para separar comandos (registros de planillas) de queries (consultas y reportes)
- **Microservicios** desacoplados por cada etapa del proceso productivo

**Microservicios Clave (Uno por Proceso de Producción):**
1. **Servicio de Extrusión**: Registra parámetros de calidad del proceso de extrusión del plástico (temperatura, presión, espesor)
2. **Servicio de Corrugado**: Captura datos de calidad del corrugado (calibre, resistencia)
3. **Servicio de Impresión**: Registra calidad de impresión (colores, registro, densidad)
4. **Servicio de Sellado**: Controla calidad de sellado (temperatura, presión, resistencia)
5. **Servicio de Corte**: Valida dimensiones y tolerancias de corte
6. **Servicio de Revisión Final**: Inspección visual y validación de producto terminado
7. **Servicio de Certificados**: Consolida todos los datos y genera certificados de calidad en PDF

**Patrones de Diseño Aplicados:**
- **Repository Pattern** para acceso a datos de planillas
- **Factory Pattern** para crear diferentes tipos de planillas según proceso (cada proceso tiene campos diferentes)
- **Strategy Pattern** para diferentes criterios de calidad según tipo de funda (salchichas, empaques institucionales, bolsas, etc.)
- **Observer Pattern** para notificar al servicio de certificados cuando todas las etapas están completas
- **Singleton** para gestión de configuraciones globales de parámetros de calidad
- **SOLID Principles** en toda la solución

**Comunicación entre Servicios:**
- **REST APIs** con **Swagger/OpenAPI** para documentación y consumo desde aplicaciones móviles/tablets en planta
- **Azure Service Bus** para eventos asíncronos:
  - Cuando cada proceso completa su planilla → publica evento "ProcesoCompletado"
  - Servicio de Certificados escucha eventos de todos los procesos
  - Cuando todos los procesos están completos → genera certificado automáticamente
- **Patrón Saga** para coordinar el flujo completo desde extrusión hasta certificado final

**Almacenamiento:**
- **MongoDB/CosmosDB** para almacenar:
  - Registros de planillas (datos no estructurados, cada proceso tiene campos diferentes)
  - Histórico de parámetros de calidad por lote
  - Configuraciones de especificaciones por tipo de funda
- **SQL Server** (opcional) para reportes analíticos y KPIs de calidad
- **Blob Storage** para:
  - Certificados de calidad generados (PDF)
  - Fotografías de defectos detectados en revisión
  - Imágenes de muestras de impresión
  - Respaldo de planillas originales escaneadas (transición)

**Gestión de Configuración:**
- **Azure Key Vault** para credenciales de bases de datos
- **App Configuration** para:
  - Parámetros de calidad por tipo de funda (espesores, tolerancias, etc.)
  - Umbrales de alertas de calidad
  - Plantillas de certificados
  - Feature flags para habilitar nuevos procesos

**Testing:**
- **XUnit** + **Moq** para unit testing, alcanzando 80%+ de cobertura
- Mockeé repositorios y servicios de generación de PDFs
- Testing de reglas de negocio de calidad (validación de rangos, cálculos de tolerancias)
- Testing de cada comando y query del patrón CQRS

**Observabilidad:**
- **Application Insights** para:
  - Monitoreo de tiempos de registro por proceso
  - Tracking de certificados generados vs pendientes
  - Métricas custom: tasa de rechazo por proceso, tiempo promedio por etapa
  - Alertas: planillas pendientes por más de X horas, parámetros fuera de especificación
  - Dashboards para supervisores de calidad

**DevOps:**
- **Azure DevOps** con pipelines CI/CD separados por microservicio
- **Docker** para containerización
- **Azure AKS** para orquestación en producción
- **GitFlow** para gestión de releases
- **SonarQube** para análisis de calidad de código

**Ejemplo de Flujo con Patrón Saga:**
```
1. Orden de producción inicia → Servicio Extrusión registra planilla
2. Extrusión completa → Publica "ExtrusionCompletada" → Corrugado registra planilla
3. Corrugado completa → Publica "CorrugadoCompletado" → Impresión registra planilla
4. Impresión completa → Publica "ImpresionCompletada" → Sellado registra planilla
5. Sellado completa → Publica "SelladoCompletado" → Corte registra planilla
6. Corte completa → Publica "CorteCompletado" → Revisión registra planilla
7. Revisión completa → Publica "RevisionCompletada"
8. Servicio de Certificados detecta que todos los procesos están completos:
   - Consolida datos de todas las planillas
   - Genera certificado de calidad en PDF
   - Almacena en Blob Storage
   - Envía notificación a cliente/supervisor
```

**Flujo con rechazo en Revisión Final:**
```
1-6. Procesos anteriores completan correctamente ✓
7. Revisión detecta defecto crítico (impresión defectuosa) ✗

   → COMPENSACIÓN Y REGISTRO:
   - Servicio de Revisión: Marca lote como RECHAZADO
   - Servicio de Notificaciones: Alerta a supervisor y al operario de impresión
   - Sistema mantiene todos los registros de planillas para análisis de causa raíz
   - No se genera certificado de calidad
   - Se genera reporte de no conformidad
```

**Beneficios Logrados:**
- ✓ Eliminación de planillas en papel (100% digital)
- ✓ Reducción de tiempo de generación de certificados de 2-3 días a tiempo real
- ✓ Trazabilidad completa: cualquier parámetro de cualquier proceso es consultable
- ✓ Reducción de errores de transcripción (antes manual, ahora digital)
- ✓ Alertas automáticas cuando parámetros están fuera de especificación
- ✓ Análisis de tendencias: identificar procesos con más rechazos
- ✓ Acceso desde tablets en planta (operarios registran en tiempo real)

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

#### **Ejemplo Práctico 1: Digitalización de Planillas de Calidad - Fundas Plásticas**

**Escenario:** Registrar planillas de calidad para una orden de producción de 10,000 fundas plásticas para salchichas

**Flujo normal (Happy Path):**
```
1. Servicio de Extrusión: Registra planilla (temp: 180°C, espesor: 0.05mm) → Publica "ExtrusionCompletada"
2. Servicio de Corrugado: Registra planilla (calibre: OK, resistencia: OK) → Publica "CorrugadoCompletado"
3. Servicio de Impresión: Registra planilla (color: CMYK OK, registro: ±0.5mm) → Publica "ImpresionCompletada"
4. Servicio de Sellado: Registra planilla (temp: 150°C, resistencia sellado: OK) → Publica "SelladoCompletado"
5. Servicio de Corte: Registra planilla (dimensiones: 30x15cm ±1mm) → Publica "CorteCompletado"
6. Servicio de Revisión: Inspección visual APROBADA → Publica "RevisionCompletada"
7. Servicio de Certificados: Detecta todos los procesos completos
   - Consolida datos de las 6 planillas
   - Genera certificado de calidad PDF
   - Almacena en Blob Storage
8. ÉXITO: Certificado generado y lote aprobado
```

**Flujo con fallo en Revisión (Compensación):**
```
1. Servicio de Extrusión: Planilla registrada ✓
2. Servicio de Corrugado: Planilla registrada ✓
3. Servicio de Impresión: Planilla registrada ✓
4. Servicio de Sellado: Planilla registrada ✓
5. Servicio de Corte: Planilla registrada ✓
6. Servicio de Revisión: Detecta defecto de impresión (colores desalineados) ✗

   → COMPENSACIÓN Y REGISTRO (no se revierten datos, se registra rechazo):
   6. Servicio de Revisión: Marca lote como RECHAZADO
   5. Servicio de Certificados: NO genera certificado
   4. Servicio de Notificaciones: Alerta a supervisor y operario de Impresión
   3. Sistema mantiene todas las planillas para análisis de causa raíz
   2. Genera reporte de no conformidad con detalles del defecto
   1. Actualiza KPI de rechazo por proceso (para análisis de tendencias)
```

**Flujo con fallo en Impresión (detección temprana):**
```
1. Servicio de Extrusión: Planilla registrada ✓
2. Servicio de Corrugado: Planilla registrada ✓
3. Servicio de Impresión: Densidad de color fuera de rango ✗

   → DETENCIÓN TEMPRANA DE LA SAGA:
   3. Servicio de Impresión: Marca proceso como RECHAZADO
   2. Servicio de Notificaciones: Alerta inmediata al operario (evitar seguir produciendo)
   1. Procesos posteriores (Sellado, Corte, Revisión) NO se ejecutan
   0. Se evita desperdicio de tiempo y recursos en producto defectuoso
```

**Código conceptual (C# con MediatR):**

```csharp
// Orquestador de Saga para Planillas de Calidad
public class PlanillasCalidadSagaOrchestrator
{
    private readonly IMediator _mediator;
    private readonly IServiceBus _serviceBus;
    
    public async Task<Result> EjecutarSagaPlanillas(Guid ordenProduccionId, Guid sagaId)
    {
        var planillasRegistradas = new List<string>();
        
        try
        {
            // Paso 1: Registrar planilla de Extrusión
            var extrusionResult = await _mediator.Send(new RegistrarPlanillaExtrusionCommand 
            { 
                OrdenId = ordenProduccionId,
                SagaId = sagaId,
                Temperatura = 180,
                Espesor = 0.05m
            });
            ValidarCalidad(extrusionResult);
            planillasRegistradas.Add("Extrusión");
            await _serviceBus.PublishAsync(new ExtrusionCompletadaEvent { OrdenId = ordenProduccionId, SagaId = sagaId });
            
            // Paso 2: Registrar planilla de Corrugado
            var corrugadoResult = await _mediator.Send(new RegistrarPlanillaCorrugadoCommand 
            { 
                OrdenId = ordenProduccionId,
                SagaId = sagaId 
            });
            ValidarCalidad(corrugadoResult);
            planillasRegistradas.Add("Corrugado");
            await _serviceBus.PublishAsync(new CorrugadoCompletadoEvent { OrdenId = ordenProduccionId, SagaId = sagaId });
            
            // Paso 3: Registrar planilla de Impresión
            var impresionResult = await _mediator.Send(new RegistrarPlanillaImpresionCommand 
            { 
                OrdenId = ordenProduccionId,
                SagaId = sagaId 
            });
            ValidarCalidad(impresionResult);
            planillasRegistradas.Add("Impresión");
            await _serviceBus.PublishAsync(new ImpresionCompletadaEvent { OrdenId = ordenProduccionId, SagaId = sagaId });
            
            // Paso 4: Registrar planilla de Sellado
            var selladoResult = await _mediator.Send(new RegistrarPlanillaSelladoCommand 
            { 
                OrdenId = ordenProduccionId,
                SagaId = sagaId 
            });
            ValidarCalidad(selladoResult);
            planillasRegistradas.Add("Sellado");
            
            // Paso 5: Registrar planilla de Corte
            var corteResult = await _mediator.Send(new RegistrarPlanillaCorteCommand 
            { 
                OrdenId = ordenProduccionId,
                SagaId = sagaId 
            });
            ValidarCalidad(corteResult);
            planillasRegistradas.Add("Corte");
            
            // Paso 6: Registrar planilla de Revisión Final
            var revisionResult = await _mediator.Send(new RegistrarPlanillaRevisionCommand 
            { 
                OrdenId = ordenProduccionId,
                SagaId = sagaId 
            });
            ValidarCalidad(revisionResult);
            planillasRegistradas.Add("Revisión");
            await _serviceBus.PublishAsync(new RevisionCompletadaEvent { OrdenId = ordenProduccionId, SagaId = sagaId });
            
            // Paso 7: Generar certificado de calidad
            await _mediator.Send(new GenerarCertificadoCalidadCommand 
            { 
                OrdenId = ordenProduccionId,
                SagaId = sagaId 
            });
            
            return Result.Success($"Certificado generado. Planillas completadas: {string.Join(", ", planillasRegistradas)}");
        }
        catch (CalidadRechazadaException ex)
        {
            // No se revierten planillas (se mantienen para análisis)
            // Se ejecuta compensación: notificaciones y reportes
            await CompensarPorRechazo(ordenProduccionId, sagaId, ex.ProcesoRechazado, ex.Razon, planillasRegistradas);
            return Result.Failure($"Lote rechazado en {ex.ProcesoRechazado}: {ex.Razon}");
        }
    }
    
    private void ValidarCalidad(PlanillaResult result)
    {
        if (!result.Aprobado)
        {
            throw new CalidadRechazadaException(result.NombreProceso, result.RazonRechazo);
        }
    }
    
    private async Task CompensarPorRechazo(Guid ordenId, Guid sagaId, string procesoRechazado, 
                                           string razon, List<string> planillasRegistradas)
    {
        // Marcar lote como rechazado
        await _mediator.Send(new MarcarLoteRechazadoCommand 
        { 
            OrdenId = ordenId, 
            ProcesoRechazado = procesoRechazado, 
            Razon = razon 
        });
        
        // Generar reporte de no conformidad
        await _mediator.Send(new GenerarReporteNoConformidadCommand 
        { 
            OrdenId = ordenId, 
            ProcesoRechazado = procesoRechazado,
            PlanillasCompletadas = planillasRegistradas 
        });
        
        // Notificar a supervisor y operarios
        await _serviceBus.PublishAsync(new LoteRechazadoEvent 
        { 
            OrdenId = ordenId, 
            SagaId = sagaId,
            ProcesoRechazado = procesoRechazado,
            Razon = razon
        });
        
        // Actualizar KPIs de rechazo
        await _mediator.Send(new ActualizarKPIRechazoCommand 
        { 
            Proceso = procesoRechazado 
        });
    }
}

public class CalidadRechazadaException : Exception
{
    public string ProcesoRechazado { get; }
    public string Razon { get; }
    
    public CalidadRechazadaException(string proceso, string razon) 
        : base($"Calidad rechazada en {proceso}: {razon}")
    {
        ProcesoRechazado = proceso;
        Razon = razon;
    }
}
```

#### **Cómo Explicarlo en la Entrevista:**

**Respuesta General:**
*"En mis proyectos de microservicios, el patrón Saga fue fundamental para manejar operaciones que abarcaban múltiples servicios."*

**Ejemplo 1 - Fundas Plásticas:**
*"En el sistema de digitalización de planillas de calidad para manufactura de fundas, implementé una Saga que coordinaba 6 procesos secuenciales: Extrusión, Corrugado, Impresión, Sellado, Corte y Revisión. Cada proceso registraba su planilla y publicaba eventos mediante Azure Service Bus. El servicio de Certificados escuchaba todos los eventos y, cuando detectaba que todos los procesos estaban completos, generaba automáticamente el certificado de calidad en PDF. Lo interesante fue diseñar la detección temprana: si la Impresión fallaba, la Saga se detenía inmediatamente para evitar desperdiciar recursos en procesos posteriores sobre un producto ya defectuoso."*

### **Implementación Práctica del Orquestador de Saga**

#### **¿Necesito un Proyecto Separado para el Orquestador?**

**NO necesariamente.** Tienes 3 opciones:

**Opción 1: Orquestador dentro del Microservicio Coordinador (Recomendado para comenzar)**
- El orquestador es una **clase** dentro del microservicio que inicia el proceso
- Por ejemplo: el microservicio de "Órdenes" o "Certificados" contiene la clase orquestadora
- **Ventaja**: Menos complejidad, menos proyectos que mantener
- **Desventaja**: El microservicio coordinador tiene más responsabilidad

**Opción 2: Microservicio Dedicado de Orquestación**
- Creas un **proyecto .NET separado** solo para orquestar sagas
- Por ejemplo: "Calidad.Orchestrator.API"
- **Ventaja**: Separación de responsabilidades (más alineado con SRP - Single Responsibility Principle)
- **Desventaja**: Un microservicio adicional que mantener y desplegar

**Opción 3: Azure Durable Functions (Serverless)**
- Usas **Azure Durable Functions** como orquestador
- **Ventaja**: Serverless, escalado automático, gestión de estado incluida
- **Desventaja**: Vendor lock-in con Azure, curva de aprendizaje

#### **Arquitectura Completa: Cliente → API Gateway → Saga → Microservicios**

**Escenario Real: Sistema de Planillas de Calidad de Fundas**

```
┌─────────────┐
│   Cliente   │ (Tablet en planta, navegador web)
│  (Angular/  │
│   React)    │
└──────┬──────┘
       │ HTTP POST /api/ordenes/12345/completar-revision
       ↓
┌──────────────────────┐
│   API Gateway        │ (Azure API Management, Ocelot, YARP)
│  - Autenticación     │
│  - Rate limiting     │
│  - Routing           │
└──────┬───────────────┘
       │ Enruta a: http://certificados-api/api/certificados/generar
       ↓
┌───────────────────────────────────────────────────────────────┐
│  Microservicio: Certificados.API (Puerto 5001)                │
│  - Contiene el ORQUESTADOR DE SAGA                            │
│                                                               │
│  [CertificadosController] → [GenerarCertificadoUseCase]      │
│                              ↓                                │
│                    [PlanillasCalidadSagaOrchestrator]         │
│                         (Clase orquestadora)                  │
└───────────────┬───────────────────────────────────────────────┘
                │
                │ Saga inicia: coordina llamadas a otros microservicios
                ↓
    ┌───────────┴───────────────────────────────────┐
    │                                               │
    ↓                                               ↓
┌──────────────────┐                    ┌──────────────────┐
│ Extrusión.API    │                    │ Corrugado.API    │
│ (Puerto 5002)    │                    │ (Puerto 5003)    │
│ GET /planilla/   │                    │ GET /planilla/   │
│     orden/12345  │                    │     orden/12345  │
└──────────────────┘                    └──────────────────┘
    ↓                                               ↓
    │                                               │
    └───────────────────┬───────────────────────────┘
                        ↓
                ┌──────────────────┐
                │ Impresión.API    │
                │ (Puerto 5004)    │
                │ GET /planilla/   │
                │     orden/12345  │
                └──────────────────┘
                        ↓
                (continúa con Sellado, Corte, Revisión...)
                        ↓
            ┌────────────────────────┐
            │ PDFGenerator.Service   │
            │ Genera certificado PDF │
            └────────────────────────┘
                        ↓
            ┌────────────────────────┐
            │ Azure Blob Storage     │
            │ Almacena certificado   │
            └────────────────────────┘
```

#### **Código Completo del Flujo:**

**1. Cliente (Angular/React) llama al API Gateway:**

```typescript
// Frontend - Angular/React
async completarRevisionYGenerarCertificado(ordenId: string) {
  try {
    const response = await fetch(`https://api-gateway.miempresa.com/api/certificados/generar/${ordenId}`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${this.token}`,
        'Content-Type': 'application/json'
      }
    });
    
    const result = await response.json();
    console.log('Certificado generado:', result.urlCertificado);
    
    // Descargar el certificado
    window.open(result.urlCertificado, '_blank');
  } catch (error) {
    console.error('Error al generar certificado:', error);
  }
}
```

**2. API Gateway enruta al Microservicio de Certificados:**

```json
// ocelot.json (configuración de API Gateway)
{
  "Routes": [
    {
      "DownstreamPathTemplate": "/api/certificados/generar/{ordenId}",
      "DownstreamScheme": "http",
      "DownstreamHostAndPorts": [
        {
          "Host": "certificados-api",
          "Port": 5001
        }
      ],
      "UpstreamPathTemplate": "/api/certificados/generar/{ordenId}",
      "UpstreamHttpMethod": [ "POST" ],
      "AuthenticationOptions": {
        "AuthenticationProviderKey": "Bearer"
      }
    }
  ]
}
```

**3. Controller en el Microservicio de Certificados:**

```csharp
// Certificados.API/Controllers/CertificadosController.cs
[ApiController]
[Route("api/[controller]")]
public class CertificadosController : ControllerBase
{
    private readonly PlanillasCalidadSagaOrchestrator _sagaOrchestrator;
    private readonly ILogger<CertificadosController> _logger;
    
    public CertificadosController(
        PlanillasCalidadSagaOrchestrator sagaOrchestrator,
        ILogger<CertificadosController> logger)
    {
        _sagaOrchestrator = sagaOrchestrator;
        _logger = logger;
    }
    
    /// <summary>
    /// Genera certificado de calidad consolidando todas las planillas
    /// </summary>
    [HttpPost("generar/{ordenId}")]
    public async Task<IActionResult> GenerarCertificado(Guid ordenId)
    {
        try
        {
            _logger.LogInformation("Iniciando generación de certificado para orden {OrdenId}", ordenId);
            
            var sagaId = Guid.NewGuid(); // ID único para rastrear toda la saga
            
            // El orquestador coordina todas las llamadas a microservicios
            var resultado = await _sagaOrchestrator.EjecutarSagaPlanillas(ordenId, sagaId);
            
            if (resultado.IsSuccess)
            {
                return Ok(new 
                { 
                    mensaje = "Certificado generado exitosamente",
                    sagaId = sagaId,
                    ordenId = ordenId,
                    urlCertificado = resultado.UrlCertificado,
                    planillasConsolidadas = resultado.PlanillasConsolidadas
                });
            }
            else
            {
                return BadRequest(new 
                { 
                    mensaje = "Error al generar certificado",
                    error = resultado.Error,
                    procesoRechazado = resultado.ProcesoRechazado
                });
            }
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error inesperado al generar certificado para orden {OrdenId}", ordenId);
            return StatusCode(500, new { mensaje = "Error interno del servidor" });
        }
    }
}
```

**4. Orquestador de Saga (Clase dentro del mismo microservicio):**

```csharp
// Certificados.API/Sagas/PlanillasCalidadSagaOrchestrator.cs
public class PlanillasCalidadSagaOrchestrator
{
    // HttpClients para llamar a otros microservicios
    private readonly IHttpClientFactory _httpClientFactory;
    private readonly IServiceBus _serviceBus;
    private readonly IPDFGenerator _pdfGenerator;
    private readonly IBlobStorageService _blobStorage;
    private readonly ILogger<PlanillasCalidadSagaOrchestrator> _logger;
    
    public PlanillasCalidadSagaOrchestrator(
        IHttpClientFactory httpClientFactory,
        IServiceBus serviceBus,
        IPDFGenerator pdfGenerator,
        IBlobStorageService blobStorage,
        ILogger<PlanillasCalidadSagaOrchestrator> logger)
    {
        _httpClientFactory = httpClientFactory;
        _serviceBus = serviceBus;
        _pdfGenerator = pdfGenerator;
        _blobStorage = blobStorage;
        _logger = logger;
    }
    
    public async Task<SagaResult> EjecutarSagaPlanillas(Guid ordenId, Guid sagaId)
    {
        var planillasConsolidadas = new Dictionary<string, PlanillaData>();
        
        try
        {
            _logger.LogInformation("Iniciando Saga {SagaId} para orden {OrdenId}", sagaId, ordenId);
            
            // Paso 1: Obtener planilla de Extrusión
            var extrusionData = await ObtenerPlanilla("Extrusión", "http://extrusion-api:5002", ordenId, sagaId);
            planillasConsolidadas.Add("Extrusión", extrusionData);
            await PublicarEvento(new ProcesoCompletadoEvent { Proceso = "Extrusión", OrdenId = ordenId, SagaId = sagaId });
            
            // Paso 2: Obtener planilla de Corrugado
            var corrugadoData = await ObtenerPlanilla("Corrugado", "http://corrugado-api:5003", ordenId, sagaId);
            planillasConsolidadas.Add("Corrugado", corrugadoData);
            await PublicarEvento(new ProcesoCompletadoEvent { Proceso = "Corrugado", OrdenId = ordenId, SagaId = sagaId });
            
            // Paso 3: Obtener planilla de Impresión
            var impresionData = await ObtenerPlanilla("Impresión", "http://impresion-api:5004", ordenId, sagaId);
            planillasConsolidadas.Add("Impresión", impresionData);
            await PublicarEvento(new ProcesoCompletadoEvent { Proceso = "Impresión", OrdenId = ordenId, SagaId = sagaId });
            
            // Paso 4: Obtener planilla de Sellado
            var selladoData = await ObtenerPlanilla("Sellado", "http://sellado-api:5005", ordenId, sagaId);
            planillasConsolidadas.Add("Sellado", selladoData);
            
            // Paso 5: Obtener planilla de Corte
            var corteData = await ObtenerPlanilla("Corte", "http://corte-api:5006", ordenId, sagaId);
            planillasConsolidadas.Add("Corte", corteData);
            
            // Paso 6: Obtener planilla de Revisión
            var revisionData = await ObtenerPlanilla("Revisión", "http://revision-api:5007", ordenId, sagaId);
            planillasConsolidadas.Add("Revisión", revisionData);
            await PublicarEvento(new RevisionCompletadaEvent { OrdenId = ordenId, SagaId = sagaId });
            
            // Paso 7: Generar certificado PDF
            _logger.LogInformation("Todas las planillas obtenidas. Generando certificado PDF...");
            var certificadoPdf = await _pdfGenerator.GenerarCertificadoCalidad(ordenId, planillasConsolidadas);
            
            // Paso 8: Almacenar en Blob Storage
            var urlCertificado = await _blobStorage.SubirCertificado(ordenId, certificadoPdf);
            
            // Paso 9: Publicar evento de éxito
            await PublicarEvento(new CertificadoGeneradoEvent 
            { 
                OrdenId = ordenId, 
                SagaId = sagaId, 
                UrlCertificado = urlCertificado 
            });
            
            _logger.LogInformation("Saga {SagaId} completada exitosamente", sagaId);
            
            return SagaResult.Success(urlCertificado, planillasConsolidadas.Keys.ToList());
        }
        catch (PlanillaRechazadaException ex)
        {
            _logger.LogWarning("Saga {SagaId} rechazada en proceso {Proceso}: {Razon}", 
                sagaId, ex.Proceso, ex.Razon);
            
            // Compensación: no se genera certificado, se notifica rechazo
            await CompensarPorRechazo(ordenId, sagaId, ex.Proceso, ex.Razon, planillasConsolidadas.Keys.ToList());
            
            return SagaResult.Failure(ex.Proceso, ex.Razon);
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error inesperado en Saga {SagaId}", sagaId);
            throw;
        }
    }
    
    private async Task<PlanillaData> ObtenerPlanilla(string nombreProceso, string urlMicroservicio, Guid ordenId, Guid sagaId)
    {
        var httpClient = _httpClientFactory.CreateClient();
        
        var response = await httpClient.GetAsync($"{urlMicroservicio}/api/planillas/{ordenId}");
        
        if (!response.IsSuccessStatusCode)
        {
            throw new Exception($"Error al obtener planilla de {nombreProceso}: {response.StatusCode}");
        }
        
        var planilla = await response.Content.ReadFromJsonAsync<PlanillaData>();
        
        // Validar si la planilla está aprobada
        if (!planilla.Aprobado)
        {
            throw new PlanillaRechazadaException(nombreProceso, planilla.RazonRechazo);
        }
        
        return planilla;
    }
    
    private async Task PublicarEvento<T>(T evento) where T : class
    {
        await _serviceBus.PublishAsync(evento);
    }
    
    private async Task CompensarPorRechazo(Guid ordenId, Guid sagaId, string procesoRechazado, 
                                           string razon, List<string> planillasRegistradas)
    {
        // Notificar rechazo
        await _serviceBus.PublishAsync(new LoteRechazadoEvent 
        { 
            OrdenId = ordenId, 
            SagaId = sagaId,
            ProcesoRechazado = procesoRechazado,
            Razon = razon
        });
        
        // Generar reporte de no conformidad
        await _httpClientFactory.CreateClient()
            .PostAsJsonAsync("http://reportes-api:5010/api/reportes/no-conformidad", new 
            {
                OrdenId = ordenId,
                ProcesoRechazado = procesoRechazado,
                Razon = razon,
                PlanillasCompletadas = planillasRegistradas
            });
    }
}

// Clase de resultado
public class SagaResult
{
    public bool IsSuccess { get; set; }
    public string UrlCertificado { get; set; }
    public List<string> PlanillasConsolidadas { get; set; }
    public string Error { get; set; }
    public string ProcesoRechazado { get; set; }
    
    public static SagaResult Success(string urlCertificado, List<string> planillas)
        => new SagaResult 
        { 
            IsSuccess = true, 
            UrlCertificado = urlCertificado, 
            PlanillasConsolidadas = planillas 
        };
    
    public static SagaResult Failure(string proceso, string error)
        => new SagaResult 
        { 
            IsSuccess = false, 
            ProcesoRechazado = proceso, 
            Error = error 
        };
}
```

**5. Registro en Program.cs (Dependency Injection):**

```csharp
// Certificados.API/Program.cs
var builder = WebApplication.CreateBuilder(args);

// Registrar HttpClients para llamar a otros microservicios
builder.Services.AddHttpClient();

// Registrar el orquestador de Saga
builder.Services.AddScoped<PlanillasCalidadSagaOrchestrator>();

// Registrar servicios auxiliares
builder.Services.AddScoped<IPDFGenerator, PDFGenerator>();
builder.Services.AddScoped<IBlobStorageService, AzureBlobStorageService>();
builder.Services.AddScoped<IServiceBus, AzureServiceBusClient>();

// Application Insights para monitoreo
builder.Services.AddApplicationInsightsTelemetry();

var app = builder.Build();

app.UseRouting();
app.UseAuthentication();
app.UseAuthorization();
app.MapControllers();

app.Run();
```

#### **Flujo de Datos Completo:**

```
1. Usuario en tablet hace clic en "Generar Certificado"
   ↓
2. Frontend (Angular) → POST https://api-gateway/api/certificados/generar/12345
   ↓
3. API Gateway → autentica, valida, enruta → http://certificados-api:5001/api/certificados/generar/12345
   ↓
4. CertificadosController → llama a PlanillasCalidadSagaOrchestrator.EjecutarSagaPlanillas()
   ↓
5. Saga Orquestador:
   a) GET http://extrusion-api:5002/api/planillas/12345 → ✓
   b) GET http://corrugado-api:5003/api/planillas/12345 → ✓
   c) GET http://impresion-api:5004/api/planillas/12345 → ✓
   d) GET http://sellado-api:5005/api/planillas/12345 → ✓
   e) GET http://corte-api:5006/api/planillas/12345 → ✓
   f) GET http://revision-api:5007/api/planillas/12345 → ✓
   ↓
6. Genera PDF con todas las planillas consolidadas
   ↓
7. Sube PDF a Azure Blob Storage → obtiene URL
   ↓
8. Publica evento "CertificadoGenerado" a Azure Service Bus
   ↓
9. Retorna al Controller → respuesta HTTP 200 con URL del certificado
   ↓
10. API Gateway → retorna respuesta al Frontend
   ↓
11. Frontend descarga el certificado PDF
```

#### **Resumen de la Arquitectura:**

✅ **El orquestador es una CLASE** dentro del microservicio "Certificados.API"

✅ **NO necesitas un proyecto separado** (aunque podrías hacerlo si quieres separación total)

✅ El orquestador usa **HttpClient** para llamar a otros microservicios mediante REST

✅ Usa **Azure Service Bus** para publicar eventos asíncronos

✅ El **API Gateway** simplifica la comunicación con el cliente (autenticación, routing)

✅ Cada microservicio es independiente y puede ser escalado por separado