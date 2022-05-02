class Node():
  def __init__(self, value, children):
    self.value = value
    self.children = children
  
  def Evaluate(self, symbol_table):
    pass

class Identifier(Node):
  def Evaluate(self, symbol_table):
    return symbol_table.getter(self.value)

class Assignment(Node):
  def Evaluate(self, symbol_table):
    symbol_table.setter(self.children[0].value, self.children[1].Evaluate(symbol_table))

class Printf(Node):
  def Evaluate(self, symbol_table):
    print(self.children[0].Evaluate(symbol_table))

class Block(Node):
  def Evaluate(self, symbol_table):
    for child in self.children:
      child.Evaluate(symbol_table)

class BinOp(Node):
  def Evaluate(self, symbol_table):
    if self.value == "vezes":
      return self.children[0].Evaluate(symbol_table) * self.children[1].Evaluate(symbol_table)
    elif self.value == "dividido":
      return self.children[0].Evaluate(symbol_table) // self.children[1].Evaluate(symbol_table)
    elif self.value == "mais":
      return self.children[0].Evaluate(symbol_table) + self.children[1].Evaluate(symbol_table)
    elif self.value == "menos":
      return self.children[0].Evaluate(symbol_table) - self.children[1].Evaluate(symbol_table)
    elif self.value == "igual":
      return self.children[0].Evaluate(symbol_table) == self.children[1].Evaluate(symbol_table)
    elif self.value == "and":
      return self.children[0].Evaluate(symbol_table) and self.children[1].Evaluate(symbol_table)
    elif self.value == "or":
      return self.children[0].Evaluate(symbol_table) or self.children[1].Evaluate(symbol_table)
    elif self.value == "maior que":
      return self.children[0].Evaluate(symbol_table) > self.children[1].Evaluate(symbol_table)
    elif self.value == "menor que":
      return self.children[0].Evaluate(symbol_table) < self.children[1].Evaluate(symbol_table)
    else:
      raise Exception("BinOp error")

class UnOp(Node):
  def Evaluate(self, symbol_table):
    if self.value == "mais":
      return self.children[0].Evaluate(symbol_table)
    elif self.value == "menos":
      return -self.children[0].Evaluate(symbol_table)
    elif self.value == "inverso":
      return not self.children[0].Evaluate(symbol_table)
    else:
      raise Exception("UnOp error")

class IntVal(Node):
  def Evaluate(self, symbol_table):
    return self.value

class NoOp(Node):
  def Evaluate(self, symbol_table):
    pass

class While(Node):
  def Evaluate(self, symbol_table):
    while self.children[0].Evaluate(symbol_table):
      self.children[1].Evaluate(symbol_table)

class If(Node):
  def Evaluate(self, symbol_table):
    if self.children[0].Evaluate(symbol_table):
      self.children[1].Evaluate(symbol_table)
    elif len(self.children) > 2:
      self.children[2].Evaluate(symbol_table)

class Scanf(Node):
  def Evaluate(self, symbol_table):
    return int(input())