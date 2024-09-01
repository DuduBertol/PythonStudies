#Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

num = int(input("Digite um número: "))

X1 = num * 1
X2 = num * 2
X3 = num * 3
X4 = num * 4
X5 = num * 5
X6 = num * 6
X7 = num * 7
X8 = num * 8
X9 = num * 9

print(f"A tabuada do número {num} é: \n",
      "-"* 12,
      f"\n{num} x 1 = {X1};\n"
      f"{num} x 2 = {X2};\n"
      f"{num} x 3 = {X3};\n"
      f"{num} x 4 = {X4};\n"
      f"{num} x 5 = {X5};\n"
      f"{num} x 6 = {X6};\n"
      f"{num} x 7 = {X7};\n"
      f"{num} x 8 = {X8};\n"
      f"{num} x 9 = {X9}.\n",
      "-"* 12)
