class Program():
    '''
       Class representation of ProgramNode
    '''

    def __init__(self):
        self.__declarations = []
        self.__statements = []

    def setDeclarations(self, declarations):
        self.__declarations = declarations

    def setStatements(self, statements):
        self.__statements = statements

    def getDeclarations(self):
        return self.__declarations

    def getStatements(self):
        return self.__statements


    def accept(self, visitor):
        return visitor.visitProgram(self)