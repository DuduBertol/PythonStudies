# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

peopleMore18 = 0
mans = 0
womenLess20 = 0

while True:
    answer = ""
    gender = ""

    print("-" * 20)
    print("REGISTER A USER: ")
    print("-" * 20)

    age = int(input("AGE: "))
    while gender != "M" and gender != "F":
        gender = input("GENDER: [M/F] ").strip().upper()
    print("-" * 20)

    if age > 18:
        peopleMore18 += 1
    if gender == "M":
        mans += 1
    elif age < 20:
        womenLess20 += 1

    while answer != "Y" and answer != "N":
        answer = input("You want continue? [Y/N] ").strip().upper()
    if answer == "N":
        break

print("-"*20)
print("FINISHING PROGRAM")
print("-"*20)

print(f">> {peopleMore18} users have more than 18 years.")
print(f">> {mans} users are mans.")
print(f">> {womenLess20} users are womens and have less than 20 years.")


