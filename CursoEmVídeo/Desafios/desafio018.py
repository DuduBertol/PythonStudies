#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan

angulo = float(input("Digite um ângulo: "))

sinAngulo = sin(angulo)
cosAngulo = cos(angulo)
tanAngulo = tan(angulo)

print(f"O ângulo escolhido foi {angulo}º. Seu SENO vale {sinAngulo:.2f}, seu COSSENO {cosAngulo:.2f} e sua TANGENTE {tanAngulo:.2f}.45")