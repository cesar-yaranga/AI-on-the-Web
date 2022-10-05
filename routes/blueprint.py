from flask import Blueprint
from controllers.homeController import index, create, insert

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/', methods=['GET'])(index)
# blueprint.route('/video', methods=['GET'])(video)
blueprint.route('/create', methods=['GET'])(create)
blueprint.route('/insert', methods=['GET'])(insert)
