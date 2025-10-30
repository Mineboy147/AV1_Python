# Esse código irá imprimir seu nome com uma mensagem de boas vindas, mas se for mais de 120 caracteres vai mandar um amensagem de erro

while True:
    fulano = input("Digite seu nome (até 120 caracteres): ")
    if len(fulano) <= 120:
        break
    print("Nome muito longo! Tente novamente.")

print(f"Seja muito bem-vindo(a) {fulano}!")
