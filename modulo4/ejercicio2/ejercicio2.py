from math import sqrt

casos = int(input())
for c in range(casos):
    numero_heredero_str = input()
    numero_heredero_int = int(numero_heredero_str)

    numero_heredero_str_ordenado = "".join(sorted(numero_heredero_str))
    heredero = False
    
    if len(numero_heredero_str_ordenado) % 2 == 0:
        for i in range(1,int(sqrt(numero_heredero_int))+1):
            if numero_heredero_int%i == 0:
                d = numero_heredero_int//i
                numeros_divisores_str = "".join(sorted(str(d) + str(i)))
                if numeros_divisores_str == numero_heredero_str_ordenado:
                    heredero = True
                    break
    
    if heredero:
        print("Heredero")
    else:
        print("No")