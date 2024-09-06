#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
from emoji import emojize

print("Iniciando contagem dos fogos de artifício:")

sec = 10

sleep(1)

for c in range(10, -1, -1):
    print(f" || {sec} || ")
    sec -= 1
    sleep(1)

print(emojize(f"*Fogos Explodindo! :fireworks::fireworks:"))

