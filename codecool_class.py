from mentor import Mentor
from student import Student
# from story import choose_student
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



    # def presentation(self):



    #     chosen_student = CodecoolClass.choose_student()

    #     if chosen_student.motivation < 60:
    #         chosen_student.energy -= 10
    #         print("Student's energy has been decreased by 10 because his motivation is low :(\n")
    #     else:
    #         chosen_student.knowledge += 15
    #         print("Student's knowledge has been increased by 15!\n")



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
        return student_array[choosen - 1]

    def choose_mentor():
        mentors_object_list = Mentor.create_by_csv('data/mentors.csv')
        counter = 1
        for mentor in mentors_object_list:
            print(str(counter) + ".", mentor.first_name, mentor.last_name, mentor.nickname)
            counter += 1
        choice = int(input("\nChoose mentor you want to play: "))
        print("You have chosen ", mentors_object_list[choice - 1])
        return mentors_object_list[choice - 1]


    def call_up(mentor, student):
        '''Function operates on student's motivation, knowledge, energy level
           and on mentor's irritation level changing their values'''

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


    def private_mentoring(self):
        os.system('clear')
        mentor = CodecoolClass.choose_mentor()
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


    def checkpoint():
        print('\nCheckpoint time!')
        os.system('clear')
        mentor = CodecoolClass.choose_mentor()
        student = CodecoolClass.choose_student()
        time.sleep(2)
        print('\nCheckpoint starts!\n', mentor, ' vs ', student, '!')
        time.sleep(2)
        irritation_level = int(mentor.irritation)
        knowledge_level = int(student.knowledge)
        motivation_level = int(student.motivation)
        print("Mentor's irritation level is: ", irritation_level)
        print("Student's knowledge level is: ", knowledge_level)
        print("Student's motivation level is: ", motivation_level)
        time.sleep(2)
        if irritation_level >= 60:
            print('\nYou have 3min to build a game <battleship>!\nWithout an internet connection.\n')
            if knowledge < 80 and motivation < 80:
                print('Your score is: RED CARD')
            elif knowledge < 80 and motivation > 80:
                print('Your score is: YELLOW CARD')
            else:
                print('Victory! Your score is: GREEN CARD!')
        elif irritation_level >= 20:
            print('\nIt is your lucky day!\nWhat is a string?')
            if knowledge > 30 and motivation > 20:
                print('Congrats! You are so smart and so motivated! Your score is: GREEN CARD!')
            elif knowledge < 20 and motivation < 10:
                print('Your score is: RED CARD!')
            else:
                print('Keep going! Your score is: YELLOW CARD.')


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



    def is_int(value):
        try:
            int(value)
            return True
        except:
            return False
