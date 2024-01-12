list = []

while len(list) < 3:
    new_name = input("Please add a new name: ").strip().capitalize()
    list.append(new_name)

print("The list is now full.")
print(list)
