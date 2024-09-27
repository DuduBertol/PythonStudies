# Crie um programa onde o usuário possa digitar sete valores numéricos e
# cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

listaNum = [[], []]

for i in range(7):
    num = int(input("Digite um número: "))

    if num % 2 == 0:
        listaNum[0].append(num)
    else:
        listaNum[1].append(num)

listaNum[0].sort()
listaNum[1].sort()

print(f"Os valores PARES são: {listaNum[0]}")
print(f"Os valores ÍMPARES são: {listaNum[1]}")