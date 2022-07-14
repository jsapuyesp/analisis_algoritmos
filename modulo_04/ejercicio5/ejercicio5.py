Casos = int(input())
tMax = 4320
inicial = 360
noDisponible = [1440, 1800, 2880, 3240]
for c in range(Casos):
    n = int(input())
    tiempos = []
    for _ in range(n):
        entrada = [x for x in input().split()]
        minutosIniciales = 0
        if entrada[0] == 'lunes':
            minutosIniciales = 2880
        if entrada[0] == 'domingo':
            minutosIniciales = 1440

        h = entrada[1].split(':')
        
        mInicial = minutosIniciales + (int  (h[0]) * 60) + int  (h[1])
        mFinal = mInicial + int(entrada[2])
        posibleValor = [mInicial, mFinal, entrada[0]]
        valido = False
        if posibleValor[2] == 'sabado':
            if 360 <= posibleValor[0] <= 1440 and 360 <= posibleValor[1] <= 1440:
                valido = True
        if posibleValor[2] == 'domingo':
            if 1800 <= posibleValor[0] <= 2880 and 1800 <= posibleValor[1] <= 2880:
                valido = True
        if posibleValor[2] == 'lunes':
            if 3240 <= posibleValor[0] <= 4320 and 3240 <= posibleValor[1] <= 4320:
                valido = True
        if valido:
            tiempos.append(posibleValor)
    tiempos.sort(key=lambda t: t[1])
    result = []
    if len(tiempos) == 0:
        print(0)
    else:
        result.append(tiempos[0])
        k = 0
        for i in range(1, len(tiempos)):
            if tiempos[i][0] >= tiempos[k][1]:
                result.append(tiempos[i])
                k = i
        print(len(result))