"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""
import ast

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


    pass
