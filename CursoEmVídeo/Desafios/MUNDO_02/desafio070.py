# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

totalValue = 0
more1000RSAmount = 0
shippestName = ""
shippestPrice = 0

while True:
    answer = ""
    print("-" * 20)
    print("BUY A PRODUCT: ")
    print("-" * 20)

    price = float(input("PRICE: "))
    productName = input("PRODUCT NAME: ")

    if shippestPrice == 0 or price <= shippestPrice:
        shippestPrice = price
        shippestName = productName

    if price > 1000:
        more1000RSAmount += 1

    totalValue += price

    print("-" * 20)

    while answer != "Y" and answer != "N":
        answer = input("You want continue? [Y/N] ").strip().upper()
    if answer == "N":
        break

print("-" * 20)
print("FINISHING PROGRAM: ")
print("-" * 20)

print(f">> The TOTAL VALUE of your shopping is: R$ {totalValue:.2f}")
print(f">> {more1000RSAmount} products cost more than R$ 1000,00.")
print(f">> The NAME of the shippest product is {shippestName}")
