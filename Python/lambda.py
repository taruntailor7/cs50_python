people = [
    {"name": "Harry", 'house': "Gryffindo"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

# with normal function
def f(person):
    return person["name"]
people.sort(key=f)

# with lambda function
people.sort(key=lambda person: person["name"])

print(people)