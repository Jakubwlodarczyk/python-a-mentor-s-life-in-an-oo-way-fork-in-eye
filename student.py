from person import Person
import csv

class Student(Person):

    def __init__(self, first_name, last_name, year_of_birth, gender, coffee, energy, knowledge, motivation, sweets):
        Person.__init__(self, first_name, last_name, year_of_birth, gender, coffee, energy)
        try:
            self.knowledge = int(knowledge)
        raise ValueError('Knowledge level must be an integer value')

        try:
            self.motivation = int(motivation)
        raise ValueError('Motivation level must be an integer value')

        self.sweets = sweets

    @classmethod
    def create_by_csv(cls, file_path):

        try:
            with open('data/students.csv') as students_data:
                student_list = csv.reader(students_data, quotechar=",")
                list_of_students =[]
                for student in student_list:
                    students = Student(student[0], student[1], student[2], student[3], student[4], student[5], student[6], student[7], student[8])
                    list_of_students.append(students)
        except FileNotFoundError:
            print("\nOops! The file does not exist!")
        
        return list_of_students


Student.create_by_csv('data/students.csv')
