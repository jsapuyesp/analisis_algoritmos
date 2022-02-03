grafoActual = {}
familiaActual = []


def verMiembros(key):
    global grafoActual
    global familiaActual

    registro = [key]
    while(len(registro) != 0):
        nodo = registro.pop()
        if(grafoActual[nodo]['explorado'] == True):
            continue
        else:
            grafoActual[nodo]['explorado'] = True
            if (nodo not in familiaActual):
                familiaActual.append(nodo)

            for nodoN in grafoActual[nodo]['related']:
                if(grafoActual[nodoN]['explorado'] == False):
                    registro.append(nodoN)


def info(grafo: object):
    global grafoActual
    global familiaActual

    grafoActual = grafo
    familias = []
    for key in grafo:
        nodoActial = grafo[key]
        if(nodoActial['explorado'] == False):
            familiaActual = []
            verMiembros(key)
            familias.append(familiaActual)

    maxN = 0
    for family in familias:
        maxN = max(maxN, len(family))

    print(f"{len(familias)} {maxN}")


def main():
    casos = int(input())
    arr = []
    for _ in range(casos):
        R = int(input())
        grafo = {}
        for __ in range(R):
            registro = [x for x in input().split()]

            if(grafo.get(registro[0]) == None):
                grafo[registro[0]] = {
                    "explorado": False,
                    "related": []
                }

            if(grafo.get(registro[1]) == None):
                grafo[registro[1]] = {
                    "explorado": False,
                    "related": []
                }

            related1 = grafo[registro[0]]['related']
            related2 = grafo[registro[1]]['related']

            if(registro[1] not in related1):
                related1.append(registro[1])

            if(registro[0] not in related2):
                related2.append(registro[0])

        arr.append(grafo)

    for grafo in arr:
        info(grafo)


main()