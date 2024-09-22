# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

tuplaPalavras = ("APRENDER", "JOGAR", "CORRER", "LER", "ESTUDAR")

for palavra in tuplaPalavras:
    print(f"A palavra {palavra} possui vogais: ", end="")
    for i in range(len(palavra)):
        if palavra[i].upper() in "AEIOU":
            print(palavra[i], end=" ")
    print()