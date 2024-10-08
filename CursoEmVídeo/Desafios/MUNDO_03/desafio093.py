# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
jogador["Nome"] = str(input("Nome >> "))
jogador["Gols"] = list()
jogador["Total"] = 0

partidas = int(input(f"Quantas partidas {jogador["Nome"]} jogou? >> "))
for c in range(partidas):
    gols = int(input(f"Quantos gols na partida {c+1}? >> "))
    jogador["Gols"].append(gols)
    jogador["Total"] += gols

print()
print("-"*20)
print()

for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}.")

print(f"O jogador {jogador["Nome"]} jogou {partidas} partidas: ")
for partida, gol in enumerate(jogador["Gols"]):
    print(f"\t>> Na {partida+1}º partida, fez {gol} gols.")


