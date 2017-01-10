class Person:

    def __init__(self, first_name, last_name, year_of_birth, gender, coffee, energy):

        boolean_list = ['True', 'False']
        gender_list = ['male', 'female', 'notsure']

        # below we check if the attributes are empty, or not valid
        if first_name is None:
            raise TypeError("Please write only a letters")
        if last_name is None:
            raise TypeError("Please write only a letters")
        if year_of_birth is None:
            raise TypeError("Please write only a year of birth")
        if gender not in gender_list:
            raise TypeError("Please choose from male/female/notsure")
        if coffee not in boolean_list:
            raise TypeError("Please write True or False")
        if energy is None:
            raise TypeError("Please write from 0-100")

        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth
        self.gender = gender
        self.coffee = coffee
        self.energy = energy
