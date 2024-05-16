"""This module defines the `Car` class, which represents a car in the system.

The `Car` class stores information about a car, including its type (sport, van, sedan),
rim type (sport, winter, standard), external color (`Color` object), engine displacement
(in cubic centimeters), and internal color (`Color` object).
"""

from dataclasses import dataclass
from typing import Optional

from utils.color import Color

@dataclass
class Car:
    """Represents a car in the system.

    Attributes:
        _type (str): The type of car (e.g., sport, van, sedan).
        _rim (str): The type of rim (e.g., sport, winter, standard).
        _external_color (Color): The external color of the car (a `Color` object).
        _engine_displacement (int): The engine displacement of the car in cubic centimeters.
        _internal_color (Color): The internal color of the car (a `Color` object).
    """

    _type: Optional[str] = None
    _rim: Optional[str] = None
    _external_color: Optional[Color] = None
    _engine_displacement: Optional[int] = None
    _internal_color: Optional[Color] = None
