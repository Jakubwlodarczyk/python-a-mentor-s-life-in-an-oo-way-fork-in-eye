from person import Person
import csv


class Student(Person):

    def __init__(self, first_name, last_name, year_of_birth, gender, coffee, energy, knowledge, motivation, sweets):
        Person.__init__(self, first_name, last_name, year_of_birth, gender, coffee, energy)

        # Data validation for knowledge level
        try:
            self.knowledge = int(knowledge)
        except:
            raise ValueError('Knowledge level must be an integer value')

        # data validation fod motivation level
        try:
            self.motivation = int(motivation)
        except:
            raise ValueError('Motivation level must be an integer value')

        self.sweets = int(sweets)

    def __str__(self):
        return "{}{}".format(self.first_name,  self.last_name)

    @classmethod
    def create_by_csv(cls, file_path):

        try:
            with open(file_path) as students_data:
                student_list = csv.reader(students_data, quotechar=",")
                list_of_students = []
                for student in student_list:
                    students = Student(student[0], student[1], student[2], student[3],
                                       student[4], student[5], student[6], student[7], student[8])
                    list_of_students.append(students)
        except FileNotFoundError:
            print("\nOops! The file does not exist!")

        return list_of_students

    def students_list():

        students = Student.create_by_csv('data/students.csv')

        students_list = []
        for student in students:
            students_list.append([student.first_name, student.last_name, student.year_of_birth,
                                  student.gender, student.coffee, student.energy, student.knowledge,
                                  student.motivation, student.sweets])
        return students_list

    @staticmethod
    def student_table():

        students_list = Student.converter()
        # Student.converter()
        title_list = ['| First_name | Last_name    | Birth |  Gender  | Coffee   | Energy | Knowledge | Motivation| Sweets']

        print(''.join(title_list))
        for students in students_list:
            print('|', students[0], ' ' * (9 - len(students[0])), '|', students[1], ' ' * (11 - len(students[1])),
                  '|', students[2], ' ' * (4 - len(str(students[2]))), '|', students[3], ' ' * (7 - len(students[3])),
                  '|', students[4], ' ' * (7 - len(students[4])), '|', students[5], ' ' * (5 - len(str(students[5]))),
                  '|', students[6], ' ' * (8 - len(str(students[6]))), '|', students[7], ' ' *
                  (8 - len(str(students[7]))),
                  '|', students[8], ' ' * (11 - len(str(students[8]))))
        print('')
        return students_list

    def converter():

        students_list = Student.students_list()
        for item in students_list:
            if " True" in item:
                for i in item:
                    if i == ' True':
                        item[item.index(' True')] = 'Like'
                    elif i == ' False':
                        item[item.index(' False')] = 'Dislike'
            for i in item:
                if i == ' False':
                    item[item.index(' False')] = 'Dislike'
        return students_list
