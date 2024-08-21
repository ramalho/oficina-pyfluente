import sys

import pytest

from utf8 import unpack, pack, decode, encode

BIT_PATTERNS = [
    (0,   [0, 0, 0, 0, 0, 0, 0, 0]),
    (1,   [0, 0, 0, 0, 0, 0, 0, 1]),
    (2,   [0, 0, 0, 0, 0, 0, 1, 0]),
    (3,   [0, 0, 0, 0, 0, 0, 1, 1]),
    (4,   [0, 0, 0, 0, 0, 1, 0, 0]),
    (255, [1, 1, 1, 1, 1, 1, 1, 1]),
]

@pytest.mark.parametrize('octet, expected', BIT_PATTERNS)
def test_unpack(octet, expected):
    got = unpack(octet)
    assert got == expected

@pytest.mark.parametrize('expected, bits', BIT_PATTERNS)
def test_pack(expected, bits):
    got = pack(bits)
    assert got == expected

@pytest.mark.parametrize('expected', [
    'A', 'á', '…', '\N{cat}',
])
def test_decode(expected):
    got = decode(expected.encode('utf8'))
    assert got == expected

@pytest.mark.parametrize('expected', [
    'A', 'á', '…', '\N{cat}',
])
def test_encode(expected):
    got = encode(expected)
    assert got == expected.encode('utf8')


def test_invalid_bit_pattern():
    expected = 'Invalid UTF-8 start pattern: 1000_0000'
    with pytest.raises(ValueError) as excinfo:
        decode(bytes([0b1000_0000]))
    assert expected in str(excinfo.value)


def test_incomplete_byte_sequence():
    expected = 'Incomplete UTF-8 byte sequence'
    with pytest.raises(ValueError) as excinfo:
        decode(bytes([0b1100_0000]))
    assert expected in str(excinfo.value)


@pytest.mark.slow
def test_encode_all_chars():
    codes = range(0, sys.maxunicode + 1)
    for char in (chr(c) for c in codes):
        try:
            octets = char.encode('utf8')
        except UnicodeEncodeError:
            continue  # skip surrogates
        assert encode(char) == octets


@pytest.mark.slow
def test_decode_all_chars():
    codes = range(0, sys.maxunicode + 1)
    for char in (chr(c) for c in codes):
        try:
            octets = char.encode('utf8')
        except UnicodeEncodeError:
            continue  # skip surrogates
        assert decode(octets) == char


