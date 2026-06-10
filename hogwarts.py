# This is a list function that prints the names of students in a class with their corresponding numbers.
students = ["Alice", "Bob", "Charlie", "David", "Eve"]

for i in range(len(students)):
    print(i + 1, students[i])


# This is a dictionary function that prints the names of students in a class with their corresponding houses.
students = {
    "Alice": "Gruffindor",
    "Bob": "Gryffindor",
    "Charlie": "Gryffindor",
    "David": "Slytherin",    
}

for student in students:
    print(student, students[student], sep=": ")


# This is a list of dictionaries function that prints the names of students in a class with their corresponding houses and patronuses.
students = [
    {"name": "Hermione", "house": "Gruffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student)