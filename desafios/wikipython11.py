import unittest

# TDD - Test Development Driven -> Programar orientado à testes


class TestDesafios(unittest.TestCase):
    def test_produto(self):
        num1 = 10
        num2 = 20
        resultado = produto_do_dobro_mais_metade_do_segundo(num1, num2)
        esperado = (num1 * 2) * (num2 / 2)
        self.assertEqual(resultado, esperado)

    def test_soma_do_triplo(self):
        num1 = 10
        num3 = 30
        resultado = soma_do_triplo_do_primeiro_com_terceiro(num1, num3)
        esperado = (num1 * 3) + num3
        self.assertEqual(resultado, esperado)

    def test_terceiro_elevado(self):
        num3 = 30
        resultado = terceiro_elevado_ao_cubo(num3)
        esperado = 30 ** 3
        self.assertEqual(resultado, esperado)


def produto_do_dobro_mais_metade_do_segundo(a, b):
    return (a * 2) * (b / 2)


def soma_do_triplo_do_primeiro_com_terceiro(a, b):
    return (a * 3) + b


def terceiro_elevado_ao_cubo(a):
    return a ** 3


def main():
    primeiro = int(input("Digite um número inteiro: "))
    segundo = int(input("Digite um número inteiro: "))
    terceiro = int(input("Digite um número real: "))
    resultado1 = produto_do_dobro_mais_metade_do_segundo(primeiro, segundo)
    resultado2 = soma_do_triplo_do_primeiro_com_terceiro(primeiro, terceiro)
    resultado3 = terceiro_elevado_ao_cubo(terceiro)
