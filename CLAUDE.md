# CLAUDE.md

Guía para Claude Code al trabajar en este proyecto.

## Regla obligatoria: usar siempre el ambiente virtual

Para **ejecutar cualquier script de Python, instalar paquetes, correr notebooks o
cualquier tarea relacionada con Python**, se debe usar **siempre** el ambiente
virtual del proyecto, ubicado en `.venv` en la raíz del repositorio.

Nunca uses el Python global del sistema ni `python`/`pip` sin activar o
referenciar el entorno virtual.

### Cómo usar el ambiente virtual (Windows / PowerShell)

Opción A — Activar el entorno antes de ejecutar:

```powershell
.\.venv\Scripts\Activate.ps1
python script.py
pip install <paquete>
```

Opción B (recomendada para comandos individuales) — Referenciar directamente el
ejecutable del entorno, sin activarlo:

```powershell
.\.venv\Scripts\python.exe script.py
.\.venv\Scripts\python.exe -m pip install <paquete>
```

### Notebooks (.ipynb)

Los notebooks en `Ciencia_datos/files/` deben ejecutarse con el kernel del
ambiente virtual `.venv`. No uses kernels de otra instalación de Python.

### Verificación rápida

Antes de ejecutar, confirma que estás usando el intérprete correcto:

```powershell
.\.venv\Scripts\python.exe -c "import sys; print(sys.executable)"
```

La ruta resultante debe apuntar a `...\Mi Dory\.venv\Scripts\python.exe`.

## Dependencias

Las dependencias de Python se registran en `requirements.txt`. Para instalarlas
en el ambiente virtual:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Al instalar un paquete nuevo, actualiza `requirements.txt` (por ejemplo con
`.\.venv\Scripts\python.exe -m pip freeze`).

## Scripts (`scripts/`)

Utilidades de Python del proyecto. Ejecútalas siempre con el ambiente virtual.

- **`scripts/pdf_a_imagenes.py`** — Genera una imagen PNG por cada página de un
  PDF, con resolución (DPI) configurable.

  ```powershell
  .\.venv\Scripts\python.exe scripts\pdf_a_imagenes.py "archivo.pdf" --dpi 300
  .\.venv\Scripts\python.exe scripts\pdf_a_imagenes.py archivo.pdf -o salida --dpi 150
  ```

  Por defecto usa 200 DPI y crea la carpeta `<nombre_del_pdf>_imagenes` junto al
  PDF. Requiere `PyMuPDF` (incluida en `requirements.txt`).

## Estructura del proyecto

El contenido está organizado por tema en carpetas de primer nivel:

- **`Geometria_vectorial/`** — Sitio web educativo de geometría vectorial
  ("para mi Dory"). Los `.html` en la raíz de la carpeta forman el sitio
  (entrada: `index.html`) y se enlazan entre sí con rutas relativas; mantenlos
  juntos para no romper los enlaces. En `files/` está el material fuente (no
  referenciado por el HTML): notas y las subcarpetas `Taller_Parcial_Institucional/`
  y `Parcial/` con sus PDF, imágenes y transcripciones.
- **`Ciencia_datos/`** — Proyecto de ciencia de datos de la cafetería: PDF del
  proyecto final y, en `files/`, los notebooks (limpieza y modelo ML) e informe.
- **`Preparacion_entrevista/`** — Material de preparación de entrevista (.NET/Azure).
- **`scripts/`** — Utilidades de Python del proyecto (ver sección "Scripts").
- **`_temp/`** — Archivos temporales o sin clasificar.

## Notas del proyecto

- Python del entorno: **3.13.11** (creado con miniconda/venv).
