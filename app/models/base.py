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

    def _repr__(self):
        return '<%s %s>' % (type(self).__name__ ,self.id)  

    @classmethod
    def deleteById(cls, id):
        res = cls.query.filter_by(id=id).first()
        if res:
            res.delete()

    @classmethod
    def query(cls):
        return cls.query.filter(cls.isDeleted == 0)

    @classmethod
    def queryAll(cls):
        return cls.query

    @classmethod
    def queryById(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def queryByIds(cls, ids):
        return cls.query.filter(cls.id.in_(ids)).all()

