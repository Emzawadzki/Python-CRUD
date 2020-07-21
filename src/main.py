print("Pick one of the options below:\n1) Create new record\nq) Exit")
is_running = True


def handle_choice(choice):
    print("You picked " + choice + "!")
    if choice == "q":
        print("Closing program ...")
        exit()


while is_running == True:
    option = input()
    handle_choice(option)
