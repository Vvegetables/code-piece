from enum import Enum

class TestEnum(Enum):
    CREATE = 1

class A:
    a = "a"
    def _new(self):
        print(type(self))
        print(self.__class__)
        return self.__class__()
    
if __name__ == "__main__":
#     raise AttributeError("CREATE") from None
    print(TestEnum.CREATE.name)
    AA = A()
    AA2 = AA._new()
    print(AA2.a)
    print(AA.a)
    print(AA.__class__().a)