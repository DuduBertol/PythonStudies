# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))
num4 = int(input("Digite um número: "))

tuplaNum = (num1, num2, num3, num4)

typed9 = 0
pares = ""

for i in range(len(tuplaNum)):
    if tuplaNum[i] == 9:
        typed9 += 1

    if tuplaNum[i] % 2 == 0:
        pares += str(tuplaNum[i]) + " "

print(f"Você digitou os valores: {tuplaNum}")
print(f"O número 9 apareceu {typed9} vezes.")
print(f"O número 3 apareceu na posição {tuplaNum.index(3) + 1}ª posição." if tuplaNum.count(3) != 0
      else f"O número 3 não apareceu em nenhuma posição.")
print(f"Os números pares foram: {pares}")