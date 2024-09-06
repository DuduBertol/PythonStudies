#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

print("Exibindo todos os números pares entre 1 e 50.")

for c in range(0, 50):
    if c % 2 == 0:
        print(f" | {c} | ")

print("Números Exibidos.")
