from ..desafios import string_to_contador_string


def test_frase1():
    frase = "aaaaabbbbccccccaaaaaaa"
    resultado = string_to_contador_string(frase)
    assert resultado == "5a4b6c7a"


def test_frase2():
    frase = "zzzzyyyykkkkk"
    resultado = string_to_contador_string(frase)
    assert resultado == "4z4y5k"
