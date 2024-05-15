"""Module docstring"""

from user.user import User
from car.car import Car

class Purchase:
    """Class docstring"""
    def __init__(self) -> None:
        self._user: User
        self._car: Car
        self._payment_method: str
