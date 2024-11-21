buddy = {
    "species": "dog",
    "owner": "Alex"
}

whiskers = {
    "species": "cat",
    "owner": "Sophia"
}

fluffy = {
    "species": "rabbit",
    "owner": "John"
}

pets = [buddy, whiskers, fluffy]

for pet in pets:
    print(f"{pet['owner']} is the owner of a pet - a {pet['species']}.")