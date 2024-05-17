"""Module docstring"""
import datetime
from src.user.user import User
from src.db.database import Database
from src.exceptions import db_exceptions

def enter_user() -> User:
    """Function docstring"""
    print("Please enter your information to continue with the process")

    try:
        name = input("enter your name: ")
        phone_number = int(input("enter your phone number: "))

        if not Database.users_exist(phone_number):
            Database.add_user(name = name, phone_number = phone_number)

        return Database.get_user(phone_number, name)

    except ValueError:
        print("Please enter only numbers for the phone number.")
        enter_user()
    except db_exceptions.PhoneNumberRepeated:
        print("This phone number is already associated with another user.")
        enter_user()
    except db_exceptions.NoFoundUser:
        print("The user you entered does not exist.")
        enter_user()
    except Exception:
        print("An unexpected error has occurred.")


print("""Welcome to our dealership! What can we help you with today?

a.) Take a test drive
b.) But car""")

option: str = input()

while option.lower() != 'a' and option.lower() != 'b':
    print("invalid option. Please enter one of the options (a or b)")
    option = input()

# login/register user
user: User = enter_user()

if option.lower() == 'a':
    print("""Select a day for you driver test""")
    year: str = input("Enter the year: ")
    moth: str = input("Enter the month: ")
    day: str = input("Ente the day: ")


else:
    pass
