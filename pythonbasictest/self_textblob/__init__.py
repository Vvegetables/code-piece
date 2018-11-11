#coding=utf-8
from textblob import TextBlob
from textblob.blob import Word
from textblob.classifiers import NaiveBayesClassifier


def test():
    #创建一个Textblob
    wiki = TextBlob("Python is a high-level, general-purpose programming language.")
    #词性标注
    _tags = wiki.tags
    #获得名词短语
    _nouns = wiki.noun_phrases
    #情感分析
    '''
    sentiment属性返回Sentiment形式的namedtuple（极性，主观性）。 极性分数是在[-1.0,1.0]范围内的浮点数。 
    主观性是在[0.0,1.0]范围内的浮点数，其中0.0是非常客观的，1.0是非常主观的。
    '''
    sentiment_info = wiki.sentiment
    print("情感分析：",sentiment_info)
    
    #分词
    zen = TextBlob("beautiful is better than ugly."
                   "Explicit is better than implicit."
                   "Simple is better than complex.")
    words = zen.words
    #Sentence objects have the same properties and methods as TextBlobs.
    sentences = zen.sentences
    for sentence in zen.sentences:
        print(sentence.sentiment)
    
    #词语变形和词形还原
    #单词单数形式
    print(zen.words[0].singularize())
    #单词复数形式
    print(zen.words[0].pluralize())
    
    w = Word("octopi")
    print(w.lemmatize())
    
    w = Word("went")
    print(w.lemmatize("v")) #通过词形还原
    
    #词汇网！
    #这个等等看！！
    
    
    #检查拼写(准确率为70%)
    b = TextBlob("I havv goood speling!")
    print("检查拼写：",b.correct())
    
    #Word.spellcheck()
    w = Word('falibility')
    w.spellcheck()
    print(w)
    
    #获取单词和名词短语频率
    b.word_counts['I'] #如果以这种方式访问频率，搜索将不区分大小写，并且未找到的单词的频率为0。
    
    b.words.count('I', case_sensitive=True)
    
    #这些方法中的每一种也可以与名词短语一起使用。
    wiki.noun_phrases.count('python')
    
    #可以进行翻译和语言检测(谷歌翻译api)
#     chinese_blob = TextBlob(u"美丽优于丑陋")
#     info = chinese_blob.translate(from_lang="zh-CN", to='en')
#     print(info)
#     print(chinese_blob.detect_language())
    
    #返回n个连续单词的元组列表。
    blob = TextBlob("Now is better than never.")
    print(blob.ngrams(n=3))
    
    
    #文本分类器
    train = [
        ('I love this sandwich.', 'pos'),
        ('this is an amazing place!', 'pos'),
        ('I feel very good about these beers.', 'pos'),
        ('this is my best work.', 'pos'),
        ("what an awesome view", 'pos'),
        ('I do not like this restaurant', 'neg'),
        ('I am tired of this stuff.', 'neg'),
        ("I can't deal with this", 'neg'),
        ('he is my sworn enemy!', 'neg'),
        ('my boss is horrible.', 'neg')
    ]
    
    test = [
        ('the beer was good.', 'pos'),
        ('I do not enjoy my job', 'neg'),
        ("I ain't feeling dandy today.", 'neg'),
        ("I feel amazing!", 'pos'),
        ('Gary is a friend of mine.', 'pos'),
        ("I can't believe I'm doing this.", 'neg')
    ]
    cl = NaiveBayesClassifier(train)
    


def handle_data():
    data = []
    document = None
     


    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    test()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    