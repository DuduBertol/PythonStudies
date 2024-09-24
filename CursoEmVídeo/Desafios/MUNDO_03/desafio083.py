# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

#talvez possa não funcionar em alguns casos, mas essa foi a estrutura proposta por mim

#a do professor foi criar uma lista que armazena "(" a cada abertura e retira um deles da lista a cada encontro de seu par,
# ou seja, "( )". Assim, caso a lista esteja vazia a espressão é valida, caso contrário não é.


formula = input("Digite uma fórmula: ")
parentesesAbertos = 0
parentesesFechados = 0

for i in range(len(formula)):
    if formula[i] == "(":
        parentesesAbertos += 1
    elif formula[i] == ")":
        parentesesFechados += 1

if parentesesAbertos == parentesesFechados:
    print("A expressão é válida.")
else:
    print("A expressão não é válida.")