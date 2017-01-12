from mentor import Mentor
from student import Student
import csv
import os
import time


class CodecoolClass:

    def __init__(self, location, year, mentors, students):
        self.location = location
        self.year = year
        self.mentors = mentors
        self.students = students

    def create_local_school():
        mentors = Mentor.create_by_csv('data/mentors.csv')
        students = Student.create_by_csv('data/students.csv')
        codecool_class = CodecoolClass("Krakow", 2016, mentors, students)
        return codecool_class

    @staticmethod
    def find_student_by_full_name(students_object_list, full_name):
        full_name_student = full_name.split()
        checker = 0
        remember = "me"
        for student in students_object_list:
            if student.first_name == full_name_student[0] and student.last_name[1:] == full_name_student[1]:
                checker = 1
                remember = student
        if checker == 1:
            print("Student has been found in school.")
            return remember
        else:
            print("Student has not been found.")

    @staticmethod
    def find_mentor_by_full_name(mentors_object_list, full_name):
        full_name_mentor = full_name.split()
        checker = 0
        remember = "me"
        for mentor in mentors_object_list:
            if mentor.first_name == full_name_mentor[0] and mentor.last_name[1:] == full_name_mentor[1]:
                checker = 1
                remember = mentor
        if checker == 1:
            print("Mentor has been found in school.")
            return remember
        else:
            print("Mentor has not been found.")

    def presentation(self):
        for student in Student.create_by_csv('data/students.csv'):
                remember = student.knowledge
                student.knowledge = student.knowledge + int((self.engagement/100)) + int(int((self.engagement/100)*(student.motivation/4))) + int(student.energy/6)
                end_student_knowledge = student.knowledge - remember
                print("Student {} knowledge has been increased by {}.".format(student.first_name, end_student_knowledge) )

    def call_up():
        print('\ncall_up')

    def call_up(self, mentor, student):
        #print('\ncall_up')
        pass

    def cofee():
        print('\ncofee')

    def private_mentoring(mentor):
        os.system('clear')
        if mentor.engagement < 20:
            print(mentor.first_name, 'have too low engagement to conduct lessons! :()')
            time.sleep(4)
        else:
            os.system('clear')
            print('You have to choose student for private mentoring from list below:')
            choosen_student = CodecoolClass.choose_student()
            upgraded_knowledge = choosen_student.knowledge + 50
            os.system('clear')
            print(choosen_student.first_name,
                  'knowledge has incrased from {} to {}!!! Good job!!!'
                  .format(choosen_student.knowledge, upgraded_knowledge))
            time.sleep(4)
            choosen_student.knowledge += 50

    def choose_student():
        student_array = Student.create_by_csv('data/students.csv')
        number = 1
        for student in student_array:
            print(number, student.first_name)
            number += 1
        while True:
            try:
                choosen = int(input("Choose a student: "))
                if choosen > 0 and choosen <= len(student_array):
                    print("You have chosen ", student_array[choosen - 1])
                    return student_array[choosen - 1]
                else:
                    print("Type correct number...\n")
                    continue
            except:
                print("Type an integer...\n")

    def checkpoing():
        print('\nheckpoing')

    def is_int(value):
        try:
            int(value)
            return True
        except:
            return False
