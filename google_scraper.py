# -*- coding: utf-8 -*-
"""Написать программу, которая на вход принимает строку от пользователя
(на любом языке, проверить как минимум на русском и английском), дальше
делает запрос в гугл, и выдает первые 3 ссылки из поиска по данному запросу.
Протестировать код, сделать так чтобы при кривом запросе работа программы не
ломалась, а выводился новый запрос строки, до тех пор пока не будут
выведены 3 результата"""

import requests
from lxml import html


def request_to_site():
    """Function do search to google.com by user's request"""

    my_str = raw_input('Please, enter your request here: ')
    try:
        request = requests.get('https://www.google.com/search',
                               params={'q': my_str})
        try:
            root = html.fromstring(request.text)
            results_list = root.xpath(".//*[@class='kv']/cite")
            for i in range(3):
                print(results_list[i].xpath('string()'))
        except IndexError:
            print "At your request no results were found. "\
                "Please, check your request."
            request_to_site()
    except requests.exceptions.ConnectionError:
        print "No connection to site"
        exit(1)


if __name__ == '__main__':
    request_to_site()
