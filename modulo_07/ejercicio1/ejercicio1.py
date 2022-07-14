contador = 0

def union(izquierda, derecha, largo):
  global contador
  i = 0
  j = 0
  k = 0
  auxLista = []
  largoI = len(izquierda)
  largoD = len(derecha)

  while k < largo:
    if(i<largoI):
      if(j<largoD):
        if(izquierda[i]<=derecha[j]):
          auxLista.append(izquierda[i])
          i += 1
        else:
          auxLista.append(derecha[j])
          contador += (largoI - i)
          j += 1
      else:
        auxLista.extend(izquierda[i:])
        break
    else:
      if(j < largoD):
        auxLista.extend(derecha[j:])
        break
    k += 1
  return auxLista

def ordenamiento(lista):
  if len(lista)>1:
    medio = len(lista)//2
    izquierda = lista[:medio]
    derecha = lista[medio:]
    return union(ordenamiento(izquierda),ordenamiento(derecha), len(lista))
  
  else:
    return lista

def ganadorEs(lista):
  ordenamiento(lista)

  if(contador == 0):
    print("Empate")
  elif(contador % 2 == 0):
    print("Pedro")
  else:
    print("Susana")
  
def main():
  lista = []
  while True:
    entrada = int(input())
    if entrada == 0:
      break
    arrayCaso = []
    for i in range(0,entrada):
      arrayCaso.append(int(input()))
    lista.append(arrayCaso)

  for caso in lista:
    ganadorEs(caso)
    global contador
    contador = 0
main()

