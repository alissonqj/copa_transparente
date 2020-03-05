from ..desafios import string_to_dict


def test_script1():
    frase = "teste jcavi treinamentos"
    resultado = string_to_dict(frase)
    assert resultado == {
        "t": 4,
        "e": 4,
        "s": 2,
        " ": 2,
        "j": 1,
        "c": 1,
        "a": 2,
        "v": 1,
        "i": 2,
        "r": 1,
        "n": 2,
        "m": 1,
        "o": 1,
    }


def test_script2():
    frase = "teste simples"
    resultado = string_to_dict(frase)
    assert resultado == {"t": 2, "e": 3, "s": 3, "i": 1, "m": 1, "p": 1, "l": 1, " ": 1}
