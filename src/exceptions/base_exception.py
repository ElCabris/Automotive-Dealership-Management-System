"""This module defines the `BaseAppException` class,
which serves as the base class for all custom exceptions in the application.

`BaseAppException` provides a common structure and error handling mechanism
for application-specific errors.
It inherits from the built-in `Exception` class and provides additional
attributes and methods for consistent error handling.
"""

class BaseAppException(Exception):
    """Base class for all custom exceptions in the application.

    Attributes:
        _message (str): The error message associated with the exception.
        _code (int): An optional error code that can be used for identification or classification.

    Methods:
        get_message() -> str: Retrieves the error message associated with the exception.
        get_code() -> int: Retrieves the error code associated with the exception (if set).
    """

    def __init__(self, message: str = "", code: int = 0):
        super().__init__(message)
        self._message: str = message
        self._code: int = code

    def get_message(self) -> str:
        """Retrieves the error message associated with the exception.

        This method returns the error message that was provided when the exception was created
        or a default message if no message was specified.

        Returns:
            str: The error message associated with the exception.
        """
        return self._message

    def get_code(self) -> int:
        """Retrieves the error code associated with the exception (if set).

        This method returns the error code that was provided when the exception was created
        or 0 (default) if no code was specified.

        Returns:
            int: The error code associated with the exception (if set).
        """
        return self._code
