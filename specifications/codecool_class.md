# CodecoolClass

## Description
This class represents a real class @ Codecool, containing mentors and students working at the class.

## Parent class
None

## Attributes

* ```location```
  * data type: string
  * description: stores the city where the the class started
* ```year```
  * data type: integer
  * description: stores the year when the class started
* ```mentors```
   * data type: list (containing Mentor objects)
   * description: stores the mentors of the class
* ```students```
  * data type: list (containing Student objects)
  * description: stores the students of the class

## Class methods


### ```create_local_school```

Creates a ```CodecoolClass``` object having some real-life data from the implementer students' real class.

#### Arguments
None

#### Return value

```CodecoolClass``` object



### ```find_student_by_full_name```

Gives back a student with the same full name as the argument from ```students```

#### Arguments
* ```full_name```
  * data_type: string
  * description: holds the full name of the student to be found

#### Return value
```Student``` object



### ```find_mentor_by_full_name```
Gives back a mentor with the same full name as the argument from ```mentors```

#### Arguments
* ```full_name```
  * data_type: string
  * description: holds the full name of the mentor to be found

#### Return value
```Mentor``` object



### ```make_presentation```

Operates on list of students objects and mentor object by increasing or decreasing motivation, energy, knowledge and engagement values .

#### Arguments
* ```Mentor```
  * data type: object
  * description: holds information about mentor

#### Return value
None



### ```call_up_to_the_board```

Operates on student and mentor objects by
increasing or decreasing motivation, energy, knowledge and irritation values .

#### Arguments
* ```Mentor```
  * data type: object
  * description: holds information about mentor
* ```Student```
  * data type: object
  * description: holds information about student


#### Return value
 None



### ```drink_coffee```

Operates on student object by increasing energy values.

#### Arguments
* ```Student```
  * data type: object
  * description: holds information about student

#### Return value
  None



### ```do_private_mentoring```

Operates on student and mentor objects by increasing or decreasing knowledge.

#### Arguments
* ```Mentor```
  * data type: object
  * description: holds information about mentor
* ```Student```
  * data type: object
  * description: holds information about student

#### Return value
None



### ```do_checkpoint```

Operates on student and mentor objects.
Checks mentor's irritation level and student's energy and motivation level.

#### Arguments
* ```Mentor```
  * data type: object
  * description: holds information about mentor
* ```Student```
  * data type: object
  * description: holds information about student

#### Return value
None


## Instance methods



### ```__init__```
The constructor of the object.

#### Arguments

All of the arguments of the class itself.

#### Return value
<<<<<<< HEAD
None



### ```find_student_by_full_name```

Gives back a student with the same full name as the argument from ```students```

#### Arguments
* ```full_name```
  * data_type: string
  * description: holds the full name of the student to be found

#### Return value
```Student``` object



### ```find_mentor_by_full_name```
Gives back a mentor with the same full name as the argument from ```mentors```

#### Arguments
* ```full_name```
  * data_type: string
  * description: holds the full name of the mentor to be found

#### Return value
```Mentor``` object
=======
None


### ```students_list```

Operates on a list of students from 'create_by_csv' method file and gives back a list of 
students and creates a list of student objects.

#### Arguments
   
* ```students```
  * data_type: object
  * description: holds full information about students.

#### Return value

  * data type: list
  * description: contains a list of students objects


### ```student_table```

Operates on a list of students returned from the function 'converter' method and gives back the formatted list wich includes
title and students list with all data.

#### Arguments
 * ```students```
  * data_type: object
  * description: holds full information about students.

#### Return value

  * data type: list
  * description: contains a list of students objects




