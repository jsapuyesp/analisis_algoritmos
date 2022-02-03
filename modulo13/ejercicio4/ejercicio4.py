grafo = {}
nodosOrdenados = []
t = 0


def DFS1(idNodo):
    global grafo
    global nodosOrdenados
    global t

    nodo = grafo[idNodo]
    nodo['explorado2'] = True
    for idNodoN in nodo['related2']:
        nuevoNodo = grafo[idNodoN]
        if(nuevoNodo['explorado2'] == False):
            DFS1(idNodoN)

    nodosOrdenados[t] = idNodo
    t += 1


def DFS2(idNodo):
    global grafo

    nodo = grafo[idNodo]
    nodo['explorado'] = True
    for idNodoN in nodo['related']:
        nuevoNodo = grafo[idNodoN]
        if(nuevoNodo['explorado'] == False):
            DFS2(idNodoN)


def combos(iGrafo: object):
    global grafo
    global nodosOrdenados
    global t

    grafo = iGrafo
    nodosOrdenados = [None for _ in range(len(grafo))]
    t = 0

    for idNodo in grafo:
        if(grafo[idNodo]['explorado2'] == False):
            DFS1(idNodo)

    combos = 0
    nodosOrdenados.reverse()

    for idNodo in nodosOrdenados:
        if(grafo[idNodo]['explorado'] == False):
            DFS2(idNodo)
            combos += 1

    print(combos)


def main():
    arr = []
    while True:
        M = int(input())
        if(M == 0):
            break

        iGrafo = {}
        for _ in range(M):
            arrN = input().split()
            origen = arrN[0]
            destino = arrN[1]
            # Create new nodos
            if(iGrafo.get(origen) == None):
                iGrafo[origen] = {
                    "explorado": False,
                    "related": [],
                    "explorado2": False,
                    "related2": []
                }
            if(iGrafo.get(destino) == None):
                iGrafo[destino] = {
                    "explorado": False,
                    "related": [],
                    "explorado2": False,
                    "related2": []
                }

            # Add information to the nodos
            iGrafo[origen]["related"].append(destino)
            iGrafo[destino]["related2"].append(origen)

        arr.append(iGrafo)

    for iGrafo in arr:
        combos(iGrafo)


main()