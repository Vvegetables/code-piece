from logging import Logger
from typing import Dict, Tuple, List, NewType, Callable, TypeVar, Sequence, \
    Generic


ConnectionOptions = Dict[str,str]
Address = Tuple[str,int]
Server = Tuple[Address,ConnectionOptions]

#type alias
def broadcast_message(message:str,servers:List[Server]) -> None:
    print(message,servers)

#newtype
UserId = NewType('UserId',int)
def get_user_name(user_id=UserId) -> str:
    print(user_id)

#class AdminUserId(UserId): pass

#callable
def feeder(get_next_item:Callable[[],str]) -> None:
    pass

#generics
T = TypeVar('T')

def first(l:Sequence[T]) -> T:
    return l[0]

class LoggedVar(Generic[T]):
    def __init__(self, value: T, name: str, logger: Logger) -> None:
        self.name = name
        self.logger = logger
        self.value = value

    def set(self, new: T) -> None:
        self.log('Set ' + repr(self.value))
        self.value = new

    def get(self) -> T:
        self.log('Get ' + repr(self.value))
        return self.value

    def log(self, message: str) -> None:
        self.logger.info('%s: %s', self.name, message)

def loggedvar_test(p : LoggedVar):
    print(p)

if __name__ == "__main__":
    broadcast_message("message", "servers")
    #-------------#
    some_id = UserId(333)
    get_user_name(some_id + some_id)
    get_user_name(UserId([]))
    print(some_id)
    #--------------#
    
    list_ = [1,2,3,4]
    print(first(list_))
    
    #--------------#
    loggedvar_test("test")
    
    