class FuncTable():
  table = {}
  def getter(name):
    if name not in FuncTable.table.keys():
      raise Exception(f"{name} is not defined")
    return FuncTable.table[name]

  def create(name, pointer):
    if name in FuncTable.table.keys():
      raise Exception(f"{name} is already defined")
    FuncTable.table[name] = pointer