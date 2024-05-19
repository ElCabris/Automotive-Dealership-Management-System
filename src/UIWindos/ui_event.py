from abc import ABC
from src.models.user import User
import tkinter.ttk
from src.app import UISelectEvent

class Event(ABC):

    def __init__(self, user: User) -> None:
        self._user: User = user
        self._window: tkinter.Toplevel = tkinter.Toplevel()

    def return_page(self):
        UISelectEvent(self._window)
        self._window.destroy()
