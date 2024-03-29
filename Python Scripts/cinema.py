films = {
    "Finding Dory": [3,5],
    "Bourne": [18,5],
    "Tarzan": [15,5],
    "Ghostbusters": [12,5]
    }

while True:
    choice = input("What movie would you like to watch?: ").strip().title()

    if choice in films:
        age = int(input("How old are you?: ").strip())

        if age >= films[choice][0]:
            num_seats = films[choice][1]
            tickets = int(input("How many tickets do you need?: ").strip())
            if tickets > num_seats:
                print("There are not enough available seats left.")
                print(films)
            if tickets <= num_seats:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1] - tickets
                print(films)
            if num_seats == 0:
                print("This movie is sold out.")
                print(films)
        else:
            print("You are too young to see that film!")
    else:
        print("We don't have that film")
