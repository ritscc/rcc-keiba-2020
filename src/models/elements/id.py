# -*- coding: utf-8 -*-


class ID:
    def __init__(self, id):
        if id is None:
            raise Exception('idがNoneです')
        if id < 0 or type(id) is not int:
            raise Exception('idは0以上の整数を指定してください')

        self.__id = id

    def get_id(self):
        return self.__id
