"""
@author Corentin Goetghebeur (github.com/CorentinGoet)
"""

import sys
import re

regexExpressions = [
    (r'main', 'MAIN'),

    # Special chars
    (r'\(', 'L_PARENTHESIS'),
    (r'\)', 'R_PARENTHESIS'),
    (r'\{', 'L_CURLYBRACKET'),
    (r'\}', 'R_CURLYBRACKET'),
    (r'\;', 'TERMINATOR'),
    (r'\=', 'ASSIGN'),
    (r'\+', 'ADDITION'),
    (r'\-', 'SUBTRACTION'),
    (r'\*', 'MULTIPLICATION'),
    (r'\/', 'DIVISION'),

    # End of line
    (r'[ \n\t]+', None),

    # Types
    (r'(int|bool|char|float)\s', 'TYPE'),
    (r'([a-zA-Z](\d|[a-zA-Z])*)\s', 'VARIABLE'),
    (r'\d+', 'NUMBER')
]


class Lexem:
    '''
    Our token definition:
    lexem (tag and value) + position in the program raw text

    Parameters
    ----------
    tag: string
        Name of the lexem's type, e.g. IDENTIFIER

    value: string
        Value of the lexem,       e.g. integer1

    position: integer tuple
        Tuple to point out the lexem in the input file (line number, position)
    '''
    def __init__(self, tag, value, position):
        self.tag      = tag
        self.value    = value
        self.position = position

    def __repr__(self):
        return self.tag

class Lexer:
    '''
    Component in charge of the transformation of raw data to lexems.
    '''

    def __init__(self):
        self.lexems = []

    def lex(self, inputText):
        '''
        Main lexer function:
        Creates a lexem for every detected regular expression
        The lexems are composed of:
            - tag
            - values
            - position
        SEE lexem for more info
        '''
        # Crawl through the input file
        for lineNumber, line in enumerate(inputText):
            lineNumber += 1     # Numéro de ligne
            position = 0        # Position du caractère en cours de lecture sur la ligne

            # go through the line
            while position < len(line):

                match = None
                for lexemRegex in regexExpressions:
                    pattern, tag = lexemRegex
                    regex = re.compile(pattern)     # Transforms the string into a regex pattern object
                    match = regex.match(line, position)
                    if match:
                        # if the match was successful
                        data = match.group(0)
                        if tag:
                            lexem = Lexem(tag, data, [lineNumber, position])
                            self.lexems.append(lexem)
                        position = match.end(0)
                        break
                # no matches in the line
                if not match:
                    print("No match detected on line and position:")
                    print(line[position:])
                    sys.exit(1)






if __name__ == '__main__':
    pass
