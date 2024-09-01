#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = input("Digite uma frase: ").strip()

fraseUpper = frase.upper()

qntA = fraseUpper.count("A")

primeiraPosA = fraseUpper.find("A") + 1
ultimaPosA = fraseUpper.rfind("A") + 1

print(f"""Na frase {frase}, a letra A aparece {qntA} vezes.
Aparece pela primeira vez na posição {primeiraPosA}, e pela última vez na posição {ultimaPosA}.""")