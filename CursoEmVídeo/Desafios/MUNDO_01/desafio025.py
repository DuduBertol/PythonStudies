#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input("Digite seu nome: ").strip()

nomeUpper = nome.upper()

if "SILVA" in nomeUpper:
    print(f"O nome {nome} contém Silva.")
else:
    print(f"O nome {nome} não contém Silva.")