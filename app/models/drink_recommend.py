#!/usr/bin/env python
# coding=utf-8

from .base import *


class DrinkRecommend(db.Model, BaseModel):

    __tablename__ = 'drink_recommend'

    id = Column(BigInteger, primary_key=True)
    expireTime = Column(DateTime)

    def __init__(self, id, userId):
        self.id = id
        self.userId = userId


