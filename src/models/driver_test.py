"""This module defines the `DriverTest` class, which represents a driver's test appointment
in the system.

A `DriverTest` instance stores information about a scheduled driver's test, including:
* The date of the test (`datetime.date` object).
* The time of the test (`datetime.time` object).
* The user taking the test (`User` object).
* The car to be used in the test (`Car` object).
"""

import datetime
from src.models.user import User
from src.models.car import Car


class DriverTest:
    """Represents a scheduled driver's test in the system.

    Attributes:
        _day (datetime.date): The date of the driver's test.
        _hour (datetime.time): The time of the driver's test.
        _user (User): The user taking the driver's test (a `User` object).
        _car (Car): The car to be used in the driver's test (a `Car` object).
    """

    def __init__(self, day: datetime.date = None,
                 hour: datetime.time = None,
                 user: User = None,
                 car: Car = None,
                 number_id: int = None):
        self._day: datetime.date = day
        self._hour: datetime.time = hour
        self._user: User = user
        self._car: Car = car
        self._id: int = number_id

    def get_id(self) -> int:
        return self._id
