# Guion para el Dashboard de Power BI — Proyecto Cafetería

Guía paso a paso para construir el entregable **Dashboard de Power BI** (guía 6.5 y 7.2)
sobre el dataset limpio `cafeteria_limpio.csv`.

> **Objetivo según la guía (6.5):** mostrar la *distribución de las variables principales*
> y las *correlaciones más relevantes con la variable objetivo* (`Propina`).

Archivo final a entregar: **`YennyCastano_ProyectoFinal_Dashboard.pbix`**

---

## 0. Requisitos

- **Power BI Desktop** (gratis, Windows): descárgalo de Microsoft Store o
  [powerbi.microsoft.com/desktop](https://powerbi.microsoft.com/desktop/).
- El archivo **`cafeteria_limpio.csv`** (está en `Ciencia_datos/files/`).

---

## 1. Importar los datos

1. `Inicio → Obtener datos → Texto/CSV`.
2. Selecciona `cafeteria_limpio.csv`.
3. En la vista previa, confirma **Origen de archivo: 65001: Unicode (UTF-8)** (el CSV se
   exportó con `utf-8-sig`, así las tildes y la `ñ` se ven bien).
4. Pulsa **Transformar datos** (abre Power Query) para revisar tipos antes de cargar.

### Tipos de dato correctos (Power Query)

| Columna | Tipo |
|---|---|
| `Fecha` | Fecha |
| `Hora de Cobro` | Número entero (0–23) |
| `Mesa`, `Precio`, `Propina` | Número entero |
| `Cantidad` | Número decimal |
| `Latitud`, `Longitud` | Número decimal |
| `Codigo Ciudad` | Texto *(es un código, no una cifra a sumar)* |
| Resto (`Vendedor`, `Zona`, `Tipo de pago`, …) | Texto |

5. `Cerrar y aplicar`.

> Sugerencia: para `Latitud`/`Longitud`, en el panel de campos marca la categoría de
> datos como **Latitud** y **Longitud** (`Herramientas de columna → Categoría de datos`),
> así el mapa las ubica bien.

---

## 2. Crear una tabla de calendario (para el análisis temporal)

En `Modelado → Nueva tabla`, pega:

```DAX
Calendario =
ADDCOLUMNS (
    CALENDAR ( MIN ( cafeteria_limpio[Fecha] ), MAX ( cafeteria_limpio[Fecha] ) ),
    "Año", YEAR ( [Date] ),
    "Mes", FORMAT ( [Date], "MMM" ),
    "MesNum", MONTH ( [Date] ),
    "AñoMes", FORMAT ( [Date], "YYYY-MM" )
)
```

Luego relaciona `Calendario[Date]` ↔ `cafeteria_limpio[Fecha]` (vista **Modelo**, arrastra
una columna sobre la otra; relación 1:* ).

---

## 3. Medidas DAX (cópialas con `Nueva medida`)

```DAX
Total Transacciones = COUNTROWS ( cafeteria_limpio )

Propina Promedio = AVERAGE ( cafeteria_limpio[Propina] )

Total Propinas = SUM ( cafeteria_limpio[Propina] )

Precio Promedio = AVERAGE ( cafeteria_limpio[Precio] )

Ingreso Total = SUMX ( cafeteria_limpio, cafeteria_limpio[Precio] * cafeteria_limpio[Cantidad] )

% Propina sobre Precio =
DIVIDE ( [Total Propinas], SUM ( cafeteria_limpio[Precio] ) )
```

> Da formato de moneda (COP) a `Propina Promedio`, `Total Propinas`, `Precio Promedio` e
> `Ingreso Total` desde `Herramientas de medida → Formato`.

---

## 4. Diseño del dashboard (1–2 páginas)

### Página 1 — "Visión general y variable objetivo"

**Fila de tarjetas (KPIs)** arriba — visual *Tarjeta*:
- `Total Transacciones`
- `Propina Promedio`
- `Precio Promedio`
- `Total Propinas`

**Distribución de la variable objetivo (Propina):**
- Visual *Gráfico de columnas agrupadas* o *Histograma*.
  - Eje X: `Propina` (crea grupos/bins: clic derecho en el campo → *Nuevo grupo* → tamaño
    de bin, p. ej. 5 COP).
  - Eje Y: `Total Transacciones`.

**Correlaciones con la variable objetivo (lo que pide la guía):**
- Visual *Gráfico de dispersión* (scatter) #1:
  - Eje X: `Precio` · Eje Y: `Propina` → muestra la correlación alta (r ≈ 0.83).
- Visual *Gráfico de dispersión* #2:
  - Eje X: `Cantidad` · Eje Y: `Propina` (r ≈ 0.83).

**Segmentaciones (slicers)** a la izquierda: `Año`, `Zona`, `Tipo de pago`.

### Página 2 — "Negocio: vendedor, zona y tiempo"

- **Propina/ventas por Vendedor** — *Gráfico de barras*:
  - Eje Y: `Vendedor` · Valores: `Total Transacciones` (y/o `Propina Promedio`).
- **Distribución geográfica (Zona / Tolima)** — *Mapa*:
  - Ubicación: `Municipio` (o `Latitud`+`Longitud`) · Tamaño: `Total Transacciones`.
  - Alternativa sin mapa: *barras* por `Zona`.
- **Tipo de pago** — *Gráfico de anillo (donut)*:
  - Leyenda: `Tipo de pago` · Valores: `Total Transacciones` (≈ 72% Contado / 28% Crédito).
- **Evolución temporal** — *Gráfico de líneas*:
  - Eje X: `Calendario[AñoMes]` · Valores: `Total Transacciones` (o `Total Propinas`).
- **Ventas por Categoría/Producto** — *Treemap* o *barras*:
  - Categoría: `Categoria` · Valores: `Total Transacciones`.

---

## 5. Formato y tema

- `Vista → Temas → Buscar temas` e importa **`files/PowerBI_Theme_Cafeteria.json`**
  (paleta de tonos café acorde al proyecto, ya incluido en el repo).
- Añade un **título** a cada página (cuadro de texto): "Cafetería — Análisis de Propinas".
- Activa **interacciones cruzadas**: al hacer clic en un vendedor/zona, el resto de visuales
  se filtra (es lo que hace el dashboard "interactivo", requisito 6.5).

---

## 6. Guardar y entregar

1. `Archivo → Guardar como` → **`YennyCastano_ProyectoFinal_Dashboard.pbix`**.
2. Guárdalo en `Ciencia_datos/files/` junto al resto de entregables.

---

## Mapa: requisito de la guía → visual del dashboard

| Requisito (6.5) | Cómo se cumple |
|---|---|
| Distribución de variables principales | Histograma de `Propina`, barras por `Vendedor`/`Zona`/`Categoria`, donut de `Tipo de pago` |
| Correlaciones con la variable objetivo | Scatter `Precio` vs `Propina` y `Cantidad` vs `Propina` |
| Dashboard **interactivo** | Slicers (`Año`, `Zona`, `Tipo de pago`) + interacciones cruzadas entre visuales |

> Hallazgos que el dashboard debe dejar ver (coherentes con el informe): la propina sube
> con el precio y la cantidad; el reparto entre vendedores es equilibrado; la zona **Sur**
> lidera en volumen; predomina el pago de **Contado**.
