#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado

valorCasa = float(input("Digite o valor da casa: "))
salario = float(input("Digite seu salário: "))
anos = float(input("Digite em quantos anos irá pagar: "))

prestacao = valorCasa/(anos*12)

if prestacao > salario * 0.3:
    print("A prestação excede em mais de 30% do seu salário. Empréstimo negado.")
else:
    print("Empréstimo aprovado.")