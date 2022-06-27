from credentials import student
import uuid

studentList = []
dictionary = {
    1: "Freshmen",
    2: "Sophomore",
    3: "Junior",
    4: "Senior"
}


def add_user(name, gpa, grade_level, student_id, email, password):
    new_students = student(name, gpa, grade_level, student_id, email, password)
    studentList.append(new_students)


def remove_user(num):
    for student in studentList:
        if student.student_id == num:
            studentList.remove(student)


def view_user():
    print("\n")
    print("Registered students: ")
    print("Name\tGPA\tGrade Level\tID\tEmail")
    for student in studentList:
        print(f"{student.name}\t{student.gpa}\t{student.grade_level}\t{student.student_id}\t{student.email}\n")
    print("\n")


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


# Ensures that the value is in between 1 and 5
def range_num(input):
    input = int(input)
    if input > 0 and input < 5:
        return True
    else:
        return False


# Makes sure the value is numerical
def gpa_checker(gpa):
    while not is_number(gpa):
        print("\n\nThe value must be numeric (ex: 3.8, 2.0, 4, etc)\n\n")
        gpa = input("What is the gpa of the student: ")
    return gpa


# Checks if you correctly chose one of the four values
def level_checker(grade_level):
    while not is_number(grade_level):
        print("This option is not valid. Make sure the value is a number (1,2,3 or 4)")
        grade_level = input("Which grade level is the student currently in (1,2,3 or 4): ")
    grade_level = int(grade_level)
    while not range_num(grade_level):
        grade_level = input("Make sure you pick one of the four options (1,2,3, or 4): ")
    grade_level = int(grade_level)
    return grade_level


def student_email(name, student_id):
    email = f"{name}{student_id[:4]}@schools.acc.edu"
    return email


# Add student
def option_one(user_input):
    user_input = int(user_input)
    if user_input == 1:
        print("\nThere are 3 requirements that must be completed to register the student:")
        name = input("What is the name of the student: ")
        gpa = input("What is the gpa of the student: ")
        gpa = gpa_checker(gpa)
        print("Grade Levels: \n     1.Freshmen\n     2.Sophomore\n     3.Junior\n     4.Senior")
        grade_level = input("Which grade level is the student currently in (1,2,3 or 4): ")
        level = level_checker(grade_level)
        grade = dictionary.get(level, "Unavailable")
        student_id = uuid.uuid4().hex[:8]
        password = student_id
        email = student_email(name, student_id)
        add_user(name, gpa, grade, student_id, email, password)


# Remove student
def option_two(user_input):
    user_input = int(user_input)
    if user_input == 2:
        view_user()
        x = input("\nTo remove a student from the database, enter the student ID: ")
        remove_user(x)


# View student
def option_three(user_input):
    user_input = int(user_input)
    if user_input == 3:
        view_user()


# Allows the user to go into this interface
def registrar_option():
    while True:
        user_input = input(
            "Welcome to the Student Registrar (1,2,3 or 4). \n 1. Would you like to register a student?\n 2. Would you like to remove a student?\n 3. Would you like to view the students registered?\n 4. Exit\nUser: ")
        if not is_number(user_input):
            print("\n\n **This is not a valid option. Try Again!** \n \n")
            continue
        user_input = float(user_input)
        option_one(user_input)
        option_two(user_input)
        option_three(user_input)
        if user_input == 4:
            break
