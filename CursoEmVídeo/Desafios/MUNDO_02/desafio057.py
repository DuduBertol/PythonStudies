#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = input("Digite seu sexo: [M/F] ").strip().upper()

while sexo not in "MF":
    print()
    sexo = input("Valor Inválido.\nDigite seu sexo novamente: [M/F] ").strip().upper()

print(f"Seu sexo é {sexo}.")