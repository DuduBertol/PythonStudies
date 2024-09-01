#Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input("Digite um número inteiro qualquer: "))

conversao = int(input("[1] - BINÁRIO \n[2] - OCTAL \n[3] - HEXADECIMAL \nEscolha o tipo de Conversão: "))

if conversao == 1:
    print(f"O número {num} convertido para BINÁRIO é {bin(num) [2:]}.")
elif conversao == 2:
    print(f"O número {num} convertido para BINÁRIO é {oct(num) [2:]}.")
elif conversao == 3:
    print(f"O número {num} convertido para BINÁRIO é {hex(num) [2:]}.")
    #[2:] fatia a string e printa somente do index [2] em diante (eliminando os 2 primeiros dígitos[0,1])
else:
    print("Opção Inválida.")