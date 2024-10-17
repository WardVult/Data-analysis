input_string = "13 5 62 7 3"

digits = input_string.split()

reversed_digits = digits[::-1]

result_number = ''.join(reversed_digits)

print(result_number)