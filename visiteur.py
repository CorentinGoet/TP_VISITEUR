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
        vDec = program.getDeclarations().accept(self)
        return "Program{\n" + vDec + "}\n"

    def visitDeclarations(self, declarations):
        tmplist = ""
        for d in declarations.declaration:
            tmplist += (d.accept(self) + "\n")
        return tmplist

    def visitDeclaration(self, declaration):
        strTyp = declaration.type.accept(self)
        if(declaration.integer == None):
            return strTyp + " " + str(declaration.identifier) + "\n"
        else:
            return strTyp + " " + str(declaration.identifier) + "[" + str(declaration.integer.value) + "]\n"

    def visitType(self, type):
        return type.getValue()


if __name__ == '__main__':
    file = open("test_minic.txt")
    src = file.readlines()
    lex = Lexer()
    lex.lex(src)
    p = Parser()
    ast = p.parse(lex.lexems)
    visitor = Visiteur()
    print(ast.accept(visitor))



