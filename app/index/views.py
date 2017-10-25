#!/usr/bin/env python
# encoding: utf-8

import logging

from flask import render_template
from flask import redirect
from flask import url_for
from ..models import User
from ..core.response import SuccessResponse
from ..core.response import PagerData

from . import index


@index.route('/', methods=['GET'])
def index():
    logging.info("route index")
    return render_template('index.html')
