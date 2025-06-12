# Esse código irá ler 2 valores e imprimir todos os valores entre eles que o resto da divisão deles por 5 for 2 ou 3

x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))

inicio = min(x, y) + 1
fim = max(x, y)

for i in range(inicio, fim):
    if i % 5 == 2 or i % 5 == 3:
        print(i)