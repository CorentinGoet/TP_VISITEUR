class Number():
    '''
       Class representation of TypeNode
    '''

    def __init__(self):
        self.__value = None

    def setValue(self, value):
        self.__value = value

    def getValue(self):
        return self.__value


    def accept(self, visitor):
        return visitor.visitNumber(self)