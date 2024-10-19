from typing import List, Sequence, Union, Tuple
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

# Funciones para graficar


def plot_pzmap(
    axes: plt.Axes,
    poles: Sequence[Union[complex, float]],
    zeros: Sequence[Union[complex, float]],
    radius: int = None,
) -> None:
    """
        Función que grafica el diagrama de polos y ceros

        :param axes:  Eje en donde se grafican los polos y ceros
        :param poles: Lista de polos. Recordar que los imaginarios se ponen con 1j
        :param zeros: Lista de ceros. Recordar que los imaginarios se ponen con 1j
        :param radius: Valor del radio del círculo que se dibuja. Si es None, no se dibuja ningún círculo

    """
    axes.grid()
    axes.plot(np.real(poles), np.imag(poles), "bx")
    axes.plot(np.real(zeros), np.imag(zeros), "bo")
    axes.set_xlabel("$\\sigma$")
    axes.set_ylabel("$j\\omega$")
    if radius is not None:
        circle = plt.Circle(
            (0, 0), radius, color="black", fill=False, linestyle="dotted"
        )
        axes.add_patch(circle)


def plot_plantilla(
    ax: plt.Axes,
    wa: Union[List[float], float],
    wp: Union[List[float], float],
    gp: float,
    ga: float,
) -> None:
    """
        Función que grafica la plantilla

        :param ax: Eje en donde se grafica la plantilla
        :param wa: Frecuencia de atenuación en rad/s
        :param wp: Frecuencia de paso en rad/s
        :param gp: Ganancia de la banda de paso
        :param ga: Ganancia de la banda de atenuación
    """
    if isinstance(wa, (float, int)):
        # Lowpass
        if wa > wp:
            ax.add_patch(Rectangle((0, 0), wp, -gp,
                         facecolor="green", alpha=0.2))
            ax.add_patch(Rectangle((wa, -ga), 100, -ga,
                         facecolor="red", alpha=0.2))
        # Highpass
        elif wp > wa:
            ax.add_patch(Rectangle((wp, 0), 100, -gp,
                         facecolor="green", alpha=0.2))
            ax.add_patch(Rectangle((0, -ga), wa, -ga,
                         facecolor="red", alpha=0.2))

    else:
        # Notch
        if wa[0] > wp[0]:
            ax.add_patch(
                Rectangle((0, 0), wp[0], -gp, facecolor="green", alpha=0.2))
            ax.add_patch(
                Rectangle((wa[0], -ga), wa[1] - wa[0], -
                          ga, facecolor="red", alpha=0.2)
            )
            ax.add_patch(
                Rectangle((wp[1], 0), 100, -gp, facecolor="green", alpha=0.2))
        # Bandpas
        elif wp[0] > wa[0]:
            ax.add_patch(
                Rectangle((wp[0], 0), wp[1] - wp[1], -gp,
                          facecolor="green", alpha=0.2)
            )
            ax.add_patch(
                Rectangle((0, -ga), wa[0], -ga, facecolor="red", alpha=0.2))
            ax.add_patch(
                Rectangle((wa[1], -ga), 100, -ga, facecolor="red", alpha=0.2))
        # el valor 100 hardcodeado se puede modificar para que se extienda el cuadrado la longitud que quieran


def plot_bode(
    mag_axes: plt.Axes,
    ph_axes: plt.Axes,
    magnitude: Sequence[float],
    phase: Sequence[float],
    freqs: Sequence[float],
) -> None:
    """
        Función que grafica el bode

        :param mag_axes: Eje donde se graficará la magnitud de la respuesta en frecuencia
        :param ph_axes: Eje donde se graficará la fase de la respuesta en frecuencia
        :param magnitude: Valores de magnitud de la respuesta en frecuencia en dB
        :param phase: Valores de la fase de la respuesta en frecuencia en grados (deg)
        :param freqs: Puntos de frecuencia donde la magnitud o fase fueron evaluados en Hz
    """
    ph_axes.sharex(mag_axes)
    mag_axes.semilogx(freqs, magnitude)
    ph_axes.semilogx(freqs, phase)
    mag_axes.grid()
    ph_axes.grid()
    mag_axes.set_title("Magnitud")
    mag_axes.set_ylabel("Magnitud (dB)")
    ph_axes.set_title("Fase")
    ph_axes.set_ylabel("Fase (grados)")
    ph_axes.set_xlabel("Frecuencia (Hz)")


def plot_time(
    axes: plt.Axes,
    t: Sequence[float],
    y1: Sequence[float],
    y2: Sequence[float],
    label1=None,
    label2=None,
    color1="blue",
    color2="red",
) -> None:
    """
        Funcion para graficar dos funciones temporales en el mismo gráfico

        :param axes: Eje donde se graficarán las funciones temporales
        :param t: Vector de tiempo
        :param y1: Vector de valores para la función temporal 1
        :param y2: Vector de valores para la función temporal 2
        :param label1: Etiqueta para la función temporal 1 (opcional)
        :param label2: Etiqueta para la función temporal 2 (opcional)
        :param color1: Color para la función temporal 1 (opcional). Default: azul
        :param color2: Color para la función temporal 2 (opcional). Default: rojo

    """
    axes.grid()
    axes.plot(t, y1, color=color1, label=label1)
    axes.plot(t, y2, color=color2, label=label2)
    axes.set_xlabel("Tiempo")
    axes.set_ylabel("Amplitud")


def create_figure(width, height, axes_num=1) -> Tuple[plt.Figure, Union[plt.Axes, List[plt.Axes]]]:
    """
        Función que crea una figura y un eje

        :param width: Ancho de la figura en cm
        :param height: Alto de la figura en cm
    """
    return plt.subplots(nrows=axes_num, figsize=(width, height))
