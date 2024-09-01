#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math
from math import trunc

num = float(input("Digite um número real: "))

parteInt = trunc(num)

print(f"A parte inteira do número {num} é {parteInt}.")