# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time do Internacional.

tuplaTimes = ("Botafogo", "Fortaleza", "Palmeiras", "Flamengo", "São Paulo", "Bahia", "Cruzeiro", "Internacional", "Vasco da Gama", "Atlético-MG",
              "Juventude", "Bragantino", "Athletico-PR", "Grêmio", "EC Vitória", "Criciúma", "Corinthians", "Fluminense", "Cuiabá", "Atlético-GO")

print("-"*20)
print("Os cinco primeiros colocados:")
print(tuplaTimes[:5])

print("-"*20)
print("Os 4 últimos colocados:")
print(tuplaTimes[-4:])

print("-"*20)
print("Os times em ordem alfabética:")
print(sorted(tuplaTimes))

print("-"*20)
print(f"O INTERNACIONAL está na {tuplaTimes.index("Internacional")+1}ª Posição.")
