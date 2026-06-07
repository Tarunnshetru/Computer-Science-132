#name: Tarun Nandihalli Shetru

class Userdata:
    def __init__(self, first_name, last_name, username, password):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__username = username
        self.__password = password

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_first_name(self):
        return self.__first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_last_name(self):
        return self.__last_name

    def set_username(self, username):
        self.__username = username

    def get_username(self):
        return self.__username

    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password

    def print_user(self):
        print(f"{self.__first_name:<18}{self.__last_name:<18}{self.__username:<18}{self.__password:<18}")


def load_users(filename):
    users = []

    try:
        infile = open(filename, "r")
        lines = infile.readlines()
        infile.close()

        for line in lines[1:]:
            line = line.strip()

            if line != "":
                parts = line.split(",")

                if len(parts) == 4:
                    first_name = parts[0].strip()
                    last_name = parts[1].strip()
                    username = parts[2].strip()
                    password = parts[3].strip()

                    user = Userdata(first_name, last_name, username, password)
                    users.append(user)

    except FileNotFoundError:
        print(filename, "was not found.")

    return users


def search_by_last_name(users):
    last_name = input("enter the user's name in the form: lastname\n")

    found = False

    for user in users:
        if user.get_last_name().lower() == last_name.lower():
            print("Password:", user.get_password())
            found = True

    if found == False:
        print("Not found")


def search_by_username(users):
    username = input("Enter user's username:\n")

    found = False

    for user in users:
        if user.get_username().lower() == username.lower():
            print("Password:", user.get_password())
            found = True

    if found == False:
        print("Not found")


def insert_user(users, filename):
    user_info = input("Enter user info in the following format: first name, last name, username, password\n")
    parts = user_info.split(",")

    if len(parts) == 4:
        first_name = parts[0].strip()
        last_name = parts[1].strip()
        username = parts[2].strip()
        password = parts[3].strip()

        new_user = Userdata(first_name, last_name, username, password)
        users.append(new_user)

        outfile = open(filename, "a")
        outfile.write("\n" + first_name + "," + last_name + "," + username + "," + password)
        outfile.close()

    else:
        print("Enter a valid option")


def display_all_users(users):
    print(f"{'FIRST NAME':<18}{'LAST NAME':<18}{'USERNAME':<18}{'PASSWORD':<18}")

    for user in users:
        user.print_user()


def print_menu():
    print("A: Search by last name")
    print("B: Search by username")
    print("C: Insert a user")
    print("E. Display all users")


def main():
    filename = "UD.txt"
    users = load_users(filename)

    keep_going = True

    while keep_going:
        print_menu()
        choice = input().upper()

        if choice == "A":
            search_by_last_name(users)
        elif choice == "B":
            search_by_username(users)
        elif choice == "C":
            insert_user(users, filename)
        elif choice == "E" or choice == "D":
            display_all_users(users)
        elif choice == "Q":
            keep_going = False
        else:
            print("Enter a valid option")


main()
