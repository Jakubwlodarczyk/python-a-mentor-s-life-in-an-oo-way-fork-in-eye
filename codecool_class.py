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

    @staticmethod
    def create_local_school():
        '''
        Creates a CodecoolClass object having some real-life data from the implementer students' real class
        '''
        mentors = Mentor.create_by_csv('data/mentors.csv')
        students = Student.create_by_csv('data/students.csv')
        codecool_class = CodecoolClass("Krakow", 2016, mentors, students)
        return codecool_class

    @staticmethod
    def find_student_by_full_name(self, full_name):
        '''
        Gives back a student with the same full name as the argument from students.
        '''

        full_name_student = full_name.split()  # create list of words from input
        checker = 0  # if 1, student has been found
        remember = "me"  # create a remember variable (will return student if found)

        if len(full_name_student) == 1:
            print("Student has not been found.")
            return None
        for student in self.students:
            if student.first_name == full_name_student[0] and student.last_name[1:] == full_name_student[1]:
                #  compares name and surename of student
                checker = 1
                remember = student
        if checker == 1:
            print("Student has been found in school.")
            return remember
        else:
            print("Student has not been found.")

    @staticmethod
    def find_mentor_by_full_name(mentors_object_list, full_name):
        '''
        Gives back a mentor with the same full name as the argument from mentors.
        '''
        full_name_mentor = full_name.split()
        checker = 0
        remember = "me"
        if len(full_name_mentor) == 1:
            print("Mentor has not been found.")
            return None
        for mentor in mentors_object_list:
            if mentor.first_name == full_name_mentor[0] and mentor.last_name[1:] == full_name_mentor[1]:
                checker = 1
                remember = mentor
        if checker == 1:
            print("Mentor has been found in school.")
            return remember
        else:
            print("Mentor has not been found.")

    def presentation(self, mentor):
        '''
        Operates on list of students objects and mentor object
        by increasing or decreasing motivation, energy, knowledge and engagement level values.
        '''
        os.system('clear')
        print("{}'s mentor engagement is on level {}, so:\n".format(mentor.first_name, mentor.engagement))
        time.sleep(2)
        for student in self.students:
            remember = student.knowledge
            remember2 = student.knowledge
            student.knowledge = student.knowledge + \
                int((mentor.engagement / 100)) + int(int((mentor.engagement / 100) #  equation describes how student knowledge increases
                                                         * (student.motivation / 4))) + int(student.energy / 6)
            end_student_knowledge = student.knowledge - remember
            print("Student {} knowledge has been increased by {}. (was {}, now {})".format(student.first_name, end_student_knowledge, remember2, student.knowledge))
            time.sleep(1)
        print("\nNice!")

    def call_up(self, mentor, student):
        '''
        Function operates on student's motivation, knowledge, energy level
        and on mentor's irritation level changing their values.
        '''
        os.system('clear')
        if mentor.sweets == 1:
            print('YAY! {} has some sweets to encourage {}!'.format(mentor.first_name, student.first_name))
            time.sleep(3)
            if student.sweets == 1:
                print('{} likes sweets and is indeed encouraged.'.format(student.first_name))
                student.motivation += 10
                time.sleep(2)
                print("{}'s motivation increases by 10 thanks to sweets! Motivation is now {}.".format(
                    student.first_name, student.motivation))
                student.knowledge += 10
                time.sleep(2)
                print("Thanks to being by the board {}'s knowledge increases by 10 and is now {}.".format(
                    student.first_name, student.knowledge))
                student.energy -= 2
                time.sleep(2)
                print("But thinking is soo exhausting. {}'s energy drops by 5 and is now {}.".format(
                    student.first_name, student.energy))

            else:
                print("{} doesn't like sweets anyway. The motivation has not change then and is now {}.".format(
                    student.first_name, student.motivation))
                time.sleep(2)
                student.knowledge += 10
                print("{} decided to go by the board anyway. {}'s knowledge increases by 10 and is now {}.".format(
                    student.first_name, student.first_name, student.knowledge))

        else:
            print("Oops, looks like {} doesn't have any sweets to encourage students...".format(mentor.first_name))
            time.sleep(3)
            print("Let's see if that is a deal breaker.")
            time.sleep(2)
            print("{}'s motivation is now {}.".format(student.first_name, student.motivation))

            if student.motivation < 50:
                print("Well, looks like {} doesn't feel like going to the board. Bummer.".format(student.first_name))
                mentor.irritation += 10
                time.sleep(2)
                print("O-oh, student insubordination is annoying... {}'s irritation drops by 10 and is now {}.".format(mentor.first_name, mentor.irritation))
            else:
                student.knowledge += 10
                time.sleep(2)
                print("{} decided to go by the board anyway. {}'s knowledge increases by 10 and is now {}.".format(
                    student.first_name, student.first_name, student.knowledge))


    def drink_coffee(self, chosen_student):


        '''
        Operates on student object by increasing energy values.
        '''

        os.system('clear')
        print('Students want to drink coffee, but the work is not done yet. \nYou can allow only one student to go kitchen room. Choose one from the list:\n')
        student = []
        student.extend([chosen_student.first_name, chosen_student.last_name, chosen_student.coffee, chosen_student.energy, chosen_student.motivation])
        time.sleep(1)
        if student[2] == ' True':
            chosen_student.energy += 10
            chosen_student.motivation += 10

            print('.')
            time.sleep(0.5)
            print('.')
            time.sleep(1)
            print("{}'s mood increased. Now energy = {}, motivation = {}".format(student[0], chosen_student.energy, chosen_student.motivation))
            time.sleep(1)
            print("Good.")

        else:
            print("%s don't drink coffee" % student[0])
        if chosen_student.energy >= 100:
            print('Student is having heart attack and cannot attend classes')

    def private_mentoring(self, mentor, student):
        '''
        Operates on student and mentor objects by increasing or decreasing knowledge
        '''
        os.system('clear')
        print('Checking if {} have enought engagement to conduct lessons...'.format(mentor.first_name))
        time.sleep(2)
        if mentor.engagement < 35:
            print('\n')
            print(mentor.first_name, 'have too low engagement!! Today will be no private mentoring...')
            time.sleep(4)
        else:
            print('\nYes! Prepare for "face to face" mentoring!')
            print('.')
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('.')
            time.sleep(1)
            old_knowledge = student.knowledge
            new_knowledge = int(old_knowledge) + 50
            print(student.first_name,
                  'knowledge has incrased from {} to {}!!! Good job!!!'
                  .format(old_knowledge, new_knowledge))
            time.sleep(3)
            student.knowledge += 50

    def checkpoint(self, mentor, student):

        '''
        Operates on student and mentor objects.
        Checks mentor's irritation level and student's energy and motivation level.
        '''
        os.system('clear')
        print('\nCheckpoint time!')
        time.sleep(2)
        print('\nCheckpoint starts!\n', mentor.first_name, '<', mentor.nickname,
              '>', mentor.last_name, ' vs ', student.first_name, student.last_name)
        time.sleep(2)
        irritation_level = int(mentor.irritation)
        knowledge_level = int(student.knowledge)
        motivation_level = int(student.motivation)
        print("\nMentor's irritation level is: ", irritation_level)
        print("\nStudent's knowledge level is: ", knowledge_level)
        print("\nStudent's motivation level is: ", motivation_level)
        time.sleep(4)
        if irritation_level >= 60:
            print('\nIrritation level is high! Beware!')
            print('\nStudent have 3min to build a game <battleship>!\nWithout an internet connection.\n')
            time.sleep(4)
            if knowledge_level < 80 and motivation_level < 80:
                print("\nStudent's score is: RED CARD")
                student.energy -= 10
                student.motivation -= 10
                mentor.irritation += 10
            elif knowledge_level < 80 and motivation_level > 80:
                print("\nStudent's score is: YELLOW CARD")
            else:
                print("\nVictory! Student's score is: GREEN CARD!")
                student.energy += 10
                student.motivation += 10
                mentor.irritation -= 10
        elif irritation_level <= 59:
            print("\nIt is lucky day for students! Irritation level is low.")
            print('\nWhat is a string?')
            time.sleep(4)
            if knowledge_level > 30 and motivation_level > 20:
                print("\nStudent is smart and so motivated! Student's score is: GREEN CARD!")
                student.energy += 10
                student.motivation += 10
                mentor.irritation -= 10
            elif knowledge_level < 20 and motivation_level < 10:
                print("\nStudent's score is: RED CARD")
                student.energy -= 10
                student.motivation -= 10
                mentor.irritation += 10
            else:
                print("\nStudent's score is: YELLOW CARD")


    def students_list(students):

        # students = Student.create_by_csv('data/students.csv')
        # students = Student
        students_list = []
        for student in students:
            students_list.append([student.first_name, student.last_name, student.year_of_birth,
                                  student.gender, student.coffee, student.energy, student.knowledge,
                                  student.motivation, student.sweets])
        return students_list

    
    @staticmethod
    def student_table(students):

        students_list = CodecoolClass.students_list(students)
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

 

    def is_int(value):
        try:
            int(value)
            return True
        except:
            return False

