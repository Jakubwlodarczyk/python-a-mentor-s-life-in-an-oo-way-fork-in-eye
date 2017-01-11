from person import Person
import csv

class Student(Person):

    def __init__(self, first_name, last_name, year_of_birth, gender, coffee, energy, knowledge, motivation, sweets):
        Person.__init__(self, first_name, last_name, year_of_birth, gender, coffee, energy)

        #Data validation for knowledge level
        try:
            self.knowledge = int(knowledge)
        except:
            raise ValueError('Knowledge level must be an integer value')

        #data validation fod motivation level
        try:
            self.motivation = int(motivation)
        except:
            raise ValueError('Motivation level must be an integer value')

        self.sweets = sweets

    def __str__(self):
        return "{} {}".format(self.first_name,  self.last_name)

    @classmethod
    def create_by_csv(cls, file_path):

        try:
            with open(file_path) as students_data:
                student_list = csv.reader(students_data, quotechar=",")
                list_of_students =[]
                for student in student_list:
                    students = Student(student[0], student[1], student[2], student[3], student[4], student[5], student[6], student[7], student[8])
                    list_of_students.append(students)
        except FileNotFoundError:
            print("\nOops! The file does not exist!")

        return list_of_students

    def remove_student():
        student_list = Student.create_by_csv('data/students.csv')
        print(student_list[0].energy)

list_of_student_objects = Student.create_by_csv('data/students.csv')
Student.remove_student()
