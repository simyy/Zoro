#!/usr/bin/env python
# encoding: utf-8

from flask import render_template
from flask import redirect
from flask import session
from flask import url_for
from .  import main
from .. import db
from ..models.models import User


@main.route('/', methods=['GET', 'POST'])
def index():
    print(User.query.all())
    #return 'Hello'
    return render_template('index.html')
