# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

listaJogadores = list()
resp = "S"

while resp in "S":

    print("-" * 20)
    print(f"{"NOVO JOGADOR":^20}")
    print("-"*20)

    jogador = dict()
    jogador["Nome"] = str(input("Nome >> "))
    jogador["Gols"] = list()
    jogador["Total"] = 0

    partidas = int(input(f"Quantas partidas {jogador["Nome"]} jogou? >> "))
    for c in range(partidas):
        gols = int(input(f"Quantos gols na partida {c + 1}? >> "))
        jogador["Gols"].append(gols)
        jogador["Total"] += gols

    listaJogadores.append(jogador.copy())

    resp = input("Deseja continuar? [S/N] >> ").upper()
    while resp not in "SN":
        resp = input("Inválido. Deseja continuar? [S/N] >> ").upper()

print()
print("-"*20)
print("-"*20)
print()

for i, jogadores in enumerate(listaJogadores):
    print(f"Jogador [{i+1}] - {jogadores["Nome"]}")

escolha = int(input("Qual jogador você deseja escolher? [999 encerra] >> "))-1

while escolha != 999:
    print("-"*20)
    for k, v in listaJogadores[escolha].items():
        print(f"O campo {k} tem o valor {v}.")

    print(f"O jogador {listaJogadores[escolha]["Nome"]} jogou {len(listaJogadores[escolha]["Gols"])} partidas: ")
    for partida, gol in enumerate(listaJogadores[escolha]["Gols"]):
        print(f"\t>> Na {partida + 1}º partida, fez {gol} gols.")

    print("-"*20)
    for i, jogadores in enumerate(listaJogadores):
        print(f"Jogador [{i + 1}] - {jogadores["Nome"]}")
    escolha = int(input("Qual jogador você deseja escolher? [999 encerra] >> "))

print("\n\nPrograma Encerrado!")




