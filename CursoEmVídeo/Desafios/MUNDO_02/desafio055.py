# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos

maiorPeso = 0
menorPeso = 0

for c in range(0, 5):
    pesoTemp = int(input(f"Digite seu peso ({c+1}ª Pessoa): (Kg) "))

    if c == 1:
        maiorPeso = pesoTemp
        menorPeso = pesoTemp

    if pesoTemp > maiorPeso:
        maiorPeso = pesoTemp

    if pesoTemp < menorPeso:
        menorPeso = pesoTemp

print(f"O MAIOR peso foi: {maiorPeso} Kg.")
print(f"O MENOR peso foi: {menorPeso} Kg.")