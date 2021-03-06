# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 17:55:57 2022
@author: Quentin Ducasse
"""

import sys

from ast import *

from mini_c_grammar.declarations import Declarations
from mini_c_grammar.program import Program
from mini_c_grammar.declaration import Declaration
from mini_c_grammar.statements import Statements
from mini_c_grammar.whileStatement import WhileStatement
from mini_c_grammar.IfStatement import IfStatement
from mini_c_grammar.type import Type
from mini_c_grammar.number import Number


class Parser:
    '''
    Toy language parser.
    '''

    # ==========================
    #      Helper Functions
    # ==========================

    def error(self, message):
        '''
        Error template.
        '''
        print('ERROR at {}:'.format(str(self.peek().position)), message)
        sys.exit(1)

    def peek(self, n=1):
        '''
        Returns the next token in the list WITHOUT popping it.
        '''

        try:
            return self.lexems[n - 1]
        except IndexError:
            self.error('No more lexems left.')


    def expect(self, tag):
        '''
        Pops the next token from the lexems list and tests its type through the tag.
        '''
        next_lexem = self.peek()
        if next_lexem.tag == tag:
            return self.accept()
        else:
            self.error('Expected {}, got {} instead'.format(tag, next_lexem.tag))


    def accept(self):
        '''
        Pops the lexem out of the lexems list and log its tag/value combination.
        '''
        lexem = self.peek()
        return self.lexems.pop(0)


    def remove_comments(self):
        '''
        Removes the comments from the token list by testing their tags.
        '''
        self.lexems = [lexem for lexem in self.lexems if lexem.tag!="COMMENT"]


    # ==========================
    #      Parse Functions
    # ==========================

    def parse(self, lexems):
        '''
        Main function: launches the parsing operation given a lexem list.
        '''
        self.lexems = lexems
        self.remove_comments()
        ast = self.parse_program()
        return ast


    def parse_program(self):
        '''
        Parses a program which is a succession of assignments.
        '''
        program_node = Program()
        '''
        while(len(self.lexems) > 0):
            assignment = self.parse_assignment()
            program_node.assignments.append(assignment)
        '''
        self.expect('TYPE')
        self.expect('MAIN')
        self.expect('L_PARENTHESIS')
        self.expect('R_PARENTHESIS')
        self.expect('L_CURLYBRACKET')
        declarations = self.parse_declarations()
        program_node.setDeclarations(declarations)
        #statements = self.parse_statements()
        #program_node.setStatements(statements)
        self.expect('R_CURLYBRACKET')


        return program_node

    def parse_type(self):
        type = Type()
        token = self.expect('TYPE')
        type.setValue(token.value)
        return type

    def parse_declaration(self):
        declaration = Declaration()
        declaration.type = self.parse_type()
        declaration.identifier = self.parse_variable().name

        if self.peek().tag == 'L_BRACKET':
            print("COUCOU")
            self.expect('L_BRACKET')
            declaration.integer = self.parse_number()
            self.expect('R_BRACKET')
        self.expect('TERMINATOR')

        return declaration


    def parse_declarations(self):
        declarations_node = Declarations()
        while( self.peek().tag == 'TYPE'):
            declarations_node.addDeclaration(self.parse_declaration())
        return declarations_node

    def parse_statements(self):
        statements_node = Statements()


    def parse_assignment(self):
        '''
        Parses an assignment that looks like:
            Variable, '=', Expression ';'
        '''
        assignment_node = AssignmentNode()
        assignment_node.variable = self.parse_variable()
        self.expect('ASSIGN')
        assignment_node.expression = self.parse_expression()
        self.expect('TERMINATOR')
        return assignment_node


    def parse_expression(self):
        '''
        Parses an expression that looks like:
            Unary, {[ "/" | "+" | "-" | "*" ], Expression}
        '''
        expression_node = ExpressionNode()
        expression_node.lhs = self.parse_unary()
        # To check the type of the expression, we look for a ';' after the first variable or number
        if not self.peek().tag == 'TERMINATOR':
            # Binary operation so operator and another expression
            if self.peek().tag in ['ADDITION', 'SUBTRACTION', 'MULTIPLICATION', 'DIVISION']:
                expression_node.operator = self.accept()
            else:
                self.error("Missing operator in expression.")
            expression_node.rhs = self.parse_expression()
        return expression_node


    def parse_unary(self):
        '''
        Parses an unary that looks like:
            Variable | Number
        '''
        unary_node = UnaryNode()
        if self.peek().tag == 'VARIABLE':
            unary_node.value = self.parse_variable()
        elif self.peek().tag == 'NUMBER':
            unary_node.value = self.parse_number()
        else:
            self.error("Unary is either variable or number")
        return unary_node


    def parse_variable(self):
        '''
        Parses a variable that looks like:
            Character, {Character | Digit}
        '''
        variable_node = VariableNode()
        token = self.expect('VARIABLE')
        variable_node.name = token.value
        return variable_node


    def parse_number(self):
        '''
        Parses a number that looks like:
            Digit, {Digit}
        '''
        number_node = Number()
        token = self.expect('NUMBER')
        number_node.value = token.value
        return number_node
