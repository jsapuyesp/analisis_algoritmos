modulo = 999999937
moduloUno = 1 % modulo
arrPascal = [[moduloUno], [moduloUno, moduloUno]]
arrMax = [moduloUno, moduloUno]
nivelMaximo = 0


def pascal():
    global nivelMaximo
    if(nivelMaximo <= 2):
        return
    else:
        global arrPascal
        global arrMax
        global modulo
        global moduloUno
        for level in range(1, nivelMaximo - 1):
            siguienteNivel = [moduloUno]
            nivelActual = arrPascal[level]
            
            maxsuma = 0
            for i in range(1, len(nivelActual)):
                suma = nivelActual[i - 1] + nivelActual[i]
                maxsuma = suma if(suma > maxsuma) else maxsuma
                siguienteNivel.append(suma)

            siguienteNivel.append(moduloUno)
            arrMax.append(maxsuma)
            arrPascal.append(siguienteNivel)


def getPascal(arr: list):
    global arrMax
    global nivelMaximo
    global modulo
    pascal()
    for level in arr:
        print(arrMax[level - 1] % modulo)


def main():
    global nivelMaximo
    cases = int(input())
    finalArr = []
    for _ in range(cases):
        level = int(input())
        nivelMaximo = level if(level > nivelMaximo) else nivelMaximo
        finalArr.append(level)

    getPascal(finalArr)


main()