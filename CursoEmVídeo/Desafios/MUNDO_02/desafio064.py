#Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

num = int(input("Digite um número: "))
soma = 0
qntNum = 0

while num != 999:
    soma += num
    qntNum += 1
    num = int(input("Digite outro número: "))

print(f"Foram digitados {qntNum} números, e a SOMA é {soma}.")
