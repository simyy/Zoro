#!/usr/bin/env python
# encoding: utf-8

from flask import Blueprint


index = Blueprint('index', __name__)
from . import views
