class student:
    def __init__(self, name, gpa, grade_level, student_id, email, password):
        self.name = name
        self.gpa = gpa
        self.grade_level = grade_level
        self.student_id = student_id
        self.email = email
        self.password = password
        self.course_selected = []
    

    class course:
        def __init__(self, subject, course_num, course_desc, sect, instructor):
            self.subject = subject
            self.course_num = course_num
            self.course_desc = course_desc
            self.sect = sect
            self.instructor = instructor 

        