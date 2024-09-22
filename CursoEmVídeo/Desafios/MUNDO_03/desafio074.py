#  Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#  Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

num1 = randint(1,10)
num2 = randint(1,10)
num3 = randint(1,10)
num4 = randint(1,10)
num5 = randint(1,10)

maiorNum = num1
menorNum = num1

tuplaNum = (num1, num2, num3, num4, num5)

for i in range(len(tuplaNum)):
    if tuplaNum[i] > maiorNum:
        maiorNum = tuplaNum[i]
    if tuplaNum[i] < menorNum:
        menorNum = tuplaNum[i]

print(f"A TUPLA é: {tuplaNum}")
print(f"O MAIOR é: {maiorNum}")
print(f"O MENOR é: {menorNum}")