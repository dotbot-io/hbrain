from datetime import datetime
from flask import render_template, session, redirect, url_for

from . import main
# from .forms import NameForm
# from .. import db
# from ..models import User


@main.route("/stream_test")
def stream_test():
    return render_template('main/stream_test.html')
