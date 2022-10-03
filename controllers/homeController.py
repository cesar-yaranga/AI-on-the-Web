import json
# from models.machine import Inserttable, db
from services.user_service import insert_logic, create_logic
from services.computer_vision_service import malla_facial, deteccion_manos
from flask import render_template, Response


def index():
    return render_template('Index.html')


def video():
    # return Response(malla_facial(), mimetype='multipart/x-mixed-replace; boundary=frame')
    return Response(deteccion_manos(), mimetype='multipart/x-mixed-replace; boundary=frame')
    # return Response(deteccion_manos(), mimetype='application/json')


def create():
    create_logic()


def insert():
    insert_logic()
