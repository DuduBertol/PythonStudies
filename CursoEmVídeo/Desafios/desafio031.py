#Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input("Digite a distância da sua viagem: "))
passagem = 0

if distancia <= 200:
    passagem = 0.5 * distancia
else:
    passagem = 0.45 * distancia

print(f"Você viajou {distancia} e o preço da sua passagem foi R$ {passagem:.2f}.")
