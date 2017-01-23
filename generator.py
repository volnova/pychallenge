# -*- coding: utf-8 -*-
"""Написать «вечный» генератор, который выдаёт всё время одно значение"""


def gen(my_value):
    """function return generator"""

    while True:
        yield my_value


if __name__ == '__main__':
    gen(1)
