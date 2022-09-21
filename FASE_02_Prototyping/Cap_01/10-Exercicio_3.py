# Os colaboradores de sua equipe foram sorteados para ganhar um console de última geração cada um, por conta do bom desempenho que tiveram nos últimos projetos. Por um questão de logística, a empresa pede que todos os 5 membros da equipe recebem o mesmo aparelho.

# Este algorito receberá o voto de cada um dos 5 membros da equipe e, ao final, exibirá o console escolhido e a quantidade de votos.
# As opções são: PLAYSTATION 5, XBOX ONE, E NINTEDO SWITCH.

voto1 = input("Informe qual prêmio deseja ganhar, PLAYSTATION 5, XBOX ONE OU NINTEDO SWITCH:")
voto2 = input("Informe qual prêmio deseja ganhar, PLAYSTATION 5, XBOX ONE OU NINTEDO SWITCH:")
voto3 = input("Informe qual prêmio deseja ganhar, PLAYSTATION 5, XBOX ONE OU NINTEDO SWITCH:")
voto4 = input("Informe qual prêmio deseja ganhar, PLAYSTATION 5, XBOX ONE OU NINTEDO SWITCH:")
voto5 = input("Informe qual prêmio deseja ganhar, PLAYSTATION 5, XBOX ONE OU NINTEDO SWITCH: ")

playstation = 0
xbox = 0
nintendo = 0

if voto1.upper() == "PLAYSTATION 5":
    playstation = playstation + 1
elif voto1.upper() == "XBOX ONE":
    xbox = xbox + 1
elif voto1.upper() == "NINTENDO SWITCH":
    nintendo = nintendo + 1

if voto2.upper() == "PLAYSTATION 5":
    playstation = playstation + 1
elif voto2.upper() == "XBOX ONE":
    xbox = xbox + 1
elif voto2.upper() == "NINTENDO SWITCH":
    nintendo = nintendo + 1

if voto3.upper() == "PLAYSTATION 5":
    playstation = playstation + 1
elif voto3.upper() == "XBOX ONE":
    xbox = xbox + 1
elif voto3.upper() == "NINTENDO SWITCH":
    nintendo = nintendo + 1

if voto4.upper() == "PLAYSTATION 5":
    playstation = playstation + 1
elif voto4.upper() == "XBOX ONE":
    xbox = xbox + 1
elif voto4.upper() == "NINTENDO SWITCH":
    nintendo = nintendo + 1

if voto5.upper() == "PLAYSTATION 5":
    playstation = playstation + 1
elif voto5.upper() == "XBOX ONE":
    xbox = xbox + 1
elif voto5.upper() == "NINTENDO SWITCH":
    nintendo = nintendo + 1

if playstation > xbox and playstation > nintendo:
    print("O console escolhido foi o Playstation 5.")
elif xbox > playstation and xbox > nintendo:
    print("O console escolhido foi o XBOX ONE.")
elif nintendo > playstation and nintendo > xbox:
    print("O console escolhido foi o Nintendo Switch.")
else:
    print("Houve um empate de votos, por favor entre em contato com a direção.")