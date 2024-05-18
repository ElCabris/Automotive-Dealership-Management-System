"""module docstring"""
from src.exceptions.base_exception import BaseAppException

class NoValidDate(BaseAppException):
    """The date cannot be earlier than the current date."""
