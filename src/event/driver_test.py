"""Module docstring"""

import datetime
from user.user import User
from car.car import Car

class DriverTest:
    """Class docstring"""
    def __init__(self):
        self._day: datetime.date
        self._hour: datetime.time
        self._user: User
        self._car: Car
