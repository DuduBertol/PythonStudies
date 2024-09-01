#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida

#IGUAL AO L04_02

massa = float(input("Digite sua massa: (Kg)"))
altura = float("Digite sua altura: (m)")

imc = massa / altura**2

if massa < 18.5:
    print(f"Seu IMC é {imc} e você se enquadra em: Abaixo do Peso.")
elif 18.5 <= massa < 25:
    print(f"Seu IMC é {imc} e você se enquadra em: Peso Ideal.")
elif 25 <= massa < 30:
    print(f"Seu IMC é {imc} e você se enquadra em: Sobrepeso.")
elif 30 <= massa < 40:
    print(f"Seu IMC é {imc} e você se enquadra em: Obesidade.")
elif massa > 40:
    print(f"Seu IMC é {imc} e você se enquadra em: Obesidade Mórbida.")

