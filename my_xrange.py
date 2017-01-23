# -*- coding: utf-8 -*-
"""Написать собственную реализацию xrange().
Принять во внимание второй опциональный параметр"""


def my_xrange(*args):
    """function has a functionality of xrange()"""

    if len(args) == 1:
        num = 0
        while num < args[0]:
            yield num
            num += 1
    elif len(args) == 2:
        num = args[0]
        while num < args[1]:
            yield num
            num += 1
    elif len(args) == 3:
        num = args[0]
        while num < args[1]:
            yield num
            num += args[2]
