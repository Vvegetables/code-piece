#coding=utf-8
'''
简单标签：
    simple_tag
'''
import datetime

from django import template

from self_template_define.models import Task


register = template.Library()

#显示当前时间
@register.assignment_tag(name="ctime") # simple_tag效果一样
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)


#展示一个下拉框
@register.inclusion_tag("template/task_template.html")
def task_list():
    task = Task.objects.all()
    return {"task" : task}

#高级自定义
#---------------------------------------#
#定义一个upper标签，酱字符串全部转换成大写
class upperNode(template.Node):
    def __init__(self,nodelist):
        self.nodelist = nodelist
        
    def render(self,context):
        content = self.nodelist.render(context)
        return content.upper()
    

@register.tag
def upper(parser,token):
    nodelist = parser.parse("endupper") #指定结束符
    parser.delete_first_token()
    return upperNode(nodelist)
#-------------------------------------------#

#第二弹
#----------------------------------------#

class CurrentTimeNode(template.Node):
    def __init__(self, format_string):
        self.format_string = format_string

    def render(self, context):
        return datetime.datetime.now().strftime(self.format_string)


def do_current_time(parser,token):
    try:
        tag_name,format_string = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            "%r tag requires a single argument" % token.contents.split()[0]
        )
    if not (format_string[0] == format_string[-1] and format_string[0] in ('"', "'")):
        raise template.TemplateSyntaxError(
            "%r tag's argument should be in quotes" % tag_name
        )
    return CurrentTimeNode(format_string[1:-1])


#----------------------------------------#


#自定义模板过滤器
@register.filter(name="cut")
def cut(value,args):
    return value.replace(args,"")

@register.filter
def lower(value):
    return value.lower()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    