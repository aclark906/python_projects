students = {
    "male":["Tom", "Charlie", "Harry", "Frank"],
    "female":["Sarah", "Huda", "Samantha", "Emily", "Elizabeth"]
    }

for gender in students.keys():
    for name in students[gender]:
        if "a" in name:
            print(name)
