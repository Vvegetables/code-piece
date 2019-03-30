'''
导出yaml文件
'''
import yaml
document = '''
a: 1
b:
    c: 3
    d: 4
'''
#到处yaml格式文件
k = yaml.dump(yaml.load(document), default_flow_style=False)
# k 是字符串类型，不是dict
print(k)