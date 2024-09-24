# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

listaNum = []
resp = "S"

print (listaNum)

while resp == "S":
    num = int(input("Digite um número: "))

    if num not in listaNum:
        listaNum.append(num)
        print("Valor adicionado...")
    else:
        print("Valor duplicado. Não foi adicionado...")

    resp = input("Quer continuar? [S/N] ").upper()
    while resp != "N" and resp != "S":
        resp = input("Inválido. Quer continuar? [S/N] ").upper()

listaNum.sort()
print(f"Você digitou os números: {listaNum}")