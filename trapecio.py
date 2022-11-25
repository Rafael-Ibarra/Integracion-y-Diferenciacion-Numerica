def procesoTrapecio(funcion, segundaDerivadaIntegrada, segmentos, a, b):
    h  = (b - a) / segmentos
    x  = [a]
    fx = [funcion(a)]
    sumatoria = a

    for i in range(segmentos):
        sumatoria += h
        x.append(sumatoria)
        fx.append(funcion(x[i+1]))
    
    sumatoria = 0
    size = len(fx)

    for i in range(len(fx)):
        if((i > 0) and (i < size-1)):
            sumatoria += fx[i]
    
    i = ((fx[0] + (2*sumatoria) + fx[size-1]) / (2*segmentos)) * (b - a)
    e = ((-(b-a)**2) / (12*(segmentos**2))) * (segundaDerivadaIntegrada(b) - segundaDerivadaIntegrada(a))

    return i, e