from person import Person


class Student(Person):

    def __init__(self, knowledge, motivation, sweets):
        Person.__init__(self, first_name, last_name, year_of_birth, gender, coffee, energy)
        self.knowledge = knowledge
        self.motivation = motivation
        self.sweets = sweets

    def create_by_csv():
        #return list of students
