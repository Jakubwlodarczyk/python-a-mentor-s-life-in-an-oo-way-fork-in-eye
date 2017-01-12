from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
import sys
import os
import time


students = Student.create_by_csv('data/students.csv')

mentors = Mentor.create_by_csv('data/mentors.csv')
codecool_krk = CodecoolClass('Krakow', 2016, mentors, students)
s_table = Student


def choose_activity(mentor):
    user_input = input('Please enter a number: ')
    option = user_input
    if option == "1":
        os.system('clear')
        codecool_krk.presentation(mentor)
    elif option == '2':
        os.system('clear')
        chosen_student = choose_student()
        codecool_krk.call_up(mentor, chosen_student)
    elif option == '3':
        os.system('clear')
        print('Students want to drink coffee, but the work is not done yet. \nYou can allow only one student to go kitchen room. Choose one from the list:\n')
        chosen_student = choose_student()
        codecool_krk.coffee(chosen_student)
    elif option == '4':
        os.system('clear')
        print('Choose a student for private mentoring:\n')
        chosen_student = choose_student()
        print('\n')
        codecool_krk.private_mentoring(mentor, chosen_student)
    elif option == '5':
        student = choose_student()
        codecool_krk.checkpoint(mentor, student)
    elif option == '6':
        os.system('clear')
        s_table.student_table()
    elif option == '7':
        os.system('clear')
        students_object_list = Student.create_by_csv('data/students.csv')
        # counter = 1 UNHASH IF YOU WANT TO PRINT STUDENT LIST
        # for student in students_object_list:
        #    print(str(counter) + ".", student.first_name, student.last_name)
        #    counter += 1
        full_name = input("Type a student: ")
        codecool_krk.find_student_by_full_name(students_object_list, full_name)
    elif option == '8':
        os.system('clear')
        mentors_object_list = Mentor.create_by_csv('data/mentors.csv')
        full_name = input("Type a mentor: ")
        codecool_krk.find_mentor_by_full_name(mentors_object_list, full_name)
    elif option == '0':
        os.system('clear')
        sys.exit()
    elif option == "":
        print("Type something.")
    else:
        raise KeyError("There is no such option.")


def story_menu():

    options = ['Presentation', 'Call up', 'Cofee', 'Private Mentoring', 'Checkpoint',
               'Print student table', 'Find student by full name', 'Find mentor by full name']

    print('\nEvent list:')
    for i, n in enumerate(options):
        print(i + 1, n)
    print('0 Exit\n')


def choose_mentor():
    mentors_object_list = Mentor.create_by_csv('data/mentors.csv')
    counter = 1
    for mentor in mentors_object_list:
        print(str(counter) + ".", mentor.first_name, mentor.last_name, mentor.nickname)
        counter += 1
    while True:
        try:
            choice = int(input("\nChoose mentor you want to play: "))
            if choice > 0 and choice <= len(mentors_object_list):
                os.system('clear')
                print("You have chosen ", mentors_object_list[choice - 1])
                return mentors_object_list[choice - 1]
            else:
                print("Type correct number...\n")
                continue
        except:
            print("Type an integer...\n")


def choose_student():
    student_array = Student.create_by_csv('data/students.csv')
    number = 1
    for student in student_array:
        print(number, student.first_name)
        number += 1
    while True:
        try:
            choosen = int(input("\nType a number: "))
            if choosen > 0 and choosen <= len(student_array):
                print("You have chosen ", student_array[choosen - 1])
                return student_array[choosen - 1]
            else:
                print("Type correct number...\n")
                continue
        except:
            print("Type an integer...\n")


def main():
    """Main function"""
    codecool_class = CodecoolClass.create_local_school()
    len_mentors = len(Mentor.create_by_csv('data/mentors.csv'))
    print(
        "School @ {}, in year {} is created, with {} mentors and 53 students\n".format(codecool_class.location,
                                                                                       codecool_class.year,
                                                                                       len_mentors))
    chosen_mentor = choose_mentor()
    while True:
        story_menu()
        choose_activity(chosen_mentor)
        time.sleep(4)
        os.system('clear')


   


main()
