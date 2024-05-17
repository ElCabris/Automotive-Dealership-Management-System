"""Module doctring"""

from src.db.database import Database
from src.exceptions import db_exceptions 
phone_number = int(input("ingresa el numero de telefono: "))

try:
    Database.del_user(phone_number)
except db_exceptions.DatabaseException as e:
    print("tremendo error pa")
