# Guía de Trabajo Práctico · Experimental

> Talleres y Laboratorios de Docencia ITM
>
> | Código | Versión | Fecha |
> |---|---|---|
> | FGL 029 | 03 | 18-07-2023 |

*Transcripción del documento `2026-01_ProyectoFinal.pdf` (4 páginas).*

---

## 1. Identificación de la guía

| Campo | Valor |
|---|---|
| Nombre de la guía | Proyecto de aula |
| Código de la guía (No.) | 001 |
| Taller(es) o Laboratorio(s) aplicable(s) | — |
| Tiempo de trabajo práctico estimado | 8 horas |
| Asignatura(s) aplicable(s) | Introducción a la ciencia de datos |
| Programa(s) Académico(s) / Facultad(es) | Ingeniería Electrónica |

### Competencias, contenido temático e indicadores de logro

| Competencias | Contenido temático | Indicador de logro |
|---|---|---|
| **C3** – Capacidad para desarrollar y realizar experimentos aplicados, analizar e interpretar datos, y utilizar el criterio de ingeniería para extraer conclusiones. | Inspección técnica, perfilado estadístico descriptivo y estrategias de preprocesamiento de conjuntos de datos estructurados. | Ejecuta el perfilado descriptivo y aplica estrategias técnicas justificadas de preprocesamiento sobre el dataset, asegurando la integridad, limpieza y consistencia de los datos. |
| | Análisis de relaciones y dependencias críticas entre variables mediante matrices de correlación lineal y mapas térmicos. | Evalúa las relaciones y dependencias entre variables mediante herramientas gráficas y numéricas, emitiendo juicios técnicos fundamentados sobre la relevancia de los datos analizados. |
| **C4** – Capacidad para comunicarse eficazmente con diversos públicos. | Diseño y desarrollo de dashboards interactivos de Inteligencia de Negocios para la visualización de distribuciones y variables principales. | Diseña y construye dashboards interactivos que sintetizan de manera clara la distribución de variables clave y facilitan la interpretación visual de los datos para usuarios técnicos y no técnicos. |
| **C5** – Capacidad para trabajar eficazmente en un equipo cuyos miembros, en conjunto, proporcionan liderazgo, crean un entorno colaborativo e inclusivo, establecen metas, planifican tareas y cumplen objetivos. | Implementación, optimización y evaluación de rendimiento de algoritmos de aprendizaje automático supervisado para tareas de clasificación y regresión. | Implementa y optimiza modelos de aprendizaje automático supervisado mediante la búsqueda rigurosa de hiperparámetros, validando su desempeño técnico con métricas de ingeniería adecuadas al problema. |
| | Estructuración de informes técnicos ejecutivos y resúmenes analíticos de datos orientados a la toma de decisiones informadas. | Estructura y comunica hallazgos de ingeniería mediante informes ejecutivos sintéticos y sustentaciones orales efectivas, facilitando la toma de decisiones basadas en datos e interpretaciones técnicas. |
| | Planificación de proyectos de analítica de datos y distribución de tareas complejas en entornos colaborativos de desarrollo. Gestión del tiempo y cumplimiento de metas técnicas multifactoriales bajo plazos y estándares profesionales. | Planifica y coordina actividades en entornos de desarrollo colaborativo, asignando roles técnicos y gestionando el tiempo con efectividad para cumplir con la totalidad de los entregables bajo plazos estrictos. |

---

## 2. Fundamento teórico

En el ejercicio profesional de la Ciencia de Datos, el desarrollo de soluciones analíticas y predictivas se fundamenta en un ciclo metodológico riguroso que transforma datos crudos en activos estratégicos para la toma de decisiones e interpretaciones de ingeniería. Este proceso inicia con la inspección técnica y el perfilado estadístico descriptivo, etapas críticas para diagnosticar la calidad de la información, comprender la naturaleza multivariada del dataset e identificar anomalías como registros duplicados o vacíos de información. El preprocesamiento de datos aborda estas inconsistencias mediante un balance técnico, aplicando mecanismos de limpieza e imputación estadística que preservan la integridad de la muestra sin introducir sesgos.

Para descubrir la estructura interna de la información, se utiliza el análisis de relaciones y dependencias críticas, el cual evalúa la fuerza y dirección de las interacciones entre variables mediante matrices de correlación lineal y mapas térmicos. Complementariamente, el diseño de dashboards interactivos actúa como el puente de comunicación visual, permitiendo la exploración dinámica de distribuciones y variables principales de forma intuitiva.

La fase predictiva se sustenta en el Aprendizaje Automático Supervisado, abordando tareas de clasificación o regresión según la naturaleza de la variable objetivo seleccionada. La rigurosidad de esta etapa exige tanto la optimización de hiperparámetros para maximizar la generalización del modelo, como una evaluación de rendimiento basada en métricas estadísticas de ingeniería que validen con precisión el éxito de la solución propuesta. Finalmente, la viabilidad técnica se integra con principios de planificación y desarrollo colaborativo, asegurando la gestión eficiente de metas complejas bajo plazos y estándares de entrega profesionales.

---

## 3. Objetivos

### 3.1 Objetivo general

Implementar un proyecto integral de ciencia de datos en un entorno colaborativo, abarcando desde la inspección técnica, preprocesamiento y visualización interactiva de conjuntos de datos estructurados, hasta el desarrollo, optimización y evaluación de modelos predictivos de aprendizaje supervisado, orientando los hallazgos técnicos hacia la toma de decisiones informadas y la comunicación efectiva de ingeniería.

### 3.2 Objetivos específicos

- Ejecutar la inspección técnica y el perfilado estadístico descriptivo sobre un conjunto de datos estructurado para diagnosticar su calidad y aplicar estrategias justificadas de limpieza, imputación y preprocesamiento de datos.
- Analizar las relaciones y dependencias críticas entre las variables del dataset mediante el uso de matrices de correlación lineal y mapas térmicos para identificar patrones relevantes y redundancias de información.
- Diseñar y construir dashboards interactivos en Power BI para visualizar la distribución de las variables principales y sus interacciones clave.
- Desarrollar, evaluar y optimizar algoritmos de aprendizaje automático supervisado mediante la búsqueda de hiperparámetros, validando su desempeño con métricas técnicas adecuadas para la toma de decisiones estratégicas.
- Estructurar informes técnicos ejecutivos escritos y realizar sustentaciones orales efectivas que sinteticen los hallazgos y la toma de decisiones estratégicas.
- Planificar y coordinar el flujo de trabajo técnico en parejas, gestionando de forma eficiente la distribución de tareas complejas y el tiempo para cumplir con las metas multifactoriales del proyecto bajo plazos estrictos.

---

## 4. Recursos requeridos

Los elementos requeridos para realizar el taller son:

- Computador personal con internet.
- Acceso a software tipo Visual Studio Code, Google Colab, Kaggle Notebooks, entre otros.
- Material de estudio entregado en clase (Notebooks).

---

## 5. Aspectos de seguridad

No aplica.

---

## 6. Procedimiento o metodología para el desarrollo

El objetivo de este proyecto es trabajar en parejas para implementar un proyecto de ciencia de datos, desde la selección del dataset, posterior limpieza, pasando por la visualización hasta finalmente implementar un modelo predictivo basado en aprendizaje supervisado.

### 6.1. Selección del dataset

Buscar una base de datos de acceso libre (Open Data), que cumpla las siguientes condiciones:

- Se recomienda buscar una base de datos que contenga por lo menos 10.000 registros (filas).
- El dataset debe requerir limpieza (valores nulos, formatos inconsistentes, etc.).
- Adicionalmente, debe ser apto para implementar un modelo de Aprendizaje Supervisado (Clasificación o Regresión). Debes identificar claramente cuál es su variable objetivo (target).

**Fuentes sugeridas:**

- Kaggle — <https://www.kaggle.com>
- Google Dataset Search — <https://datasetsearch.research.google.com>
- UCI Machine Learning Repository — <https://archive.ics.uci.edu>
- SNIES — <https://snies.mineducacion.gov.co/portal/ESTADISTICAS/Bases-consolidadas>
- Datos Abiertos Colombia — <https://www.datos.gov.co>

### 6.2. Inspección y perfilado

Cargar el dataset en Python (Pandas) y **realizar un análisis descriptivo inicial** donde establezca dimensiones, tipos de datos, distribución de variables, identificación de valores faltantes (nulls/NaN), detección de valores atípicos (outliers), gráficos de correlación y matriz de correlaciones inicial.

### 6.3. Preprocesamiento y limpieza de datos

En esta etapa debe definir y aplicar una estrategia de limpieza para las columnas afectadas. Se espera que utilice imputación (media, mediana, moda), eliminación de filas/columnas (justificada), codificación de variables categóricas, o normalización/escalado si aplica.

### 6.4. Inspección y perfilado

Realizar nuevamente el análisis de distribución y correlaciones con el dataset limpio. Comparar métricas y gráficos con la etapa inicial para evidenciar la mejora en la calidad de los datos. **Exportar el dataset limpio en un archivo `*.csv`.**

### 6.5. Dashboard interactivo

Implementar un Dashboard interactivo en **Power BI** conectado al dataset ya limpio. El dashboard debe mostrar la distribución de las variables principales y las correlaciones más relevantes con la variable objetivo.

### 6.6. Implementación de un modelo de aprendizaje supervisado

**6.6.1.** Implementación de un modelo de aprendizaje supervisado a partir del dataset limpio. En esta etapa debe implementar un modelo de aprendizaje automático supervisado para predecir la variable objetivo. Se debe evaluar el modelo usando métricas de desempeño adecuadas al tipo de problema (por ejemplo, matriz de confusión, accuracy, F1-score para **clasificación**; MSE, RMSE, R² para **regresión**).

**6.6.2.** Realizar una optimización de hiperparámetros usando GridSearch para intentar mejorar el resultado base. Comparar el desempeño del modelo antes y después de optimizar.

---

## 7. Parámetros para elaboración del informe

**7.1.** Elaborar un **informe final**, el cual debe incluir un informe corto (de máximo 2-3 páginas) donde describan la base de datos, resuman el proceso de limpieza que realizaron, los gráficos y/o resultados más relevantes y mostrar los hallazgos y conclusiones. Renombrar los archivos con la estructura `Nombre1Apellido1_Nombre1Apellido1_ProyectoFinal`.

**7.2.** Al momento de entregar deberán **presentar los siguientes archivos:**

- Informe final.
- Notebook de Python, en el cual realizaron la limpieza de la base de datos.
- Dashboard de Power BI.
- Notebook de Python, en donde implementaron el modelo de aprendizaje supervisado.

**7.3.** La **sustentación** se realizará el **jueves 28 de mayo de 2026** en el aula (presencial). Cada equipo tendrá 15 minutos para presentar sus hallazgos y mostrar el funcionamiento del modelo y el dashboard.

---

## 8. Disposición de residuos

No aplica.

---

## 9. Bibliografía

1. <https://github.com/estebangonzalezITM/DataScience>
2. McKinney, W. (2022). *Pandas: Powerful Python data analysis toolkit.*
3. Healy, K. (2019). *Data visualization: A practical introduction.*

---

| Campo | Valor |
|---|---|
| Elaborado por | Esteban Gonzalez Valencia |
| Revisado por | — |
| Versión | 1 |
| Fecha | Mayo de 2026 |
