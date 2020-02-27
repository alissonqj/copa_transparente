import random

aleatorio = random.randint(1, 101)


def get_input():
    while True:
        x = input("Chute um numero de 1 a 100, ou digite sair: ")
        if x == 'sair':
            return x
        x = int(x)
        if x > 0 and x <= 100:
            return x
        else:
            print("Por favor, digite um número de 1 a 100, ou digite sair.")


def acertou_o_numero(aleatorio, x):
    if x > aleatorio:
        print("Chute foi muito alto")
        return False
    elif x < aleatorio:
        print("Chute foi muito baixo")
        return False
    else:
        return True


def main():
    print("Bem vindo ao programa.")
    contador = 0
    while True:
        x = get_input()
        contador += 1
        if x == 'sair':
            print('Fim do programa')
            break
        resultado = acertou_o_numero(aleatorio, x)
        if resultado:
            print(f'Parabéns, você acertou após {contador} tentativas')
            break


if __name__ == "__main__":
    main()
