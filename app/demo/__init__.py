#!/usr/bin/env python
# encoding: utf-8

from flask import Blueprint


demo = Blueprint('demo', __name__)
from . import views, errors

