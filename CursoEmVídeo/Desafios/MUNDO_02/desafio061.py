# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

a1 = int(input("Digite o primeiro termo de uma PA: "))
r = int(input("Digite a razão de uma PA: "))
n = 10
a10 = a1 + (n - 1) * r

an = a1

c = 1
while an <= a10:
    print(f"O {c}º termo da PA é {an}")
    c += 1
    an += r
