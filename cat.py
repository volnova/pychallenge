# -*- coding: utf-8 -*-
"""Написать программу cat не ограничивая количества файлов-аргументов"""


def cat_files(*args):
    """function cat files in console"""
    try:
        for filename in args:
            with open(filename, 'r') as my_file:
                read_data = my_file.read()
                print(read_data)
    except IOError as my_excp:
        print(my_excp)
    except TypeError:
        print('Function expected string name of files as arguments')
