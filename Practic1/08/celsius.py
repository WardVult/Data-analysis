celsius = float(input("Enter temperature in degrees Celsius: "))

fahrenheit = 32 + (9/5) * celsius
kelvin = celsius + 273.15

print("{:^15} : {:.2f}".format("Fahrenheit", fahrenheit))
print("{:^15} : {:.2f}".format("Kelvin", kelvin))