from Token import Token

class Tokenizer:
  def __init__(self, origin):
    self.origin = origin
    self.position = 0
    self.actual_token = None
    self.reserved_words = {
      "mostre": "PRINTF",
      "sorta": "SCANF",
      "se": "IF",
      "enquanto": "WHILE", 
      "senao": "ELSE"
    }

    self.operators = {
      "vezes": "MULT",
      "dividido": "DIV",
      "mais": "PLUS",
      "menos": "MINUS",
      "igual": "EQUALTO",
      "and": "AND",
      "or": "OR",
      "maior que": "GREATER",
      "menor que": "MINOR",

      "inverso": "NOT",
      
      "receba": "EQUAL",

      "apenas;": "SEMICOLON"
    }

  def select_next(self):    
    while self.position < len(self.origin) and self.origin[self.position] == "\n":
      self.position += 1

    #checar se o proximo caracter é um EOF
    if self.position >= len(self.origin):
      self.actual_token = Token("EOF", " ")
      return self.actual_token

    elif self.origin[self.position] == "(":
      self.position += 1
      self.actual_token = Token("OPEN_PAR", " ")
      return self.actual_token

    elif self.origin[self.position] == ")":
      self.position += 1
      self.actual_token = Token("CLOSE_PAR", " ")
      return self.actual_token

    elif self.origin[self.position] == "[":
      self.position += 1
      self.actual_token = Token("OPEN_BRACKET", " ")
      return self.actual_token
    
    elif self.origin[self.position] == "]":
      self.position += 1
      self.actual_token = Token("CLOSE_BRACKET", " ")
      return self.actual_token
    
    #checar se o proximo caracter é um digito
    elif self.origin[self.position].isnumeric():
      candidato = self.origin[self.position]
      self.position += 1

      #enquanto o caractere não estiver no fim
      while self.position < len(self.origin):
        
        #se o caractere for um digito
        if self.origin[self.position].isnumeric():
          #concatena o caractere ao candidato
          candidato += self.origin[self.position]
          self.position += 1
        
        #se não for um digito
        else:
          self.actual_token = Token("NUMBER", int(candidato))
          return self.actual_token

      #atualiza o token
      self.actual_token = Token("NUMBER", int(candidato))
      return self.actual_token
    
    
    # elif self.origin[self.position].isalpha():
    #   operator = self.origin[self.position]
    #   self.position += 1
    #   while self.position < len(self.origin) and (self.origin[self.position].isalpha()):
    #     operator += self.origin[self.position]
    #     self.position += 1
    #   if operator in self.operators:
    #     self.actual_token = Token(self.operators[operator], operator)
    #     return self.actual_token
    #   else:
    #     print("saindo")
    #     print(self.actual_token.token_type)

    elif self.origin[self.position].isalpha():
      variable = self.origin[self.position]
      self.position += 1

      #enquanto o caractere não estiver no fim
      while self.position < len(self.origin) and (self.origin[self.position].isalpha() or self.origin[self.position] == "_"  or self.origin[self.position].isnumeric()):
        #concatena o caractere ao variable
        variable += self.origin[self.position]
        self.position += 1
        #se não for um digito
      
      print(variable)
      if variable in self.reserved_words or variable in self.operators:
        self.actual_token = Token(self.reserved_words[variable], variable)
        return self.actual_token
      elif variable not in self.operators:
        self.actual_token = Token("IDENTIFIER", variable)
        return self.actual_token

    else:
      raise Exception("select next error")