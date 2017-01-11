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
        codecool_krk.private_mentoring()
    elif option == '5':
        codecool_krk.checkpoing()
    elif option == '0':
        sys.exit()   
    else:
        raise KeyError("There is no such option.")



def story_menu():
    options = ['Presentation', 'Call up', 'Cofee', 'Private Mentoring', 'Checkpoint']
    print('Event list:')
    for i,n in enumerate(options):
        print(i+1, n)

def main():
    """Main function"""
    codecool_class = CodecoolClass.create_local_school()
    len_mentors = len(Mentor.create_by_csv('data/mentors.csv'))
    print("Mentors are initialized from CSV.")
    print("Students are initialized from CSV.")
    print(
        "School @ {}, in year {} is created, with {} mentors and 53 students\n".format(codecool_class.location,
                                                                                       codecool_class.year,
                                                                                       len_mentors))
    CodecoolClass.choose_mentor()
    story_menu()
    print('')
    choose_activity()

main()