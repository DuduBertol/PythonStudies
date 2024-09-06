#Dia 21/08/2024
#AULA 08 - UTILIZANDO MÓDULOS

#import math >> Importa TUDO (aqui eu referencio como math.sqrt(x))
#from math import sqrt >> Importa só o que eu precisar (aqui eu chamo diretamento a função - sqrt(x))

#https://carpedm20.github.io/emoji/

import random
from emoji import emojize

num = random.random() #me devolve um número float entre 0-1
numInt = random.randint(1, 10) #me devolve um número entre 2 ints

print(emojize(f"O número sorteado foi {numInt} :thumbs_up:"))