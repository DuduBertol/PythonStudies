# Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

#EU
print("Eu")
num = int(input("Digite um número e mostrarei seu fatorial: "))
fat = 1

print(f"O fatorial de {num} é: >> ", end="")
while num > 1:
    fat = fat * num
    print(f"{num} * ", end="")
    num -= 1
print(f"1 = {fat}")

#GUANABARA
print("Guanabara")
num = int(input("Digite um número e mostrarei seu fatorial: "))
fat = 1

print(f"O fatorial de {num} é: >> ", end="")
while num > 0:
    print(f"{num}", end="")
    print(" * " if num > 1 else " = ", end="") #Tá, isso parece útil.
    fat *= num
    num -= 1
print(f"{fat}")


