#!/usr/bin/env python
# encoding: utf-8

import logging

from flask import render_template
from flask import redirect
from flask import url_for
from .  import demo
from ..models import User
from ..core.response import SuccessResponse
from ..core.response import PagerData


@demo.route('/demo', methods=['GET', 'POST'])
def index():
    users = User.query.all()
    if not users:
        users = [User()]
    logging.info(users)
    return render_template('index.html', user=users[0])


@demo.route('/demo/json', methods=['GET', 'POST'])
def testJson():
    users = User.query.all()
    data = PagerData(0, 10, users)
    return SuccessResponse.of(data)
