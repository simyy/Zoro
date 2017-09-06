#!/usr/bin/env python
# coding=utf-8

from . import models


class User(models.User):

    def save(self):
        self.db.session.add(self)
        self.db.session.commit()
