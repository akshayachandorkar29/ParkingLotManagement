""" This file contains parent class Vehicle and its child class Car
Author: Akshaya Revaskar
Date: 02/03/2020
"""

# this is parent class for every vehicle type
class Vehicle:
    def __init__(self, reg_no, color):
        self.color = color
        self.reg_no = reg_no


# this class has extended parent class Vehicle
class Car(Vehicle):
    def __init__(self, reg_no, color):
        Vehicle.__init__(self, reg_no, color)

    def get_type(self):  # this will return the type of the vehicle
        return "Car"