from flask import Blueprint

api_2_0 = Blueprint('api_2_0', __name__)

from . import hbrain_api
