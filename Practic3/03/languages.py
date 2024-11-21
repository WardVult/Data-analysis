programming_languages = {
    "Python": "Guido van Rossum",
    "Java": "James Gosling",
    "C++": "Bjarne Stroustrup",
    "Ruby": "Yukihiro Matsumoto"
}

for language, developer in programming_languages.items():
    print(f"My favorite programming language is {language}. It was created by {developer}.")

del programming_languages["Java"]

print("\nUpdated dictionary:")
print(programming_languages)