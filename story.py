from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
import sys
import os

codecool_krk = CodecoolClass


def choose_activity(mentor):
    user_input = input('Please enter a number: ')
    option = user_input
    if option == "1":
        codecool_krk.presentation(mentor)
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

def choose_mentor():
    mentors_object_list = Mentor.create_by_csv('data/mentors.csv')
    counter = 1
    for mentor in mentors_object_list:
        print(str(counter) + ".", mentor.first_name, mentor.last_name, mentor.nickname)
        counter += 1
    choice = int(input("\nChoose mentor you want to play: "))
    print("You have chosen ", mentors_object_list[choice - 1])
    return mentors_object_list[choice - 1]


def main():
    """Main function"""
    codecool_class = CodecoolClass.create_local_school()
    len_mentors = len(Mentor.create_by_csv('data/mentors.csv'))
    print("\nMentors are initialized from CSV.")
    print("Students are initialized from CSV.")
    print(
        "School @ {}, in year {} is created, with {} mentors and 53 students\n".format(codecool_class.location,
                                                                                       codecool_class.year,
                                                                                       len_mentors))
    chosen_mentor = choose_mentor()

    story_menu()
    print('')
    choose_activity(chosen_mentor)

main()
