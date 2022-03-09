"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""


class Block:
    """
    Class representation of the Block node.
    """
    def __init__(self, statements=None):
        self.statements = statements

    def getStatements(self):
        return self.statements

    def setStatements(self, statements):
        self.statements = statements

if __name__ == '__main__':
    pass
