#coding=utf-8
from enum import Enum, auto


class RequestCtrlMethods(Enum):
    delete = auto()
    add = auto()
    update = auto()
    query = auto()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.__str__()

if __name__ == "__main__":
    for k in RequestCtrlMethods:
        print(k.name)
        print(k.value)