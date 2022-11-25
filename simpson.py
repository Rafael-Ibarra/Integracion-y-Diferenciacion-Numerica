def reglaPar(cuartaDerivada, fx, segmentos, a, b, separacion=0):
    sumatoriaPar   = 0
    sumatoriaImpar = 0
    size = len(fx)

    for i in range(size):
        if((i > 0) and (i < size-1)):
            if(i % 2 == 0):
                sumatoriaPar += fx[i]
            else:
                sumatoriaImpar += fx[i]
    
    if(separacion > 0):
        i = ((fx[0] + (4*sumatoriaImpar) + (2*sumatoriaPar) + fx[separacion]) / (3*(size-1))) * (b - a)
    else:
        i = ((fx[0] + (4*sumatoriaImpar) + (2*sumatoriaPar) + fx[size-1]) / (3*segmentos)) * (b - a)
    
    promedio = (cuartaDerivada(a) + cuartaDerivada(b)) / 2
    e = ((-(b-a)**5) / (180*(segmentos**4))) * promedio

    return i, e

def reglaImpar(cuartaDerivada, fx, a, b):
    i = ((fx[0] + 3*(fx[1]) + 3*(fx[2]) + fx[3]) / 8) * (b - a)

    promedio = (cuartaDerivada(a) + cuartaDerivada(b)) / 2
    e = ((-(b-a)**5) / 6480) * promedio

    return i, e

def procesoSimpson(funcion, cuartaDerivada, segmentos, a, b):
    h  = (b - a) / segmentos
    x  = [a]
    fx = [funcion(a)]
    sumatoria = a

    for i in range(segmentos):
        sumatoria += h
        x.append(sumatoria)
        fx.append(funcion(x[i+1]))   
    
    size = len(fx)

    if(segmentos % 2 == 0):
        return reglaPar(funcion, cuartaDerivada, segmentos, a, b)
    elif(segmentos > 3):
        separacion = segmentos - 3
        
        i1, e1 = reglaPar(cuartaDerivada, fx[0:(separacion+1)], separacion, x[0], x[separacion], separacion)
        i2, e2 = reglaImpar(cuartaDerivada, fx[separacion:(size+1)], x[separacion], x[size-1])

        return (i1 + i2), (e1 + e2)
    else:
        return reglaImpar(funcion, cuartaDerivada, segmentos, a, b)