# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e
# que se encontram no intervalo de 1 até 500

somatorio = 0

for c in range(0, 500):
    if c % 3 == 0:
        somatorio += c

print(f"O somatório de todos os múltiplos de 3 entre [1, 500] é: {somatorio}.")