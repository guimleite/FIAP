# Programa receberá o noem dos convidados que chegaram em um festa infantil
# Após isso, exibirá a quantidade de convidados que compareceram, a lista delesem ordem de chegada e em ordem alfabética

resposta = "sim"
convidados = []
while resposta.upper() != "NÃO":
    nome_convidado = input("Informe o nome do convidado: ")
    convidados.append(nome_convidado)
    resposta = input("Deseja informar mais um convidado, SIM ou NÃO? ")

print(f"Compareceram {len(convidados)} convidados! \n")
print("Ordem de chegada dos convidados: ")
for convidado in convidados:
    print(convidado)

convidados.sort()
print("\nOrdem alfabética dos convidos: ")
for convidado in convidados:
    print(convidado)