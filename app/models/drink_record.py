#!/usr/bin/env python
# coding=utf-8

from .base import *


class DrinkRecord(db.Model, BaseModel):

    __tablename__ = 'drink_record'

    id = Column(BigInteger, primary_key=True)
    userId = Column(BigInteger)
    status = Column(Integer)
    expireTime = Column(DateTime)
    isDeleted = Column(Integer)

    def __init__(self, id, userId, status, expireTime):
        self.id = id
        self.userId = userId
        self.status = status
        self.expireTime = expireTime

    @classmethod
    def queryByUserId(cls, userId):
        return cls.query.filter_by(userId=userId).all()

    @classmethod
    def queryByDate(cls, date):
        pass

