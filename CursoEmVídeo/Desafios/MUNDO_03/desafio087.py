# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha

somaPares = 0
somaColuna3 = 0
maiorValorLinha2 = -99999

matriz = []
width = int(input("Digite a LARGURA da matriz (X): "))
heigth = int(input("Digite a ALTURA da matriz (Y): "))

while len(matriz) < heigth:
    matriz.append([])

for i in range(0,heigth):
    for j in range(0,width):
        num = int(input(f"Digite um número para [{i},{j}]: "))
        matriz[i].append(num)

        if num % 2 == 0:
            somaPares += num

        if j+1 == 3:
            somaColuna3 += num

        if i+1 == 2:
            if num > maiorValorLinha2:
                maiorValorLinha2 = num

    print()

for linha in matriz:
    for num in linha:
        print(f"[{num:^5}]", end=" ")
    print()

print()

print(f"A SOMA dos valores PARES é: {somaPares}")
print(f"A SOMA dos valores da 3ª COLUNA é: {somaColuna3}")
print(f"O MAIOR valor da 2ª LINHA é: {maiorValorLinha2}")


