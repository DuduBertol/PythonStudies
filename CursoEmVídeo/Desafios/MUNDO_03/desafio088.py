# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e
# vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint

jogos = []
qntJogos = int(input("Digite quantos jogos você quer sortear: "))

while len(jogos) < qntJogos:
    jogos.append([])

for i in range(qntJogos):
    while len(jogos[i]) < 6:
        randNum = randint(1, 60)
        for num in jogos[i]:
            if randNum == num:
                continue
        jogos[i].append(randNum)
        jogos[i].sort()

print()
print(f"Os jogos formados foram:")
for jogo in jogos:
    print(jogo)
