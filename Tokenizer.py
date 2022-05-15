from Token import Token

class Tokenizer:
  def __init__(self, origin):
    self.origin = origin
    self.position = 0
    self.actual_token = None
    self.reserved_words = {
      "printf": "PRINTF",
      "scanf": "SCANF",
      "if": "IF",
      "while": "WHILE", 
      "else": "ELSE",
      "str": "STRING",
      "int": "INT"
    }

  def select_next(self):
    while self.position < len(self.origin) and self.origin[self.position] == "\n":
      self.position += 1

    if self.position >= len(self.origin):
      self.actual_token = Token("EOF", " ")
      return self.actual_token
    
    if self.origin[self.position] == " ":
      self.position += 1
      return self.select_next()

    if self.origin[self.position] == "*":
      self.position += 1
      self.actual_token = Token("MULT", "*")
      return self.actual_token
      
    elif self.origin[self.position] == "/":
      self.position += 1
      self.actual_token = Token("DIV", "/")
      return self.actual_token
    
    elif self.origin[self.position] == "+":
      self.position += 1
      self.actual_token = Token("PLUS", " ")
      return self.actual_token
    
    elif self.origin[self.position] == "-":
      self.position += 1
      self.actual_token = Token("MINUS", " ")
      return self.actual_token

    elif self.origin[self.position] == ".":
      self.position += 1
      self.actual_token = Token("CONCATENATE", " ")
      return self.actual_token

    elif self.origin[self.position] == ",":
      self.position += 1
      self.actual_token = Token("SEPARATOR", " ")
      return self.actual_token

    elif self.origin[self.position] == "(":
      self.position += 1
      self.actual_token = Token("OPEN_PAR", " ")
      return self.actual_token

    elif self.origin[self.position] == ")":
      self.position += 1
      self.actual_token = Token("CLOSE_PAR", " ")
      return self.actual_token
    
    elif self.origin[self.position] == "=":
      self.position += 1
      if self.origin[self.position] == "=":
        self.position += 1
        self.actual_token = Token("EQUALTO", " ")
        return self.actual_token
      
      self.actual_token = Token("EQUAL", " ")
      return self.actual_token
    
    elif self.origin[self.position] == ";":
      self.position += 1
      self.actual_token = Token("SEMICOLON", " ")
      return self.actual_token

    elif self.origin[self.position] == "{":
      self.position += 1
      self.actual_token = Token("OPEN_BRACKET", " ")
      return self.actual_token
    
    elif self.origin[self.position] == "}":
      self.position += 1
      self.actual_token = Token("CLOSE_BRACKET", " ")
      return self.actual_token
    
    elif self.origin[self.position] == '"':
      self.position += 1
      new_str = self.origin[self.position]
      self.position += 1
      while self.position < len(self.origin) and self.origin[self.position] != '"':
        new_str += self.origin[self.position]
        self.position += 1
      self.actual_token = Token("STRING", new_str)
      self.position += 1
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
          self.actual_token = Token("INT", int(candidato))
          return self.actual_token

      #atualiza o token
      self.actual_token = Token("INT", int(candidato))
      return self.actual_token

    elif self.origin[self.position].isalpha():
      variable = self.origin[self.position]
      self.position += 1

      #enquanto o caractere não estiver no fim
      while self.position < len(self.origin) and (self.origin[self.position].isalpha() or self.origin[self.position] == "_"  or self.origin[self.position].isnumeric()):
        #concatena o caractere ao variable
        variable += self.origin[self.position]
        self.position += 1
        #se não for um digito
      
      if variable in self.reserved_words:
        self.actual_token = Token(self.reserved_words[variable], variable)
        return self.actual_token
      else:
        self.actual_token = Token("IDENTIFIER", variable)
        return self.actual_token

    elif self.origin[self.position] == ">":
      self.position += 1
      self.actual_token = Token("GREATER", " ")
      return self.actual_token

    elif self.origin[self.position] == "<":
      self.position += 1
      self.actual_token = Token("MINOR", " ")
      return self.actual_token

    elif self.origin[self.position] == "!":
      self.position += 1
      self.actual_token = Token("NOT", " ")
      return self.actual_token
    
    elif self.origin[self.position] == "|":
      self.position += 1
      if self.origin[self.position] == "|":
        self.position += 1
        self.actual_token = Token("OR", " ")
        return self.actual_token
      else:
        raise Exception("Invalid token |")

    elif self.origin[self.position] == "&":
      self.position += 1
      if self.origin[self.position] == "&":
        self.position += 1
        self.actual_token = Token("AND", " ")
        return self.actual_token
      else:
        raise Exception("Invalid token &")

    else:
      raise Exception("select next error")