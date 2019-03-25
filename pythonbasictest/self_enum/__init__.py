from enum import Enum, unique, auto, IntEnum

#Enums are not normal Python classes. 
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    #alias
    PURPLE = 3 #bind to BLUE
    
    
#access to attribute
print(Color.RED)
print(repr(Color.RED))

#iterate
for c in Color:
    print(c)
print("---------")
#programmatic access
print(Color(1))
print(Color["RED"])

member = Color.BLUE
print(member.name)
print(member.value)

#unique assurance
try:
    @unique
    class Mistake(Enum):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 3
except Exception as e:
    print(e)
    
    
#using automatic values
class AutoValue(Enum):
    VALUE1 = auto()
    VALUE2 = auto()
    VALUE3 = auto()

print(list(AutoValue))  

print("-----------------")
print([name for name, member in Color.__members__.items()]) 
    
#Functional API
Animal = Enum('Animal',"ANT BEE CAT DOG")
print(type(Animal.ANT))

#the variation of enum
class Shape(IntEnum):
    CIRCLE = 1
    SQUARE = 2

class Request(IntEnum):
    POST = 1
    GET = 2

print(type(Shape.CIRCLE | Request.GET))
    
    
    
    
    
    
    
