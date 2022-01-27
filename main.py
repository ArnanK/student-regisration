from Registrar import registrar_option, is_number
from login import student_option


if __name__ == "__main__":
    while True:
        initiation = input("Welcome to the academic initiation. Choose an option \n   1. Registrar account\n   2. Student account\n   3.Exit\nUser: ")
        if not is_number(initiation):
            print("\n\n **This is not a valid option. Try Again!** \n \n")
            continue
        initiation = float(initiation)
        if initiation == 1:
            registrar_option()
        elif initiation == 2:
            student_option()
        elif initiation == 3:
            exit()
