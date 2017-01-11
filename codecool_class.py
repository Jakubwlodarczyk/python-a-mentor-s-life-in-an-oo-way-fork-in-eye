from mentor import Mentor
from student import Student
import csv


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

    def find_student_by_full_name(self):
        full_name_student_not_list = input("Type a student: ")
        full_name_student = full_name_student_not_list.split()
        remember = "me"
        for student in self.students:
            if student.first_name == full_name_student[0] and student.last_name == full_name_student[1]:
                remember = student
        return remember

    def find_mentor_by_full_name(self):
        full_name_mentor_not_list = input("Type a mentor: ")
        full_name_mentor = full_name_mentor_not_list.split()
        remember = "me"
        for mentor in self.mentors:
            if mentor.first_name == full_name_mentor[0] and mentor.last_name == full_name_mentor[1]:
                remember = mentor
        return remember

    def presentation(self):
        for student in Student.create_by_csv('data/students.csv'):
                remember = student.knowledge
                student.knowledge = student.knowledge + int((self.engagement/100)) + int(int((self.engagement/100)*(student.motivation/4))) + int(student.energy/6)
                end_student_knowledge = student.knowledge - remember
                print("Student {} knowledge has been increased by {}.".format(student.first_name, end_student_knowledge) )

    def choose_student():
        student_array = Student.create_by_csv('data/students.csv')
        number = 1
        for student in student_array:
            print(number, student.first_name)
            number += 1
        choosen = input("Choose student: ")
        choosen = int(choosen)
        choosen_student = student_array[choosen-1]
        return choosen_student

    def call_up():
        print('\ncall_up')

    def call_up(self, mentor, student):
        #print('\ncall_up')
        pass

    def cofee():
        print('\ncofee')

    def private_mentoring():
        pass

    def checkpoing():
        print('\nheckpoing')
