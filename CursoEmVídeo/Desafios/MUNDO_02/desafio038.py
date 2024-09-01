#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#- O primeiro valor é maior
#- O segundo valor é maior
#- Não existe valor maior, os dois são iguais

#IGUAL AO L04_08

a = int(input("Digite um número inteiro A: "))
b = int(input("Digite um número inteiro B: "))


if a == b:
    print(f"Não existe valor maior, os dois são iguais.")
elif a > b:
    print(f"O maior valor é A: {a}.")
else:
    print(f"O maior valor é B: {b}.")
