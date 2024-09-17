#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

a1 = int(input("Digite o primeiro termo de uma PA: "))
r = int(input("Digite a razão de uma PA: "))
n = 10
an = a1

c = 1
while c <= n:
    print(f"O {c}º termo da PA é {an}")
    c += 1
    an += r
    if c > n:
        nAdd = int(input(">> Você quer ver mais quantos termos (0 para sair): "))
        n += nAdd

print("\nSaindo...")