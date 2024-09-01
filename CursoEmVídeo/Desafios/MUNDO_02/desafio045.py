# Crie um programa que faça o computador jogar Jokenpô com você.

# IGUAL AO L05_03

from random import randint
from time import sleep

print("Vamos jogar Joquempô! ")

jogadaPlayer = int(input("[1] - Pedra \n[2] - Papel \n[3] - Tesoura. \nEscolha sua jogada: "))
jogadaPC = randint(1,3)

jogadasTypes = {1:"PEDRA", 2:"PAPEL", 3:"TESOURA"}
pedra = 1
papel = 2
tesoura = 3

sleep(0.5)
print("Pedra...")
sleep(0.5)
print("Papel...")
sleep(0.5)
print("Tesoura...")
sleep(0.5)
print("Já!")

vencedor = ""


if jogadaPlayer == jogadaPC:
    vencedor = ""
elif jogadaPlayer == pedra:
    if jogadaPC == papel:
        vencedor = "Computador"
    elif jogadaPC == tesoura:
        vencedor = "Você"

elif jogadaPlayer == papel:
    if jogadaPC == pedra:
        vencedor = "Você"
    elif jogadaPC == tesoura:
        vencedor = "Computador"

elif jogadaPlayer == tesoura:
    if jogadaPC == pedra:
        vencedor = "Computador"
    elif jogadaPC == papel:
        vencedor = "Você"

else:
    print("Jogada inválida.")


sleep(1)
print("Processando vencedor...")
sleep(1)
print(f"Você jogou {jogadasTypes[jogadaPlayer]} e o Computador jogou {jogadasTypes[jogadaPC]}.")

if vencedor != "":
    print(f"O vencedor foi: {vencedor}!")
else:
    print("O jogo Empatou!")

