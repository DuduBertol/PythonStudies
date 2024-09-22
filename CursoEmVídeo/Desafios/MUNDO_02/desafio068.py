# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

wins = 0
sumSide = ""
print("Let's play Even-Odd:")
print("-"*20)

while True:
    playerSide = input("You want EVEN or ODD? [E/O] ").strip().upper()
    playerNum = int(input("Type a number: [1-10] "))
    print("-" * 20)

    randomNum = randint(1,10)
    sum = playerNum + randomNum

    if sum % 2 == 0:
        sumSide = "EVEN"
    else:
        sumSide = "ODD"

    print(f"You played {playerNum} and the PC played {randomNum}.")
    print(f"The total is {sum} and it's {sumSide}")
    print("-" * 20)

    if "E" in playerSide and "EVEN" in sumSide:
        wins += 1
        print("You WIN!")
    elif "O" in  playerSide and "ODD" in sumSide:
        wins += 1
        print("You WIN!")
    else:
        print("You LOSE!")
        break

    print("-" * 20)
    print("Let's play again...")
    print("-"*20)

print(f"GAME OVER. You win {wins} times in a row.")

