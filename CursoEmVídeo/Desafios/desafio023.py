#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = int(input("Digite um número de 0 a 9999: "))

unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print(f"""O valor {num} tem como: 
        Unidade = {unidade} 
        Dezena = {dezena} 
        Centena = {centena} 
        Milhar = {milhar} """)

#EX.: 1234
# Unidade = 1234 // 1 = 1234 % 10 = 1230 + 4 = 4
# Dezena = 1234 // 10 = 123 % 10 = 120 + 3 = 3
# Centena = 1234 // 100 = 12 % 10 = 10 + 2 = 2
# Milhar = 1234 // 1000 = 1 % 10 = 0 + 1 = 1

# ta bom, isso é mtt foda