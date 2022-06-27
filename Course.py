from credentials import student
from Registrar import studentList, is_number
import pandas as pd

#This is to create a filtered array of all the subjects that are available - accessible for course registeration
def subject_array():
    df = pd.read_csv('Grade Distribution 2012-2022 Queens College - f2019.csv')
    subjects = []
    for index, rows in df.iterrows():
        i = df.iloc[index, df.columns.get_loc('Subject')]
        subjects.append(i)
    return(remove_duplicates(subjects))

#This function removes the duplicates in the subjects to ensure that the user only has accessible options
def remove_duplicates(list):
    noduplist = []
    for element in list:
        if element not in noduplist:
            noduplist.append(element)
    return noduplist

#This checks if the subject you entered if valid 
def subject_checker(sub_array, usr_sub):
    if usr_sub not in sub_array:
        print("The subject you entered in not valid!")
        return False
    else:
        return True

#This allows you to view all the courses that allign with the subject you choose
#Ask the user for subject you want to select
def filter_subject(sub_select):
    
    df = pd.read_csv('Grade Distribution 2012-2022 Queens College - f2019.csv')
    sub_select = sub_select.upper()
    for subject in subject_array():
        if sub_select == subject:
            df = df.loc[df['Subject'] == sub_select]    
    df = df.reset_index()
    return df

#This gives you an array of all the catalog numbers for the subjects you filter
def view_cat_nbr(df):
    courses_num = []
    for index, row in df.iterrows():
        i = df.iloc[index, df.columns.get_loc('Catalog Nbr')]
        courses_num.append(i)
    return(remove_duplicates(courses_num))

#This updates the data frame to output only the subject and catalog number the user chooses
#Ask the user for usr_cat_nbr
def view_course(view_cat_nbr,usr_cat_nbr, df): #for df, pass in filter_subject
    usr_cat_nbr = str(usr_cat_nbr)
    usr_cat_nbr = usr_cat_nbr.upper()
    for num in view_cat_nbr:
        if usr_cat_nbr == num:
            df = df.loc[df['Catalog Nbr'] == usr_cat_nbr]
    df = df[['Class Section','Subject', 'Catalog Nbr', 'Crs Descr', 'Instructor']]
    df = df.reset_index()
    df = df.drop(columns = ['index'])
    df = df.sort_values('Class Section')

    return df

#This function takes in a section number the user inputs based on the filtered df based on catalog numbers.
#Returns an object of all the data in the df which is in the 'course' class. 
#Prompt: use this data to add to the array of .courses in the 'student' class. 
def select_course(num_c, input_subject, cat_nbr):
    df = view_course(view_cat_nbr(filter_subject(input_subject)), cat_nbr, filter_subject(input_subject))
    num_c = str(num_c)
    num_c = num_c.upper()
    
    df = df.loc[df['Class Section'] == num_c]
    subject = df.iloc[0, df.columns.get_loc('Subject')]   
    course_num = df.iloc[0, df.columns.get_loc('Catalog Nbr')]
    course_desc = df.iloc[0, df.columns.get_loc('Crs Descr')]
    sect = df.iloc[0, df.columns.get_loc('Class Section')]
    instructor = df.iloc[0, df.columns.get_loc('Instructor')]

    c = student.course(subject, course_num, course_desc, sect, instructor)
    return c
    
    

#Returns a boolean value to make sure the usr option is included in the filtered array.
#Pass in view_coures data frame into df.
def available_option(df, usr_inp):
    avl_sections = []
    status = False
    usr_inp = str(usr_inp)
    for index, row in df.iterrows():
        i = df.iloc[index, df.columns.get_loc('Class Section')]
        avl_sections.append(i)
    
    for section in avl_sections:
        section = str(section)
        if usr_inp == section:
            status = True
    return status

#This functions makes sure that the user selected option is an available option within the array of options. 
def check_cat_num(all_cat_nbr, usr_cat_num):
    if usr_cat_num not in all_cat_nbr:
        print("**Catalog Number not valid!\n")
        return False
    else:
        return True

#for df, pass in all_courses/view_courses()
def overlap(email, df, usr):
    usr = str(usr)
    status = False
    usr_selected_course = df.loc[df['Class Section'] == usr] 
    for x in studentList:
        if email == x.email:
            for course in x.course_selected:
                if course.subject == usr_selected_course.iloc[0, df.columns.get_loc('Subject')] and course.course_num == usr_selected_course.iloc[0, df.columns.get_loc('Catalog Nbr')] and course.instructor == usr_selected_course.iloc[0, df.columns.get_loc('Instructor')]:
                    status = True
            return status
            

def course_register(email):
    for x in studentList:
        if email == x.email: #This makes sure that there are changes to your account                    
            #This prints all available subjects
            print("Available Subjects:\n")
            for subject in subject_array():
                print(f"-{subject}\n")
            #USR INP
            sub_select = input("Enter the subject you want to register for:")
            sub_select = sub_select.upper()
            #Makes sure the usr enters a valid inp, if not, breaks from program
            if not subject_checker(subject_array(), sub_select):
                break

            filtered_df = filter_subject(sub_select) #Stores all the subjects into one array
            print("Available Catalog Numbers: ")
            all_cat_nums = view_cat_nbr(filtered_df)
            for cat_num in all_cat_nums:
                print(f"-{cat_num}\n")
            usr_cat_num = input("Select a Catalog Number: ")
            usr_cat_num = str(usr_cat_num).upper()
            if not check_cat_num(all_cat_nums, usr_cat_num):
                break

            #This displays all the courses that are available
            all_courses = view_course(all_cat_nums, usr_cat_num, filtered_df)
            print(all_courses)
            usr_inp = input("Select the section number for the class you want to register for: ")
            usr_inp = str(usr_inp).upper()
            if not available_option(all_courses, usr_inp):
                print("**Section Number Not Valid!\n")
                break
            #This checks overlap
            if overlap(email, all_courses, usr_inp):
                print("**You already registered for this course")
                break

            c = select_course(usr_inp, sub_select, usr_cat_num)

            x.course_selected.append(c)
            


def view_student_course(email):
    for x in studentList:
        if email == x.email:
            print("No\tSection\tSubject\tCatalog Number\tCourse Name\tInstructor")
            counter = 1
            for course in x.course_selected:
                print(f"{counter}\t{course.sect}\t{course.subject}\t{course.course_num}\t{course.course_desc}\t{course.instructor}")
                counter = counter + 1
    

def delete_course(email):
    for x in studentList:
        if email == x.email:
            view_student_course(email)
            usr = input("\nEnter the No. for the course you want to remove: ")
            
            if is_number(usr):
                index = 1
                usr = int(usr)
                for course in x.course_selected:
                    if usr == index:
                        #delete course
                        x.course_selected.remove(course)
                    index = index + 1
            else:
                print("Invalid Option!\n")

            
                            




