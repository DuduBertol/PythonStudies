# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
from CursoEmVídeo.Desafios.MUNDO_01.desafio033 import maior

galera = list()
dado = list()
resp = "S"

qntPessoas = 0
maiorPesoList = list()
maiorPeso = 0
menorPesoList = list()
menorPeso = 0

while resp == "S":

    dado.append(str(input("Nome: ")))
    dado.append(float(input("Peso: ")))
    galera.append(dado[:])

    if len(galera) == 0:
        maiorPeso = menorPeso = dado[1]
    elif dado[1] > maiorPeso:
        maiorPeso = dado[1]
    elif dado[1] < menorPeso:
        menorPeso = dado[1]

    dado.clear()


    resp = input("Deseja continuar? [S/N] ").upper()
    while resp not in "SN":
        resp = input("Inválido. Deseja continuar? [S/N] ").upper()

for p in galera:
    if p[1] == maiorPeso:
        maiorPesoList.append(p[0])
    elif p[1] == menorPeso:
        menorPesoList.append(p[0])


print(f"""
Foram cadastradas {len(galera)} pessoas.
As pessoas mais PESADAS são: {maiorPesoList}, com {maiorPeso} Kgs.
As pessoas mais LEVES são: {menorPesoList}, com {menorPeso} Kgs.
""")