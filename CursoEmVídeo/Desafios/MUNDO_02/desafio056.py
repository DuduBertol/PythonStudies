# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

homem = 1
mulher = 2

numPessoas = 4

mediaIdade = 0
nomeHomemVelho = ""
idadeHomem = 0
qntMulherMenos20 = 0

for c in range(0, numPessoas):
    print("="*20)
    print(f"{c+1}º PESSOA:")
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    sexo = int(input("Selecione seu sexo: [1] Homem - [2] Mulher: "))
    print("="*20)

    mediaIdade += idade

    if sexo == 1:
        if idade > idadeHomem:
            idadeHomem = idade
            nomeHomemVelho = nome
    else:
        if idade < 20:
            qntMulherMenos20 += 1

mediaIdade = mediaIdade / numPessoas

print(f"""
>> A média de idade do grupo é {mediaIdade} anos. \n
>> O nome do homem mais velho é {nomeHomemVelho}, com {idadeHomem} anos. \n
>> Existem {qntMulherMenos20} mulheres com menos de 20 anos.""")

