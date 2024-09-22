# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print("-" * 20)
print(f"{"BANCO DUDUDU":^20}")
print("-" * 20)

amount = int(input("How many REAL(R$) do you want to withdraw? "))

noteValue = 50
noteAmount = 0

while True:
    if amount >= noteValue:
        amount -= noteValue
        noteAmount += 1

    else:
        if noteAmount > 0:
            print(f">> {noteAmount} notes of R${noteValue}.")
            noteAmount = 0

        if noteValue == 50:
            noteValue = 20
        elif noteValue == 20:
            noteValue = 10
        elif noteValue == 10:
            noteValue = 1
        else:
            break

print("-"*20)

