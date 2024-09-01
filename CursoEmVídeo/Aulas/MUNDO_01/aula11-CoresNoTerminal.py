
# Padrão ANSI escape sequence

# SINTAXE>> \033[_style_;_text_;_back_m
    #Padrão do terminal >> \033[m
#Se um dos 3 valores for 0 é nulo

#VALORES DE STYLE
    # 0 - Sem Estilo, sem formatação
        # Pode ser desconsiderado
    # 1 - Bold
    # 4 - Underline
    # 7 - Negative (inverte TEXT e BACK)

#VALORES DE TEXT
    # 30 - Branco (pra mim ta preto - deve ser do theme dark)
    # 31 - Vermelho
    # 32 - Verde
    # 33 - Amarelo
    # 34 - Azul
    # 35 - Roxo
    # 36 - Ciano
    # 37 - Cinza

#VALORES DE BACK
    # 40 - Branco (preto tbm)
    # 41 - Vermelho
    # 42 - Verde
    # 43 - Amarelo
    # 44 - Azul
    # 45 - Roxo
    # 46 - Ciano
    # 47 - Cinza

#Como fazer TEXT preto>> \033[7;30m
    #Ele inverte o branco(text padrão) com o preto(030) e faz o text virar preto


#EXs contendo:
# - desconsiderando style
# - text e back
# - quebrando formatação no final (retornando ao padrão)

print("\033[37;42m"
      "Olá, Mundo!"
      "\033[m")

print("\033[40m"
      "Olá, Mundo!"
      "\033[m")

textAzul = "\033[34m"
print(f"{textAzul}Olá mundo!")

cores = {"limpa":"\033[m",
        "azul":"\033[34m",
        "vermelho":"\033[30;41m",
         }

print(f"{cores["vermelho"]}Olá mundo!{cores["limpa"]}")
