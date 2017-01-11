from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
import sys
import os

codecool_krk = CodecoolClass


def choose_activity():
    user_input = input('Please enter a number: ')
    option = user_input
    if option == "1":
        codecool_krk.presentation()
    elif option == '2':
        codecool_krk.call_up()
    elif option == '3':
        codecool_krk.cofee()
    elif option == '4':
        choose_student()
        codecool_krk.private_mentoring()
    elif option == '5':
        codecool_krk.checkpoing()
    elif option == '0':
        sys.exit()
    else:
        raise KeyError("There is no such option.")


def choose_student():
    student_array = Student.create_by_csv('data/students.csv')
    number = 1
    for student in student_array:
        print(number, student.first_name)
        number += 1
    choosen = input("Choose student for private mentoring:")
    choosen = int(choosen)
    choosen_student = student_array[choosen]
    return choosen_student


def story_menu():

    options = ['Presentation', 'Call up', 'Cofee', 'Private Mentoring', 'Checkpoint']
    print('Event list:')
    for i, n in enumerate(options):
        print(i + 1, n)


def main():
    while True:
        story_menu()
        print('')
        choose_activity()

main()
