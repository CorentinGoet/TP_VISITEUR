"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""

import ast

class Statements:
    """
    Class representation of the Statement Node.
    """

    def __init__(self):
        self.statement = []

    def accept(self, visitor):
        visitor.visitStatements(self)

    def addStatement(self, statement):
        self.statement.append(statement)



if __name__ == '__main__':
    pass
