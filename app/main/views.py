#!/usr/bin/env python
# encoding: utf-8

from flask import render_template
from flask import redirect
from flask import session
from flask import url_for
from .  import main
from .. import db
from ..models import User


@main.route('/', methods=['GET', 'POST'])
def index():
    user = User.query.all()
    if user:
        print(user[0])
    #return 'Hello'
    return render_template('index.html')
