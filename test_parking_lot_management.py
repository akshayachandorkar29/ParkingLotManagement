""" This file contains test cases for parking lot management problem
Author: Akshaya Revaskar
Date: 02/03/2020
"""

import pytest
from Vehicle import Car
from parking_lot_management import ParkingLot
parking = ParkingLot()


# test case for getting type of the vehicle
def test_get_type_of_vehicle():
    car_vehicle = Car(1, "red")
    assert car_vehicle.get_type() == "Car"


# test case for checking created parking slot
def test_create_parking_lot():
    assert parking.create_parking_lot(2) == 2


# test case to getting empty slot when all the slots are empty
def test_get_empty_slot_when_all_slots_are_empty():
    assert parking.get_empty_slot() == 0


# test case for checking car has actually parked or not
def test_park_the_car():
    assert parking.park(101, "red") == 1


# test case for unparking
def test_leave_the_car():
    assert parking.leave(1) == True


# test case for getting status
def test_get_status():
    assert parking.get_status() == "VACANT"


# test case for redirecting security staff
def test_airport_security_person_update():
    assert parking.airport_security_person_update() == False


