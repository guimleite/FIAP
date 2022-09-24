# Função sem return
def saudacao_noturno():
    print("Boa noite, galerinha da noite!")
# Função sem argumentos
def saudacao(nome):
    print(f"Boa noite, {nome:str}")
# Função com return
def saudacao_com_return(nome):
    return f"Boa noite, {nome}"

nomes = ["PacMan", "Edward", "Mance"]
for nome in nomes:
    saudacao(nome)

