#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros

#IGUAL L04_07

preco = float(input("Digite o preço do produto: "))
formaPagamento = int(input("Escolha sua forma de pagamento: \n"
                           "[1] - À vista dinheiro/cheque: 10% de desconto. \n"
                           "[2] - À vista no cartão: 5% de desconto. \n"
                           "[3] - Em até 2x no cartão: preço formal. \n"
                           "[4] - Em 3x ou mais no cartão: 20% de juros. \n"
                           "Sua escolha: "))

valorTotal = preco

if formaPagamento == 1:
    valorTotal = preco * 0.90

elif formaPagamento == 2:
    valorTotal = preco * 0.95

elif formaPagamento == 3:
    valorTotal = preco

elif formaPagamento == 4:
    valorTotal = preco * 1.20

else:
    print("Forma de pagamento inválida.")

print(f"O produto sairá por R${valorTotal:.2f}.")