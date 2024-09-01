#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda
# vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import datetime

anoNasc = int(input("Digite em que ano você nasceu: "))
anoAtual = datetime.today().year

idade = anoAtual - anoNasc

if idade < 18:
    print(f"No ano de {anoAtual} você completará {idade} anos. Faltam {18-idade} anos para se alistar.")
elif idade == 18:
    print(f"No ano de {anoAtual} você completará {idade} anos. Você deve se alistar!")
else:
    print(f"No ano de {anoAtual} você completará {idade} anos. Você passou {idade-18} anos do prazo do alistament.")
