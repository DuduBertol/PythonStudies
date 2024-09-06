#Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

anoNasc = 0
anoAtual = 2024
maioridade = 21

pessMaior = 0
pessMenor = 0

strNums = ""

for c in range(0, 7):
    anoNasc = float(input(f"Digite o ano de Nascimento da ({c+1}º) pessoa: "))

    if anoAtual - anoNasc >= 21:
        strNums += "\033[035m "
        pessMaior += 1
    else:
        strNums += "\033[036m "
        pessMenor += 1

    strNums += str(c + 1)

print("="*20)
print(f"{"\033[035m"}Maioridade{"\033[m"} | {"\033[036m"}Menoridade{"\033[m"}")
print(f"As pessoas foram: {strNums}{"\033[m"}.")
print(f"{pessMaior} pessoas atigiram a maioridade, e {pessMenor} atingiram a menoridade.")
