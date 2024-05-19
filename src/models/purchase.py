"""This module defines the `Purchase` class, which represents a car purchase in the system.

A `Purchase` instance stores information about a completed car purchase, including:
* The user who made the purchase (`User` object).
* The car that was purchased (`Car` object).
* The payment method used for the purchase (string).
"""

from src.models.user import User
from src.models.car import Car

class Purchase:
    """Represents a completed car purchase in the system.

    Attributes:
        _user (User): The user who made the purchase (a `User` object).
        _car (Car): The car that was purchased (a `Car` object).
        _payment_method (str): The payment method used for the purchase
        (e.g., "cheque", "cash", "transfer", "card").
    """

    def __init__(self) -> None:
        self._user: User
        self._car: Car
        self._payment_method: str
