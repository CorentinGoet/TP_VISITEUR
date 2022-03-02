"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""
import ast
from mini_c_lexer import Lexer

class Visiteur:
    pass

if __name__ == '__main__':
    file = open("test_minic.txt")
    src = file.readlines()
    lex = Lexer()
    lex.lex(src)
    print(lex.lexems)
