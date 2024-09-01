#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

notaUm = int(input("Digite sua primeira nota: "))
notaDois = int(input("Digite sua segunda nota: "))

media = (notaUm + notaDois) / 2

print(f"Se você tirou {notaUm} e {notaDois}, sua média fica {media}.")