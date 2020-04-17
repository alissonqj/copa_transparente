def imprimir_numeros(n):
    """Printar números até n no formato de pirâmide
    Exemplo:
    1
    1 2
    1 2 3
    1 2 3 ... n
    """
    resultado = ""
    for numero in range(1, n + 1):
        resultado += f"{numero}{' '}"
        com_quebra_de_linha = resultado + "\n"
        # resultado = "{}{}".format(numero, " " * numero)
        print(com_quebra_de_linha, end="")
