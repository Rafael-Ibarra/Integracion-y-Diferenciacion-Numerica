from simpson import *
from trapecio import *
from math import log
from math import e

def funcion_1(x):
    return (x**2) * log(x)

def cuartaDerivada_1(x):
    return -2/(x**2)

def funcion_2(x):
    return (x**2)*(e**(-x))

def cuartaDerivada_2(x):
    return ((x**2) - (8*x) +12) * (e**(-x))

def funcion_8(x):
    return (x-1)*((2*x)+3)

def segundaDerivadaIntegrada_8(x):
    return 4*x

if(__name__) == "__main__":
    print(procesoSimpson(funcion_1, cuartaDerivada_1, 5, 1, 1.5))
    print(procesoSimpson(funcion_2, cuartaDerivada_2, 7, 0, 1))
    print(procesoTrapecio(funcion_8, segundaDerivadaIntegrada_8, 7, -1, 2))