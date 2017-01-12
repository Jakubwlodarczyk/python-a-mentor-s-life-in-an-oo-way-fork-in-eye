# Mentor

## Description
This class represents a mentor in real life.

## Parent class
Person()

## Attributes

* ```nickname```
  * data type: string
  * description: stores the mentor's secret nickname between the students

* ```engagement_level```
  * data type: int
  * description: stores points of the mentor's engagement

* ```irritation_level```
   * data type: int
   * description: stores the mentor's level of irritation

* ```has_sweets```
  * data type: Boolean
  * description: stores information about candies if he has it or not

## Class methods


### ```create_by_csv```

Gets a csv file path as an argument (the csv contains all the data needed to instantiate a mentor object) and gives back an object list of mentors.
raise an error, if empty


#### Arguments
arguments of Person() and the class itself

#### Return value

object list of mentors


## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments

All of the arguments of the class itself.

#### Return value
None

