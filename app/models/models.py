#!/usr/bin/env python
# encoding: utf-8

from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import BigInteger
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy import Text

from .. import db


class BaseModel:
    """
    Base DB Model
    
    Every table must have isDeleted, then can use the function of query with valid data !!!
    queryAll is the origin query function !!!
    """

    db = db

    # save or update
    def save(self):
        self.db.session.add(self)
        self.db.session.commit()

    def delete(self):
        self.isDeleted = 1
        self.save()

    @classmethod
    def query(cls):
        return cls.query.filter(cls.isDeleted == 0)

    @classmethod
    def queryAll(cls):
        return cls.query


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

    def __repr__(self):
        return '<DrinkRecord %s>' % self.id
