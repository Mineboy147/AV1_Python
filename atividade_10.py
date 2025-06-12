# Esse código irá ler os números inteiros inseridos e imprimir de forma inversa e decrescente

entrada = input("Digite os números desejados (separados por espaço): ")
numeros = list(map(int, entrada.split()))

print("\nOrdem inversa:\n")
for num in reversed(numeros):
    print(num)

print("\nOrdem decrescente:\n")
for num in sorted(numeros, reverse=True):
    print(num)