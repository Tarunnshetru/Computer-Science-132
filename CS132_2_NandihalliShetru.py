#name: Tarun Nandihalli Shetru
FILE_NAME = "UD.txt"


def load_users():
    # This will load all users from the text file into a list.

    users = []

    file = open(FILE_NAME, "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        line = line.strip()

        if line == "":
            continue

        if line.upper().startswith("FIRST"):
            continue

        line_list = line.split(",")

        first_name = line_list[0].strip()
        last_name = line_list[1].strip()
        username = line_list[2].strip()
        password = line_list[3].strip()

        users.append([first_name, last_name, username, password])

    return users


def print_user(user):
    #To prints a user's information.

    print(user[0] + "," + user[1] + "," + user[2] + "," + user[3])


def search_user(users, search_index, search_value):
    #Searches for a user in the users list.

    for user in users:
        if user[search_index].lower() == search_value.lower():
            return user

    return []


def output(users, sort_index):
    #For the output of all users in alphabetical order.
    sorted_users = sorted(users, key=lambda user: user[sort_index].lower())

    for user in sorted_users:
        print_user(user)


def insert_user(users):
    #Inserts a new user into the list and the text file.
    
    user_info = input("Enter user info in the following format: First name,last name,username,password: ")

    line_list = user_info.split(",")

    if len(line_list) != 4:
        print("Invalid format")
        return

    first_name = line_list[0].strip()
    last_name = line_list[1].strip()
    username = line_list[2].strip()
    password = line_list[3].strip()

    new_user = [first_name, last_name, username, password]
    users.append(new_user)

    file = open(FILE_NAME, "a")
    file.write("\n" + first_name + "," + last_name + "," + username + "," + password)
    file.close()

    print("User inserted")


def display_menu():
    #Displays the main menu.
    print()
    print("A: Search by last name")
    print("B: Search by first name")
    print("C: Search by username")
    print("D: Display all users alphabetically by First name")
    print("E: Display all users alphabetically by Last name")
    print("F: Insert a user")
    print("Q: Quit")
    print()


def main():
    users = load_users()

    choice = ""

    while choice != "Q":
        display_menu()
        choice = input("Enter your choice: ").upper()

        if choice == "A":
            last_name = input("Enter user's last name: ")
            user = search_user(users, 1, last_name)

            if user == []:
                print("Not found")
            else:
                print_user(user)

        elif choice == "B":
            first_name = input("Enter user's first name: ")
            user = search_user(users, 0, first_name)

            if user == []:
                print("Not found")
            else:
                print_user(user)

        elif choice == "C":
            username = input("Enter user's username: ")
            user = search_user(users, 2, username)

            if user == []:
                print("Not found")
            else:
                print_user(user)

        elif choice == "D":
            output(users, 0)

        elif choice == "E":
            output(users, 1)

        elif choice == "F":
            insert_user(users)

        elif choice == "Q":
            print("Goodbye")

        else:
            print("Invalid choice")


main()
