class Student:
    def _init_(self, name=None, age=None, grades=None):
        self.name = name
        self.age = age
        self.grades = grades

    def get_avvr_grades(self):
        if self.grades is None:
            return 0
        else:
            return sum(self.grades) / len(self.grades)


class Group:
    def _init_(self):
        self.student = []

    def add_student(self, student):
        self.students.append(student)

    def delete_student(self, student):
        self.student.remove(student)

    def avvr_grades(self):
        summ = 0
        for student in self.students:
            summ += student.get_avvr_grades()
        return summ / len(self.students)

    def print_students(self):
        for student in self.students:
            print(student.name)
