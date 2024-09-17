#Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

num = 0
soma = 0
media = 0
qntNum = 0
maiorNum = 0
menorNum = 0

digitando = "S"

while digitando == "S":
    num = int(input("Digite um número inteiro: "))

    qntNum += 1
    soma += num

    if qntNum == 1: #Start( )
        maiorNum = num
        menorNum = num

    if num > maiorNum:
        maiorNum = num
    if num < menorNum:
        menorNum = num

    digitando = input("Deseja continuar digitando? [S/N] ").upper()

media = soma/qntNum
print(f"\nForam digitados {qntNum} valores.")
print(f"A MÉDIA desses valores é {media}.")
print(f"O MENOR valor foi {menorNum}.")
print(f"A MAIOR valor foi {maiorNum}.")

