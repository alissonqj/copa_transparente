import time


def time_this(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"A função foi executada em {fim - inicio} segundos")
        return resultado

    return wrapper
