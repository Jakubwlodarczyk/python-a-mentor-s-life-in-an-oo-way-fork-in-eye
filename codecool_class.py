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
        #print('\npresentation')
        chosen_student = CodecoolClass.choose_student()
        if chosen_student.motivation < 60:
            chosen_student.energy -= 10
            print("Student's energy has been decreased by 10 because his motivation is low :(\n")
        else:
            chosen_student.knowledge += 15
            print("Student's knowledge has been increased by 15!\n")


    def call_up(mentor, student):

        if mentor.sweets == 1:
            print('{} has some sweets to encourage {}'.format(mentor.first_name, student.first_name))
            if student.sweets == 1:
                print('{} likes sweets and is indeed encouraged'.format(student.first_name))
                student.motivation += 10
                print("{}'s motivation increases by 10 thanks to sweets! Motivation is now {}".format(student.first_name, student.motivation))
                student.knowledge += 10
                print("Thanks to being by the board {}'s knowledge increases by 10 and is now {}".format(student.first_name, student.knowledge))
                print("But thinking is soo exhausting. {}'s energy drops by 5 and is now {}.".format(student.first_name, student.energy))

            else:
                print("{} doesn't like sweets anyway. The motivation has not change then and is now {}".format(student.first_name, student.motivation))
                student.knowledge+= 10
                print("{} decided to go by the board anyway. {}'s knowledge increases by 10 and is now {}".format(student.first_name, student.first_name, student.knowledge))

        else:
            print("Oops, looks like {} doesn't have any sweets to encourage students...".format(mentor.first_name))
            print("Let's see if that is a deal breaker.")
            print("{}'s motivation is now {}.".format(student.first_name, student.motivation))

            if student.motivation < 50:
                print("Well, looks like {} doesn't feel like going to the board. Bummer.".format(student.first_name))
                mentor.irritation+= 10
                print("O-oh, student insubordination is annoying... {}'s irritation drops by 10 and is now {}".format(mentor.first_name, mentor.irritation))
            else:
                student.knowledge+= 10
                print("{} decided to go by the board anyway. {}'s knowledge increases by 10 and is now {}".format(student.first_name, student.first_name, student.knowledge))


    def cofee():
        print('\ncofee')

    def private_mentoring():
        pass

    def checkpoing():
        print('\nheckpoing')
