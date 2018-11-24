#! /usr/bin/python3.6

films = {
    "Finding Dory": [3,5],
    "Bourne": [18,5],
    "Tarzan": [15,5],
    "GhostBusters": [12,5]
}

while True:
    choice = input("What movie would you like to watch? ").strip().title()

    if choice in films:
        age = int(input("How old are you? ").strip())
        if age >= films[choice][0]:  #Checks age of user

# Check if there's enough seats
            num_seats = films[choice][1]
            if num_seats > 0:
                print("Enjoy the movie!")
                films[choice][1] = films[choice][1] - 1
            else:
                print("Sorry, we are out of tickets for that movie.")
        else:
            print("You aren't old enough for that movie!")
    else:
        print("We don't have that movie.")
