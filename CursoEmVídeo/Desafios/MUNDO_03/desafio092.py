# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

pessoa = dict()

pessoa["Nome"] = str(input("Nome >> "))
pessoa["Idade"] = 2024 - int(input("Ano de Nascimento >> "))
pessoa["CTPS"] = int(input("Carteira de Trabalho (0 se não tem) >> "))

if pessoa["CTPS"] != 0:
    pessoa["Contratação"] = int(input("Ano de Contratação >> "))
    pessoa["Salário"] = float(input("Salário >> "))
    pessoa["Aposentadoria"] = (35 + pessoa["Idade"]) - (2024 - pessoa["Contratação"])

print("-"*20)

for k, v in pessoa.items():
    print(f"{k} tem o valor {v}")