#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

from time import sleep
#Um Timer Wait

print("O computador sorteou um número entre 0-10.")
print("Processando...")
sleep(1.5)

sortedNum = randint(0,10)
userNum = int(input("Que número ele escolheu? "))
tries = 1

while userNum != sortedNum:
    if userNum > sortedNum:
        print("Menor...")
    elif userNum < sortedNum:
        print("Maior...")
    userNum = int(input("Número incorreto. Tente novamente: "))
    tries += 1

print(f"Parabéns, você acertou em {tries} tentativas! O número sorteado foi: {sortedNum}.")


