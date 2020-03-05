class Carro:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    @property
    def descreva(self):
        return f"<Carro {self.nome}> <Cor {self.cor}>"


class Ferrari(Carro):
    def __init__(self, nome, cor, modelo):
        super().__init__(nome, cor)
        self.modelo = modelo

    @property
    def descreva(self):
        return f"{super().descreva} <Modelo {self.modelo}>"
