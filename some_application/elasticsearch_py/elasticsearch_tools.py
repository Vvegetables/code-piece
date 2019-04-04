class ESQuery:
    def __init__(self):
        self._must = []
        self._must_not = []
        self._should = []
        self._filter = []
    
    def new_instance(self):
        return self.__class__()
    
if __name__ == "__main__":
    pass
    