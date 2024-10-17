input_string = "2 -1 9 6"

numbers_as_strings = input_string.split()

numbers = list(map(int, numbers_as_strings))

total_sum = sum(numbers)

print(total_sum)