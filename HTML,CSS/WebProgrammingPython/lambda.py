people = [
    {"name": "Carlos", "house": "El Salvador"},
    {"name": "Jesus", "house": "Acajutla"},
    {"name": "Isaias", "house": "Sonsonate"}
]


people.sort(key=lambda person: person["name"])

print(people)
