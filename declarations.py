"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""

import ast

class Declarations:
    """
    Class representation of the Declarations Node.
    """

    def __init__(self):
        self.declaration = []

    def accept(self, visitor):
        return visitor.visitDeclarations(self)

    def addDeclaration(self, declaration):
        self.declaration.append(declaration)



if __name__ == '__main__':
    pass
