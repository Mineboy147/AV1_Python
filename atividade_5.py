# Esse código irá ler a quantidade de alunos e as notas e calcula a média

n = int(input("Digite a quantidade de alunos: "))
notas = []

for _ in range(n):
    nota = float(input("Digite as notas: "))
    notas.append(nota)

media = sum(notas) / n
limite_superior = media * 1.10 
limite_inferior = media * 0.90  

acima = 0
abaixo = 0

for nota in notas:
    if nota > limite_superior:
        acima += 1
    elif nota < limite_inferior:
        abaixo += 1

print(f"{media:.2f}")
print(acima)
print(abaixo)