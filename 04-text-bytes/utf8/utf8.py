"""
utf8.decode(…): The world's slowest UTF-8 decoder function.

A didactic example to explain the UFT-8 encoding algorithm.
"""

bit = bool  # type alias for values 0 or 1

def unpack(octet: int, width: int = 8) -> list[bit]:
    bits = [False] * width
    for i in reversed(range(width)):
        bits[i] = bool(octet & 1)
        octet >>= 1
    return bits


def pack(bits: list[bit]) -> int:
    octet = 0
    for i, bit in enumerate(reversed(bits)):
        octet += 2 ** i * bit
    return octet


def decode(octets: bytes) -> str:
    stream = iter(octets)
    out: list[str] = []
    while True:
        try:
            bits = unpack(next(stream))
        except StopIteration:
            break
        try:
            match bits:
                case [0, *rest]:                    # 0xxx_xxxx -> 7 bits
                    out_bits = rest
                case [1, 1, 0, *head]:              # 110x_xxxx
                    tail = unpack(next(stream), 6)  # 10xx_xxxx -> 11 bits
                    out_bits = head + tail
                case [1, 1, 1, 0, *head]:           # 1110_xxxx
                    body = unpack(next(stream), 6)  # 10xx_xxxx
                    tail = unpack(next(stream), 6)  # 10xx_xxxx -> 16 bits
                    out_bits = head + body + tail
                case [1, 1, 1, 1, 0, *head]:        # 1111_0xxx
                    neck = unpack(next(stream), 6)  # 10xx_xxxx
                    body = unpack(next(stream), 6)  # 10xx_xxxx
                    tail = unpack(next(stream), 6)  # 10xx_xxxx -> 21 bits
                    out_bits = head + neck + body + tail
                case _:
                    bit_str = f'{pack(bits):_b}'
                    raise ValueError(f'Invalid UTF-8 start pattern: {bit_str}')
        except StopIteration:
            raise ValueError('Incomplete UTF-8 byte sequence')
        out.append(chr(pack(out_bits)))
    return ''.join(out)


def encode(text: str) -> bytes:
    out = bytearray()
    for char in text:
        code = ord(char)
        if code < 0x80:                                  # 0xxx_xxxx
            out.append(code)
        elif 0x80 <= code < 0x800:
            head = code >> 6 | 0b1100_0000               # 110x_xxxx
            tail = code & 0b11_1111 | 0b1000_0000        # 10xx_xxxx
            out.extend([head, tail])
        elif 0x800 <= code < 0x1_0000:
            head = code >> 12 | 0b1110_0000              # 1110_xxxx
            body = code >> 6 & 0b11_1111 | 0b1000_0000   # 10xx_xxxx
            tail = code & 0b11_1111 | 0b1000_0000        # 10xx_xxxx
            out.extend([head, body, tail])
        else:
            head = code >> 18 | 0b1111_0000              # 1111_0xxx
            neck = code >> 12 & 0b11_1111 | 0b1000_0000  # 10xx_xxxx
            body = code >> 6 & 0b11_1111 | 0b1000_0000   # 10xx_xxxx
            tail = code & 0b11_1111 | 0b1000_0000        # 10xx_xxxx
            out.extend([head, neck, body, tail])
    return bytes(out)
