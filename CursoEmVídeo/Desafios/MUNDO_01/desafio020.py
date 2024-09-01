#O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

nome1 = input("Digite o nome do 1º Aluno: ")
nome2 = input("Digite o nome do 2º Aluno: ")
nome3 = input("Digite o nome do 3º Aluno: ")
nome4 = input("Digite o nome do 4º Aluno: ")

alunosLista = [nome1, nome2, nome3, nome4] #isso é uma lista (??)
#alunosEscolhidos = random.choices(alunosLista, weights=[1,1,1,1], k = 4) >> Não é assim

shuffle(alunosLista) #Correção do guanabara >> random.shuffle(list[])

print(f"A lista de alunos escolhidos foi: {alunosLista}.")
#Corrigir problema de repetição