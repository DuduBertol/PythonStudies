#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

nomeCidade = input("Digite o nome de uma cidade: ").strip()

nomeUpperSplit = nomeCidade.upper().split()

if "SANTO" in nomeUpperSplit[0]:
    print(f"A cidade {nomeCidade} começa com Santo.")
else:
    print(f"A cidade {nomeCidade} não começa com Santo.")