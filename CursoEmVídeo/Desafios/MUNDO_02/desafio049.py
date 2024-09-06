#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input("Digite um número e eu exibirei sua tabuada: "))

print(f"\n A tabuada do número {num} é:")
print("-"* 20)

for c in range(0, 10):
    print(f"| {num} x {c+1} = {num * (c+1)} | ")

print("-"* 20)
