# O Menu Daora solicita uma escolha para o usuário:
# 1 - Receber um elogio.
# 2 - Receber uma frase motivacional
# 3 - Sair

# O menu deve continuar a ser exibido até que o usuário escolha a opção 3.

while opcao != 3:
    print("MENU DAORA")
    print("1 - Receber um elogio")
    print("2 - Frase motivacional")
    print("3 - Sair do sistema")
    opcao = int(input("Informe sua opção: "))

    if opcao == 1:
        print("Você é uma pessoa incrível! ")
    elif opcao == 2:
        print("Nunca desista, você pode alcançar qualquer coisa! ")
    elif opcao == 3:
        print("Saindo...")
    else:
        print("Opção inválida! ")