# Student

## Description
This class represents a real students @ Codecool at the class.

## Parent class
Person

## Attributes
  
* ```knowledge```
  * data type: integer
  * description: stores the knowledge level of the student in programming (from 0 to 100)

* ```motivation```
   * data type: integer
   * description: stores the current motivation level (from 0 to 100)

* ```sweets```
  * data type: boolean
  * description: stores information if student likes sweets or not


## Class methods

### ```create_by_csv```

Gets a csv file and gives back a list of students

#### Arguments
* ```file_path```
  * data type: string
  * description: path to the CSV file

#### Return value

```list_of_students```


### ```students_list```

Operates on a list of students from 'create_by_csv' method file and gives back a list of 
students and creates a list of student objects.

#### Arguments
   None

#### Return value

  * data type: list
  * description: contains a list of students objects


### ```student_table```

Operates on a list of students returned from the function 'converter' method and gives back the formatted list wich includes
title and students list with all data.

#### Arguments
   None

#### Return value

  * data type: list
  * description: contains a list of students objects



### ```converter```
Operates with the list returned from the function students_list 

#### Arguments
   None

#### Return value

  * data type: list
  * description: contains a list of students objects


## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments

All of the arguments of the class itself.

#### Return value
None
