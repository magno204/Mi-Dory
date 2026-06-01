"""Genera las gráficas de los ángulos solución del Taller #1 (puntos 4 y 5).

Cada ángulo se dibuja como un radio sobre el círculo unitario, en el plano
cartesiano, con su etiqueta en grados y radianes. Las imágenes se guardan en
esta misma carpeta para incrustarlas en el documento de soluciones.

Ejecutar con el ambiente virtual del proyecto:
    .\\.venv\\Scripts\\python.exe Matematicas_basicas\\graficar_angulos.py
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # backend sin ventana, solo guardar archivos
import matplotlib.pyplot as plt
import numpy as np

SALIDA = Path(__file__).parent


def base_plano(ax, titulo):
    """Dibuja ejes, círculo unitario y rejilla del plano cartesiano."""
    theta = np.linspace(0, 2 * np.pi, 400)
    ax.plot(np.cos(theta), np.sin(theta), color="#bbbbbb", lw=1.2, zorder=1)

    # Ejes
    ax.axhline(0, color="#444444", lw=1.0, zorder=2)
    ax.axvline(0, color="#444444", lw=1.0, zorder=2)

    ax.set_xlim(-1.45, 1.45)
    ax.set_ylim(-1.45, 1.45)
    ax.set_aspect("equal")
    ax.set_xticks([-1, -0.5, 0.5, 1])
    ax.set_yticks([-1, -0.5, 0.5, 1])
    ax.grid(True, color="#eeeeee", zorder=0)
    ax.set_title(titulo, fontsize=13, weight="bold")
    ax.set_xlabel("x")
    ax.set_ylabel("y")


def dibujar_angulos(ax, angulos, color):
    """angulos: lista de (grados, etiqueta_radianes)."""
    for grados, etiqueta in angulos:
        r = np.radians(grados)
        x, y = np.cos(r), np.sin(r)
        # Radio
        ax.annotate(
            "",
            xy=(x, y),
            xytext=(0, 0),
            arrowprops=dict(arrowstyle="-|>", color=color, lw=2),
            zorder=3,
        )
        # Punto sobre el círculo
        ax.plot(x, y, "o", color=color, ms=7, zorder=4)
        # Etiqueta un poco más afuera del círculo
        ax.annotate(
            f"{grados}°\n{etiqueta}",
            xy=(1.22 * x, 1.22 * y),
            ha="center",
            va="center",
            fontsize=10,
            color=color,
            weight="bold",
            zorder=5,
        )


def main():
    # ----- Punto 4: cos x + 1 = 2 sen^2 x -----
    fig, ax = plt.subplots(figsize=(6, 6))
    base_plano(ax, "Punto 4:  cos x + 1 = 2 sen²x")
    dibujar_angulos(
        ax,
        [(60, "π/3"), (180, "π"), (300, "5π/3")],
        color="#1f77b4",
    )
    fig.tight_layout()
    fig.savefig(SALIDA / "punto4_angulos.png", dpi=150)
    plt.close(fig)

    # ----- Punto 5: tan a + tan^2 a = 0 -----
    fig, ax = plt.subplots(figsize=(6, 6))
    base_plano(ax, "Punto 5:  tan α + tan²α = 0")
    dibujar_angulos(
        ax,
        [(0, "0 / 2π"), (135, "3π/4"), (180, "π"), (315, "7π/4")],
        color="#d62728",
    )
    fig.tight_layout()
    fig.savefig(SALIDA / "punto5_angulos.png", dpi=150)
    plt.close(fig)

    print("Imágenes generadas en:", SALIDA)


if __name__ == "__main__":
    main()
