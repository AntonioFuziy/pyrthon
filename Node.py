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
    symbol_table.setter(self.children[0].value, self.children[1].Evaluate(symbol_table)[0])

class Printf(Node):
  def Evaluate(self, symbol_table):
    print(self.children[0].Evaluate(symbol_table)[0])

class Block(Node):
  def Evaluate(self, symbol_table):
    for child in self.children:
      child.Evaluate(symbol_table)
    
class VarDec(Node):
  def Evaluate(self, symbol_table):
    for child in self.children:
      symbol_table.create(child.value, self.value)


class BinOp(Node):
  def Evaluate(self, symbol_table):
    first_children = self.children[0].Evaluate(symbol_table)
    second_children = self.children[1].Evaluate(symbol_table)
    
    if self.value == ".":
      return (str(first_children[0]) + str(second_children[0]), "STRING")

    if first_children[1] != second_children[1]:
      raise Exception("Type doesnt match")

    if first_children[1] == "STRING" and second_children[1] == "STRING":
      if self.value == ">":
        if first_children[0] > second_children[0]:
          return (1, "INT")
        else:
          return (0, "INT")

      elif self.value == "<":
        if first_children[0] < second_children[0]:
          return (1, "INT")
        else:
          return (0, "INT")

      elif self.value == "==":
        if first_children[0] == second_children[0]:
          return (1, "INT")
        else:
          return (0, "INT")

    elif first_children[1] == "INT" and second_children[1] == "INT":
      if self.value == "*":
        return (first_children[0] * second_children[0], "INT")

      elif self.value == "/":
        return (first_children[0] // second_children[0], "INT")
        
      elif self.value == "+":
        return (first_children[0] + second_children[0], "INT")

      elif self.value == "-":
        return (first_children[0] - second_children[0], "INT")

      elif self.value == "==":
        if first_children[0] == second_children[0]:
          return (1, "INT")
        else:
          return (0, "INT")

      elif self.value == "&&":
        if first_children[0] and second_children[0]:
          return (1, "INT")
        else:
          return (0, "INT")

      elif self.value == "||":
        if first_children[0] or second_children[0]:
          return (1, "INT")
        else:
          return (0, "INT")

      elif self.value == ">":
        if first_children[0] > second_children[0]:
          return (1, "INT")
        else:
          return (0, "INT")

      elif self.value == "<":
        if first_children[0] < second_children[0]:
          return (1, "INT")
        else:
          return (0, "INT")

    else:
      raise Exception("BinOp error")

class UnOp(Node):
  def Evaluate(self, symbol_table):
    unique_children = self.children[0].Evaluate(symbol_table)
    
    if unique_children[1] == "STRING":
      raise Exception("STRING cannot be used for this operation")

    if self.value == "+":
      return (unique_children[0], "INT")
    elif self.value == "-":
      return (-unique_children[0], "INT")
    elif self.value == "!":
      return (not unique_children[0], "INT")
    else:
      raise Exception("UnOp error")

class IntVal(Node):
  def Evaluate(self, symbol_table):
    return (self.value, "INT")
  
class StrVal(Node):
  def Evaluate(self, symbol_table):
    return (self.value, "STRING")

class NoOp(Node):
  def Evaluate(self, symbol_table):
    pass

class While(Node):
  def Evaluate(self, symbol_table):
    while self.children[0].Evaluate(symbol_table)[0]:
      self.children[1].Evaluate(symbol_table)

class If(Node):
  def Evaluate(self, symbol_table):
    if self.children[0].Evaluate(symbol_table)[0]:
      self.children[1].Evaluate(symbol_table)
    elif len(self.children) > 2:
      self.children[2].Evaluate(symbol_table)

class Scanf(Node):
  def Evaluate(self, symbol_table):
    return (int(input()), "INT")