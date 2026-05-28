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


#### **Cómo Explicarlo en la Entrevista:**

**Respuesta General:**
*"En mis proyectos de microservicios, el patrón Saga fue fundamental para manejar operaciones que abarcaban múltiples servicios."*

**Ejemplo 1 - Fundas Plásticas:**
*"En el sistema de digitalización de planillas de calidad para manufactura de fundas, implementé una Saga que coordinaba 6 procesos secuenciales: Extrusión, Corrugado, Impresión, Sellado, Corte y Revisión. Cada proceso registraba su planilla y publicaba eventos mediante Azure Service Bus. El servicio de Certificados escuchaba todos los eventos y, cuando detectaba que todos los procesos estaban completos, generaba automáticamente el certificado de calidad en PDF. Lo interesante fue diseñar la detección temprana: si la Impresión fallaba, la Saga se detenía inmediatamente para evitar desperdiciar recursos en procesos posteriores sobre un producto ya defectuoso."*

**Ejemplo 2 - Farmacéutica:**
*"En el sistema de control de calidad farmacéutico, evaluar una materia prima requería coordinar análisis microbiológicos y fisicoquímicos en paralelo. Implementé una Saga con orquestación usando MediatR y Azure Service Bus. Cada análisis publicaba eventos cuando completaba, y el servicio de resultados consolidaba ambos. Si el análisis microbiológico fallaba, inmediatamente cancelábamos el fisicoquímico para evitar costos innecesarios. Lo más crítico fue diseñar compensaciones idempotentes y mantener un SagaId para rastrear toda la operación en Application Insights, cumpliendo con requisitos de auditoría FDA."*

**Puntos Clave a Mencionar:**
- ✓ Usé **orquestación** (más fácil de debuggear que coreografía)
- ✓ Cada paso publicaba eventos mediante **Azure Service Bus**
- ✓ Implementé **detección temprana de fallos** para optimizar recursos
- ✓ Las compensaciones no revertían datos sino que generaban **reportes de no conformidad**
- ✓ Mantuve un **SagaId** único para trazar todo el flujo en **Application Insights**
- ✓ Las operaciones eran **idempotentes** (podían ejecutarse múltiples veces sin problemas)

---

