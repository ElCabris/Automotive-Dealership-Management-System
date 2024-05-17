"""Module docstring"""

import sqlite3
from typing import Optional

from src.exceptions import db_exceptions
class Database:
    """
    A class to interact directly with the SQLite database file.

    Attributes:
        _con (Optional[sqlite3.Connection]): A connection object representing
        the SQLite database connection.
        _cur (Optional[sqlite3.Cursor]): A cursor object used to execute SQL commands.
    """

    _con: Optional[sqlite3.Connection] = None
    _cur: Optional[sqlite3.Cursor] = None

    @staticmethod
    def _connect():
        """
        Establishes a connection to the SQLite database file.

        Opens a connection to the SQLite database file named 'app.db' and creates
        a cursor object for executing SQL commands.
        """
        Database._con = sqlite3.connect('src/db/app.db')
        Database._cur = Database._con.cursor()

    @staticmethod
    def _disconnect():
        """
        Closes the connection to the SQLite database file.

        Closes the cursor and the connection to the SQLite database file.
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
        """

        Database._connect()
        Database._cur.execute("SELECT name FROM users WHERE phone_number = :phone_number",
                              {"phone_number": phone_number})
        result: list[tuple[str]] = Database._cur.fetchall()

        if len(result) != 0:
            raise db_exceptions.PhoneNumberRepeated

        # Question marks are used to prevent SQL injection.
        Database._cur.execute("INSERT INTO users(name, phone_number) VALUES(?, ?)",
                                (name, phone_number))
        Database._con.commit()
        Database._disconnect()

    @staticmethod
    def del_user(phone_number: int):
        """method docstrings"""
        Database._connect()
        Database._cur.execute("SELECT name FROM users WHERE phone_number = :phone_number",
                              {"phone_number": phone_number})
        result: list[tuple[str]] = Database._cur.fetchall()

        if len(result) == 0:
            raise db_exceptions.NoFoundPhoneNumber

        Database._cur.execute("DELETE FROM users WHERE phone_number = :phone_number",
                              {"phone_number": phone_number})
        Database._con.commit()
        Database._disconnect()
