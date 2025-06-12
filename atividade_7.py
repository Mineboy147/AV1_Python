# Esse código irá imprimir o resultado da substituição de caracteres escolhidos

palavra = str(input("Digite uma palavra: "))
primeiro_caracter = str(input("Digite a letra que você quer subistituir: "))
segundo_caracter = str(input("Você quer subustituir a letra escolhida por qual letra?: "))

resultado = palavra.replace(primeiro_caracter, segundo_caracter)

print(f"Resultado final foi: {resultado}")