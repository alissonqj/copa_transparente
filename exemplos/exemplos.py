class Usuario:
    def __init__(self, nome, endereco, cidade, pais):
        self._nome = nome
        self.endereco = endereco
        self.cidade = cidade
        self.pais = pais

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, outro_nome):
        if outro_nome != "superman":
            self._nome = outro_nome
        else:
            print("Você não é o superman!!!")


class UsuarioPessoaFisica(Usuario):
    def __init__(self, nome, endereco, cidade, pais, cpf, data_de_nascimento):
        super().__init__(nome, endereco, cidade, pais)
        self._cpf = cpf
        self._data_de_nascimento = data_de_nascimento

    @property
    def representar(self):
        return (
            f"Nome: {self._nome} | Cpf: {self._cpf}"
            + f"| Data de Nascimento: {self._data_de_nascimento}"
        )

    @classmethod
    def criar(cls, nome, cpf, data_de_nascimento):
        return cls(
            nome=nome,
            endereco="",
            cidade="",
            pais="",
            cpf=cpf,
            data_de_nascimento=data_de_nascimento,
        )

    @property
    def cpf(self):
        return self._cpf

    @property
    def data_de_nascimento(self):
        return self._data_de_nascimento


class UsuarioPessoaJuridica(Usuario):
    def __init__(self, nome, endereco, cidade, pais, cnpj, capital_social):
        super().__init__(nome, endereco, cidade, pais)
        self._cnpj = cnpj
        self._capital_social = capital_social

    @property
    def representar(self):
        return f"Nome: {self.nome} | CNPJ: {self.cnpj} | Capital: {self.capital_social}"

    @classmethod
    def criar(cls, nome, cnpj, capital_social):
        return cls(
            nome=nome,
            endereco="",
            cidade="",
            pais="",
            cnpj=cnpj,
            capital_social=capital_social,
        )

    @property
    def cnpj(self):
        return self._cnpj

    @property
    def capital_social(self):
        return self._capital_social


class Conta:
    def __init__(self, saldo, usuario):
        self.saldo = saldo
        self.usuario = usuario

    def sacar(self, valor):
        try:
            self.validar_valor(valor)
        except ValueError:
            print("Não pode sacar negativo meu chapa!")
        self.saldo -= valor
        self.printar_saldo()

    def depositar(self, valor):
        try:
            self.validar_valor(valor)
        except ValueError:
            print("Não pode sacar negativo meu chapa!")
        self.saldo += valor
        self.printar_saldo()

    def printar_saldo(self):
        print("Novo saldo é de:", self.saldo)

    @staticmethod
    def validar_valor(valor):
        if valor <= 0:
            raise ValueError("Valor incorreto")


class ContaCorrente(Conta):
    def __init__(self, saldo, usuario):
        super().__init__(saldo, usuario)


class ContaPoupanca(Conta):
    def __init__(self, saldo, usuario):
        super().__init__(saldo, usuario)

    def depositar(self, valor):
        valor += 0.1
        super().depositar(valor)
