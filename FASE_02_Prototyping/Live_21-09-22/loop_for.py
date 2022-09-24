# Será solicitado ao usuário o faturamento médio de sua empresa para cada um dos 12 meses do ano

faturamento_anual = 0

for mes in range(1, 13, 1):
    faturamento_mes = float(input(f"Informe o faturamento do mês de {mes}: "))
    faturamento_anual = faturamento_anual + faturamento_mes

    if mes == 1:
        maior_faturamento = faturamento_mes
        menor_faturamento = faturamento_mes
    else:
        if faturamento_mes > maior_faturamento:
            maior_faturamento = faturamento_mes
        if faturamento_mes < menor_faturamento:
            menor_faturamento = faturamento_mes

faturamento_medio = faturamento_anual / 12
print(f"A média de faturamento foi R$ {faturamento_medio:.2f}")
print(f"O menor faturamento foi {menor_faturamento}")
print(f"O maior faturamento é {maior_faturamento}")
