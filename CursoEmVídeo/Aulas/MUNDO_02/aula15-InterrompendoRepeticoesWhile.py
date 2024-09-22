
#WHILE COM FLAG
n = 0
while n != 999:
    n = int(input("Digite um número: "))

# WHILE TRUE
n = s = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n
print(f"A soma vale {s}.")

#SANDBOX
nome = "Dudu"
print(f"{nome:020}")