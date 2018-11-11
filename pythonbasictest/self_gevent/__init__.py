#coding=utf-8

'''
gevent，它是一个并发网络库。它的协程是基于greenlet的，并基于libev实现快速事件循环（Linux上是epoll，
FreeBSD上是kqueue，Mac OS X上是select）。有了gevent，协程的使用将无比简单，
你根本无须像greenlet一样显式的切换，每当一个协程阻塞时，程序将自动调度，gevent处理了所有的底层细节。
'''

'''
#生成器：    http://python.jobbole.com/87154/
#greenlet： http://python.jobbole.com/87182/
#gevent： http://python.jobbole.com/87181/
'''


