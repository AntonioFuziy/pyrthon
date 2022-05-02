import re

class PrePro:
  def __init__(self, entire_string):
    self.entire_string = entire_string
  
  def filter_expression(self):
    self.entire_string = re.sub("/\*.*?\*/", "", self.entire_string)
    return re.sub(" ", "", self.entire_string)