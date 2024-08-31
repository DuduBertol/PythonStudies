#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

reta1 = float(input("Digite um primeira reta segmento de reta: "))
reta2 = float(input("Digite um segunda reta segmento de reta: "))
reta3 = float(input("Digite um terceira segmento de reta: "))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("Os segmentos de reta PODEM formar um triângulo.")
else:
    print("Os segmentos de reta NÃO PODEM formar um triângulo.")