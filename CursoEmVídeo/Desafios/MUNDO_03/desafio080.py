# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

listaNum = []
num = int(input("Digite um número: "))
listaNum.append(num)

while len(listaNum) < 5:
    num = int(input("Digite um número: "))
    for i in range(len(listaNum)):
        if num < listaNum[i]:
            listaNum.insert(i,num)
            break
        elif i+1 == len(listaNum):
            listaNum.append(num)
            break

print(f"A lista digitada foi: {listaNum}")