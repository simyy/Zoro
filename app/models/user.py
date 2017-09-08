#!/usr/bin/env python
# coding=utf-8

from .base import *


class User(db.Model, BaseModel):

    __tablename__ = 'user'

    id   = Column(BigInteger, primary_key=True)
    unionId = Column(String(256))
    nickName = Column(String(256))
    avatarUrl = Column(String(1024))
    gender = Column(Integer)
    province = Column(String(128))
    city = Column(String(128))
    country = Column(String(128))
    isDeleted = Column(Integer)

    def __init__(self, unionId, nickName, avatarUrl, gender, province=None, city=None, country=None):
        self.unionId = unionId 
        self.nickName = nickName
        self.avatarUrl = avatarUrl
        self.gender = gender
        self.province = province
        self.city = city
        self.country = country

    def __repr__(self):
        return '<User %s>' % self.id

    @classmethod
    def queryByUnionId(cls, unionId):
        return cls.query.filter_by(unionId=unionId).first()

    @classmethod
    def queryById(cls, id):
        return cls.query.filter_by(id=id).first()
