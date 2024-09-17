#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

n = int(input("Digite o número de elementos que você deseja ver da sequência de Fibonacci: "))
lastNum = 0
num = 1
nextNum = 0

print(f"{lastNum} - {num} - ", end="")

c = 1
while c < n:
    nextNum = lastNum + num
    lastNum = num
    num = nextNum
    c += 1
    print(f"{nextNum} - ", end="")

print("FIM")
print(f"\n{n} elementos foram mostrados.")
