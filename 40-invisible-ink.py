
# def int_to_bin(x):
#     bits = []
#     while x > 0:
#         bits.append(x % 2)
#         x = x // 2
#     return list(reversed(bits))

def int_to_bin(x):
    bits = []
    for i in range(8):
        bits.append(x % 2)
        x = x // 2
    return list(reversed(bits))

def bin_to_int(bits):
    x = 0
    for b in bits:
        x = x * 2 + b
    return x

def char_to_bin(x):
    return int_to_bin(ord(x))

def bin_to_char(x):
    return chr(bin_to_int(x))

def str_to_bin(str):
    result = []
    for c in str:
        result = result + char_to_bin(c)
    return result


def bin_to_str(bits):
    result = ""
    while len(bits) > 0:
        chunk = bits[0:8]
        result = result + bin_to_char(chunk)
        bits = bits[8:]
    return result
        


print(bin_to_int(int_to_bin(234)))
print(bin_to_char(char_to_bin("x")))
print(str_to_bin("Hello world.... abcd"))
print(bin_to_str([0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0]))


