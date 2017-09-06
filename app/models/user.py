#!/usr/bin/env python
# coding=utf-8

from . import models


class User(models.User):

    @classmethod
    def queryByUnionId(cls, unionId):
        return cls.query.filter_by(unionId=unionId).first()

    @classmethod
    def queryById(cls, id):
        return cls.query.filter_by(id=id).first()
