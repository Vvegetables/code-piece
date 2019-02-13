#coding=utf-8
import datetime
from json import JSONEncoder
import json


class TupleJsonEncode(JSONEncoder):
    '''
    使得tuple也能json化再传给前端
    '''
    def default(self, obj):
        if isinstance(obj, tuple):
            return list(obj)
        return JSONEncoder.default(self, obj)

    
class TimeJsonEncode(TupleJsonEncode):
    '''
    JSONEncoder subclass that knows how to encode date/time, decimal types, and
    UUIDs.
    '''
    
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            value = format(obj, "%Y-%m-%d %H:%M:%S")
            return value
        elif isinstance(obj, datetime.date):
            value = format(obj, "%Y-%m-%d")
            return value
        else:
            return super().default(obj)

if __name__ == "__main__":
    data = {
        "times" : datetime.datetime.now(),
        "nums" : 1,
        "tuple_data" : (1,2,3)
    }
    res = json.dumps(data, cls=TimeJsonEncode)
    print(res)
    
    