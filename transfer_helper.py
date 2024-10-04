from typing import Tuple, Union
import scipy.signal as ss
import numpy as np
import sympy as sp


#Funciones para conseguir la función transferencia

def poly_to_hsqr(poly: sp.Poly, xi: Union[float, sp.Symbol]) -> sp.Expr:
    """
        Función que parte de un polinomio y un Xi y devuelve la funcion H^2(w)

        :param poly: Polinomio a partir del cual se calcula H^2(w)
        :param xi: variable simbolica o numerica que representa el Xi
        :return: Expresión simbolica de H^2(w)
    """
    raise NotImplementedError("Esta función no está implementada")


def hsqrw_to_hs(hsqr: sp.Expr, w: sp.Symbol) -> ss.TransferFunction:
    """
        Función que parte de una funcion H^2(w) y devuelve la funcion H(s)

        :param hsqr: funcion H^2(w). Tiene que contenes una unica variable angular w
        :param w: variable simbolica que representa la frecuencia angular
        :return: funcion H(s)
    """
    # TODO: Implementar matematica y separacion de numerador y denominador
    
    # Completar num y den con lo pedido
    num: sp.Poly = 1
    den: sp.Poly = 1
    #Calculos de polos y ceros
    
    # Devuelve los coeficientes del polinomio, incluidos los que son 0
    num_coeffs = num.all_coeffs()   
    den_coeffs = den.all_coeffs()

    polos = np.roots(num_coeffs)
    ceros = np.roots(den_coeffs)

    # TODO: Seleccionar polos y ceros

    # TODO: Generar la transferencia con la clase de scipy. Recomndacion: Investigar ZPK y SOS en la documentacion de scipy.

    raise NotImplementedError("Esta función no está implementada")