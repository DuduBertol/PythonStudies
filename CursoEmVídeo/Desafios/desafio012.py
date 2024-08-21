#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco = float(input("Digite o preço de um produto: "))

precoDesc = preco * 0.95 # (1 - 0.05 >> 5/100)

print(f"O preço do produto custa R${preco:.2f}. Entretanto, esse produto saí por R${precoDesc:.2f} com 5% de desconto.")