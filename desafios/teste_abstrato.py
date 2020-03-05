# coding: utf-8
# essa é a solução SEM Closure
def maior_que_100k(valor):
    return valor > 100000


def maior_que_200k(valor):
    return valor > 200000


# essa é a solução COM Closure
def maior(valor_fixo):
    def _maior(valor):
        return valor > valor_fixo

    return _maior


# 1. -> return _maior
# 2. -> _maior(150000)

maior_que_100k = maior(100000)
print("Maior que 100k", maior_que_100k(150000))

maior_que_200k = maior(200000)
print("Maior que 200k", maior_que_200k(199999))
