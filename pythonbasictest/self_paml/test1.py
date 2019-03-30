import yaml
'''
导入yaml文件
'''
def test1():
    result = yaml.load("""
    - Hesperiidae
    - Papilionidae
    - Apatelodidae
    - Epiplemidae
    """)
    print(result)
    print(type(result))
    
    result2 = yaml.load("""
    a: 1
    b: 
      c: 10
      d: 20
    """)
    print(result2)
    print(type(result2))

def test2():
    #: > 表示最后一行保留换行符
    documents = """
---
name: The Set of Gauntlets 'Pauraegen'
description: >
    A set of handgear with sparks that crackle
    across its knuckleguards.
---
name: The Set of Gauntlets 'Paurnen'
description:
 A set of gauntlets that gives off a foul,
 acrid odour yet remains untarnished.
---
name: The Set of Gauntlets 'Paurnimmen'
description: >
 A set of handgear, freezing with unnatural cold.
"""
    for data in yaml.load_all(documents):
        print(data)
        
def test3():
    documents = """
none: [~, null]
bool: [true, false, on, off]
int: 42
float: 3.14159
list: [LITE, RES_ACID, SUS_DEXT]
dict: {hp: 13, sp: 5}
    """
    print(yaml.load(documents))
    
#使用!!python/object标记构建Python类的实例
class Hero:
    def __init__(self, name, hp, sp):
        self.name = name
        self.hp = hp
        self.sp = sp
    def __repr__(self):
        return "%s(name=%r, hp=%r, sp=%r)" % (
            self.__class__.__name__, self.name, self.hp, self.sp)

def test4():
    print(yaml.load("""
    !!python/object:__main__.Hero
    name: Welthyr Syxgon
    hp: 1200
    sp: 0
    """))
    
    print(yaml.dump(Hero(name="SpiderMan", hp=100, sp=1000)))

#您可以定义自己的特定于应用程序的标记。最简单的方法是定义一个子类yaml.YAMLObject
class Monster(yaml.YAMLObject):
    yaml_tag = u'!Monster'
    def __init__(self, name, hp, ac, attacks):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.attacks = attacks
    def __repr__(self):
        return "%s(name=%r, hp=%r, ac=%r, attacks=%r)" % (
            self.__class__.__name__, self.name, self.hp, self.ac, self.attacks)

def test5():
    print(yaml.load("""
--- !Monster
name: Cave spider
hp: [2,6]    # 2d6
ac: 16
attacks: [BITE, HURT]
    """))
    
    print(
        yaml.dump(
            Monster(
                name='Cave lizard', hp=[3,6], ac=16, attacks=['BITE','HURT']
                )
            )
        ) 
     
if __name__ == "__main__":
    test4()

