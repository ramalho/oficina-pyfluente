from enum import Enum
from typing import NamedTuple


class Operação(Enum):
    PAGAR = "pagar"
    RECEBER = "receber"


class Contrib(NamedTuple):
    nome: str
    valor: float

    @classmethod
    def construir(cls, nome, valor):
        try:
            return cls(nome, float(valor))
        except ValueError:
            raise ValueError(f'Valor inválido para {nome!r}.')


def totalizar(contribs):
    return sum(c.valor for c in contribs)


class Ajuste(NamedTuple):
    contrib: Contrib
    operação: Operação
    valor: float

