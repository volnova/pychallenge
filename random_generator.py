# -*- coding: utf-8 -*-
"""Написать генератор строк случайной длины,
состоящих из случайных символов (буквы и цифры), и валидатор для него.
Валидатор (который должен тоже быть генератором) на вход принимает три
параметра: длину строки, количество строк, которые необходимо получить,
и количество цифр, которое должно быть в строке. В случае если не
задана длина строки - просто вывести необходимое количество строк.
Минимальное количество цифр в строке должно быть 1. В случае если не
указано количество строк - завершить выполнение программы
с сообщением об ошибке."""

import random
import string


def random_generator(my_len):
    """function return generator of random strings"""
    chars = string.ascii_letters + string.digits
    while True:
        yield ''.join(random.choice(chars) for _ in range(my_len))


def validator(num_of_str, len_of_str=0, num_of_digits=1):
    """function return random string if it's valid"""

    if not len_of_str:
        len_of_str = random.randint(1, 80)

    if all(isinstance(item, int) for item in
           [num_of_str, len_of_str, num_of_digits])\
            and len_of_str >= num_of_digits:
        while num_of_str:
            for i in random_generator(len_of_str):
                if sum(c.isdigit() for c in i) == +num_of_digits:
                    yield i
                    num_of_str -= 1
                    break
    else:
        print('Function expected integer argument and number of '
              'digits is must be less or equal than lenght of srting')
