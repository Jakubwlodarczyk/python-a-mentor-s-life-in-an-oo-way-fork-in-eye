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

    def presentation():
        print('\npresentation')

    def call_up(self, mentor, student):
        #print('\ncall_up')
        
    def cofee():
        print('\ncofee')

    def private_mentoring():
        pass

    def checkpoing():
        print('\nheckpoing')

    #@staticmethod
    def choose_mentor():
        mentors_object_list = Mentor.create_by_csv('data/mentors.csv')
        counter = 1
        for mentor in mentors_object_list:
            print(str(counter) + ".", mentor.first_name, mentor.last_name, mentor.nickname)
            counter += 1
        choice = int(input("\nChoose mentor you want to play: "))
        print("You have chosen ", mentors_object_list[choice-1])
        return mentors_object_list[choice-1]
