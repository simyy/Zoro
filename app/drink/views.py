#!/usr/bin/env python
# coding=utf-8

from . import drink
from ..models import DrinkRecord


@drink.route('/user/<userId>/drink')
def queryByUserId(userId):
    pass

@drink.route('/user/<userId>/date/<date>/drink')
def queryByUserIdAndDate(userId, date):
    pass

@drink.route('/user/<userId>/date/<date>/drink/status/<status>')
def queryByRequest(user_id, date, status):
    pass
