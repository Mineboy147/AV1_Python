# Esse código irá mostrar o indice da letra escolhida que aparece pela primeira vez em uma palavra

texto = input("Digite uma palavra: ")
caractere = input("Digite uma letra: ")
indice = texto.find(caractere)

if indice == -1:
    print("Esse caractere não está presente na palavra inserida")
else:
    print(f"O indice do caractere inserido é :{indice}")

