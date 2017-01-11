class Person:

    def __init__(self, first_name, last_name, year_of_birth, gender, coffee, energy):

        # below we check if the attributes are empty
        if first_name is None:
            raise TypeError("First name cannot be empty")
        if last_name is None:
            raise TypeError("Last name cannot be empty")
        if year_of_birth is None:
            raise TypeError("Year of birth cannot be empty")
        if gender is None:
            raise TypeError("Please write a gender (male/female/notsure)")
        if coffee is None:
            raise TypeError("Please write True or False")
        if energy is None:
            raise TypeError("Please write from 0-100")

        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth
        self.gender = gender
        self.coffee = coffee
        self.energy = energy
