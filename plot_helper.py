from typing import List, Union, Tuple
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

#Funciones para graficar


def plot_pzmap(
    axes: plt.Axes,
    poles: np.ndarray[complex | float],
    zeros: np.ndarray[complex | float],
    radius: int = None,
) -> None:
    """
    Función que grafica el diagrama de polos y ceros

    :param poles: lista de polos. Recordar que los imaginarios se ponen con 1j
    :param zeros: lista de ceros
    :param radius: valor del radio del círculo que se dibuja. Si es None, no se dibuja ningún círculo

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

    :param wa: frecuencia de atenuación en rad/s
    :param wp: frecuencia de paso en rad/s
    :param gp: ganancia de la banda de paso en dB
    :param ga: ganancia de la banda de atenuación en dB

    """
    if isinstance(wa, float):
        # Lowpass
        if wa > wp:
            ax.add_patch(Rectangle((0, 0), wp, -gp, facecolor="green", alpha=0.2))
            ax.add_patch(Rectangle((wa, -ga), 100, -ga, facecolor="red", alpha=0.2))
        # Highpass
        elif wp > wa:
            ax.add_patch(Rectangle((wp, 0), 100, -gp, facecolor="green", alpha=0.2))
            ax.add_patch(Rectangle((0, -ga), wa, -ga, facecolor="red", alpha=0.2))

    else:
        # Notch
        if wa[0] > wp[0]:
            ax.add_patch(Rectangle((0, 0), wp[0], -gp, facecolor="green", alpha=0.2))
            ax.add_patch(
                Rectangle((wa[0], -ga), wa[1] - wa[0], -ga, facecolor="red", alpha=0.2)
            )
            ax.add_patch(Rectangle((wp[1], 0), 100, -gp, facecolor="green", alpha=0.2))
        # Bandpas
        elif wp[0] > wa[0]:
            ax.add_patch(
                Rectangle((wp[0], 0), wp[1] - wp[1], -gp, facecolor="green", alpha=0.2)
            )
            ax.add_patch(Rectangle((0, -ga), wa[0], -ga, facecolor="red", alpha=0.2))
            ax.add_patch(Rectangle((wa[1], -ga), 100, -ga, facecolor="red", alpha=0.2))
        # el valor 100 hardcodeado se puede modificar para que se extienda el cuadrado la longitud que quieran


def plot_bode(
    mag_axes: plt.Axes,
    ph_axes: plt.Axes,
    magnitude: np.ndarray[float],
    phase: np.ndarray[float],
    freqs: np.ndarray[float],
) -> None:
    """
    Función que grafica el bode

    :param mag_axes: eje donde se graficará la magnitud de la respuesta en frecuencia
    :param ph_axes: eje donde se graficará la fase de la respuesta en frecuencia
    :param magnitude: valores de magnitud de la respuesta en frecuencia en dB
    :param phase: valores de la fase de la respuesta en frecuencia en grados (deg)
    :param freqs: puntos de frecuencia donde la magnitud o fase fueron evaluados en Hz
    """
    ph_axes.sharex(mag_axes)
    mag_axes.grid()
    ph_axes.grid()
    mag_axes.plot(freqs, magnitude)
    ph_axes.plot(freqs, phase)
    mag_axes.set_title("Magnitud")
    mag_axes.set_ylabel("Magnitud (dB)")
    ph_axes.set_title("Fase")
    ph_axes.set_ylabel("Fase (grados)")
    ph_axes.set_xlabel("Frecuencia (Hz)")


def plot_time(
    axes: plt.Axes,
    t: np.ndarray[float],
    y1: np.ndarray[float],
    y2: np.ndarray[float],
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


def create_figure(width, height) -> Tuple[plt.Figure, plt.Axes]:
    """
    Función que crea una figura y un eje

    :param width: Ancho de la figura en cm
    :param height: Alto de la figura en cm
    """
    return plt.subplots(figsize=(width / 100, height / 100))
