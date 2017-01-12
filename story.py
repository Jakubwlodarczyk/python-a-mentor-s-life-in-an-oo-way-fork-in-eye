from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
import sys
import os


students = Student.create_by_csv('data/students.csv')

mentors = Mentor.create_by_csv('data/mentors.csv')
codecool_krk = CodecoolClass('Krakow', 2016, mentors, students)
s_table = Student

def choose_activity():
    user_input = input('Please enter a number: ')
    option = user_input
    if option == "1":
        codecool_krk.presentation()
    elif option == '2':
        codecool_krk.call_up()
    elif option == '3':
        codecool_krk.coffee()
    elif option == '4':
        codecool_krk.private_mentoring()
    elif option == '5':
        codecool_krk.checkpoing()
    elif option == '6':
        s_table.student_table()
    elif option == '0':
        sys.exit()
    else:
        raise KeyError("There is no such option.")


def story_menu():

    options = ['Presentation', 'Call up', 'Cofee', 'Private Mentoring', 'Checkpoint', 'Student table']
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
    print(
        "School @ {}, in year {} is created, with {} mentors and 53 students\n".format(codecool_class.location,
                                                                                       codecool_class.year,
                                                                                       len_mentors))

    chosen_mentor = choose_mentor()


    # CodecoolClass.presentation()
    while True:
        story_menu()
        print('')
        choose_activity()

main()
