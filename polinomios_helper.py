from typing import Tuple
import scipy.signal as ss
import numpy as np
import sympy as sp
# Funciones para obtener los polinomios de orden n

def butter(ord: int) -> Tuple[sp.Poly, sp.Symbol]:
    """
        Función que devuelve el polinomio de Butterworth de orden n
        
        :param ord: Orden del polinomio de Butterworth
        :return: Polinomio de Butterworth de orden n (poly) y la variable del polinomio (symbol)
    """
    raise NotImplementedError("Esta función no está implementada")


def chebyshev(ord: int) -> Tuple[sp.Poly, sp.Symbol]:
    """
        Función que devuelve el polinomio de Chebyshev de orden n
        
        :param ord: Orden del polinomio de Chebyshev
        :return: Polinomio de Chebyshev de orden n (poly) y la variable del polinomio (symbol)
    """
    raise NotImplementedError("Esta función no está implementada")


def cauer(ord: int) -> Tuple[sp.Poly, sp.Symbol]:
    """
        Función que devuelve el polinomio de Cauer de orden n

        :param ord: Orden del polinomio de Cauer
        :return: Polinomio de Cauer de orden n (poly) y la variable del polinomio (symbol)
    """
    raise NotImplementedError("Esta función no está implementada")


def optimo_L(ord: int) -> Tuple[sp.Poly, sp.Symbol]:
    """
        Función que devuelve el polinomio L de orden n

        :param ord: Orden del polinomio L
        :return: Polinomio L de orden n (poly) y la variable del polinomio (symbol)
    """
    raise NotImplementedError("Esta función no está implementada")


def bessel(ord: int) -> Tuple[sp.Poly, sp.Symbol]:
    """
        Función que devuelve el polinomio de Bessel de orden n

        :param ord: Orden del polinomio de Bessel
        :return: Polinomio de Bessel de orden n (poly) y la variable del polinomio (symbol)
    """
    raise NotImplementedError("Esta función no está implementada")