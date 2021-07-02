"""CS1.3 Module 4: Base Conversions"""

def binary_to_decimal(binary_str):
    """returns the decimal number for the given binary digits"""
    decimal = 0
    pow_of_2 = 0

    binary_dict = {'0': 0, '1': 1}

    while binary_str:
        binary_digit = binary_dict[binary_str[-1]]
        decimal += binary_digit * (2 ** pow_of_2)
        binary_str = binary_str[:-1]
        pow_of_2 += 1

    return decimal

assert binary_to_decimal('1011') == 11
assert binary_to_decimal('00000') == 0
assert binary_to_decimal('00001') == 1
assert binary_to_decimal('11111') == 31

print("`binary_to_decimal` tests passed")

def decimal_to_binary(decimal_num):
    """the binary representation of the given decimal number"""
    # take my decimal number
    # keep dividing by base (2): loop?
    # I want to record the remainders some how: maybe store in a list?
    # I want to stop when my thing I'm dviding by is less than the
    # base: conditional or loop stopper: while loop?

    # special case for 0 and 1

    if decimal_num in range(2):
        return str(decimal_num)

    remainders = []

    while decimal_num > 0:

        remainder = decimal_num % 2
        remainders.append(str(remainder))
        # print("Remainder: ", remainder)

        decimal_num = decimal_num // 2
        # print("Decimal: ", decimal_num)

    # print("".join(remainders))
    return "".join(remainders)[::-1]

assert decimal_to_binary(0) == '0'
assert decimal_to_binary(1) == '1'
assert decimal_to_binary(2) == '10'
assert decimal_to_binary(55) == '110111'
assert decimal_to_binary(389) == '110000101'

print("`decimal_to_binary` tests passed")

# STRETCH: can you use what you have written so far to
# create hex_to_decimal() and decimal_to_hex() functions?

def hex_to_decimal(hex_str):
    """returns the decimal number for the given hex digits"""
    decimal = 0
    pow_of_16 = 0

    hex_dict = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
    }

    while hex_str:
        hex_digit = hex_dict[hex_str[-1]]
        decimal += hex_digit * (16 ** pow_of_16)
        hex_str = hex_str[:-1]
        pow_of_16 += 1

    return decimal

assert hex_to_decimal('B') == 11
assert hex_to_decimal('2F9B') == 12187
assert hex_to_decimal('FF') == 255
assert hex_to_decimal('1F') == 31

print("`hex_to_decimal` tests passed")

def decimal_to_hex(decimal_num):
    """the binary representation of the given decimal number"""
    # take my decimal number
    # keep dividing by base (2): loop?
    # I want to record the remainders some how: maybe store in a list?
    # I want to stop when my thing I'm dviding by is less than the
    # base: conditional or loop stopper: while loop?

    # special case for 0 and 1

    hex_dict = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F',
    }

    if decimal_num in range(16):
        return hex_dict[decimal_num]

    remainders = []

    while decimal_num > 0:
        remainder = decimal_num % 16
        remainders.append(hex_dict[remainder])
        # print("Remainder: ", remainder)

        decimal_num = decimal_num // 16
        # print("Decimal: ", decimal_num)

    # print("".join(remainders))
    return "".join(remainders)[::-1]


assert decimal_to_hex(1096) == '448'
assert decimal_to_hex(4096) == '1000'
assert decimal_to_hex(652) == '28C'
assert decimal_to_hex(255) == 'FF'
assert decimal_to_hex(2_147_483_647) == '7FFFFFFF'
assert decimal_to_hex(5) == '5'
assert decimal_to_hex(15) == 'F'
assert decimal_to_hex(0) == '0'

print("`decimal_to_hex` tests passed")
