#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

m = int(input("Digite um valor em metros: "))

cm = m * 100
mm = m * 1000

print(f"{m} metros equivalem a {cm} centímetros e {mm} milímetros.")