from ladon.compat import PORTABLE_STRING
from ladon.ladonizer import ladonize

'''
pip install ladon
编写 Calculator类
运行测试服务器 python3 E:\program\py366\Scripts\ladon-3.6-ctl.py testserve E:\github_repo\python_basic\some_application\ladon_test\__init__.py -p 8080
'''

class Calculator:
    @ladonize(int, int, rtype=int)
    def add(self, a, b):
        return a + b
    
    @ladonize(rtype=PORTABLE_STRING)
    def extract_remote_addr(self, **exports):
        '''
        Fetch the client's remote address
        @rtype: the address
        '''
        return exports['REMOTE_ADDR']