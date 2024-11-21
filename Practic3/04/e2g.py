e2g = {
    "stork": "storch",
    "hawk": "falke",
    "woodpecker": "specht",
    "owl": "eule"
}

print("English-German dictionary:")
print(e2g)

print("\nThe German word for 'owl' is:", e2g["owl"])

e2g["sparrow"] = "spatz"
e2g["eagle"] = "adler"

print("\nUpdated dictionary:")
print(e2g)

keys = list(e2g.keys())
values = list(e2g.values())

print("\nKeys:", keys)
print("Values:", values)
