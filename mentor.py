from person import Person
import csv


class Mentor(Person):

    def __init__(self, first_name, last_name, year_of_birth, gender, coffee, energy, nickname, engagement, irritation, sweets):
        Person.__init__(self, first_name, last_name, year_of_birth, gender, coffee, energy)
        self.nickname = nickname
        self.engagement = int(engagement)

        self.irritation = int(irritation)

        self.sweets = sweets

    def __str__(self):
        return "{} {} {} ".format(self.first_name,  self.last_name, self.nickname)

    @classmethod
    def create_by_csv(cls, filepath):
        try:
            with open('data/mentors.csv') as mentor_file:
                all_mentors = csv.reader(mentor_file, delimiter=',', quotechar=',')
                mentors_list = []
                for mentor in all_mentors:
                    mentors = Mentor(mentor[0], mentor[1], mentor[2], mentor[3], mentor[4],
                                     mentor[5], mentor[6], mentor[7], mentor[8], mentor[9])
                    mentors_list.append(mentors)
        except FileNotFoundError:
            print("File does not exist")
        return mentors_list

Mentor.create_by_csv('data/mentors.csv')

'''mentors_array = Mentor.create_by_csv('data/mentors.csv')
print(mentors_array[0].sweets)  # check elements in my list for now
for mentor in mentors_array:  # yay its so brilliant!
    print(mentor.first_name, mentor.gender)'''
