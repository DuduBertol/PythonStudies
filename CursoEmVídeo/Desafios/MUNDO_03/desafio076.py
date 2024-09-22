# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

tabelagem = ("Leite", 4.50, "Ovos", 15, "Pão", 1, "Frango", 16.90, "Arroz", 24.85)

print("-"*30)
print(f"{"LISTA DE PREÇOS":^30}")
print("-"*30)

nome = ""
preco = 0

for i in range(len(tabelagem)):
    if i % 2 == 0:
        nome = tabelagem[i]
    else:
        preco = tabelagem[i]
        print(f"{nome:.<20} R$ {preco: >6.2f}")