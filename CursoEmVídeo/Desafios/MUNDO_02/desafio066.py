# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

sum = 0
amount = 0
while True:
    num = int(input("Type a number: "))
    if num == 999:
        break
    sum += num
    amount += 1
print(f">> {amount} numbers were typed and their SUM is {sum}.")