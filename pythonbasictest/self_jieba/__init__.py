#coding=utf-8
import jieba

import jieba.posseg as pseg

'''
结巴分词的三种分词模式：
Output: 
【全模式】: 我/ 来到/ 北京/ 清华/ 清华大学/ 华大/ 大学 
【精确模式】: 我/ 来到/ 北京/ 清华大学 
【新词识别】：他, 来到, 了, 网易, 杭研, 大厦 (此处，“杭研”并没有在词典中，但是也被Viterbi算法识别出来了) 
【搜索引擎模式】： 小明, 硕士, 毕业, 于, 中国, 科学, 学院, 科学院, 中国科学院, 计算, 计算所, 后, 在, 日本, 京都, 大学, 日本京都大学, 深造

结巴词性：
https://blog.csdn.net/suibianshen2012/article/details/53487157
'''

#结巴分词的3种分词模式
def cut_method():
    seg_list = jieba.cut("我来到北京清华大学",cut_all=True)
    print("Full Mode:", "/ ".join(seg_list)) #全模式
    
    seg_list = jieba.cut("我来到北京清华大学",cut_all=False)
    print("Default Mode:", "/ ".join(seg_list)) #精确模式
    
    seg_list = jieba.cut("他来到了网易杭研大厦") #默认是精确模式
    print(", ".join(seg_list))
    
    seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造") #搜索引擎模式
    print(", ".join(seg_list))
    
#载入自定义词典 
def jieba_loaddict(): 
    jieba.load_userdict("txt/userdict.txt")
    #在程序中动态修改词典  
    jieba.add_word('石墨烯')
    jieba.add_word('凱特琳')
    jieba.del_word('自定义词')
    
    test_sent = (
    "李小福是创新办主任也是云计算方面的专家; 什么是八一双鹿\n"
    "例如我输入一个带“韩玉赏鉴”的标题，在自定义词库中也增加了此词为N类\n"
    "「台中」正確應該不會被切開。mac上可分出「石墨烯」；此時又可以分出來凱特琳了。"
    )
    words = jieba.cut(test_sent)
    print('/'.join(words))
    
    print("="*40)
    
    result = pseg.cut(test_sent)
    
    for w in result:
        print(w.word, "/", w.flag, ", ", end=' ')
    
    print("\n" + "="*40)
    
    terms = jieba.cut('easy_install is great')
    print('/'.join(terms))
    terms = jieba.cut('python 的正则表达式是好用的')
    print('/'.join(terms))
    
    print("="*40)
    # test frequency tune
    testlist = [
    ('今天天气不错', ('今天', '天气')),
    ('如果放到post中将出错。', ('中', '将')),
    ('我们中出了一个叛徒', ('中', '出')),
    ]
    
    for sent, seg in testlist:
        print('/'.join(jieba.cut(sent, HMM=False)))
        word = ''.join(seg)
        #可调节单个词语的词频，使其能（或不能）被分出来。
        print('%s Before: %s, After: %s' % (word, jieba.get_FREQ(word), jieba.suggest_freq(seg, True)))
        print('/'.join(jieba.cut(sent, HMM=False)))
        print("-"*40)
        
#提取关键词
def get_keyword():
    '''
    jieba.analyse.extract_tags(sentence, topK=20, withWeight=False, allowPOS=())
    sentence 为待提取的文本
    topK 为返回几个 TF/IDF 权重最大的关键词，默认值为 20
    withWeight 为是否一并返回关键词权重值，默认值为 False
    allowPOS 仅包括指定词性的词，默认值为空，即不筛选
    jieba.analyse.TFIDF(idf_path=None) 新建 TFIDF 实例，idf_path 为 IDF 频率文件
    '''  
