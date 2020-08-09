# -*- coding: utf-8 -*-


class Name:
    def __init__(self, name):
        if name is None:
            raise Exception('nameがNoneです')
        if name == '' or type(name) is not str:
            raise Exception('nameは長さ1以上の文字列を指定してください')

        self.__name = name

    def get_name(self):
        return self.__name
