"""This module defines the `Color` class, which represents a color using RGB values.

The `Color` class provides a way to represent and manage colors using their red, green,
and blue (RGB) components.
It ensures that the RGB values are within the valid range (0 to 255) and raises an exception
if invalid values are provided.
"""

class Color:
    """Represents a color using RGB values.

    Attributes:
        _r (int): The red component of the color (0 to 255).
        _g (int): The green component of the color (0 to 255).
        _b (int): The blue component of the color (0 to 255).

    Raises:
        ValueError: If any of the RGB values are not within the range 0 to 255.
    """

    def __init__(self, r: int, g: int, b: int):
        """Creates a `Color` object with the specified RGB values.

        Args:
            r (int): The red component of the color (0 to 255).
            g (int): The green component of the color (0 to 255).
            b (int): The blue component of the color (0 to 255).

        Raises:
            ValueError: If any of the RGB values are not within the range 0 to 255.
        """
        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            raise ValueError("Invalid RGB values. Each value must be between 0 and 255.")

        self._r = r
        self._g = g
        self._b = b

    def __str__(self) -> str:
        return f"{self._r}, {self._g}, {self._b}"

    @staticmethod
    def from_string(color_str: str):
        r, g, b = map(int, color_str.split(','))
        return Color(r, g, b)
