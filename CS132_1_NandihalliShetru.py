#name:Tarun Nandihalli Shetru. 


FILE_NAME = "UD.txt"

def load_users():
    """
    Loads all users list from UD.txt into a list.
    """
    users = []

    file = open(FILE_NAME, "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        line = line.strip()

        if line == "":
            continue

        if line.upper().startswith("FIRSTNAME"):
            continue

        line_list = line.split(",")

        first_name = line_list[0].strip()
        last_name = line_list[1].strip()
        username = line_list[2].strip()
        password = line_list[3].strip()

        users.append([first_name, last_name, username, password])

    return users


def save_new_user(first_name, last_name, username, password):
    """
    Saves a new user into UD.txt.
    """
    file = open(FILE_NAME, "a")

    file.write(
        first_name + "," +
        last_name + "," +
        username + "," +
        password + "\n"
    )

    file.close()


def find_user(users, username):
    """
    Finds a user in the database.
    """
    for user in users:
        if user[2] == username:
            return user

    return []


def create_username(first_name, last_name, student_id):
    """
    Creates a username.
    """
    username = (
        first_name[0] +
        last_name[0:2] +
        student_id[0:3]
    )

    return username.lower()


def login(users):
    """
    Logs in an existing user.
    """
    print("Please enter your user name and hit enter")
    username = input()

    user = find_user(users, username)

    if user == []:
        print("User not found")
        return False

    print("Enter password")
    password = input()

    if password == user[3]:
        print("you are logged in")
        return True

    print("wrong password")
    return False

# this is the important function that uses some of the above helper functions.
def create_user(users):
    """
    Creates a new user account.
    """
    print("Please enter your first name, last name, and student ID, separated by a space")

    user_info = input().split()

    first_name = user_info[0]
    last_name = user_info[1]
    student_id = user_info[2]

    username = create_username(
        first_name,
        last_name,
        student_id
    )

    passwords_match = False

    while not passwords_match:

        print("Please enter password")
        password = input()

        print("Please reenter password:")
        password_check = input()

        if password == password_check:
            passwords_match = True
        else:
            print("Password did not match")

    save_new_user(
        first_name,
        last_name,
        username,
        password
    )

    users.append([
        first_name,
        last_name,
        username,
        password
    ])

    print("User created.")

    return users


def main():
    users = load_users()
    logged_in = False
    while not logged_in:

        print("Login or create a new user? Select L to login, select C to create new user.")

        choice = input()

        if choice.upper() == "L":
            logged_in = login(users)

        elif choice.upper() == "C":
            users = create_user(users)


if __name__ == "__main__":
    main()

