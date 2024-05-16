"""
database.py - Module for interacting directly with the SQLite database file.
"""

import sqlite3

class Database:
    """
    A class to interact directly with the SQLite database file.

    Attributes:
        _con (sqlite3.Connection): A connection object representing the SQLite database connection.
        _cur (sqlite3.Cursor): A cursor object used to execute SQL commands.
    """

    _con: sqlite3.Connection
    _cur: sqlite3.Cursor

    @staticmethod
    def _connect():
        """
        Establishes a connection to the SQLite database file.

        Opens a connection to the SQLite database file named 'app.db' and creates
        a cursor object for executing SQL commands.
        """
        Database._con = sqlite3.connect('app.db')
        Database._cur = Database._con.cursor()

    @staticmethod
    def _disconect():
        """
        Closes the connection to the SQLite database file.

        Closes the cursor and the connection to the SQLite database file.
        """
        Database._cur.close()
        Database._con.close()
