r"""Genera imágenes PNG a partir de las páginas de un PDF.

Por cada página del PDF se genera un archivo PNG. La resolución (DPI) es
configurable por el usuario.

Requisitos:
    PyMuPDF  ->  .\.venv\Scripts\python.exe -m pip install PyMuPDF

Uso (desde la raíz del proyecto, con el ambiente virtual):
    .\.venv\Scripts\python.exe scripts\pdf_a_imagenes.py "ruta\al\archivo.pdf"
    .\.venv\Scripts\python.exe scripts\pdf_a_imagenes.py archivo.pdf --dpi 300
    .\.venv\Scripts\python.exe scripts\pdf_a_imagenes.py archivo.pdf -o salida --dpi 150
"""

import argparse
import sys
from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError:
    sys.exit(
        "Falta la dependencia 'PyMuPDF'. Instálala en el ambiente virtual con:\n"
        "    .\\.venv\\Scripts\\python.exe -m pip install PyMuPDF"
    )


def pdf_a_imagenes(pdf_path: Path, salida: Path, dpi: int) -> list[Path]:
    """Convierte cada página de `pdf_path` en un PNG dentro de `salida`.

    Devuelve la lista de rutas de las imágenes generadas.
    """
    salida.mkdir(parents=True, exist_ok=True)
    generadas: list[Path] = []

    with fitz.open(pdf_path) as documento:
        total = documento.page_count
        ancho = len(str(total))  # para nombrar las páginas con ceros a la izquierda

        for indice, pagina in enumerate(documento, start=1):
            pixmap = pagina.get_pixmap(dpi=dpi)
            nombre = f"{pdf_path.stem}_pag{indice:0{ancho}d}.png"
            destino = salida / nombre
            pixmap.save(destino)
            generadas.append(destino)
            print(f"  [{indice}/{total}] {destino.name}  ({pixmap.width}x{pixmap.height}px)")

    return generadas


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Genera una imagen PNG por cada página de un PDF.",
    )
    parser.add_argument("pdf", type=Path, help="Ruta al archivo PDF de entrada.")
    parser.add_argument(
        "-o",
        "--salida",
        type=Path,
        default=None,
        help="Carpeta de salida. Por defecto: '<nombre_del_pdf>_imagenes' junto al PDF.",
    )
    parser.add_argument(
        "--dpi",
        type=int,
        default=200,
        help="Resolución de las imágenes en DPI (por defecto: 200).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    pdf_path: Path = args.pdf
    if not pdf_path.is_file():
        sys.exit(f"No se encontró el PDF: {pdf_path}")

    if args.dpi <= 0:
        sys.exit("El DPI debe ser un número entero mayor que 0.")

    salida: Path = args.salida or pdf_path.with_name(f"{pdf_path.stem}_imagenes")

    print(f"PDF:    {pdf_path}")
    print(f"Salida: {salida}")
    print(f"DPI:    {args.dpi}\n")

    generadas = pdf_a_imagenes(pdf_path, salida, args.dpi)

    print(f"\nListo. Se generaron {len(generadas)} imagen(es) en: {salida}")


if __name__ == "__main__":
    main()
