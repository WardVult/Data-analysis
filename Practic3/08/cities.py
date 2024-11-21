cities = {
    'Kyiv': {
        'country': 'Ukraine',
        'population': 2884000,
        'fact': 'Kyiv is known as the city of a thousand churches.'
    },
    'Paris': {
        'country': 'France',
        'population': 2148000,
        'fact': 'Paris is home to the Eiffel Tower, one of the world’s most recognizable landmarks.'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': 13929286,
        'fact': 'Tokyo is the world’s most populous metropolitan area.'
    }
}

for city, info in cities.items():
    print(f"{city}:")
    print(f"  Country: {info['country']}")
    print(f"  Population: {info['population']}")
    print(f"  Fact: {info['fact']}\n")
