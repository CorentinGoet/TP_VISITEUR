import ast


class Program():
    '''
       Class representation of ProgramNode
    '''

    def __init__(self):
        self.declarations = []
        self.statements = []

    def accept(self, visitor):
        visitor.visitProgram(self)

