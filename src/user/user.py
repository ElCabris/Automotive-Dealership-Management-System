"""This module defines the `User` class, which represents a user in the system.

The `User` class stores information about a user, including their name, phone number,
and a unique identifier npruebaumber. It provides methods to access these attributes.
"""

class User:
    """The `User` class represents a user in the system.

    Attributes:
        name (str): The user's name.
        phone_number (int): The user's phone number.
        number_id (str): A unique identifier number for the user.
    """

    def __init__(self, name: str = None, phone_number: int = None, number_id: str = None):
        """Initializes a new `User` object.

        Args:
            name (str): The user's name.
            phone_number (int): The user's phone number.
            number_id (str): A unique identifier number for the user.
        """
        self._name: str = name
        self._phone_number: int = phone_number
        self._id_number: str = number_id

    def get_name(self) -> str:
        """Returns the user's name.

        Returns:
            str: The user's name.
        """
        return self._name

    def get_id(self) -> str:
        """Returns the user's unique identifier number.

        Returns:
            str: The user's unique identifier number.
        """
        return self._id_number
