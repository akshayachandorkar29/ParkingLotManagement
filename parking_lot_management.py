"""
This file has all the functions to run parking lot management system
Author: Akshaya Revaskar
Date: 02/01/2020
"""
import Vehicle
import datetime
now = datetime.datetime.now()
curr_time = datetime.time(now.hour, now.minute, now.second)


# this is a main driver class which have all the business logic for efficient parking lot management
class ParkingLot:
    def __init__(self):  # constructor for ParkingLot
        self.capacity = 0
        self.slot_id = 0
        self.num_of_occupied_slots = 0

    # this function will create an empty parking slot with defined capacity
    def create_parking_lot(self, capacity):
        self.slots = [-1] * capacity
        self.capacity = capacity
        return self.capacity

    # this is the function to get empty slots to park the Car
    def get_empty_slot(self):
        for i in range(len(self.slots)):
            if self.slots[i] == -1:
                return i

    # this is the function to actually park the Car
    def park(self, name, reg_no, color, current_time):
        if self.num_of_occupied_slots < self.capacity:
            slot_id = self.get_empty_slot()
            self.slots[slot_id] = Vehicle.Car(name, reg_no, color, current_time)
            self.slot_id = self.slot_id + 1
            self.num_of_occupied_slots = self.num_of_occupied_slots + 1
            return slot_id + 1
        else:
            return -1

    # this will check if vehicle already there, if present, delete the slot
    def leave(self, slot_id):
        if self.num_of_occupied_slots > 0 and self.slots[slot_id - 1] != -1:
            self.slots[slot_id - 1] = -1
            self.num_of_occupied_slots = self.num_of_occupied_slots - 1
            return True
        else:
            return False

    # this will return status of the slots FULL or VACANT
    def get_status(self):
        if self.num_of_occupied_slots == self.capacity:
            status = "FULL"
        else:
            status = "VACANT"
        return status

    # this function is for airport security to check whether parking slot is full
    def airport_security_person_update(self):
        update = self.get_status()
        if update == "FULL":
            redirect = True
        else:
            redirect = False
        return redirect

    # this is getter function for registration number given color
    def get_reg_no_from_color(self, color):

        reg_nos = []
        for i in self.slots:

            if i == -1:
                continue
            if i.color == color:
                reg_nos.append(i.reg_no)  # append registration number to the list reg_no
        return reg_nos

    # this is getter function for slot number given registration number
    def get_slot_no_from_reg_no(self, reg_no):

        for i in range(len(self.slots)):  # traverse through slot list and return slot number
            if self.slots[i].reg_no == reg_no:
                return i + 1
            else:
                continue
        return -1

    # this is getter function for slot number given color
    def get_slot_no_from_color(self, color):

        slot_nos = []

        for i in range(len(self.slots)):

            if self.slots[i] == -1:
                continue
            if self.slots[i].color == color:
                slot_nos.append(i + 1)
        return slot_nos

    # this function is for helping driver to find his car given color of the car
    def search_car_given_color(self, color):
        return self.get_slot_no_from_color(color)

    # this function is for helping driver to find his car given registration number of the car
    def search_car_given_reg_no(self, reg_no):
        slot_of_the_car = self.get_slot_no_from_reg_no(reg_no)
        return slot_of_the_car

    # this function returns reg no of all the cars given time
    def get_reg_no_from_time(self, current_time):

        reg_no = []
        for i in self.slots:

            if i == -1:
                continue
            if i.current_time == current_time:
                reg_no.append(i.reg_no)  # append registration number to the list reg_no
        return reg_no

    # this function returns reg no of all the cars given time
    def get_time_from_reg_no(self, reg_no):

        time = []
        for i in self.slots:

            if i == -1:
                continue
            if i.reg_no == reg_no:
                time.append(i.current_time)  # append registration number to the list reg_no
        return time

    # this function returns list of all slot numbers which have name as given name
    def get_slot_no_from_name(self, name):

        slot_no_name = []

        for i in range(len(self.slots)):

            if self.slots[i] == -1:
                continue
            if self.slots[i].name == name:
                slot_no_name.append(i + 1)
        return slot_no_name

    # this function returns location and reg no given name of the car
    def get_slot_and_reg_no_given_name(self, name):

        details = []

        for i in range(len(self.slots)):
            inside = []
            if self.slots[i] == -1:
                continue
            if self.slots[i].name == name:
                inside.append(i+1)
                inside.append(self.slots[i].reg_no)
                details.append(inside)
        return details

    def get_all_cars(self):

        cars = []
        for i in self.slots:

            if i == -1:
                continue
            cars.append(i.reg_no)  # append registration numbers of all the cars to the list cars
        return cars






