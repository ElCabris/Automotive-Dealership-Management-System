"""This module provides a user interface for an Automotive Dealership Management System using tkinter."""

import tkinter
import tkinter.messagebox
import tkinter.ttk
from typing import Literal, Optional
from src.db.database import Database
from src.exceptions import db_exceptions
from src.models.user import User

class UILog:
    """User Interface for logging in or registering users
    in the Automotive Dealership Management System."""

    FORMAT: tuple[str, int] = ("Arial", 14)

    def __init__(self) -> None:
        """
        Initialize the login interface, setting up labels, entry boxes, and buttons.
        """
        self.__window: tkinter.Tk = tkinter.Tk()
        self.__window.title("Automotive Dealership Management System")
        self.__window.config(padx=35, pady=35)

        # Enter name
        self.__label_name: tkinter.Label = tkinter.Label(text="Ingresa tu nombre", font=self.FORMAT)
        self.__label_name.grid(column=0, row=1)

        self.__box_name: tkinter.Entry = tkinter.Entry(width=20, font=self.FORMAT)
        self.__box_name.grid(column=0, row=2)

        # Enter phone number
        self.__label_phone: tkinter.Label = tkinter.Label(text="Ingresa tu número de teléfono", font=self.FORMAT)
        self.__label_phone.grid(column=0, row=3)

        # Validation for phone number entry
        vcmd: tuple[str, Literal['%P']] = (self.__window.register(self.__validate_numeric), '%P')
        self.__box_phone: tkinter.Entry = tkinter.Entry(width=20, font=self.FORMAT,
                                         validate='key', validatecommand=vcmd)
        self.__box_phone.grid(column=0, row=4)

        self.__button_send: tkinter.Button = tkinter.Button(text="Send", font=self.FORMAT, command=self.save_data)
        self.__button_send.grid(column=0, row=5)

        self.__user: Optional[User] = None
        self.__window.mainloop()

    def __validate_numeric(self, P: str) -> bool:
        """
        Validate that the input is numeric.
        
        Args:
            P (str): The input string to validate.
        
        Returns:
            bool: True if the input is numeric or empty, False otherwise.
        """
        return P.isdigit() or P == ""

    def save_data(self) -> None:
        """
        Save data from input fields to the database. Checks if the user exists and either fetches or registers the user.
        """
        name: str = self.__box_name.get()
        phone: int = self.__box_phone.get()

        try:
            if not Database.user_exist(name, phone):
                Database.add_user(name=name, phone_number=phone)

            self.__user = Database.get_user(name=name, phone_number=phone)
            UISelectEvent(self.__user)

        except db_exceptions.PhoneNumberRepeated:
            tkinter.messagebox.showerror(
                message="The phone number has already been registered by another user."
                )

class UISelectEvent:

    """User Interface for user events after logging in."""

    def __init__(self, user: User) -> None:
        """
        Initialize the event interface, setting up buttons for different actions.
        
        Args:
            user (User): The user who has logged in.
        """
        self.__window: tkinter.Toplevel = tkinter.Toplevel()
        self.__window.config(padx=35, pady=35)
        self.__window.title("Welcome")

        self.__driver_test: tkinter.ttk.Button = tkinter.ttk.Button(self.__window,
                                                                    text="Driver Test")
        self.__driver_test.grid(column=0, row=1)

        self.__purchase: tkinter.ttk.Button = tkinter.ttk.Button(self.__window, text="Purchase")
        self.__purchase.grid(column=1, row=1)
        self.__window.focus()
        self.__window.grab_set()
        self.__user: User = user


if __name__ == "__main__":
    ui_log = UILog()
