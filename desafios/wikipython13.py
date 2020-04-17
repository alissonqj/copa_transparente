def desenha_moldura(linhas, colunas):
    """
    Desenha uma moldura com linhas e
    colunas, desenhados pelos
    caracteres: '-' '+' e '|'
    Exemplo:
    2 linhas e 2 colunas
    +--+--+
    |  |  |
    +--+--+
    |  |  |
    +--+--+
    """
    linhas = validar_numero(linhas)
    colunas = validar_numero(colunas)
    moldura = ""
    for linha in range(linhas):
        parte_superior = ""
        meio = ""
        for coluna in range(colunas):
            parte_superior += "+--"
            meio += "|  "
        parte_final = parte_superior
        moldura += f"{parte_superior}+\n{meio}|\n"
    return moldura + parte_final + "+"


def validar_numero(numero):
    """ Valida número entre 1 e 20"""
    if numero < 1:
        return 1
    elif numero > 20:
        return 20
    else:
        return numero
