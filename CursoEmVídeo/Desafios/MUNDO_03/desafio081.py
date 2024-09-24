# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

listaNum = []
resp = "S"

while resp == "S":

    num = int(input("Digite um número: "))
    listaNum.append(num)

    resp = input("Deseja continuar? [S/N] ").upper()
    while resp not in "SN":
        resp = input("Inválido. Deseja continuar? [S/N] ").upper()

listaNum.sort(reverse=True)
print(f"Foram digitados {len(listaNum)} números.")
print(f"Lista na ordem decrescente: {listaNum}")
print("O número 5 está na lista." if listaNum.count(5)>0 else "O número 5 não foi encontrado na lista.")
