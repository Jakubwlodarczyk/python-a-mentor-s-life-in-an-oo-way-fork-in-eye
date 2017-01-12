class Person:

    def __init__(self, first_name, last_name, year_of_birth, gender, coffee, energy):
        Person.error_catch(first_name, last_name, year_of_birth, gender, coffee, energy)
        self.first_name = str(first_name)
        self.last_name = str(last_name)
        self.year_of_birth = int(year_of_birth)
        self.gender = str(gender)
        self.coffee = str(coffee)
        self.energy = int(energy)

    @staticmethod
    def error_catch(first_name, last_name, year_of_birth, gender, coffee, energy):
        gender_types = [' male', ' female', ' not sure']
        try:
            first_name.isalpha()
            last_name.isalpha()
            if first_name == '':
                raise ValueError
            elif last_name == '':
                raise ValueError
            elif year_of_birth == '':
                raise ValueError
            elif gender not in gender_types:
                raise ValueError
            elif coffee == '':
                raise ValueError
            elif energy == '':
                raise ValueError
        except ValueError:
            print('Wrong type of data')
            exit()
