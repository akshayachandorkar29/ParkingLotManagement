"""
This file has all the functions to run parking lot management system
Author: Akshaya Revaskar
Date: 02/01/2020
"""
import Vehicle


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
    def park(self, reg_no, color):
        if self.num_of_occupied_slots < self.capacity:
            slot_id = self.get_empty_slot()
            self.slots[slot_id] = Vehicle.Car(reg_no, color)
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
