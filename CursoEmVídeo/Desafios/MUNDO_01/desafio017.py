#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

from math import sqrt,pow

ca = float(input("Digite um valor para o Cateto Adjacente: "))
co = float(input("Digite um valor para o Cateto Oposto: "))

h = sqrt(pow(ca,2) + pow(co, 2))

print(f"A hipotenusa deste triângulo vale {h}.")

#OBS. Da pra fazer sem importar módulos, mas fiz com pra testar.