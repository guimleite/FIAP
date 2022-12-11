# Criando funções com parâmetros e return

valor1 = float(input("Insira um valor: "))
valor2 = float(input("Insira outro valor: "))

def somar(a,b):
    soma = a+b
    return soma

somar(valor1, valor2)
print(somar(50, 35))