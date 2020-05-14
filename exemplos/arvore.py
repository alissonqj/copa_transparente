class Arvore:
    def __init__(self, cor, tipo, tamanho, tem_frutos):
        self.cor = cor
        self.tipo = tipo
        self.tamanho = tamanho
        self.tem_frutos = tem_frutos

    def atualizar(self, dicionario):
        for campo in dicionario:
            if hasattr(self, campo):
                atributo = dicionario[campo]
                setattr(self, campo, atributo)



