#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input("Digite um número: "))
divisoes = 0

print("="*30)

for c in range(0, num):
    if (num/(c+1)).is_integer(): # OU if num%c == 0:
        print("\033[33m ", end="")
        divisoes += 1
    else:
        print("\033[31m ", end="")

    print(f"{c + 1}", end="")

    #O QUE ACONTECEU AQUI?
        #Eu estou printando a cada rodada "c" o valor de c na tela, sem quebrar a linha.
        #Entretanto, antes de printar, eu checo QUAL número é, para então mudar sua cor.
            #Assim, na sequência, printo o valor de c, agora colorido.

print("\033[m")
print("="*30)

print(f"O número {num} é divisível {divisoes} vezes.")

if divisoes == 2:
    print(f"Logo ele{"\033[034m"} É PRIMO. {"\033[m"}")
else:
    print(f"Logo ele{"\033[035m"} NÃO É PRIMO. {"\033[m"}")
