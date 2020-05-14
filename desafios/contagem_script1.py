from collections import Counter


# Type Hints - tipagem
def string_to_dict(dicionario: str) -> dict:
    return Counter(dicionario)
