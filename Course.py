from credentials import course
from Registrar import studentList
from Registrar import is_number

# Uses the class course in order to build up a list
c1 = course("ENG110", "EC-1", "College Writing 1", 1)
c2 = course("MATH141", 'MQR', "Calculus/Differentiation", 2)
c3 = course("MATH142", 'MQR', "Calculus/Integration", 3)
c4 = course("ASTR2", 'LPS', " General Astronomy", 4)
c5 = course("GEOL101", 'LPS', "Physical Geology", 5)
c6 = course("HIST101", 'WCGI', "Early Modern Europe", 6)
c7 = course("HIST103", 'USED', "American History", 7)
c8 = course("ARTH102", 'CE', "History of Western Art", 8)
c9 = course("ECON101", 'IS', "Intro. to Microeconomics", 9)

courses = [c1, c2, c3, c4, c5, c6, c7, c8, c9]


def course_register(email):
    for student in studentList:
        if email == student.email:
            for x in courses: #x is every object in the list 'courses'
                print(f"{x.value}. {x.course_id}, {x.course_name}, {x.category}")
            selection = input("\n\nEnter the class you want to register: ")
            if not is_number(selection):
                print("\n\n **This is not a valid option. Try Again!** \n \n")
                continue
            selection = float(selection)
            if overlap(selection, student):
                print(
                    "ERROR: You have already registered this course. Please try again \n\n")  # This checks if the student already signed up for the same course
                break  # leaves this menu if the overlap statement is true
            for x in courses: #x is every object in the list 'courses'
                if selection == x.value:
                    student.course_id.append(x.course_id)
                    student.value.append(x.value)  # This is used as a parameter to see if courses overlap
                    print("Successful")


# Allows the student to see the courses they have registered for
def view_courses(email):
    print("Registered Courses: ")
    for student in studentList:
        if email == student.email:
            for value in student.course_id:
                for course in courses:
                    if value == course.course_id:
                        print(f"{course.course_id}     {course.course_name}     |{course.category}|")
    print("\n\n")


# Allows students to remove a course
def delete_course(email):
    while True:
        view_courses(email)
        selection = input("Would you like to drop a class(y/n): ")
        if selection.lower() == "y":
            user = input("Enter the class you would like to drop(ex:ENG110, MATH141, etc): ")
            for student in studentList:
                if email == student.email:
                    for value in student.course_id:
                        if user.lower() == value.lower():
                            student.course_id.remove(value)
                            print("Class Successfully Removed")

        elif selection.lower() == "n":
            break
        else:
            print("Invalid option")
            continue


# Verifies if the selection is the same as the value the student already registered for
def overlap(selection, student):
    for value in student.value:
        if selection == value:
            return True
        else:
            return False
