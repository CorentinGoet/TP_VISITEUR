"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""
import ast
from mini_c_lexer import Lexer
from parser_ import Parser


class Visiteur:
    def init(self):
        pass

    def visitProgram(self, program):
        print("Program{")
        self.visitDeclarations(program.getDeclarations())
        #self.visitStatements(program.getDeclarations())
        print("}\n")

    def visitDeclarations(self, declarations):
        print("Declarations{")
        for d in declarations.declaration:
            self.visitDeclaration(d)
        print("}\n")

    def visitDeclaration(self, declaration):
        print("Declaration{Type:" + str(declaration.type) + "|Identifier:" + str(declaration.identifier)+"\n");


if __name__ == '__main__':
    file = open("test_minic.txt")
    src = file.readlines()
    lex = Lexer()
    lex.lex(src)
    p = Parser()
    ast = p.parse(lex.lexems)
    visitor = Visiteur()
    visitor.visitProgram(ast)



