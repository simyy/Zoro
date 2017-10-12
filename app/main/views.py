#!/usr/bin/env python
# encoding: utf-8

import logging

from flask import render_template
from flask import redirect
from flask import url_for
from .  import main
from ..models import User
from ..core import SuccessResponse
from ..core import PagerData


@main.route('/', methods=['GET', 'POST'])
def index():
    user = User.query.all()
    if user:
        logging.info(user)
    return render_template('index.html')

@main.route('/json', methods=['GET', 'POST'])
def testJson():
    users = User.query.all()
    datas = [{"id": user.id, "nickName": user.nickName} for user in users]
    data = PagerData(0, 10, datas)
    return SuccessResponse.of(data)
