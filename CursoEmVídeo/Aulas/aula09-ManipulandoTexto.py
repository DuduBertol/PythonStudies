
#=============FATIAMENTO

# frase = "oi eu sou o DUDU"
#frase possui 16 caracteres, do index [0] ao [15]

#frase[0] = "O"

#frase[12:16] >> Ranges excluem o último valor, sendo assim de 12 a 16 ele imprime do index [12] ao [15]

#frase[0:9:2] >> Escreve do 0 ao 8 (oi eu sou) pulando de 2 em 2 = (o_ _u_s_u) onde _ são os espaços excluidos

#frase[:6] >> Omite o início, é como se eu escrevesse frase[início:5] = (oi eu)
#frase[7:] >> Omite o final, é como se eu escrevesse frase[5:final] = (sou o DUDU)

#frase [7::3] >> Escreve do [7] ao final pulando de 3 em 3 = (s__ __D__U)


#=============ANÁLISE

#len(frase) = 16 >> É o .Length( )

#frase.count("o") = 3

#frase.count("o", 0, 10) = 2 >> (oi eu sou)

#frase.find("DUDU") = 12 >> Se encontar, retorna o valor de index onde começou

#frase.find("Android") = -1 >> Retorna -1 quando não encontrar a string solicitada

#"DUDU" in frase = true >> Operador que retorna bool



#=============TRANSFORMAÇÃO

#frase.replace("DUDU", "Android")
    #Note que replace() não muda a string. String são imutáveis por natureza
        #Assim, para mudá-la é necessário rearmazenar o resultado em uma variável.

#frase.upper() >> Tudo Maiúscula
#frase.lower() >> Tudo Minúscula
#frase.capitalize() >> Joga tudo em minúsculo e a [0] fica maiúscula (Oi eu sou dudu)
#frase.title() >> Analisa os espaços e cada início de palavra fica maiúsculo (Oi Eu Sou Dudu)

#frase.strip() >> remove os espaços do início e do final
#frase.rstrip() >> remove os espaços da direita, do final
#frase.lstrip() >> remove os espaços da esquerda, do início



#=============DIVISÃO

#frase.split() >> Divisão na string onde tem espaço
    #O split gera uma lista com as strings dessa divisão
    #frase = [oi, eu, sou, DUDU]


#=============JUNÇÃO

#"-".join(frase)
    #Oi-eu-sou-DUDU


#===========EXTRA

#Aspas triplas servem para textos longos
#print("""Finding the right code and make it work out on your own is a lot more rewarding from my perspective
#      and I think not only mine, in this kata and many other ones you get to practice some dynamic programming
#      concepts basically, optimization, algorithm efficiency, which is something that's already there and every
#      coder should at least try to get familiar with, you've only got to do better and more research sometimes.""")

#Métodos podem ser "combados", ex.: frase(upper).count("o")

#frase = frase.replace("DUDU", "Android") >> Armazena o valor do replace na mesma variavel, alterando-a.
    #pois, por padrão, só com um métod não podemos mudar, strings são imutaveis

#Mais elaborado
    #frase = frase.split()
    #print(frase[3][0]) >> Debuga "D", pois pega a palavra [3] da lista do split e em seguida a string [0] que a compõe



