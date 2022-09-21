# Operador condicional "and"

valor_compra = float(input("Digite o valor da compra: "))
forma_pagamento = int(input("1 - Dinheiro / 2 - Cartão: "))

if valor_compra > 100 and forma_pagamento==1:
    valor_compra = valor_compra * 0.9
    print("Você receberá 10% de desconto!")

print("O valor a pagar é {}".format(valor_compra))
