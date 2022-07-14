def numPau(arr: object):

    nivelesObjetct = {}

    for i in range(arr['persona']):
        nivelesObjetct[str(i)] = {
            "nivel": 'INF',
            "related": []
        }

    for baile in arr["baileArr"]:
        related1 = nivelesObjetct[str(baile[0])]['related']

        if(baile[1] not in related1):
            related1.append(str(baile[1]))


        related2 = nivelesObjetct[str(baile[1])]['related']
        if(baile[0] not in related2):
            related2.append(str(baile[0]))


    nivel = 1
    siguienteItem = nivelesObjetct['0']['related']
    nivelesObjetct['0']['nivel'] = 0

    while True:
        siguienteNivel = []
        for index in siguienteItem:
            node = nivelesObjetct[index]

            if(node['nivel'] == 'INF'):
                node['nivel'] = nivel

            for newNode in node['related']:
                if(newNode not in siguienteNivel and nivelesObjetct[newNode]['nivel'] == 'INF'):
                    siguienteNivel.append(newNode)

        if(len(siguienteNivel) == 0):
            break
        else:
            nivel += 1
            siguienteItem = siguienteNivel

    for key in nivelesObjetct:
        if(key != "0"):
            print(f"{key} {nivelesObjetct[key]['nivel']}")


def main():
    casos = int(input())
    finalArr = []
    for _ in range(casos):
        fiestaArr = input().split(',')
        persona = int(fiestaArr[0])
        bailes = int(fiestaArr[1])
        baileArr = []
        for __ in range(bailes):
            baileArr.append([int(x) for x in input().split()])
        finalArr.append({
            "persona": persona,
            "bailes": bailes,
            "baileArr": baileArr
        })

    for i in range(casos):
        print(f"fiesta {i + 1}:")
        numPau(finalArr[i])
        if(i != casos - 1):
            print("")


main()