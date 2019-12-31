class student(object):
    def __init__(self, name, grade, teacher, school):
        self.name = name
        self.grade = grade
        self.teacher = teacher
        self.school = school
    
    def getName(self):
        return self.name
    
    def getGrade(self):
        return self.grade
    
    def getTeacher(self):
        return self.teacher

    def getSchool(self):
        return self.school

    def getHeader(self):
        return ('Name: ' + self.name + '\nGrade: ' + self.grade + '\nTeacher: ' + self.teacher + '\nSchool: ' + self.school + '\n\n')
