
casos = int(input())

def union(izquierda,derecha):
  listAux = izquierda+derecha
  listAux.sort()
  print(''.join(list(map(lambda x: str(x),listAux)))+'\n')
  return listAux

def ordenamient(lista):
  if len(lista)>1:
    
    medio = len(lista)//2
    izquierda = lista[:medio]
    derecha = lista[medio:]
    return union(ordenamient(izquierda),ordenamient(derecha))
  else:
    print(str(lista[0])+'\n')
    return lista



for _ in range(0,casos):
  linea = input().split()
  map_linea = map(int, linea)
  lista_int = list(map_linea)
  
  print('caso '+str(_+1)+':\n')
  ordenamient(lista_int)
  print('\n')

