import heapq, math, queue

gGrafo = {}

def sub_grafo(nodoId):
  global gGrafo
  oNodo = gGrafo[nodoId]
  oNodo['explorado'] = True
  subGrafo = {
    nodoId: oNodo
  }
  registro = queue.Queue()
  registro.put(oNodo)
  while (not registro.empty()):
    NodoAct = registro.get()
    for sigrelacion in NodoAct['relacion']:
      sigId = sigrelacion[1]
      sigNodo = gGrafo[sigId]
      if(sigNodo['explorado'] == False):
        sigNodo['explorado'] = True
        subGrafo[sigId] = sigNodo
        registro.put(sigNodo)

  return subGrafo

def prim(subGrafo):
  idPendientes = list(subGrafo.keys())
  primNodo = subGrafo[idPendientes[0]]
  primNodo['dist'] = 0
  del idPendientes[0]

  for relacion in primNodo['relacion']:
    relacionId = relacion[1]
    sigNodo = subGrafo[relacionId]
    dist = sigNodo['dist']
    sigNodo['dist'] = min(dist, relacion[0])

  pq = [[subGrafo[idPendientes[i]]['dist'], idPendientes[i]]
    for i in range(len(idPendientes))]
  heapq.heapify(pq)
  totalSubGrafo = 0

  while(len(idPendientes) > 0):
    u = heapq.heappop(pq)
    uId = u[1]
    uNodo = subGrafo[uId]

    if(uId in idPendientes):
      idPendientes.remove(uId)
      totalSubGrafo += uNodo['dist']
      for relacion in uNodo['relacion']:
        relacionId = relacion[1]
        if(relacionId in idPendientes):
          vNodo = subGrafo[relacionId]
          dist = relacion[0]
          actDist = vNodo['dist']
          if(dist < actDist):
            vNodo['dist'] = dist
            heapq.heappush(pq, [dist, relacionId])

  return totalSubGrafo


def infraestructura(arr: list):
  global gGrafo

  gGrafo = arr[0]
  costoA = arr[1][2]

  listaSubGrafos = []

  for NodoId in gGrafo:
    NodoAct = gGrafo[NodoId]
    if(NodoAct['explorado'] == False):
      listaSubGrafos.append(sub_grafo(NodoId))

  total = 0
  for subGrafo in listaSubGrafos:
    total += prim(subGrafo)

  total += (len(listaSubGrafos) * costoA)

  print(f"{total} {len(listaSubGrafos)}")


def main():
  casos = int(input())
  lista = []
  for _ in range(casos):
    caso = [int(x) for x in input().split()]
    ciudades = caso[0]
    conexiones = caso[1]

    iGrafo = {}
    for i in range(1, ciudades + 1):
      iGrafo[str(i)] = {
        "relacion": [],
        "explorado": False,
        "dist": math.inf
      }

    for __ in range(conexiones):
      lConexiones = [x for x in input().split()]
      origen = lConexiones[0]
      destino = lConexiones[1]
      costo = int(lConexiones[2])
      iGrafo[origen]['relacion'].append([costo, destino])
      iGrafo[destino]['relacion'].append([costo, origen])

    lista.append([iGrafo, caso])

  for arr in lista:
    infraestructura(arr)


main()