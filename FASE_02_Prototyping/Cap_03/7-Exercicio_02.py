# Fisando a educação financeira dos mais jovens, este aplicativo ajudará as crianças a controlarem os seus gastos.
# No protótipo, criamos um script simples, em que o usuário informa QUANTAS TRANSAÇÕES financeiras realizou ao longo do dia e o VALOR DE CADA UMA das transações.
# No fim, exibirá o valor total gasto e a média do valor de cada transação.

quantidade_transacoes = int(input("Informe a quantidade de transações: "))
total_transacoes = 0

for n_transacao in range(1, quantidade_transacoes + 1, 1):
    transacao = float(input("Por favor, informe o valor da transação {}: ".format(n_transacao)))
    total_transacoes = total_transacoes + transacao

media = total_transacoes / quantidade_transacoes
print("Neste dia foram gastos R$ {}, com uma média de R$ {} por transação.".format(total_transacoes, media))


