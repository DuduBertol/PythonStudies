#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Digite seu salário: "))

if salario > 1250:
    salario = salario * 1.1
    print(f"Seu salário com aumento de 10% ficou R${salario:.2f}")
else:
    salario = salario * 1.15
    print(f"Seu salário com aumento de 15% ficou R${salario:.2f}")

