cities = ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kyiv', 'Hong Kong']

if len(cities) > 1:
    message = ", ".join(cities[:-1]) + " and " + cities[-1]
elif cities:
    message = cities[0]
else:
    message = "void list"

print(message)