import unittest


class TestDuplicados(unittest.TestCase):
    def test_sem_duplicados(self):
        set1 = set([1, 2, 3, 4])
        set2 = set([5, 6, 7])
        resultado = duplicados(set1, set2)
        esperado = []
        self.assertEqual(resultado, esperado)

    def test_duplicados(self):
        set1 = set([1, 2, 3, 4, 5, 6])
        set2 = set([4, 5, 6, 7, 8, 9, 10])
        resultado = duplicados(set1, set2)
        esperado = [4, 5, 6]
        self.assertEqual(resultado, esperado)


def duplicados(lista_1, lista_2):
    return list(set(lista_1) & set(lista_2))


def main():
    with open("assets/happynumbers.txt", "r") as happynumbers, open(
        "assets/primenumbers.txt", "r"
    ) as primenumbers:
        lista_1 = happynumbers.read().split("\n")
        lista_2 = primenumbers.read().split("\n")
    return duplicados(lista_1, lista_2)


if __name__ == "__main__":
    resultado = main()
    print(sorted(resultado, key=lambda x: int(x)))
