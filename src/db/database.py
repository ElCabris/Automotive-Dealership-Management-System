"""This module provides a Database class for interacting directly with
an SQLite database file."""

import sqlite3
from typing import Optional
import datetime

from src.exceptions import db_exceptions
from src.models.user import User
from src.utils.color import Color
from src.models.driver_test import DriverTest
from src.exceptions import diver_test_exceptions
from src.models.car import Car

class Database:
    """
    A class to interact directly with the SQLite database file.

    Attributes:
        _con (Optional[sqlite3.Connection]): A connection object representing
        the SQLite database connection.
        _cur (Optional[sqlite3.Cursor]): A cursor object used to execute SQL commands.
    """
    __DATABASE_URL = "src/db/app.db"

    _con: Optional[sqlite3.Connection] = None
    _cur: Optional[sqlite3.Cursor] = None

    @staticmethod
    def _connect():
        """
        Establishes a connection to the SQLite database file.
        """
        Database._con = sqlite3.connect(Database.__DATABASE_URL)
        Database._cur = Database._con.cursor()

    @staticmethod
    def _disconnect():
        """
        Closes the connection to the SQLite database file.
        """
        if Database._cur:
            Database._cur.close()
        if Database._con:
            Database._con.close()

    @staticmethod
    def add_user(name: str, phone_number: int) -> None:
        """
        Adds a user to the database.

        Inserts a new user with the given name and phone number into the users table.

        Args:
            name (str): The name of the user.
            phone_number (int): The phone number of the user.

        Raises:
            db_exceptions.PhoneNumberRepeated: If a user with the same phone number already exists.
        """
        Database._connect()
        try:
            query = "SELECT name FROM users WHERE phone_number = :phone_number"
            Database._cur.execute(query, {"phone_number": phone_number})
            result: list[tuple[str]] = Database._cur.fetchall()

            if result:
                raise db_exceptions.PhoneNumberRepeated

            query: str = "INSERT INTO users(name, phone_number) VALUES(:name, :phone_number)"
            Database._cur.execute(query, {"name": name, "phone_number": phone_number})
            Database._con.commit()
        finally:
            Database._disconnect()

    @staticmethod
    def del_user(phone_number: int) -> None:
        """
        Deletes a user from the database based on their phone number.

        Args:
            phone_number (int): The phone number of the user to be deleted.

        Raises:
            db_exceptions.NoFoundPhoneNumber: If no user is found with the provided phone number.
        """
        Database._connect()
        try:
            query = "SELECT name FROM users WHERE phone_number = :phone_number"
            Database._cur.execute(query, {"phone_number": phone_number})
            result: list[tuple[str]] = Database._cur.fetchall()

            if not result:
                raise db_exceptions.NoFoundPhoneNumber

            Database._cur.execute("DELETE FROM users WHERE phone_number = :phone_number",
                                  {"phone_number": phone_number})
            Database._con.commit()
        finally:
            Database._disconnect()

    @staticmethod
    def edit_user(phone_number: int,
                  name: Optional[str] = None,
                  new_phone_number: Optional[int] = None) -> None:
        """
        Edits a user's information in the database.

        Args:
            phone_number (int): The current phone number of the user to be edited.
            name (Optional[str]): The new name for the user.
            new_phone_number (Optional[int]): The new phone number for the user.

        Raises:
            db_exceptions.NoFoundPhoneNumber: If no user is found with the provided phone number.
            db_exceptions.PhoneNumberRepeated: If the new phone number is already taken 
            by another user.
        """
        Database._connect()
        try:
            query = "SELECT name FROM users WHERE phone_number = :phone_number"
            Database._cur.execute(query, {"phone_number": phone_number})
            result: list[tuple[str]] = Database._cur.fetchall()

            if not result:
                raise db_exceptions.NoFoundPhoneNumber

            if name:
                update_query = "UPDATE users SET name = :name WHERE phone_number = :phone_number"
                Database._cur.execute(update_query, {"name": name, "phone_number": phone_number})

            if new_phone_number:
                query: str = "SELECT name FROM users WHERE phone_number = :new_phone_number"
                Database._cur.execute(query, {"new_phone_number": new_phone_number})
                new_result: list[tuple[str]] = Database._cur.fetchall()

                if new_result:
                    raise db_exceptions.PhoneNumberRepeated

                update_query: str = "UPDATE users SET phone_number = :new_phone_number WHERE phone_number = :phone_number"
                Database._cur.execute(update_query,
                                      {"new_phone_number": new_phone_number,
                                       "phone_number": phone_number}
                                    )

            Database._con.commit()
        finally:
            Database._disconnect()

    @staticmethod
    def get_all_users() -> list[User]:
        """
        Retrieves all users from the database.

        Returns:
            list[User]: A list containing all users retrieved from the database.

        Raises:
            DatabaseError: If there is an error in executing the SQL query or fetching the data.
        """
        try:
            Database._connect()
            query: str = "SELECT id, name, phone_number FROM users"
            Database._cur.execute(query)
            result_query: list[tuple[int, str, int]] = Database._cur.fetchall()
            result: list[User] = [User(number_id=i[0], name=i[1], phone_number=i[2])
                                  for i in result_query]
            return result
        finally:
            Database._disconnect()

    @staticmethod
    def get_user(phone_number: int, name: Optional[str] = None) -> User:
        """method docstring"""
        try:
            Database._connect()
            query: str = str()
            if name:
                query = "SELECT id, name, phone_number FROM users WHERE phone_number = :phone_number AND name = :name"
            else:
                query = "SELECT id, name, phone_number FROM users WHERE phone_number = :phone_number"
            Database._cur.execute(query, {"phone_number": phone_number, "name": name})
            result_query: list[tuple[int, str]] = Database._cur.fetchall()

            if not result_query:
                raise db_exceptions.PhoneNumberRepeated

            result: User = User(number_id = result_query[0][0],
                            name = result_query[0][1],
                            phone_number=result_query[0][2])

            return result
        finally:
            Database._disconnect()

    @staticmethod
    def user_exist(name: str, phone_number: int) -> bool:
        """method docstring"""
        try:
            Database._connect()
            query: str = "SELECT * FROM users WHERE phone_number = :phone_number AND name = :name"
            Database._cur.execute(query, {"phone_number": phone_number, "name": name})
            result: list[tuple[int, str, int]] = Database._cur.fetchall()

            if result:
                return True
            else:
                return False
        finally:
            Database._disconnect()

    @staticmethod
    def add_driver_test(test_day: datetime.date,
                        test_hour: datetime.time,
                        car_type: str,
                        rim_type: str,
                        engine_displacement: int,
                        external_color: Color,
                        internal_color: Color,
                        driver_id: Optional[int] = None) -> None:
        """
        Adds a driver test to the database.

        Args:
            test_day (datetime.date): The date of the test.
            test_hour (datetime.time): The hour of the test.
            car_type (str): The type of the car.
            rim_type (str): The type of the rims.
            engine_displacement (int): The engine displacement.
            external_color (Color): The external color of the car in RGB format.
            internal_color (Color): The internal color of the car in RGB format.
            available (int): Availability status (default is 1).
            driver_id (Optional[int]): The ID of the driver (must exist in users table or can be None).

        Note:
            If driver_id is None, the available field will automatically be set to 1 (true).
        """
        Database._connect()
        try:
            if driver_id is None:
                available = 1
            else:
                available = 0

            query = '''
                INSERT INTO driver_test (test_day, test_hour, car_type, rim_type, engine_displacement,
                                        external_color, internal_color, available, driver_id)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            '''
            Database._cur.execute(query, (test_day.isoformat(), test_hour.isoformat(),
                                          car_type, rim_type,
                                          engine_displacement, str(external_color),
                                          str(internal_color),
                                          available, driver_id))
            Database._con.commit()
        finally:
            Database._disconnect()

    @staticmethod
    def get_all_dates() -> list[datetime.date]:
        """
        Retrieves all unique test dates from the driver_test table

        Returns
            List[datetime.date]: A list fo uniqued test dates
        """
        Database._connect()
        try:
            query = "SELECT DISTINC test_day FROM driver_test"
            Database._cur.execute(query)
            result_query: list[tuple[str]] = Database._cur.fetchall()
            unique_dates: list[datetime.date] = [datetime.date.fromisoformat(date[0]) for date in result_query]
            return unique_dates
        finally:
            Database._disconnect()

    @staticmethod
    def get_available_datetime() -> dict[datetime.date, list[datetime.time]]:
        """
        Retrives all available hour by day from the driver_test table.

        Returns:
            dict[datetime.date, list[datetime.time]] A dictionary where keys are dates
            and values are lists of available hours for each date.
        """
        Database._connect()
        try:
            query = "SELECT test_day, test_hour FROM driver_test WHERE available = 1"
            Database._cur.execute(query)
            result_query: list[tuple[str, str]] = Database._cur.fetchall()
            available_datetime: dict[datetime.date, list[datetime.time]] = dict()

            for date_str, hour_str in result_query:
                test_date = datetime.date.fromisoformat(date_str)
                test_hour = datetime.datetime.strptime(hour_str, "%H:%M:%S").time()

                if test_date not in available_datetime:
                    available_datetime[test_date] = list()

                available_datetime[test_date].append(test_hour)

            return available_datetime
        finally:
            Database._disconnect()

    @staticmethod
    def get_available_driver_test(car: Car, date: datetime.date, hour: datetime.time):
        """metod docstring"""
        try:
            Database._connect()
            query: str = """SELECT * FROM driver_test
            WHERE car_type = ? AND rim_type = ? AND engine_displacement = ? AND external_color = ? AND internal_color = ? AND available = 1 AND test_day = ? AND test_hour = ?"""
            Database._con.execute(query,
                                  (car.get_type(),
                                   car.get_rim(),
                                   car.get_engine_displacement(),
                                   str(car.get_external_color()),
                                   str(car.get_internal_color()),
                                   date, hour))
        finally:
            Database._disconnect()
    @staticmethod
    def book_driver_test(user: User, driver_test: DriverTest) -> None:
        """
        Books a driver test for a user at a specific date and time.

        Args:
            user_id (int): The user who is going to book.
            driver_test (DriverTest): The booking to be made.
        Returns:
            bool: True if the booking was successful, False otherwise.
        """

        Database._connect()
        try:
            # Confirm that the space is available
            query: str = "SELECT available FROM driver_test WHERE id = ?"
            Database._cur.execute(query, (driver_test.get_id(),))
            result_query: list[tuple[int]] = Database._cur.fetchall()

            if not result_query[0][0]:
                raise diver_test_exceptions.NoAvaliableDriverTest

            query = "UPDATE driver_test SET available = 0, driver id = ? WHERE id = ?"
            Database._cur.execute(query, (user.get_id(), driver_test.get_id()))
            Database._con.commit()

        finally:
            Database._disconnect()


if __name__ == '__main__':
    # agregar la lógica para crear la tabla
    pass
