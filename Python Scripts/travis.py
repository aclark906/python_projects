known_users = ["Alice", "Bob", "Claire", "Dan","Emma","Fred","Georgie","Harry"]

while True:
    print("Hi! My name is Travis.")
    user = input('What is your name? ').strip().capitalize()

    if user in known_users:
        print("Hello {}!".format(user))
        remove = input("Would you like to be removed from the system? (y/n): ").strip().lower()
        if remove == "y":
            known_users.remove(user)
        elif remove == "n":
            print("No problem, I didn't want you to leave anyway!")
        
    else:
        print("Unfortunately, you are not a known user.")
        add = input("Would you like to be added to the list? (y/n): ").strip().lower()
        if add == "y":
            known_users.append(user)
        elif add == "n":
            print("No problem, see you around!")
        
    
