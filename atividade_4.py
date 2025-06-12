# Esse código é um verificador de números primos

def verificar_primo(num):
    if num < 2:
        return False

    flag = True
    for i in range(2, int(num / 2) + 1):
        if (num % i) == 0:
            flag = False
            break
    return flag

num = int(input("Digite um número: "))

if verificar_primo(num):
    print("O número informado (%d) é primo" % num)
else:
    print("O número informado (%d) não é primo" % num)