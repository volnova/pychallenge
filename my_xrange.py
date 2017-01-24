# -*- coding: utf-8 -*-
"""Написать собственную реализацию xrange().
Принять во внимание второй опциональный параметр"""


def my_xrange(stop, start=0, step=1):
    """function has a functionality of xrange()"""
    if start:
        stop, start = start, stop
    if all(isinstance(item, int) for item in [start, stop, step]):
        num = start
        while num < stop:
            yield num
            num += step
    else:
        print('Function expected integer argument')
