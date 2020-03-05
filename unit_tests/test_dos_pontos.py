import sys

sys.path.append(".")

from ..desafios.pontos import adiciona_pontos, remove_pontos


def test_adiciona_pontos():
    ponto_a = "teste"
    ponto = adiciona_pontos(ponto_a)
    assert ponto == "t.e.s.t.e"


def test_remove_pontos():
    ponto_b = "t.e.s.t.e"
    resultado = remove_pontos(ponto_b)
    assert resultado == "teste"


def test_remove_pontos_sem_pontos():
    palavra = "teste"
    resultado = remove_pontos(palavra)
    assert resultado == palavra


def test_adiciona_pontos_com_espaco():
    palavra = " teste"
    resultado = adiciona_pontos(palavra)
    assert resultado == " .t.e.s.t.e"


def test_remove_dois_pontos():
    palavra = "t..e...st....e"
    resultado = remove_pontos(palavra)
    assert "teste" == resultado


def test_adiciona_pontos_com_numero():
    palavra = 123123
    resultado = adiciona_pontos(palavra)
    assert resultado is None


def test_adiciona_pontos_none():
    resultado = adiciona_pontos(None)
    assert resultado is None


def test_adiciona_pontos_booleano():
    resultado = adiciona_pontos(True)
    assert resultado is None
