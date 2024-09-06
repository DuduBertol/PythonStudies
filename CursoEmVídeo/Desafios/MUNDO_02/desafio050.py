#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

tempNum = 0
somatorio = 0

for c in range(0, 6):
    tempNum = float(input(f"Digite um número ({c+1}º): "))

    if tempNum % 2 == 0:
        somatorio += tempNum

print("="*20)
print(f"A soma dos números pares digitados é: {somatorio}.")
