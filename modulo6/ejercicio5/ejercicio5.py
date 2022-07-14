import heapq as hp


def addRegistro (ejercicio, lista):
  equipo = int(ejercicio[0])
  numeroEjercicio = int(ejercicio[1])
  minutos = int(ejercicio[2])
  resultado = ejercicio[3]

  if (resultado != 'C' and resultado != 'I'):
    return lista
  
  nombreEquipo = 'T'+str(equipo)
  numeroEjercicio = 'E'+str(numeroEjercicio)
  equipoActual = lista.get(nombreEquipo, -1)
  current = {
    "resultado": resultado,
    "minutos": minutos
  }

  if equipoActual == -1 :
    lista[nombreEquipo] = {
      numeroEjercicio: [current],
      'numero': equipo
    }
  else:
    ejercicioActual = equipoActual.get(numeroEjercicio, -1)
    if ejercicioActual == -1 :
      equipoActual[numeroEjercicio]= [current]
    else:
      ultimoEjercicio = ejercicioActual[len(ejercicioActual)-1]

      if(ultimoEjercicio['resultado'] != 'C'):
        ejercicioActual.append(current)
  
  return lista

def mostrarTablero(lista):
  final = []
  hp.heapify(final)

  for numeroEquipo in lista:
    equipoActual = lista[numeroEquipo]
    ejResuelto = 0
    penalizacion = 0
    for numeroEjercico in equipoActual:
      if numeroEjercico == 'numero': 
        continue
      ejList = equipoActual[numeroEjercico]
      ejLen = len(ejList)
      ultimoEjercicio = ejList[ejLen-1]
      if(ultimoEjercicio['resultado'] == 'C'):
        ejResuelto += 1
        penalizacion -= ultimoEjercicio['minutos']+20 * (ejLen - 1)
    
    if ejResuelto > 0:
      objeto = [ejResuelto, penalizacion, equipoActual['numero']*-1]
      hp.heappush(final, objeto)
  
  listaFinal = []

  for _ in range(0, final):
    equipo = hp.heappop(final)
    stringEquipo = str(equipo[2]*-1)+' '+str(equipo[0])+' '+str(equipo[1]*-1)
    listaFinal.insert(0, stringEquipo)
  for resultado in listaFinal:
    print(resultado)

casos = int(input())
array = []
for i in range(1, casos +1):
  db = {}
  numeroEjercicios = int(input())
  for j in range(0, numeroEjercicios):
    arrEjercicios = [x for x in input().split()]
    db = addRegistro(arrEjercicios, db)
  
  array.append({
    'numero': i,
    'db': db
  })

for i in range(0,casos):
  maraton = array[i]
  print('maraton '+str(maraton['numero']))
  mostrarTablero(maraton['db'])
  print("")