print("CALCULADORA DE VELOCIDDE MÉDIA")
distancia = float(input("Digite a distância: "))
tempo = float(input("Digite o tempo da viagem em KM (digitar apenas os números): "))

velocidade_media = distancia / tempo

print("Para a distância {}, no tempo {} foi calculada a velocidade média {:.2f}" .format(distancia, tempo, velocidade_media))
print(f"Para a distância {distancia}, no tempo {tempo}, foi calculad a velocidade média {velocidade_media:.2f}")
