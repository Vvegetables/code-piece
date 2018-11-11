#coding=utf-8

'''
https://blog.csdn.net/u012735708/article/details/81532407
python 写词云
官方文档：http://amueller.github.io/word_cloud/generated/wordcloud.WordCloud.html#wordcloud.WordCloud
'''
from PIL import Image
import jieba
from wordcloud.color_from_image import ImageColorGenerator
from wordcloud.wordcloud import WordCloud

import matplotlib.pyplot as plt
import numpy as np


class PyCloudWords:
    def __init__(self,font_path='C:/Windows/Fonts/simkai.ttf',background_color="white",max_font_size=200,mask=None):
        self.mask = mask
        self.graph = None
        if mask:
            image = Image.open(mask)
            self.graph = np.array(image)
            self.wc =  WordCloud(font_path=font_path,background_color=background_color,max_font_size=max_font_size,mask=self.graph,collocations=False)

    def generate(self,raw_text=None,frequent_dict=None,):
        if raw_text and isinstance(raw_text,str):
            wl_space_split = " ".join(jieba.cut(raw_text))
            self.wc.generate(wl_space_split)
            plt.imshow(self.wc)
            plt.axis("off")
            plt.show()
            self.wc.to_file("my_wordcloud.png")
            return
        
        if frequent_dict and isinstance(frequent_dict,dict):
            self.wc.generate_from_frequencies(frequent_dict)
            plt.imshow(self.wc)
            plt.axis("off")
            plt.show()
            self.wc.to_file("my_wordcloud.png")
            return
        
        if self.mask:
            image_color = ImageColorGenerator(self.graph)
            self.wc.recolor(color_func=image_color)
        
if __name__ == "__main__":
    test = PyCloudWords(mask="img/heart.png")
    
#     raw_text = '''
#     床前明月光，疑是地上霜。举头望明月，低头思故乡。
#     '''
    with open("nationalsciencefund2.txt","r",encoding="utf-8") as f:
        test.generate(f.read())
#     frequent_dict = {
#         '你好' : 10,
#         "明天" : 4,
#         "快乐" : 12,
#         "开心" : 6,
#         "赵崇旭" : 21,
#     }
#     test.generate(frequent_dict=frequent_dict)
            