"""Module docstring"""
import datetime
from sqlite3 import Error
from src.user.user import User
from src.db.database import Database
from src.exceptions import db_exceptions
from src.exceptions import date_exceptions
from src.utils.utils_date import enter_date

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
    except Error:
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
    print("select a time slot")
    time_slot: dict[datetime.time, list[datetime.date]] = Database.get_available_datetime()

    for dates, times in time_slot.items():
        print(f"date: {dates} - hours:", end=' ')
        for i in times:
            print(i, end=' ')

    print("\nNow select the date on which you want to take the driving test")

    while True:
        try:
            year: int = int(input("Enter the year: "))
            month: int = int(input("Enter the month: "))
            day: int = int(input("Enter the day: "))
            date: datetime.date = enter_date(year, month, day)
            break
        except ValueError:
            print("the entered date is invalid")
        except date_exceptions.NoValidDate:
            print("The date cannot be earlier than the current date.")

    print("Select the hour")
    
    print(time_slot[date])

    hora = int(input("ingresa la hora: "))
    minute = int(input("ingresa el minuto: "))

    hour = datetime.time(hora, minute, 0)

else:
    pass
