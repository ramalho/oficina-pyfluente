#!/usr/bin/env python3

"""
Era uma vez...

>>> '\u20a2'
'₢'

>>> for res in buscar('CRUZEIRO'):
...     print(res)
(8354, 'CRUZEIRO SIGN')

>>> for res in buscar('CAT'):
...     print(res)
(41654, 'YI SYLLABLE CAT')
(52289, 'HANGUL SYLLABLE CAT')
(66028, 'PHAISTOS DISC SIGN CAT')
(128008, 'CAT')
(128049, 'CAT FACE')
(128568, 'GRINNING CAT FACE WITH SMILING EYES')
(128569, 'CAT FACE WITH TEARS OF JOY')
(128570, 'SMILING CAT FACE WITH OPEN MOUTH')
(128571, 'SMILING CAT FACE WITH HEART-SHAPED EYES')
(128572, 'CAT FACE WITH WRY SMILE')
(128573, 'KISSING CAT FACE WITH CLOSED EYES')
(128574, 'POUTING CAT FACE')
(128575, 'CRYING CAT FACE')
(128576, 'WEARY CAT FACE')

>>> for res in buscar('CAT EYES'):
...     print(res)
(128568, 'GRINNING CAT FACE WITH SMILING EYES')
(128571, 'SMILING CAT FACE WITH HEART-SHAPED EYES')
(128573, 'KISSING CAT FACE WITH CLOSED EYES')

"""

import sys
from unicodedata import name

def buscar(consulta):
    consulta = consulta.replace('-', ' ')
    palavras = frozenset(consulta.split())
    for cod in range(32, sys.maxunicode + 1):
        car = chr(cod)
        nome = name(car, None)
        if nome is None:
            continue
        nome = nome.replace('-', ' ').split()
        if palavras <= frozenset(nome):
            yield (cod, nome)

def main():
    consulta = ' '.join(sys.argv[1:]).upper()
    for cod, nome in buscar(consulta):
        print(f'U+{cod:04X}\t{chr(cod)}\t{nome}')

if __name__ == '__main__':
    main()
