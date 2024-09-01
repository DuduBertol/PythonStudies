#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes

reta1 = float(input("Digite um primeira reta segmento de reta: "))
reta2 = float(input("Digite um segunda reta segmento de reta: "))
reta3 = float(input("Digite um terceira segmento de reta: "))

tipoTriangulo = ""

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("Os segmentos de reta PODEM formar um triângulo.")

    if reta1 == reta2 == reta3:
        tipoTriangulo = "EQUILÁTERO"

    elif reta1 != reta2 and reta1 != reta3 and reta2 != reta3:
        tipoTriangulo = "ESCALENO"

    else:
        tipoTriangulo = "ISÓCELES"

    print(f"O triângulo formado é {tipoTriangulo}.")

else:
    print("Os segmentos de reta NÃO PODEM formar um triângulo.")