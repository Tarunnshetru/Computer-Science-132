#name:Tarun Nandihalli Shetru

UD_FILE = "UD.txt"
SI_FILE = "SI.txt"
CI_FILE = "CI.txt"


class Student:
    def __init__(self, username):
        self.__username = username
        self.__courses = []

    def getUsername(self):
        return self.__username

    def addCourse(self, courseName):
        if courseName not in self.__courses:
            self.__courses.append(courseName)

    def dropCourse(self, courseName):
        if courseName in self.__courses:
            self.__courses.remove(courseName)

    def getCourse(self):
        return self.__courses


class Course:
    def __init__(self, courseName):
        self.__courseName = courseName
        self.__students = []

    def getCourseName(self):
        return self.__courseName

    def addStudent(self, username):
        if username not in self.__students:
            self.__students.append(username)

    def dropStudent(self, username):
        if username in self.__students:
            self.__students.remove(username)

    def getStudents(self):
        return self.__students

    def getNumberOfStudents(self):
        return len(self.__students)


def make_file_if_missing(filename):
    try:
        file = open(filename, "r")
        file.close()
    except FileNotFoundError:
        file = open(filename, "w")
        file.close()


def load_users():
    make_file_if_missing(UD_FILE)

    users = {}

    file = open(UD_FILE, "r")
    for line in file:
        line = line.strip()

        if line != "":
            parts = line.split()

            if len(parts) >= 2:
                username = parts[0]
                password = parts[1]
                users[username] = password

    file.close()
    return users


def save_user(username, password):
    file = open(UD_FILE, "a")
    file.write(username + " " + password + "\n")
    file.close()


def generate_username(firstName, lastName, studentID):
    username = firstName[0].lower() + lastName[0:2].lower() + studentID[0:3]
    return username


def create_students_from_users(users):
    students = {}

    for username in users:
        students[username] = Student(username)

    return students


def create_courses():
    course_names = ["CS131", "CS132", "EE210", "EE310", "Math 320", "Math 220"]

    courses = {}

    for name in course_names:
        courses[name] = Course(name)

    return courses


def find_course_name(user_input, courses):
    user_input = user_input.strip().lower().replace(" ", "")

    for course_name in courses:
        clean_course_name = course_name.lower().replace(" ", "")

        if user_input == clean_course_name:
            return course_name

    return None


def load_student_info(students):
    make_file_if_missing(SI_FILE)

    file = open(SI_FILE, "r")

    for line in file:
        line = line.strip()

        if line != "":
            parts = line.split("|")

            if len(parts) == 2:
                username = parts[0]
                course_text = parts[1]

                if username in students:
                    if course_text != "":
                        courses = course_text.split(",")

                        for course in courses:
                            course = course.strip()

                            if course != "":
                                students[username].addCourse(course)

    file.close()


def load_course_info(courses):
    make_file_if_missing(CI_FILE)

    file = open(CI_FILE, "r")

    for line in file:
        line = line.strip()

        if line != "":
            parts = line.split("|")

            if len(parts) == 2:
                course_name = parts[0]
                student_text = parts[1]

                if course_name in courses:
                    if student_text != "":
                        students = student_text.split(",")

                        for student in students:
                            student = student.strip()

                            if student != "":
                                courses[course_name].addStudent(student)

    file.close()


def save_student_info(students):
    file = open(SI_FILE, "w")

    for username in students:
        course_list = students[username].getCourse()
        course_text = ",".join(course_list)
        file.write(username + "|" + course_text + "\n")

    file.close()


def save_course_info(courses):
    file = open(CI_FILE, "w")

    for course_name in courses:
        student_list = courses[course_name].getStudents()
        student_text = ",".join(student_list)
        file.write(course_name + "|" + student_text + "\n")

    file.close()


def sync_courses_from_students(students, courses):
    for course_name in courses:
        for student in list(courses[course_name].getStudents()):
            courses[course_name].dropStudent(student)

    for username in students:
        student_courses = students[username].getCourse()

        for course_name in student_courses:
            if course_name in courses:
                courses[course_name].addStudent(username)


def login_or_create_user(users, students):
    while True:
        print("Login or create a new user? (select l to login or select c to create new user.)")
        choice = input().strip().upper()

        if choice == "L":
            print("please enter your user name (and hit enter)")
            username = input().strip()

            if username not in users:
                print("Username is not found")
                continue

            print("Enter your password")
            password = input().strip()

            if users[username] == password:
                print("you are logged in.")

                if username not in students:
                    students[username] = Student(username)

                return username
            else:
                print("wrong password")
                continue

        elif choice == "C":
            print("Please enter your first name, last name, and student id")
            info = input().strip().split()

            if len(info) != 3:
                print("Invalid input")
                continue

            firstName = info[0]
            lastName = info[1]
            studentID = info[2]

            username = generate_username(firstName, lastName, studentID)

            print("Your generated username is:", username)

            if username in users:
                print("User already exists")
                continue

            print("Please enter password")
            password1 = input().strip()

            print("Please reenter password:")
            password2 = input().strip()

            if password1 != password2:
                print("Password did not match")
                continue

            users[username] = password1
            save_user(username, password1)

            students[username] = Student(username)

            print("New user created")
            continue

        else:
            continue


def show_menu():
    print("A: show all courses available")
    print("B: add a course")
    print("C: drop a course")
    print("D: show all my courses")
    print("E: exit")


def show_all_courses(courses):
    number = 1

    for course_name in courses:
        count = courses[course_name].getNumberOfStudents()
        print(str(number) + ". " + course_name + "     students number:" + str(count))
        number += 1


def add_course_for_student(username, students, courses):
    print("Enter course to add")
    course_input = input().strip()

    course_name = find_course_name(course_input, courses)

    if course_name is None:
        print("Course not found")
        return

    if course_name in students[username].getCourse():
        print("You are already enrolled in this course")
        return

    students[username].addCourse(course_name)
    courses[course_name].addStudent(username)

    print("Course added")


def drop_course_for_student(username, students, courses):
    print("Enter the course you want to drop")
    course_input = input().strip()

    course_name = find_course_name(course_input, courses)

    if course_name is None:
        print("Course not found")
        return

    if course_name not in students[username].getCourse():
        print("You are not enrolled in this course")
        return

    students[username].dropCourse(course_name)
    courses[course_name].dropStudent(username)

    print("Course dropped")


def show_my_courses(username, students):
    my_courses = students[username].getCourse()

    if len(my_courses) == 0:
        print("You are not enrolled in any courses")
    else:
        print("You are enrolled in:")

        for course in my_courses:
            print(course)


def course_management(username, students, courses):
    while True:
        show_menu()
        choice = input().strip().upper()

        if choice == "A":
            show_all_courses(courses)

        elif choice == "B":
            add_course_for_student(username, students, courses)

        elif choice == "C":
            drop_course_for_student(username, students, courses)

        elif choice == "D":
            show_my_courses(username, students)

        elif choice == "E":
            save_student_info(students)
            save_course_info(courses)
            print("Exit")
            break

        else:
            print("Invalid option")


def main():
    users = load_users()

    students = create_students_from_users(users)
    courses = create_courses()

    load_student_info(students)
    load_course_info(courses)

    sync_courses_from_students(students, courses)

    username = login_or_create_user(users, students)

    course_management(username, students, courses)


main()
