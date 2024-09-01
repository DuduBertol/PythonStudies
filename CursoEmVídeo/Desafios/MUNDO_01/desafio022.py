#Crie um programa que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao tod0 (sem considerar espaços).
#- Quantas letras tem o primeiro nome.

nome = input("Qual o seu nome completo? ").strip()

nomeUpper = nome.upper()
nomeLower = nome.lower()

nomeSplit = nome.split()
nomeSemEspaco = "".join(nomeSplit)

qntLetrasNomeSemEspaco = len(nomeSemEspaco)
qntLetrasNomePrimeiro = len(nomeSplit[0])

print(f"""Seu nome é {nome}. \n
      Seu nome em maiúsculo é {nomeUpper}. \n
      Seu nome em minúsculo é {nomeLower}. \n
      Seu nome sem espaços tem {qntLetrasNomeSemEspaco} letras. \n
      Seu primeiro nome tem {qntLetrasNomePrimeiro} letras.""")