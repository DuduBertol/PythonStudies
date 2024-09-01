# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#Ex: Ana Maria de Souza (primeiro = Ana; último = Souza.

nome = input("Digite seu nome completo: ").strip()

nomeSplit = nome.split()

primeiroNome = nomeSplit[0]
ultimoNome = nomeSplit[len(nomeSplit) - 1]

print(f"Quanto ao nome {nome}, seu primeiro nome é {primeiroNome} e o último é {ultimoNome}.")