#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input("Digite um número inteiro: "))

imparPar = num % 2

if imparPar == 0:
    print(f"O número {num} é PAR.")
else:
    print(f"O número {num} é IMPAR.")