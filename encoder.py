def string_to_bits(data):
    bits = ""
    for char in data:
        bits += format(ord(char), "08b")
    return bits


def pad_bits(bits, length):
    while len(bits) < length:
        bits += "0"
    return bits
