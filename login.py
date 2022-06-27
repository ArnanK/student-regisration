from Registrar import student_email, studentList, is_number
from Course import course_register, delete_course, view_student_course

def login(email, password):
    for student in studentList:
        if email == student.email and password == student.password:
            print(f"Welcome {student.name}!")
            return True

def student_option():
    while True:
        print("Student Login Center\n(Your password is set as your ID| You can change your password later)\n(To return back, type 'exit')")
        email = input("Enter your student email: ")
        if email.lower() == "exit":
            break
        password = input("Enter your password: ")
        if login(email, password):
            while True:
                print("  1.Register Courses\n  2.View Courses\n  3.Delete Course\n  4.Change Password\n  5.Exit")
                student_input = input("User: ")
                if not is_number(student_input):
                    print("\n\n **This is not a valid option. Try Again!** \n \n")
                    continue
                student_input = float(student_input)
                if student_input == 1:
                    course_register(email)
                elif student_input == 2:
                    view_student_course(email)
                elif student_input == 3:
                    delete_course(email)
                elif student_input == 4:
                    change_password(password, email)
                elif student_input == 5:
                    break

def change_password(password, email):
    if verification(password):
        for student in studentList:
            if email == student.email:
                if password == student.password:
                    password = input("Enter your new password: ")
                    student.password = password

def verification(password):
    old_pass = input("Verify your old password: ")
    if old_pass == password:
        print("Successful")
        return True
    else:
        print("Incorrect password")
        return False

