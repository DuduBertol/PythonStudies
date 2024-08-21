#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input("Digite seu salário: "))

salarioAum = salario * 1.15

print(f"Seu salário é R${salario:.2f}. Com 15% de aumento você passará a ganhar R${salarioAum:.2f}.")