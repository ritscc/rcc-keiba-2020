# -*- coding: utf-8 -*-


class ID:
    def __init__(self, id_):
        if id_ is None:
            raise Exception('idがNoneです')
        if id_ < 0 or type(id_) is not int:
            raise Exception('idは0以上の整数を指定してください')

        self.__id = id_

    def get_id(self):
        return self.__id
