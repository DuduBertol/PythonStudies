#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido

import random

nome1 = input("Digite o nome do 1º Aluno: ")
nome2 = input("Digite o nome do 2º Aluno: ")
nome3 = input("Digite o nome do 3º Aluno: ")
nome4 = input("Digite o nome do 4º Aluno: ")

alunosLista = [nome1, nome2, nome3, nome4]
alunoEscolhido = random.choice(alunosLista)


print(f"O aluno escolhido para apagar o quadro foi: {alunoEscolhido}.")