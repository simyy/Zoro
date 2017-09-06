#!/usr/bin/env python
# coding=utf-8

from . import models


class DrinkRecord(models.DrinkRecord):

    @classmethod
    def queryByUserId(cls, userId):
        return cls.query.filter_by(userId=userId).all()
