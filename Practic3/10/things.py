things = {
    'key': 3,
    'mace': 1,
    'gold coin': 24,
    'lantern': 1,
    'stone': 10
}

print("Equipment:")
total_things = 0  
for item, count in things.items():
    print(f"{count} {item}")
    total_things += count

print(f"Total number of things: {total_things}")
