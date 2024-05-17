"""This module provides a Database class for interacting directly with
an SQLite database file."""

import sqlite3
from typing import Optional
from src.exceptions import db_exceptions
from src.user.user import User

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
    def users_exist(phone_number: int) -> bool:
        """method docstring"""
        try:
            Database._connect()
            query: str = "SELECT id,name,phone_number FROM users WHERE phone_number = :phone_number"
            Database._cur.execute(query, {"phone_number": phone_number})
            result: list[tuple[int, str, int]] = Database._cur.fetchall()

            if result:
                return True
            else:
                return False
        finally:
            Database._disconnect()
if __name__ == '__main__':
    # agregar la lógica para crear la tabla
    pass
