
#LISTAS SÃO MUTÁVEIS

#aina usando a ideia da lista de lanches


#ADICIONAR ELEMENTOS
#lanche.append("cookie") >> Insere no fim da lista (cria um novo espaço)

#lanche.insert(0, "cookie") >> Insere na posição tal (cria um novo espaço)

#DELETAR ELEMENTOS
# del lanche[3]

#lanche.pop(3) >> normalmente usado para o último elemento (sla pq)
#lanche.pop() >> assim remove o último

#lanche.remove("cookie") >> busca o elemento para eliminar

#if "cookie" in lanche:
    #lanche.remove("cookie") >> é interessante usar assim


#Outros

valores = list(range(4,11)) # >> podemos criar assim

valores.sort() # >> Organiza em ordem crescente
valores.sort(reverse=True) # >> Contrário. Organiza em ordem decrescente

for c, v in enumerate(valores):
    pass
    # >> c é o contador
    # >> v é cada valor de valores

#LIGAÇÃO ENTRE LISTAS
a = [2, 3, 4, 7]
b = a
b[2] = 8
# O print ia mostrar as duas listas como [2, 3, 8, 7]
#Quando igualamos(atribuimos) duas listas elas criam um link(e não uma cópia)


#CÓPIA ENTRE LISTAS
b = a[:] # >> Aqui todos os valores de A são Copiados.

