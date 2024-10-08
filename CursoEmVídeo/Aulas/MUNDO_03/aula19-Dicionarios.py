
pessoas = {"nome": "Dudu", "sexo": "M", "idade": 19}

print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())

#del pessoas("sexo")

for k, v in pessoas.items():
    print(f"{k} = {v}")


#==========

brasil = []
estado1 = {"uf": "Rio de Janeiro", "sigla": "RJ"}
estado2 = {"uf": "São Paulo", "sigla": "SP"}
brasil.append(estado1)
brasil.append(estado2)

#brasil = [{},{}]

estado = dict()
brazil = list()

for c in range(0,3):
    estado["uf"] = str(input("UF >> "))
    estado["sigla"] = str(input("Sigla >> "))

    brasil.append(estado.copy()) #.copy() é um mét0do para copiar um dict, assim como o [:] para listar

for e in brasil:
    print(e)