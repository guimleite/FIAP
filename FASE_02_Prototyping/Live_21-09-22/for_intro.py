# Tabuada simples com for

numero_tabuada = int(input("Infor o valor do queal quer a tabuada: "))

for i in range(1, 11, 1):
    resultado = numero_tabuada * i
    print(f"{numero_tabuada} X {i} = {resultado}! ")