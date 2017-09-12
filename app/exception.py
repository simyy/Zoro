#!/usr/bin/env python
# coding=utf-8

class ZoroException(Exception):

    def __init__(self, code, msg):
        self.code = code
        self.msg = msg

    def __str__(self):
        return '<%s %s>' % (self.__class__.__name__, self.code)


class OneDrinkException(ZoroException):
    pass



def test():
    z = OneDrinkException(1, 2)
    print(z)
