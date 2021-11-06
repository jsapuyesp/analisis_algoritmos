casos = int(input())
monedas = [10000,5000,1000,500,100,50,10,5,1]
for c in range(casos):
    n = int(input())
    denonminacion = 0
    cantidad_total = 0
    while(n%monedas[denonminacion] != 0):
        cantidad = n//monedas[denonminacion]
        n -= cantidad*monedas[denonminacion]
        cantidad_total+=cantidad
        denonminacion+=1
    cantidad_total += n//monedas[denonminacion]
    print(cantidad_total)