# Esse script verifica se os batimentos cardíacos por minuto do usupario
# se enconstram na faixa adequada. Para isso, o usuário deve informar o
# seu número de BATIMENTOS POR MINUTO (BPM) e a IDADE.
# A partir disso o script deve verificar e exibir a mensagem
# informando se os batimentos do usuário se encontram DENTRO da faixa
# adequada, ACIMA da faixa adequada ou ABAIXO da faixa adequada, de
# acordo com o site Tua Saúde(https://www.tuasaude.com/frequencia-cardiaca/)

# IDADE - BPM
# Até 2 anos - 120 a 140
# De 8 a 17 anos - 80 a 100
# Adulto sedentário - 70 a 80
# Idosos - 50 a 60

print("VERIFICADOR DE FREQUÊNCIAS CARDÍACAS")
idade = int(input("Por favor, informe sua idade: "))
bpm = int(input("Por favor, informe seu BPM: "))

if idade <= 2:
    if bpm >= 120 and bpm <= 140:
        print("Batimentos NORMAIS para a idade.")
    else:
        print("Batimentos INADEQUADOS para a idade.")
elif idade >= 8 and idade <= 17:
    if bpm >= 80 and bpm <= 100:
        print("Frequência cardíaca adequada.")
    else:
        print("Frequência cardiaca inadequada.")
elif idade >= 18 and idade < 60:
    if bpm >= 70 and bpm <= 80:
        print("Frequência cardíaca adequada.")
    else:
        print("Frequência cardiaca inadequada.")
elif idade >= 60:
    if bpm >= 50 and bpm <= 60:
        print("Frequência cardíaca adequada.")
    else:
        print("Frequência cardiaca inadequada.")
else:
    print("Não existem dados para idade informada.")
