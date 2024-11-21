number = int(input("Enter a four-digit number: "))

if 1000 <= number <= 9999:

    thousands = number // 1000
    hundreds = (number // 100) % 10
    tens = (number // 10) % 10
    units = number % 10

    sum_digits = thousands + hundreds + tens + units

    print(f"{thousands} + {hundreds} + {tens} + {units} = {sum_digits}")
else:
    print("Please enter a four-digit number.")