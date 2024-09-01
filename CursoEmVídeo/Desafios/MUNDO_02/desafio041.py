# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER

#IGUAL AO L04_03

idade = int(input("Digite sua idade, nadador: "))

if idade <= 9:
    print(f"Sua idade é {idade} e você está na categoria - Até 9 anos: MIRIM.")

elif 9 < idade <= 14:
    print(f"Sua idade é {idade} e você está na categoria - Até 14 anos: INFANTIL")

elif 14 < idade <= 19:
    print(f"Sua idade é {idade} e você está na categoria - Até 19 anos: JÚNIOR.")

elif 19 < idade <= 25:
    print(f"Sua idade é {idade} e você está na categoria - Até 25 anos: SÊNIOR.")

else:
    print(f"Sua idade é {idade} e você está na categoria - Acima de 25 anos: MASTER.")