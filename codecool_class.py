from mentor import Mentor
from student import Student
# from story import choose_student
import csv
import os



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

    


    
        

    def call_up(self, mentor, student):
        #print('\ncall_up')
        print('\ncall_up')

    def coffee(self):

        
        os.system('clear')
        print('Students want to drink coffee, but the work is not done yet. \nYou can allow only one student to go kitchen room. Choose one from the list:\n')
        # for n,student in enumerate(self.students):
        #     print('{} {}{}'.format(n+1, student.first_name, student.last_name))
        chosen_student = CodecoolClass.choose_student()
        # print(chosen_student.energy)
        student = []
        student.extend([chosen_student.first_name, chosen_student.last_name, chosen_student.coffee])
        if student[2] == ' True':            
            chosen_student.energy += 10
            print("%s's energy has increased by 10.\n" % student[0])
        else:
            print("%s don't drink coffee" % student[0])
        if chosen_student.energy >= 100:
            print('Student is having heart attack and cannot attend classes')
            

    def private_mentoring():
        pass

    def checkpoing():
        print('\nheckpoing')

