#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

kms = float(input("Quantos Kms seu carro percorreu? "))
dias = int(input("Por quantos dias ele foi alugado? "))

precoKms = kms * 0.15
precoDia = dias * 60
precoTotal = precoKms + precoDia

print(f"O valor a se pagar por esse carro é R${precoTotal:.2f}")