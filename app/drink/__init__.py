#!/usr/bin/env python
# coding=utf-8

from flask import Blueprint


drink = Blueprint('drink', __name__)
from . import views, errors
