#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

from time import sleep
#Um Timer Wait

randomNum = randint(0,5)

userNum = int(input("O computador sorteou um número entre 0-5. Que número ele escolheu? "))

print("Processando...")
sleep(1.5)

if userNum == randomNum:
    print(f"O número escolhido pelo computador foi {randomNum} e você ACERTOU!")
else:
    print(f"O número escolhido pelo computador foi {randomNum} e você ERROU'!")