import os
import sys

import django
from django.template import Context, Template


dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir_path)
os.chdir(dir_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ddap.settings")
django.setup()


def test_template():
    t = Template("My name is {{name}}")
    c = Context({"name":"Zcxu"})
    result = t.render(c)
    print(result)
    '''
        person = dict(name = xxx,age=20)
        person.name
        list_ = [1,2,3]
        list_.0
        
    '''
    
    '''
    #https://blog.csdn.net/zhangxinrun/article/details/8095118/
    #silent_variable_failure = True，
    Class SlientAssetionError(AssertionError):
        silent_variable_failure = True
    class PersonClass4:
        def first_name(self):
            raise SilentAssertionError #出错的变量会渲染成空string
    '''
    
    '''
    alters_data=True
    '''
    
    '''
    {% for %}标签内置了一个forloop模板变量，这个变量含有一些属性可以提供给你一些关于循环的信息
    '''



if __name__ == "__main__":
    test_template()
