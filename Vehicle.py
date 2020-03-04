""" This file contains parent class Vehicle and its child class Car
Author: Akshaya Revaskar
Date: 02/03/2020
"""

# this is parent class for every vehicle type
class Vehicle:
    def __init__(self, reg_no, color, current_time):
        self.color = color
        self.reg_no = reg_no
        self.current_time = current_time


# this class has extended parent class Vehicle
class Car(Vehicle):
    def __init__(self, reg_no, color, current_time):
        Vehicle.__init__(self, reg_no, color, current_time)

    def get_type(self):  # this will return the type of the vehicle
        return "Car"

