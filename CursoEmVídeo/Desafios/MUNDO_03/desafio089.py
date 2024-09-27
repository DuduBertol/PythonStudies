# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente

galera = []
resp = "S"

c = 0
while resp == "S":
    galera.append([])

    galera[c].append(str(input("Nome: ")))

    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    notas = [nota1, nota2]
    galera[c].append(notas[:])

    media = (nota1+nota2)/len(notas)
    notas.clear()

    galera[c].append(media)

    c += 1

    resp = str(input("Deseja continuar? [S/N] ")).upper()
    while resp not in "SN":
        resp = str(input("Inválido. Deseja continuar? [S/N] ")).upper()

print("-"*20)
print(f"{"BOLETIM":^30}")
print("-"*20)
print(f"{"No."} {"NOME":<10} {"MÉDIA":>5}")
for i, pessoa in enumerate(galera):
    print(f"{i}   {pessoa[0]:<10} {pessoa[2]:>5}")


print("-"*20)
aluno = 0
while aluno != 999:
    aluno = int(input("Mostrar notas de qual aluno? (999 interrompe) "))
    if aluno <= len(galera) - 1:
        print(f"As notas do aluno {galera[aluno][0]} foram: {galera[aluno][1]}")
        print("-" * 20)
print("Programa Encerrado...")
