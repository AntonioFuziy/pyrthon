from rply import LexerGenerator

class Lexer():
  def __init__(self):
    self.lexer = LexerGenerator()

  def _add_tokens(self):
    
    self.lexer.add('OPEN_BRACKET', r'\[')
    self.lexer.add('CLOSE_BRACKET', r'\]')
    self.lexer.add('OPEN_PAR', r'\[[')
    self.lexer.add('CLOSE_PAR', r'\]]')
    self.lexer.add('SEMI_COLON', r'apenas;')
    
    self.lexer.add('PLUS', r'maris')
    self.lexer.add('MINUS', r'mernos')
    self.lexer.add('MULT', r'verzes')
    self.lexer.add('DIV', r'divirdido')
    self.lexer.add('CONCATENATE', r'corcatena')
    self.lexer.add('EQUAL', r'receba')

    self.lexer.add('NOT', r'contra')
    self.lexer.add('AND', r'tambem')
    self.lexer.add('OR', r'ou')
    self.lexer.add('GREATER', r'marior')
    self.lexer.add('MINOR', r'mernor')
    self.lexer.add('EQUALTO', r'iguar')
    
    self.lexer.add('INT', r'\d+')
    self.lexer.add('STRING', r'[a-zA-Z0-9\]*')
    self.lexer.add('IDENTIFIER', r'[a-zA-Z | _] [0-9a-zA-Z]*')
  
    self.lexer.add('WHILE', r'enquarto')  
    self.lexer.add('IF', r'sir')  
    self.lexer.add('ELSE', r'sirnao')
    self.lexer.add('PRINT', r'aspresenti')  
    self.lexer.add('SCANF', r'sorta')
    
    self.lexer.ignore('\s+')

  def get_lexer(self):
    self._add_tokens()
    return self.lexer.build()