# Este programa será para o saldão da alegria.
# No saldão os cliente podem escolher duas formas de pagamento, Boleto Bancário ou Cartão de Crédito
# Caso escolham Boleto Bancário, receberão um desconto de 5% sobre o valor da compra
# Caso escolham Cartão de Crédito, não haverá desconto, mas o cliente poderá escolher o número de parcelas

print("No saldão da alegria você é mais feliz")
total_compra = float(input("Por favor, indique o total da compra: "))
forma_pagamento = int(input("Forma de pagamento: 1 - Boleto ou 2- Cartão: "))

if forma_pagamento == 1:
    # códigos para pagamento por boleto
    valor_descontado = total_compra * 0.95
    print(f"O valor original de R$ {total_compra} sofreu um desconto de 5%, e o cliente pagará R$ {valor_descontado:.2f}")
else:
    # códigos para pagamento via cartão
    numero_parcelas = int(input("Por favor,indique o número de parcelas: "))
    valor_parcela = total_compra / numero_parcelas
    print(f"O valor de R$ {total_compra} será pago em {numero_parcelas}x de R$ {valor_parcela:.2f}")




