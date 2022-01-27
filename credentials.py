class student:
    def __init__(self, name, gpa, grade_level, student_id, email, password):
        self.name = name
        self.gpa = gpa
        self.grade_level = grade_level
        self.student_id = student_id
        self.email = email
        self.password = password
        self.course_id = []
        self.value = []



class course:
    def __init__(self, course_id, category, course_name, value):
        self.course_id = course_id
        self.category = category
        self.course_name = course_name
        self.value = value
