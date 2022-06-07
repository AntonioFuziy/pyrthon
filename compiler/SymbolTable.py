class SymbolTable():
  def __init__(self):
    self.table = {}
    
  def setter(self, name, value):
    if name not in self.table.keys():
      raise Exception(f"{name} is not defined")
    if self.table[name][1] == "INT":
      if type(value) == int:
        self.table[name] = (value, "INT")
    elif self.table[name][1] == "STRING":
      if type(value) == str:
        self.table[name] = (value, "STRING")
    else:
      raise Exception(f"{name} type doesnt match")

  def getter(self, name):
    if name not in self.table.keys():
      raise Exception(f"{name} is not defined")
    return self.table[name]

  def create(self, name, var_type):
    if name in self.table.keys():
      raise Exception(f"{name} is already defined")
    if var_type == "INT":
      self.table[name] = (None, var_type)
    elif var_type == "STRING":
      self.table[name] = (None, var_type)
    else:
      raise Exception(f"{var_type} doesnt exist")