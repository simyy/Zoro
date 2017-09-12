#!/usr/bin/env python
# encoding: utf-8

import logging

from flask import render_template
from flask import redirect
from flask import url_for
from .  import main
from ..models import User


@main.route('/', methods=['GET', 'POST'])
def index():
    user = User.query.all()
    if user:
        logging.info(user)
    return render_template('index.html')
