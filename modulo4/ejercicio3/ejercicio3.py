casos = int(input())

for _ in range(0,casos):
    n = int(input())
    matriz = []
    for _ in range(n):
        linea = input().split()
        map_linea = map(int, linea)
        lineaAux = list(map_linea)
        matriz.append(lineaAux)
    indice = 0
    for i in matriz:
        razon = i[1] / i[0]
        matriz[indice].append(razon)
        indice += 1
    matriz.sort(key=lambda e: e[2], reverse=True)
    suma = 0
    total = 0
    for i in matriz:
        tiempo = total + i[0]
        suma += (tiempo - i[0]) * i[1]
        total += i[0]
    print(suma)