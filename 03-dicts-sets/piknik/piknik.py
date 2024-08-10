#!/usr/bin/env python3

import sys, itertools
from decimal import Decimal, InvalidOperation


def parse_args(args: list[str]) -> dict[str, Decimal]:
    if len(args) == 0 or len(args) % 2 == 1:
        msg = ('Argumentos devem ser pares de nome e valor da contribuição. Exemplo:\n'
               '  {} Alice 12.30 Beto 0 Carla 25.1')
        raise TypeError(msg)
    contas = {}
    for nome, valor in itertools.batched(args, 2):
        try:
            contas[nome] = Decimal(valor)
        except InvalidOperation as e:
            raise ValueError(f'Argumento inválido: {valor!r} deveria ser um valor numérico.')
    return contas


def totalizar(contas: dict[str, Decimal])-> Decimal:
    return sum(contas.values())


def extrato(contas: dict[str, Decimal], ideal: Decimal):
    for nome, valor in sorted(contas.items()):
        saldo = valor - ideal
        if saldo == 0:
            print(f'{nome}\t{valor:0.2f}\t\N{CHECK MARK}')
        else:
            operação = 'receber' if saldo > 0 else 'pagar'
            print(f'{nome}\t{valor:0.2f}\t{abs(saldo):0.2f} a {operação}')


def main():
    try:
        contas = parse_args(sys.argv[1:])
    except (TypeError) as e:
        print(e.args[0].format(sys.argv[0]))
        sys.exit(-1)
    except (ValueError) as e:
        print(e)
        sys.exit(-2)
    total = totalizar(contas)
    print(len(contas), 'participantes.')
    print(f'Total de contribuições: {total:.2f}')
    ideal = total / len(contas)
    print(f'Contribuição ideal:     {ideal:.2f}')
    extrato(contas, ideal)


if __name__ ==  '__main__':
    main()
