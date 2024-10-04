
from typing import Tuple
import scipy.signal as ss
import numpy as np
import sympy as sp


# Funciones transformacion:
# TODO: Completar los parametros que deberían recibir


def lp2lp(h: sp.Expr, s: sp.Symbol, ) -> sp.Expr:
    """
        Función que convierte una función de transferencia LP a LP

        :param h: Función de transferencia LP
        :param s: Simbolo de la variable de Laplace
        ...
        :return: Función de transferencia LP
    """
    raise NotImplementedError("Esta función no está implementada")

def lp2hp(h: sp.Expr, s: sp.Symbol, ) -> sp.Expr:
    """
        Función que convierte una función de transferencia LP a HP

        :param h: Función de transferencia LP
        :param s: Simbolo de la variable de Laplace
        ...
        :return: Función de transferencia HP
    """
    raise NotImplementedError("Esta función no está implementada")

def lp2bp(h: sp.Expr, s: sp.Symbol, ) -> sp.Expr:
    """
        Función que convierte una función de transferencia LP a BP

        :param h: Función de transferencia LP
        :param s: Simbolo de la variable de Laplace
        ...
        :return: Función de transferencia BP
    """
    raise NotImplementedError("Esta función no está implementada")

def lp2br(h: sp.Expr, s: sp.Symbol, ) -> sp.Expr:
    """
        Función que convierte una función de transferencia LP a BR

        :param h: Función de transferencia LP
        :param s: Simbolo de la variable de Laplace
        ...
        :return: Función de transferencia BR
    """
    raise NotImplementedError("Esta función no está implementada")
