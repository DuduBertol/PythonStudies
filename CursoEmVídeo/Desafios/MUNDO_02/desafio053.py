#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

name = input("Digite um palíndromo: ").strip().upper()

nameNoSpace = "".join(name.split())
lenName = len(nameNoSpace)

isPalindromo = False

for c in range(0, lenName):
    if nameNoSpace[c] == nameNoSpace[lenName - c - 1]:
        isPalindromo = True
    else:
        isPalindromo = False
        break

if isPalindromo:
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")