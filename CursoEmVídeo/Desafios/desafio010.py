#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

valor = int(input("Digite quanto dinheiro você tem na carteira: "))
dolarAtual = 5.5

qntDol = valor / dolarAtual

print(f"Com {valor} reais, você pode comprar {qntDol} dólares, levando em consideração que o dólar esteja custando {dolarAtual} no dia 21/08/2024.")