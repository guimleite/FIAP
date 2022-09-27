# Aprendendo a impotância da modularização
import Calculadora
op = 1

while op !=5:
    print("1 - Somar dois valores")
    print("2 - Subtrair dois valores")
    print("3 - Multiplicar dois valores")
    print("4 - Dividir dois valores")
    print("5 - Sair")
    op = int(input("Escolha uma opção: "))

    if(op==1):
        print(Calculadora.somar(float(input("Digite o primeiro valor: ")), float(input("Digite o segundo valor: "))))
    elif(op==2):
        print(Calculadora.subtrair(float(input("Digite o primeiro valor: ")), float(input("Digite o segundo valor: "))))

    elif(op == 3):
        print(Calculadora.multiplicar(float(input("Digite o primeiro valor: ")), float(input("Digite o segundo valor: "))))
    elif (op == 4):
        print(Calculadora.dividir(float(input("Digite o primeiro valor: ")), float(input("Digite o segundo valor: "))))



