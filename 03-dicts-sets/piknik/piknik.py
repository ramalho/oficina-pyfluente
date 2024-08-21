#!/usr/bin/env python3

import sys, itertools
from decimal import Decimal, InvalidOperation


def parse_args(args: list[str]) -> dict[str, Decimal]:
    if len(args) == 0 or len(args) % 2 == 1:
        msg = ('Forneça pares de nome e valor para cada contribuição. Exemplo:\n'
               '  {} Alice 12.30 Beto 0 Carla 25.1')
        raise TypeError(msg)
    contas = {}
    for nome, valor in itertools.batched(args, 2):
        try:
            contas[nome] = Decimal(valor)
        except InvalidOperation as e:
            raise ValueError(f'Argumento inválido: esperava número, veio {valor!r}.')
    return contas


def extrato(contas: dict[str, Decimal], ideal: Decimal) -> list[str]:
    linhas = []
    for nome, valor in sorted(contas.items()):
        saldo = valor - ideal
        if saldo == 0:
            linhas.append(f'{nome}\t{valor:6.2f}\t\N{CHECK MARK}')
        else:
            operação = 'receber' if saldo > 0 else '  pagar'
            linhas.append(f'{nome}\t{valor:6.2f}   {operação} {abs(saldo):6.2f}')
    return linhas


def main(entradas: list[str]) -> None:
    try:
        contas = parse_args(entradas)
    except (TypeError) as e:
        print(e.args[0].format(sys.argv[0]))
        sys.exit(-1)
    except (ValueError) as e:
        print(e)
        sys.exit(-2)
    print(len(contas), 'participantes.')
    total = sum(contas.values())
    print(f'Total de contribuições: {total:7.2f}')
    ideal = total / len(contas)
    print(f'Contribuição ideal:      {ideal:6.2f}')
    print(*extrato(contas, ideal), sep='\n')


if __name__ ==  '__main__':
    main(sys.argv[1:])
