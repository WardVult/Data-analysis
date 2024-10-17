# Get temperature in Celsius from user
celsius = float(input("Enter temperature in degrees Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit = 32 + (9/5) * celsius

# Convert Celsius to Kelvin
kelvin = celsius + 273.15


"""
The formatting string {:^15} : {:.2f} works as follows:

1. {:^15}:
   - Centers the content in a field of width 15 characters.

2. {:.2f}:
   - Formats the number as a floating-point with two decimal places.
"""
print("{:^15} : {:.2f}".format("Fahrenheit", fahrenheit))
print("{:^15} : {:.2f}".format("Kelvin", kelvin))