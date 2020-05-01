import unittest

from exemplos import ContaCorrente, ContaPoupanca, UsuarioPessoaFisica


class TestContaCorrente(unittest.TestCase):
    def setUp(self):
        self.vini = UsuarioPessoaFisica.criar("Vini", "12345678910", "24/09/1993")
        self.cc = ContaCorrente(500, self.vini)

    def test_construtor(self):
        self.assertEqual(self.cc.usuario, self.vini)
        self.assertEqual(self.cc.saldo, 500)

    def test_depositar_positivo(self):
        self.assertEqual(self.cc.saldo, 500)
        self.cc.depositar(100)
        self.assertEqual(self.cc.saldo, 600)

    def test_depositar_negativo(self):
        self.assertEqual(self.cc.saldo, 500)
        self.assertRaises(ValueError, self.cc.depositar, -500)

    def test_sacar_positivo(self):
        self.assertEqual(self.cc.saldo, 500)
        self.cc.sacar(200)
        self.assertEqual(self.cc.saldo, 300)

    def test_sacar_negativo(self):
        self.assertEqual(self.cc.saldo, 500)
        with self.assertRaises(ValueError):
            self.cc.sacar(-100)


if __name__ == "__main__":
    unittest.main()
