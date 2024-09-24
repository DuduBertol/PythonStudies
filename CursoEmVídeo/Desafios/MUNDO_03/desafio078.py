# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

listaNum = []
c = 0
menorVal = 999999999
menorPos = ""
maiorVal = -999999999
maiorPos = ""

while len(listaNum) < 5:
    num = int(input(f"Digite um número para a posição {c}: "))

    if num > maiorVal:
        maiorVal = num

    if num < menorVal:
        menorVal = num


    listaNum.append(num)
    c += 1

for c, num in enumerate(listaNum):
    if num == maiorVal:
        maiorPos += (str(c) + "... ")
    if num == menorVal:
        menorPos += (str(c) + "... ")

print()
print(f"A lista digitada foi: {listaNum}")
print(f"O MAIOR valor foi {maiorVal}, e aparece nas posições: {maiorPos}")
print(f"O MENOR valor foi {menorVal}, e aparece nas posições: {menorPos}")

