"""Module docstring"""

import datetime
from src.exceptions.date_exceptions import NoValidDate

def enter_date(year: int, month: int, day: int) -> datetime.date:
    """function docstring"""

    result: datetime.date = datetime.date(year, month, day)

    if result < datetime.date.today():
        raise NoValidDate

    return result
