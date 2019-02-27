#coding=utf-8
import redis

'''
使用单个连接
'''
#decode_responses=True表示写入的键值对中的value为str类型，不加表示bytes类型
#port默认是6379
def test_1():
    r_ins = redis.Redis(host='localhost', port=6379, decode_responses=True)
    r_ins.set('name', '张三')
    print(r_ins.get('name'))
    
'''
使用连接池
使用connection pool来管理对一个redis server的所有连接，避免每次建立、释放连接的开销。
默认，每个Redis实例都会维护一个自己的连接池。
'''
def test_2():
    pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
    r = redis.Redis(connection_pool=pool)
    r.set('gender', 'male')
    print(r.get('gender'))
    

#二进制转换
def str2bin(text:str):
    container = []
    for t in text:
        num = ord(t)
        container.append(bin(num).replace('b', ''))
    return container

def string_method(r:redis):
    #批量设置值
    r.mset(
        {
            'k1': 'v1',
            'k2': 'v2'
        }
    )
    r.mset(k3="v3", k4="v4")
    
    #批量获取值
    r.mget("k1")
    r.mget("k3", "k4")
    
    #设置新的值并且获取原来的值
    r.getset('k1', 'new_v1')
    
    #获取子序列（根据字节获取），一个字母一个字节，一个汉字3个字节
    r.set('getrange', "字母aa")
    r.getrange('getrange', 0, 3)
    
    #修改字符串内容，从制定字符串索引开始向后替换（新值太长时，则向后添加）
    r.setrange('getrange', 3, '意')
    
    #对name对应值的二进制表示的位进行操作
    r.setbit('k1', 1, 0)
    
    #获取name对应的值的二进制表示中的某位的值（0或者1）
    r.getbit('k1', 0)
    
    #获取name对应的值的二进制表示中1的个数
    r.bitcount('getrange', 0, 8)
    
    #...还有很多
    
    #返回name对应值的字节长度
    r.strlen('k3')
    
    #自增name对应的值，值的大小=amount当name不存在的时候，则创建name=amount
    r.set('num', 2)
    r.incr('num', amount=1)
    
    #自增浮点型
    r.set('float_', "12.3")
    print(r.incrbyfloat("float_", amount=1.0))
    
    #自减数
    r.decr('float_', amount=1)
    
    #在name对应的值后面追加内容
    r.append('k4', 'female')
    print(r.mget('k4'))
    print(r.get('k4'))
    
def hash_test(r:redis):
    #当个增加-修改；没有就新增，有就修改
    r.hset('hash1', 'k1', 'v1')
    r.hset('hash1', 'k2', 'v2')
    
    #批量增加
    r.hmset('hash2',
            {
                'k2': 'v2',
                'k3': 'v3'
            }
        )
    
    #获取hash中所有的key
    print(r.hkeys('hash1'))
    
    #获取hash中所有的value
    print(r.hvals('hash1'))
    
    #获取单个hash的key的对应的值
    print(r.hget('hash1', 'k1'))
    
    #获取单个hash的多个key的对应的值
    print(r.hmget('hash1', 'k1', 'k2'))
    
    #如果key不存在则新建，否则不新建
    r.hsetnx('hash1', 'k1', 'v3')
    
    #取出所有的键值对
    print(r.hgetall('hash1'))
    
    #得到所有键值对的格式hash长度
    print(r.hlen('hash1'))
    
    #判断成员是否存在
    print(r.hexists('hash1', 'k4'))
    
    print(r.hdel("hash1", "k1"))
    
    #自增自减整数
    r.hincrby('hash1', 'k1', amount=-1)
    
    #自增自减浮点数
    r.hincrbyfloat('hash1', 'k1', amount=1)
    
    #取值查看器，分片读取，增量式迭代读取，对数据大的数据非常有用,当返回的cursor=0表示读取完毕
    cursor1, data1 = r.hscan("hash1", cursor=0, match=None, count=None)
    cursor2, data2 = r.hscan("hash1", cursor=cursor1, match=None, count=None)
    
    for item in r.hscan_iter('hash1'):
        print(item)

#自定义增量迭代
def list_iter(r:redis, name):
    list_count = r.llen(name)
    for index in range(list_count):
        yield r.lindex(name, index)
  
def list_test(r:redis):
    #从队列的头部加入数据
    r.lpush("list1", 11, 22, 33)
    
    #按索引取出数据
    print(r.lrange('list1', 0, -1))
    
    #从队列的尾部加入数据
    r.rpush("list2", 11, 22, 33)
    
    #列表的长度
    print(r.llen("list2"))
    
    #在对应值前插入一个新的值
    r.linsert("list2", 'before', "11", "00")
    r.linsert('list2', "after", "33", "44")
    
    #指定索引号进行修改
    r.lset('list2', 0, -11)
    
    #指定值进行删除
    '''
    num = 0,删除所有
    num = 2,从前往后删除2个
    num = -2,从后往前删除2个
    '''
    r.lrem('list2', "11", num=1)
    
    #删除并返回;从列表的左侧第一个位置
    r.lpop('list2')
    #删除并返回;从列表的右侧第一个位置
    r.rpop('list2')
    
    #删除在索引之外的值
    r.ltrim("list2", 0, 2)
    
    #根据索引号取值
    r.lindex("list2", 0)
    
    #移动，从一个列表移到另一个列表
    r.rpoplpush(src='list2', dst='list1')
    
    #移动，从一个列表移到另一个列表，可以设置超市
    '''
    timeout = 0 表示永远阻塞
            > 0 表示阻塞等待相应的时间
    '''
    r.brpoplpush(src="list2", dst="list1", timeout=0)
    
    #一次移除多个列表
    r.blpop(['list1', 'list2'], timeout=10)
    r.brpop(['list1', 'list2'], timeout=10)

def set_test(r:redis):
    r.sadd("set1", 33, 44, 55, 66)  # 往集合中添加元素
    print(r.scard("set1"))  # 集合的长度是4
    print(r.smembers("set1"))   # 获取集合中所有的成员
    print(r.sscan("set1")) # 获取集合中所有的成员--元组形式
    
    #获取集合中所有的成员--迭代器的方式
    for i in r.sscan_iter("set1"):
        print(i)
    
    print(r.sdiff("set1", "set2"))   # 在集合set1但是不在集合set2中
    
    #差集--差集存在一个新的集合中
    r.sdiffstore("set3", "set1", "set2")    # 在集合set1但是不在集合set2中
    
    print(r.sinter("set1", "set2")) # 取2个集合的交集
    
    #.交集--交集存在一个新的集合中
    print(r.sinterstore("set3", "set1", "set2")) # 取2个集合的交集
    
    #并集
    print(r.sunion("set1", "set2")) # 取2个集合的并集
    
    #并集--并集存在一个新的集合
    print(r.sunionstore("set3", "set1", "set2")) # 取2个集合的并集
    
    #判断是否是集合的成员 类似in
    print(r.sismember("set1", 33))  # 33是集合的成员
    
    #将某个成员从一个集合中移动到另外一个集合
    r.smove("set1", "set2", 44)
    
    #删除--随机删除并且返回被删除值
    print(r.spop("set2"))   # 这个删除的值是随机删除的，集合是无序的
    
    #删除--指定值删除
    print(r.srem("set2", 11))   # 从集合中删除指定值 11
    
#有序set
def zset_test(r:redis):
    r.zadd("zset1", n1=11, n2=22)
    r.zadd("zset2", 'm1', 22, 'm2', 44)
    print(r.zcard("zset1")) # 集合长度
    print(r.zcard("zset2")) # 集合长度
    print(r.zrange("zset1", 0, -1))   # 获取有序集合中所有元素
    print(r.zrange("zset2", 0, -1, withscores=True))   # 获取有序集合中所有元素和分数
    #从大到小排序(同zrange，集合是从大到小排序的)
    print(r.zrevrange("zset1", 0, -1))    # 只获取元素，不显示分数
    #按照分数范围获取name对应的有序集合的元素
    for i in range(1, 30):
        element = 'n' + str(i)
        r.zadd("zset3", element, i)
    print(r.zrangebyscore("zset3", 15, 25)) # # 在分数是15-25之间，取出符合条件的元素
    print(r.zrangebyscore("zset3", 12, 22, withscores=True))    # 在分数是12-22之间，取出符合条件的元素（带分数）

    #按照分数范围获取有序集合的元素并排序（默认从大到小排序）
    print(r.zrevrangebyscore("zset3", 22, 11, withscores=True)) # 在分数是22-11之间，取出符合条件的元素 按照分数倒序
    
    #获取所有元素--默认按照分数顺序排序
    print(r.zscan("zset3"))
    
    #获取所有元素--迭代器
    for i in r.zscan_iter("zset3"): # 遍历迭代器
        print(i)
        
    #获取name对应的有序集合中分数 在 [min,max] 之间的个数
    print(r.zrange("zset3", 0, -1, withscores=True))
    print(r.zcount("zset3", 11, 22))
    
    #自增name对应的有序集合的 name 对应的分数
    r.zincrby("zset3", "n2", amount=2)    # 每次将n2的分数自增2
    print(r.zrange("zset3", 0, -1, withscores=True))
    
    #获取值的索引号
    print(r.zrank("zset3", "n1"))   # n1的索引号是0 这里按照分数顺序（从小到大）
    print(r.zrank("zset3", "n6"))   # n6的索引号是1
    print(r.zrevrank("zset3", "n1"))    # n1的索引号是29 这里安照分数倒序（从大到小）
    
    #删除--指定值删除
    r.zrem("zset3", "n3")   # 删除有序集合中的元素n3 删除单个

    #删除--根据排行范围删除，按照索引号来删除
    r.zremrangebyrank("zset3", 0, 1)  # 删除有序集合中的索引号是0, 1的元素
    
    #删除--根据分数范围删除
    r.zremrangebyscore("zset3", 11, 22)   # 删除有序集合中的分数是11-22的元素
    
    #获取值对应的分数
    print(r.zscore("zset3", "n27"))   # 获取元素n27对应的分数27
    
    
def other_test(r:redis):
    '''
 删除
delete(*names)
根据删除redis中的任意数据类型（string、hash、list、set、有序set）
    '''
    r.delete('gender')
    
    r.exists('gender') #判断是否存在
     
    r.keys("foo*") #获得key
    
    r.lpush("list5", 11, 22)
    r.expire("list5", time=3) #设置操作的过期时间
    
    r.rename("list5", "list5-1") #重命名
    
    r.randomkey() #随机获得一个key
    
    r.type("set1") #查看类型
    
    r.dbsize() #当前redis包含多少条数据
    
    r.save() #执行检查点操作，将数据写回磁盘，保存时阻塞
    
    r.flushdb() #清空所有数据
    
'''
redis默认在执行每次请求都会创建（连接池申请连接）和断开（归还连接池）一次连接操作，
如果想要在一次请求中指定多个命令，则可以使用pipline实现一次请求指定多个命令，并且默认情况下一次pipline 是原子性操作。
管道（pipeline）是redis在提供单个请求中缓冲多条服务器命令的基类的子类。它通过减少服务器-客户端之间反复的TCP数据库包，从而大大提高了执行批量命令的功能。
'''
def pipe_test(r:redis):
    # pipe = r.pipeline(transaction=False)    # 默认的情况下，管道里执行的命令可以保证执行的原子性，执行pipe = r.pipeline(transaction=False)可以禁用这一特性。
    # pipe = r.pipeline(transaction=True)
    pipe = r.pipeline() # 创建一个管道
    
    pipe.set('name', 'jack')
    pipe.set('role', 'sb')
    pipe.sadd('faz', 'baz')
    pipe.incr('num')    # 如果num不存在则vaule为1，如果存在，则value自增1
    pipe.execute()
    
    print(r.get("name"))
    print(r.get("role"))
    print(r.get("num"))
    
    pipe.set('hello', 'redis').sadd('faz', 'baz').incr('num').execute()

        

    
    
if __name__ == "__main__":
    test_2()
    
    
    
