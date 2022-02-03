import queue


grafo = {}


def rumores(origen):
    global grafo

    # Clean grafo
    for diaN in grafo:
        grafo[diaN]['explorado'] = False
        grafo[diaN]['dia'] = 0

    nodoOrigen = grafo[origen]
    # No people to tell the rumor
    if(nodoOrigen['related'] == []):
        print('0')
        return

    nodoOrigen['explorado'] = True
    nodoOrigen['dia'] = 0
    registro = queue.Queue()
    registro.put(nodoOrigen)
    diaGrafo = {}
    while (not registro.empty()):
        nodoActual = registro.get()
        for nodeId in nodoActual['related']:
            sigNodo = grafo[nodeId]
            if(sigNodo['explorado'] == False):
                sigNodo['explorado'] = True
                sigDia =  nodoActual['dia'] + 1
                sigNodo['dia'] = sigDia

                # Set dia
                if(diaGrafo.get(sigDia) == None):
                    diaGrafo[sigDia] = 1
                else:
                    diaGrafo[sigDia] += 1

                # Update registro
                registro.put(sigNodo)

    # Select max dias
    diaMax = 0
    lenDiaMax = 0
    for diaN in diaGrafo:
        diaLength = diaGrafo[diaN]
        if(diaLength > lenDiaMax):
            diaMax = diaN
            lenDiaMax = diaLength

    print(f'{diaMax} {lenDiaMax}')


def main():
    global grafo

    personasTotal = int(input())
    grafo = {}
    for i in range(personasTotal):
        relatedArr = [x for x in input().split()]
        relatedArr = [] if relatedArr[0] == '-1' else relatedArr
        grafo[str(i)] = {
            "explorado": False,
            "related": relatedArr,
            "dia": 0
        }

    finalArr = [origen for origen in input().strip().split(', ')]

    for origen in finalArr:
        rumores(origen)


main()