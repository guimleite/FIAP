# Uma empresa de jogos quer tornar seus games mais desafiadores, e fui contratado para ajudá-la. Para isso será emplementado em futuros games um algoritmo da sorte de Fibonnaci.
# A ideia é tornar mais dificil os jogadores terem sucesso em algumas açõs realizadas no game. Por isso o algoritmo funcionará assm: o usuário digita um valor numério inteiro e o algoritmo deverá verificiar se esse valor encontra-se na sequência Fibonnaci. Caso o número esteja na sequência, o algoritmo exibirá a mensagem "Ação bem sucedidaa!" e, caso não esteja, deve exibir a mensagem "A ação falhou..."

numero_usuario = int(input("Por favor, informe um número inteiro: "))

anterior1 = 1
anterior2 = 0

for n in range(1, numero_usuario + 1, 1):
    atual = anterior1 + anterior2
    anterior1 = anterior2
    anterior2 = atual
    if numero_usuario == atual:
        print("Ação bem sucedida! ")
        break
    elif numero_usuario < atual:
        print("A ação falhou...")
        break


