# Criando as primeiras funções no curso

def somar():
    a = float(input("Digite um valor: "))
    b = float(input("Digite outro valor: "))

    soma = a+b
    print(f"A soma dos valores digitas é: {soma}")

print("Olá, amigo! ")

def subtrair():
    a = float(input("Digite um valor: "))
    b = float(input("Digite outro valor: "))

    subtracao = a - b
    print(f"O produto da subtração dos valores digitas é: {subtracao}")

def dividir():
    a = float(input("Digite um valor: "))
    b = float(input("Digite outro valor: "))

    divisao = a / b
    print(f"O produto da divisão dos valores digitas é: {divisao}")

def multiplicar():
    a = float(input("Digite um valor: "))
    b = float(input("Digite outro valor: "))

    multiplicacao = a * b
    print(f"O produto da multiplicação dos valores digitas é: {multiplicacao}")

somar()
subtrair()
dividir()
multiplicar()