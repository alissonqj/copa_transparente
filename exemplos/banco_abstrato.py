from abc import ABC, abstractmethod


class BancoDeDados(ABC):
    @abstractmethod
    def salvar(self):
        pass

    @abstractmethod
    def obter_informacao_pelo_id(self, id):
        pass
