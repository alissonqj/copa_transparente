from collections.abc import Callable


class Compras(Callable):
    def __init__(self, lista):
        self._lista = lista

    # def __call__(self, item_da_compra):
    #     self._lista.append(item_da_compra)

    @property
    def lista(self):
        return self._lista
