from crud.create import create_record

pick_text = "Pick one of the options below:\n1) Create new record\nq) Exit"
is_running = True


def handle_choice(choice):
    if choice == "q":
        print("Closing program ...")
        exit()
    elif choice == "1":
        create_record()
    else:
        print("Unknown input.\n" + pick_text)


while is_running == True:
    print(pick_text)
    option = input()
    handle_choice(option)
