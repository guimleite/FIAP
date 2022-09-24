#Esse programa recebe a distância e o tempo, e calcula a velocidade média
#primeiro vamos pedir a distância e o tempo

print("Esse é o calculador de velocidade média: ")
distancia = input("Insira a distância percorrida: ")
tempo = input("Insira o tempo decorrido: ")

#Realizando o cálculo
velocidade_media = float(distancia) / int(tempo)
print("A velocidade média calculada foi de {:.2f} km/h" .format(velocidade_media))