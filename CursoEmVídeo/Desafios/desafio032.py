#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input("Digite um ano qualquer: "))

if ano%4 == 0:
    print(f"O ano {ano} É bissexto.")
else:
    print(f"O ano {ano} NÃO É bissexto.")