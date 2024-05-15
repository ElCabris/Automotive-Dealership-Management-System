"""Module docstring"""

from utils.color import Color

class Car:
    """Class docstring"""
    def __init__(self, car_type:str):
        self._type: str = car_type
        self._rim: str
        self._external_color: tuple[int, int, int] # rgb
        self._engine_displacement: int # cubic centimeters (c.c)
        self._internal_color: Color
