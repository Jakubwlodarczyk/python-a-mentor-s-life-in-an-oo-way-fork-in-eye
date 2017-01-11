from mentor import Mentor
from student import Student
import csv


class CodecoolClass:

    def __init__(self, location, year, mentors, students):
        self.location = location
        self.year = year
        self.mentors = mentors
        self.students = students

    def create_local_school(self):
        self.mentors = funkcja_Iki()
        self.students = funkcja_Ani()
        codecool_class = CodecoolClass("Krakow", 2016, funkcja_Iki(), funkcja_Ani())
        return codecool_class

    def find_student_by_full_name(self):
        full_name_student = input("Type a student: ")
        remember = "me"
        for student in self.students:
            if student.first_name == full_name_student[0] and student.last_name == full_name_student[1]:
                remember = student
        return remember

    def find_mentor_by_full_name(self):
        full_name_mentor = input("Type a mentor: ")
        remember = "me"
        for mentor in self.mentors:
            if mentor.first_name == full_name_mentor[0] and mentor.last_name == full_name_mentor[1]:
                remember = mentor
        return remember

    def presentation():
        print('\npresentation')

    def call_up():
        print('\ncall_up')

    def cofee():
        print('\ncofee')

    def private_mentoring():
        pass

    def checkpoing():
        print('\nheckpoing')
