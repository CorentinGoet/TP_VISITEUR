class ifStatement():
    '''
       Class representation of IfStatement
    '''

    def __init__(self):
        self.__expression = None
        self.__statement = None
        self.__else_expression = None

    def setExpression(self, expression):
        self.__expression = expression

    def setStatement(self, statement):
        self.__statement = statement

    def setElseExpression(self, expression):
        self.__else_expression = expression

    def getExpression(self):
        return self.__expression

    def getStatement(self):
        return self.__statement

    def getElseExpression(self):
        return self.__else_expression

    def accept(self, visitor):
        visitor.visitIfStmt(self)
