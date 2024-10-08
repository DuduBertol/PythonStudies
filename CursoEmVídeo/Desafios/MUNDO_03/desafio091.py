# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from operator import itemgetter


jogadas = {
"Jogador 01": (randint(1,6)),
"Jogador 02": (randint(1,6)),
"Jogador 03": (randint(1,6)),
"Jogador 04": (randint(1,6)),
           }

for k, v in jogadas.items():
    print(f"O {k} jogou {v}")

print()
print("-"*20)
print()

ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True) # o itemgetter(1) pega o VALUE

for i, v in enumerate(ranking):
    print(f"{i+1}º Lugar >> {v[0]} >> {v[1]}")