#Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
#- Média abaixo de 5.0: REPROVADO
#- Média entre 5.0 e 6.9: RECUPERAÇÃO
#- Média 7.0 ou superior: APROVADO

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

media = (nota1 + nota2) / 2

if media < 5:
    print(f"Sua média é {media} e você está REPROVADO.")
elif 5 <= media < 7:
    print(f"Sua média é {media} e você está em RECUPERAÇÃO.")
else:
    print(f"Sua média é {media} e você está APROVADO.")