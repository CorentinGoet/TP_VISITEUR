"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""


class Assignment:
    """
    Class representation of the Assignment node.
    """

    def __init__(self, identifier=None, expression=None):
        self.identifier = identifier
        self.expression = expression

    def getIdentifier(self):
        return self.identifier

    def setIdentifier(self, identifier):
        self.identifier = identifier

    def getExpression(self):
        return self.expression

    def setExpression(self, expression):
        self.expression = expression


if __name__ == '__main__':
    pass
