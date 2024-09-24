# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que
# vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

listaNum = []
listaPar = []
listaImpar = []
resp = "S"

while resp == "S":

    num = int(input("Digite um número: "))
    listaNum.append(num)

    resp = input("Deseja continuar? [S/N] ").upper()
    while resp not in "SN":
        resp = input("Inválido. Deseja continuar? [S/N] ").upper()

for n in listaNum:
    if n % 2 == 0:
        listaPar.append(n)
    else:
        listaImpar.append(n)

print(f"A lista de TODOS os números é: {listaNum}")
print(f"A lista dos números PARES é: {listaPar}")
print(f"A lista dos números ÍMPARES é: {listaImpar}")