#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão

#an = a + (n - 1) * r

a = float(input("Digite o primeiro termo de um PA: "))
r = float(input("Digite a razão dessa PA: "))
maxN = 10


print("\n Os primeiros 10 termos dessa PA são: ")
print("-"*20)

for c in range(0, maxN):
    an = int(a + ((c + 1) - 1) * r)
    print(f"O {c+1}º termo vale {an}")