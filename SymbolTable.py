class SymbolTable():
  def __init__(self):
    self.table = {}
    
  def setter(self, name, value):
    self.table[name] = value
  
  def getter(self, name):
    if name not in self.table.keys():
      raise Exception(f"{name} is not defined")
    return self.table[name]