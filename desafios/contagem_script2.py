def string_to_contador_string(frase: str) -> str:
    contador = 0
    elemento = frase[0]
    frase = frase + " "
    nova_string = ""
    for letra in frase:
        if letra == elemento:
            contador += 1
        else:
            nova_string += str(contador) + elemento
            elemento = letra
            contador = 1
    return nova_string
