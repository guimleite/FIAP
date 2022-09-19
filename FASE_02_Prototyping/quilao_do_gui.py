# Este programa vai calcular o preço de um prato no restaurante "Quilão do Gui".
# No restaurante há uma promoção, caso o prato do cliente ultrapasse 1kg, ele pagará o preço
# único de R$ 88,00.

print("Quilão do Gui")
# solicitando o preço do prato
peso_prato = float(input("Por favor, informe o peso em kg do prato do cliente: "))
# solicitando valor cobrado pelo kg
valor_por_kg = float(input("Por favor,informe o valor cobrado por kg: "))
# calculando o valor cobrado pelo prato
valor_cobrado = peso_prato * valor_por_kg

mensagem = f"O valor do prato é de R${valor_cobrado:.2f}"

# verificando se o prato será aplicável na promoção
if peso_prato >= 1:
    mensagem = f"{mensagem} mas, como o preço do prato do cliente ultrapassou 1kg, ele só pagará o valor único de R$ 88,00"

print(mensagem)