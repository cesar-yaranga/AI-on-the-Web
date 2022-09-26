import json
# from models.machine import Inserttable, db
from services.user_service import insert_logic, create_logic


def index():
    return "Hola Mundo"


def create():

    create_logic()


# insert data into table.
def insert():

    insert_logic()
