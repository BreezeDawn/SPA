from flask import Blueprint

data_blue = Blueprint('data', __name__)

from .views import *
