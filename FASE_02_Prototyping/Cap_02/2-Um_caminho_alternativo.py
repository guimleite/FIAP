nome = input("Digite o nome do funcionário:")
salario = float(input("Digite o salário do funcionário: "))

if salario < 0:
    salario = salario * -1
    print("O salário é negativo")

print("O salário do funcionario {} é {}".format(nome, salario))