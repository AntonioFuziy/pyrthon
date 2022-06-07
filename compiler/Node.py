from FuncTable import FuncTable
from SymbolTable import SymbolTable


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
      if child.value == "vorte":
        return child.Evaluate(symbol_table)
      child.Evaluate(symbol_table)
    
class VarDec(Node):
  def Evaluate(self, symbol_table):
    for child in self.children:
      symbol_table.create(child.value, self.value)


class BinOp(Node):
  def Evaluate(self, symbol_table):
    first_children = self.children[0].Evaluate(symbol_table)
    second_children = self.children[1].Evaluate(symbol_table)
    
    if self.value == "corcatena":
      return (str(first_children[0]) + str(second_children[0]), "STRING")

    if first_children[1] != second_children[1]:
      raise Exception("Type doesnt match")

    if first_children[1] == "STRING" and second_children[1] == "STRING":
      if self.value == "marior":
        if first_children[0] > second_children[0]:
          return (1, "INT")
        else:
          return (0, "INT")

      elif self.value == "mernor":
        if first_children[0] < second_children[0]:
          return (1, "INT")
        else:
          return (0, "INT")

      elif self.value == "iguar":
        if first_children[0] == second_children[0]:
          return (1, "INT")
        else:
          return (0, "INT")

    elif first_children[1] == "INT" and second_children[1] == "INT":
      if self.value == "verzes":
        return (first_children[0] * second_children[0], "INT")

      elif self.value == "divirdido":
        return (first_children[0] // second_children[0], "INT")
        
      elif self.value == "maris":
        return (first_children[0] + second_children[0], "INT")

      elif self.value == "mernos":
        return (first_children[0] - second_children[0], "INT")

      elif self.value == "iguar":
        if first_children[0] == second_children[0]:
          return (1, "INT")
        else:
          return (0, "INT")

      elif self.value == "tambem":
        if first_children[0] and second_children[0]:
          return (1, "INT")
        else:
          return (0, "INT")

      elif self.value == "ou":
        if first_children[0] or second_children[0]:
          return (1, "INT")
        else:
          return (0, "INT")

      elif self.value == "marior":
        if first_children[0] > second_children[0]:
          return (1, "INT")
        else:
          return (0, "INT")

      elif self.value == "mernor":
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

    if self.value == "maris":
      return (unique_children[0], "INT")
    elif self.value == "mernos":
      return (-unique_children[0], "INT")
    elif self.value == "contra":
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

class FuncCall(Node):
  def Evaluate(self, symbol_table):
    arguments = []
    new_function = FuncTable.getter(self.value)
    new_symbol_table = SymbolTable()
    for i in range(1, len(new_function.children)-1):
      arguments.append(new_function.children[i].children[0].value)
      new_function.children[i].Evaluate(new_symbol_table)
    
    for j in range(len(arguments)):
      new_symbol_table.setter(arguments[j], self.children[j].Evaluate(symbol_table)[0])

    return new_function.children[-1].Evaluate(new_symbol_table)

class FuncDec(Node):
  def Evaluate(self, symbol_table):
    FuncTable.create(self.value, self)

class Return(Node):
  def Evaluate(self, symbol_table):
    return self.children[0].Evaluate(symbol_table)