#coding=utf-8
'''
《deep in python》
python 处理命令行参数
py2 使用optparse
py3 使用argparse

https://docs.python.org/2/library/argparse.html#module-argparse

'''
import argparse

'''
常用参数：ArgumentParser()
prog ：文件名，默认为sys.argv[0]，用来在help信息中描述程序的名称。
usage ：描述程序用途的字符串
description ：help信息前显示的信息
epilog ：help信息之后显示的信息
parents ：由ArgumentParser对象组成的列表，它们的arguments选项会被包含到新ArgumentParser对象中。(类似于继承)
formatter_class ：help信息输出的格式，为了美观…
prefix_chars ：参数前缀，默认为’-‘(最好不要修改)
fromfile_prefix_chars ：前缀字符，放在文件名之前
conflict_handler ：解决冲突的策略，默认情况下冲突会发生错误，(最好不要修改)
add_help ：是否增加-h/-help选项 (默认为True)，一般help信息都是必须的。设为False时，help信息里面不再显示-h –help信息
argument_default： - (default: None)设置一个全局的选项的缺省值，一般每个选项单独设置，基本没用
'''
parser = parser = argparse.ArgumentParser(prog='my - program', usage='%(prog)s [options] usage',description = 'my - description',epilog = 'my - epilog')
#打印帮助信息
parser.print_help()

'''
添加参数选项:ArgumentParser.add_argument()
add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])
常用参数：
name or flags - 选项字符串的名称或列表，例如 foo或-f， - foo。
action - 在命令行遇到此参数时要采取的基本操作类型。
    -store_const 值存放在const中
    -store_true和store_false 值存为false 和 true
    -append： 存为列表，可以有多个参数
    -append_const:存为列表，会根据const关键字进行添加
    -count：统计参数出现的次数
    -help： help信息
    -version：版本
    
nargs - 应该使用的命令行参数的数量。
const - 某些操作和nargs选择所需的常量值。
default - 如果命令行中不存在参数，则生成的值。
type - 应转换命令行参数的类型。
choices - 参数允许值的容器。
required - 是否可以省略命令行选项（仅限选项）。
help - 对参数的作用的简要描述。
metavar - A name for the argument in usage messages。
dest - 要添加到parse_args（）返回的对象的属性的名称。

'''
parser.add_argument('-f','--file')
parser.add_argument("name")

'''
    解析表达式
    ArgumentParser.parse_args()
当参数过多时，可以将参数放到文件中读取，ArgumentParser.parse_args([‘-f’, ‘foo’, ‘@args.txt’])解析时会从文件args.txt读取，相当于 [‘-f’, ‘foo’, ‘-f’, ‘bar’]
'''
#args = []
parser.parse_args()
