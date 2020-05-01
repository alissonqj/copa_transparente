import unittest


class TestAdicionaPontos(unittest.TestCase):
    def test_adiciona_pontos_1(self):
        texto = "teste"
        esperado = "t.e.s.t.e"
        resultado = adiciona_pontos(texto)
        self.assertEqual(esperado, resultado)

    def test_adiciona_pontos_2(self):
        texto = "abracadabra"
        esperado = "a.b.r.a.c.a.d.a.b.r.a"
        resultado = adiciona_pontos(texto)
        self.assertEqual(esperado, resultado)


class TestRemovePontos(unittest.TestCase):
    def test_remove_pontos1(self):
        texto = "t.e.s.t.e"
        esperado = "teste"
        resultado = remove_pontos(texto)
        self.assertEqual(esperado, resultado)

    def test_remove_pontos2(self):
        texto = "a.b.r.a.c.a.d.a.b.r.a"
        esperado = "abracadabra"
        resultado = remove_pontos(texto)
        self.assertEqual(esperado, resultado)


def adiciona_pontos(texto):
    """
    Adiciona pontos, entre os caracteres do texto
    Exemplo:
    "teste" -> "t.e.s.t.e"
    """
    # texto = list(texto)
    # texto = ".".join(texto)
    # return texto
    return ".".join(list(texto))


def remove_pontos(text):
    """
    Remove pontos, de uma dada string
    Exemplo:
    "t.e.s.t.e" -> "teste"
    """
    # texto = texto.split(".")
    # return "".join(texto)
    # return "".join(texto.split("."))
    resposta = ""
    if text.find("."):
        lista = text.split(".")
        for item in lista:
            resposta = resposta + item
    return resposta


if __name__ == "__main__":
    unittest.main()
