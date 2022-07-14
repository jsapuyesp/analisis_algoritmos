import itertools as it
casos = int(input())

for i in range(0,casos):
    linea = input().split()
    map_linea = map(int, linea)
    lista_int = list(map_linea)

    p = list(it.product([0,1], repeat = len(lista_int)))
    suma = 0

    for j in p:
        sumaAux = 0
        anterior = False
        for k in range(len(j)):
            if j[k] == 1:
                sumaAux += lista_int[k]
                if anterior:
                    sumaAux -= lista_int[k-1]
                anterior = True
            else:
                anterior = False
        if sumaAux > suma:
            suma = sumaAux
    print(suma)