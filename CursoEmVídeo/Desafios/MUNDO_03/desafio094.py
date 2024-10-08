# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pessoas = list()
resp = "S"

qntPessoas = 0
somaIdade = 0
mediaIdade = 0
listaMulheres = list()
listaIdadeAcima = list()

while resp == "S":
    novaPessoa = dict()
    novaPessoa["Nome"] = str(input("Nome >> "))
    novaPessoa["Sexo"] = str(input("Sexo [M/F] >> "))
    novaPessoa["Idade"] = int(input("Idade >> "))

    qntPessoas += 1
    somaIdade += novaPessoa["Idade"]

    pessoas.append(novaPessoa.copy())

    resp = input("Deseja continuar? [S/N] >> ").upper()
    while resp not in "SN":
        resp = input("Inválido. Deseja continuar? [S/N] >> ").upper()

mediaIdade = somaIdade / qntPessoas

for i, dados in enumerate(pessoas):
    if pessoas[i]["Sexo"] in "Ff":
        listaMulheres.append(pessoas[i]["Nome"])
    if pessoas[i]["Idade"] > mediaIdade:
        listaIdadeAcima.append(pessoas[i])

print("-"*20)

print(f">> O grupo tem {len(pessoas)}.")
print(f">> A média da idade é de {mediaIdade:.2f} anos.")

print(f">> As mulheres cadastradas foram: ", end="")
for mulher in listaMulheres:
    print(mulher)

print(f">> Lista de pessoas com idade acima da média: ")
for pessoa in listaIdadeAcima:
    print(f"Nome: {pessoa["Nome"]}; Sexo: {pessoa["Sexo"].upper()}, Idade: {pessoa["Idade"]}")
