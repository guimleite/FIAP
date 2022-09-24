numero_tabuada = int(input("Digite o número de que quer a tabuada: "))

contadora = 1

while contadora <= 10:
    resultado = numero_tabuada * contadora
    print(f"{numero_tabuada} x {contadora} = {resultado}")
    contadora += 1