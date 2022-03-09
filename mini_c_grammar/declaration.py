"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""
from enum import Enum


class Declaration:
    """
    Class representation of a Declaration.
    """

    def __init__(self, type=None, identifier=None, integer=None):
        self.type = type
        self.identifier = identifier
        self.integer = integer

    def accept(self, visitor):
        """
        Method to accept vist by the visitor
        :param visitor: visitor
        :return: None
        """
        visitor.visitDeclaration(self)



class Types(Enum):
    """
    Enum of types.
    """
    INT = 1
    BOOL = 2
    FLOAT = 3
    CHAR = 4

if __name__ == '__main__':
    pass
