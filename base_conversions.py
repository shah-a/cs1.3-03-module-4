def binary_to_decimal(binary_str):
  """returns the decimal number for the given binary digits"""
  pass

assert binary_to_decimal('1011') == 11
assert binary_to_decimal('00000') == 0
assert binary_to_decimal('00001') == 1
assert binary_to_decimal('11111') == 31


def decimal_to_binary(decimal_num):
  """the binary representation of the given decimal number"""
  #take my decimal number
  #keep dividing by base (2): loop?
  #I want to record the remainders some how: maybe store in a list?
  #I want to stop when my thing I'm dviding by is less than the base: conditional or loop stopper: while loop?

  #special case for 0 and 1

  if decimal_num == 0 or decimal_num == 1:
    return str(decimal_num)

  remainders = []

  while decimal_num > 0:

    remainder = decimal_num % 2
    remainders.append(str(remainder))
    print("Remainder: ", remainder)

    decimal_num = decimal_num // 2
    print("Decimal: ", decimal_num)
  
  print("".join(remainders))
  return "".join(remainders)[::-1]
  
assert decimal_to_binary(0) == '0'
#result of our code    expected result
assert decimal_to_binary(1) == '1'
assert decimal_to_binary(2) == '10'
assert decimal_to_binary(55) == '110111'
assert decimal_to_binary(389) == '110000101'


#STRETCH: can you use what you have written so far to create hex_to_decimal() and decimal_to_hex() functions?

my_string = 'abcd'
