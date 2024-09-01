#Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input("Digite a velocidade do seu carro: "))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f"Você está acima de 80 Km/h e foi multado em R$ {multa:.2f}.")
else:
    print(f"Você está em velocidade regular, abaixo de 80 Km/h.")