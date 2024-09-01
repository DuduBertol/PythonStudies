#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

num = int(input("Digite um número: "))

ante = num - 1
suce = num + 1

print(f"O número escolhido foi {num}. O seu antecessor é {ante}, e seu sucessor é {suce}.")