"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""


class WhileStatement:
    """
    Class representation of a while statement.
    """

    def __init__(self):
        """
        Constructor for class WhileStatement.
        """
        self.__expression = None
        self.__statement = None

    def accept(self, visitor):
        """
        Method called to accept the visitor.
        Visitor must have visitWhileStatement method.
        :param visitor: visitor
        :return: None
        """
        visitor.visitWhileStatement(self)

    def getExpression(self):
        """
        Getter for __expression.
        :return: expression
        """
        return self.__expression

    def setExpression(self, expression):
        """
        Setter for expression
        :param expression: new expression
        :return: None
        """
        self.__expression = expression

    def getStatement(self):
        """
        Getter for statement
        :return: statement
        """
        return self.__statement

    def setStatement(self, statement):
        """
        Setter for statement
        :param statement: new statement
        :return: None
        """
        self.__statement = statement


if __name__ == '__main__':
    pass
