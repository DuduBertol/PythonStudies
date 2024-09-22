
#VARIÁVEIS COMPOSTAS

#TUPLAS

#(é uma lista, não...?)
    #Spoiler: não é.

#>>>>>>>>>TUPLAS SÃO IMUTÁVEIS<<<<<<<<<<<<<<<<

#Não é possivel alterar tuplas
    #Uma vez definidas, elas permanecem iguais até o fim do programa

# lanche = () >> TUPLA
# lanche = [] >> LISTA
# lanche = {} >> DICIONÁRIO

lanche = ("Hamburger", "Suco", "Pizza", "Pudim") #Posso ignorar os parênteses para declarar uma tupla

print(lanche[1:3]) #Printa elemento 1 e 2, desconsiderando 3

print(lanche[2:]) #Printa do 2 ao final
print(lanche[:2]) # printa do início até o anterior ao 2, pois descosidera o 2

print(lanche[-1]) #Printa o último elemento. Começa a contagem de -1 em diante, reduzindo um a cada i, a partir do último elemento.


#Possibilidades de FOR

#1 >> for comida in lanche:
    #Esse não mostra o index, por padrao

#2 >> for c in range(0,len(lanche)):
    #Esse mostra o index

#3 (ou 1Plus)>> for pos, comida in enumerate(lanche):
    #Agora "pos" é o seu index


print(sorted(lanche)) #ORDENADO (ordem alfabética ou numérica)
    #O Sorted não altera a tupla, apenas reorganiza-a


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
    #c = (2, 5, 4, 5, 8, 1, 2)

c.count(5) #O "5" aparece 2x vezes
c.index(8) # O "8" aparece no index [4]. A primeira ocorrência do i.


#TUPLA RECEBEM MULTIPLOS TIPOS DE DADOS
pessoa = ("Dudu", 19, "M", 60)
del pessoa  #Apagar da memória



