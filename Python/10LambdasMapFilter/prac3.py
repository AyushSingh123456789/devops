students = [
    {"name": "Alice", "age": 18, "grade": "A"},
    {"name": "Bob", "age": 17, "grade": "B"},
    {"name": "Charlie", "age": 19, "grade": "A"},
    {"name": "David", "age": 16, "grade": "C"},
    {"name": "Eve", "age": 18, "grade": "A"}
]

filtered_students = list(filter(lambda s: s["age"] >= 18 and s["grade"] == "A", students))
print(filtered_students)