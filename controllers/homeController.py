import json
# from models.machine import Inserttable, db
from services.user_service import insert_logic, create_logic
from services.computer_vision_service import malla_facial
from flask import render_template, Response


def index():
    return render_template('Index.html')


def video():
    return Response(malla_facial(), mimetype='multipart/x-mixed-replace; boundary=frame')


def create():

    create_logic()


# insert data into table.
def insert():

    insert_logic()
