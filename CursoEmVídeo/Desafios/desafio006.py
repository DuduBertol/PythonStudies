#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

num = int(input("Digite um número: "))

doub = num * 2
trip = num * 3
sqrt = num**(1/2)

print(f"O número escolhido foi {num}. O seu dobro é {doub}, o seu triplo é {trip}, e sua raiz quadrada é ~={sqrt:.2f}.")