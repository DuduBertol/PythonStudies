#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e
# a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

hParede = int(input("Digite a altura de uma parede: "))
lParede = int(input("Digite a largura de uma parede: "))

areaParede = hParede * lParede
qntTinta = areaParede / 2

print(f"Para pintar uma parede de {lParede}x{hParede} m² são necessários {qntTinta} litros de tinta.")