"""Custom Exceptions for Database Operations

This module defines custom exception classes for handling errors related to database operations.
"""

from src.exceptions.base_exception import BaseAppException

class DatabaseException(BaseAppException):
    """Custom exceptionn for databvase-related errorrs"""

class PhoneNumberRepeated(DatabaseException):
    """Exceptn raised when a phone number is found to be repeated in the database"""

class NoFoundPhoneNumber(DatabaseException):
    """Class docstring"""
