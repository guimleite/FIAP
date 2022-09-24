# Este código será para uma companhia aérea
# Os cliente premium da companhia podem despachar até 32kg de bagagens sem custo adicional,
# já os cliente gold podem levar bagagens até 28kg sem custo adicional,
# todos os demais cliente devem pagar por qualquer bagagem despachada.
# Com base no plano do cliente e no peso da bagagem, devemos informar se está dentro dos limites ou não

print("AirFIAP - Te levando até as nuvens")
tipo_cliente = input("Indique o tipo de plano do cliente: PREMIUM, GOLD ou PADRÃO: ")
peso_bagagem = float(input("Informe o peso da bagem do cliente: "))

if tipo_cliente.upper() == "PREMIUM":
    if peso_bagagem <= 32:
        print("A bagagem está no peso permitido, não haverá cobranças adicionais.")
    else:
        excedente = peso_bagagem - 32
        print(f"A bagagem ultrapassou o peso de 32kg. Será cobrada uma taxa adicional pelos {excedente}kg a mais")
else:
    if tipo_cliente.upper() == "GOLD":
        if peso_bagagem <= 28:
            print("A bagagem está no peso permitido, não haverá cobranças adicionais.")
        else:
            print(f"A bagagem ultrapassou o peso de 28kg. Será cobrada uma taxa adicional pelos {excedente}kg a mais")
    else:
        if tipo_cliente.upper() == "PADRÃO":
            print("Cliente do tipo padrão não tem direito a bagagem gratuita, e devem pagar pelo peso tatal despachado")
        else:
            print("O tipo do cliete não existe.")

