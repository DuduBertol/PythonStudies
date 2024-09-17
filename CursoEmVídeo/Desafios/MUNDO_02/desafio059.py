#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

numA = float(input("Digite um valor A: "))
numB = float(input("Digite um valor B: "))

runProgram = True
while runProgram:
    print("""Escolha um dos itens abaixo:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa""")

    choose = int(input("Qual sua escolha? "))

    if choose == 1:
        soma = numA + numB
        print(f"Você escolheu SOMA: a soma de {numA} + {numB} = {soma}.")

    elif choose == 2:
        mult = numA * numB
        print(f"Você escolheu MULTIPLICAÇÃO: a multiplicação de {numA} * {numB} = {mult}.")

    elif choose == 3:
        if numA > numB:
            maior = numA
        elif numA < numB:
            maior = numB
        else:
            maior = 0

        if maior != 0:
            print(f"O maior número é {maior}.")
        else:
            print("Valores iguais. Não há maior.")

    elif choose == 4:
        print("Novos Números...")
        numA = float(input("Digite um novo valor A:"))
        numB = float(input("Digite um novo valor B:"))

    elif choose == 5:
        runProgram = False
        break

    else:
        print("Valor inválido, tente novamente...")

    print("\nVocê deseja realizar mais alguma operação? ")

print("\n\nEncerrando programa...")