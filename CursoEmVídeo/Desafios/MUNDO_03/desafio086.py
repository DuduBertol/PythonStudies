# Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matriz = []
width = int(input("Digite a LARGURA da matriz (X): "))
heigth = int(input("Digite a ALTURA da matriz (Y): "))

while len(matriz) < heigth:
    matriz.append([])

for i in range(0,heigth):
    for j in range(0,width):
        num = int(input(f"Digite um número para [{i},{j}]: "))
        matriz[i].append(num)
    print()

for linha in matriz:
    for num in linha:
        print(f"[{num:^5}]", end=" ")
    print()





