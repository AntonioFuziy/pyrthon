import sys

from Node import Assignment, BinOp, Block, FuncCall, FuncDec, Identifier, If, IntVal, NoOp, Printf, Return, Scanf, StrVal, UnOp, VarDec, While
from PrePro import PrePro
from SymbolTable import SymbolTable
from Tokenizer import Tokenizer

class Parser:
  tokens = None

  def parse_factor():
    if Parser.tokens.actual_token.token_type == "INT":
      node = IntVal(Parser.tokens.actual_token.value, [])
      Parser.tokens.select_next()

    elif Parser.tokens.actual_token.token_type == "STRING":
      node = StrVal(Parser.tokens.actual_token.value, [])
      Parser.tokens.select_next()
    
    elif Parser.tokens.actual_token.token_type == "OPEN_PAR":
      Parser.tokens.select_next()
      node = Parser.relative_expression()
      if Parser.tokens.actual_token.token_type != "CLOSE_PAR":
        raise Exception("Parenthesis error")
      Parser.tokens.select_next()
    
    elif Parser.tokens.actual_token.token_type == "PLUS":
      Parser.tokens.select_next()
      node = UnOp("maris", [Parser.parse_factor()])
      
    elif Parser.tokens.actual_token.token_type == "MINUS":
      Parser.tokens.select_next()
      node = UnOp("mernos", [Parser.parse_factor()])

    elif Parser.tokens.actual_token.token_type == "NOT":
      Parser.tokens.select_next()
      node = UnOp("contra", [Parser.parse_factor()])
    
    elif Parser.tokens.actual_token.token_type == "SCANF":
      Parser.tokens.select_next()
      if Parser.tokens.actual_token.token_type != "OPEN_PAR":
        raise Exception("Scanf error")
      node = Scanf("", [])
      Parser.tokens.select_next()
      if Parser.tokens.actual_token.token_type != "CLOSE_PAR":
        raise Exception("Scanf error")
      Parser.tokens.select_next()

    elif Parser.tokens.actual_token.token_type == "IDENTIFIER":
      function_name = Parser.tokens.actual_token.value
      node = Identifier(Parser.tokens.actual_token.value, [])
      Parser.tokens.select_next()
      if Parser.tokens.actual_token.token_type == "OPEN_PAR":
        children = []
        Parser.tokens.select_next()
        if Parser.tokens.actual_token.token_type != "CLOSE_PAR":
          node = Parser.relative_expression()
          children.append(node)
          while Parser.tokens.actual_token.token_type == "SEPARATOR":
            Parser.tokens.select_next()
            node = Parser.relative_expression()
            children.append(node)
          if Parser.tokens.actual_token.token_type == "CLOSE_PAR":
            Parser.tokens.select_next()
            node = FuncCall(function_name, children)
          else:
            raise Exception("Func call error")
        
        elif Parser.tokens.actual_token.token_type == "CLOSE_PAR":
          Parser.tokens.select_next()
    else:
      raise Exception("Parse factor error")
      
    return node

  def parse_term():
    node = Parser.parse_factor()
    
    while (Parser.tokens.actual_token.token_type in ["MULT", "DIV", "AND"]):
      if Parser.tokens.actual_token.token_type == "MULT":
        Parser.tokens.select_next()
        node = BinOp("verzes", [node, Parser.parse_factor()])

      elif Parser.tokens.actual_token.token_type == "DIV":
        Parser.tokens.select_next()
        node = BinOp("divirdido", [node, Parser.parse_factor()])
      
      elif Parser.tokens.actual_token.token_type == "AND":
        Parser.tokens.select_next()
        node = BinOp("tambem", [node, Parser.parse_factor()])
      
      else:
        raise Exception("Parse term error")

    return node
  
  def parse_expression():
    node = Parser.parse_term()

    while (Parser.tokens.actual_token.token_type in ["PLUS", "MINUS", "OR", "CONCATENATE"]):
      if Parser.tokens.actual_token.token_type == "PLUS":
        Parser.tokens.select_next()
        node = BinOp("maris", [node, Parser.parse_term()])

      elif Parser.tokens.actual_token.token_type == "MINUS":
        Parser.tokens.select_next()
        node = BinOp("mernos", [node, Parser.parse_term()])
      
      elif Parser.tokens.actual_token.token_type == "OR":
        Parser.tokens.select_next()
        node = BinOp("ou", [node, Parser.parse_term()])

      elif Parser.tokens.actual_token.token_type == "CONCATENATE":
        Parser.tokens.select_next()
        node = BinOp("corcatena", [node, Parser.parse_term()])

      else:
        raise Exception("Parse expression")

    return node

  def relative_expression():
    node = Parser.parse_expression()
    while Parser.tokens.actual_token.token_type in ["EQUALTO", "MINOR", "GREATER"]:
      if Parser.tokens.actual_token.token_type == "EQUALTO":
        Parser.tokens.select_next()
        node = BinOp("iguar", [node, Parser.parse_expression()])
      elif Parser.tokens.actual_token.token_type == "MINOR":
        Parser.tokens.select_next()
        node = BinOp("mernor", [node, Parser.parse_expression()])
      elif Parser.tokens.actual_token.token_type == "GREATER":
        Parser.tokens.select_next()
        node = BinOp("marior", [node, Parser.parse_expression()])
      else:
        raise Exception("Parse relative expression error")
    
    return node

  def parse_statement():
    if Parser.tokens.actual_token.token_type == "IDENTIFIER":
      node = Identifier(Parser.tokens.actual_token.value, [])
      Parser.tokens.select_next()
      if Parser.tokens.actual_token.token_type == "EQUAL":
        Parser.tokens.select_next()
        node = Assignment("receba", [node, Parser.relative_expression()])
        if Parser.tokens.actual_token.token_type == "SEMICOLON":
          Parser.tokens.select_next()
        else:
          raise Exception("Parse statement error")
      
      elif Parser.tokens.actual_token.token_type == "OPEN_PAR":
        Parser.tokens.select_next()
        if Parser.tokens.actual_token.token_type != "CLOSE_PAR":
          node = FuncCall(Parser.tokens.actual_token.value, [Parser.relative_expression()])
        else:
          Parser.tokens.select_next()
          if Parser.tokens.actual_token.token_type == "SEMICOLON":
            Parser.tokens.select_next()
          else:
            raise Exception("Parse statement error")
        
      # else:
      #   raise Exception("Parse statement error")

    elif Parser.tokens.actual_token.token_type == "PRINTF":
      Parser.tokens.select_next()
      if Parser.tokens.actual_token.token_type == "OPEN_PAR":
        Parser.tokens.select_next()
        node = Printf("aspresenti", [Parser.relative_expression()])
        if Parser.tokens.actual_token.token_type != "CLOSE_PAR":
          raise Exception("Parse statement error")
        else:
          Parser.tokens.select_next()
          if Parser.tokens.actual_token.token_type == "SEMICOLON":
            Parser.tokens.select_next()
          else:
            raise Exception("Parse statement error")
      else:
        raise Exception("Parse statement error")

    elif Parser.tokens.actual_token.token_type == "IF":
      Parser.tokens.select_next()
      if Parser.tokens.actual_token.token_type == "OPEN_PAR":
        Parser.tokens.select_next()
        node = Parser.relative_expression()
        if Parser.tokens.actual_token.token_type != "CLOSE_PAR":
          raise Exception("Parse statement IF error")
        else:
          Parser.tokens.select_next()
          other_node = Parser.parse_statement()
          if Parser.tokens.actual_token.token_type == "ELSE":
            Parser.tokens.select_next()
            node = If("si", [node, other_node, Parser.parse_statement()])
          else:
            node = If("si", [node, other_node])
      else:
        raise Exception("Parse statement IF error")

    elif Parser.tokens.actual_token.token_type == "WHILE":
      Parser.tokens.select_next()
      if Parser.tokens.actual_token.token_type == "OPEN_PAR":
        Parser.tokens.select_next()
        node = Parser.relative_expression()
        if Parser.tokens.actual_token.token_type != "CLOSE_PAR":
          raise Exception("Parse statement WHILE error")
        else:
          Parser.tokens.select_next()
          node = While("enquarto", [node, Parser.parse_statement()])
      else:
        raise Exception("Parse statement WHILE error")
    
    elif Parser.tokens.actual_token.token_type in ["INT", "STRING"]:
      all_types = []
      var_type = Parser.tokens.actual_token.token_type
      Parser.tokens.select_next()
      if Parser.tokens.actual_token.token_type == "IDENTIFIER":
        var_token = Parser.tokens.actual_token
        all_types.append(var_token)
        Parser.tokens.select_next()
        while Parser.tokens.actual_token.token_type == "SEPARATOR":
          Parser.tokens.select_next()
          if Parser.tokens.actual_token.token_type == "IDENTIFIER":
            var_token = Parser.tokens.actual_token
            all_types.append(var_token)
            Parser.tokens.select_next()
          else:
            raise Exception("Parse statement TYPE error")
        if Parser.tokens.actual_token.token_type == "SEMICOLON":
          Parser.tokens.select_next()
          return VarDec(var_type, all_types)
        else:
          raise Exception("Parse statement TYPE error")

    elif Parser.tokens.actual_token.token_type == "RETURN":
      Parser.tokens.select_next()
      if Parser.tokens.actual_token.token_type == "OPEN_PAR":
        Parser.tokens.select_next()
        node = Return("vorte", [Parser.relative_expression()])
        if Parser.tokens.actual_token.token_type != "CLOSE_PAR":
          raise Exception("Parse statement error")
        else:
          Parser.tokens.select_next()
          if Parser.tokens.actual_token.token_type == "SEMICOLON":
            Parser.tokens.select_next()
          else:
            raise Exception("Parse statement error")
      else:
        print(Parser.tokens.actual_token.token_type)
        raise Exception("Parse statement error")

    elif Parser.tokens.actual_token.token_type == "SEMICOLON":
      node = NoOp(None, [])
      Parser.tokens.select_next()
      
    else:
      node = Parser.parse_block()
    
    return node

  def parse_block():
    children = []
    if Parser.tokens.actual_token.token_type == "OPEN_BRACKET":
      Parser.tokens.select_next()
      while Parser.tokens.actual_token.token_type != "CLOSE_BRACKET":
        node = Parser.parse_statement()
        children.append(node)
      node = Block(None, children)
      Parser.tokens.select_next()
    else:
      raise Exception("Parse block error")
    return node
  
  def parse_declaration():
    function_name = ""
    if Parser.tokens.actual_token.token_type in ["INT", "STRING", "VOID"]:    
      children = []
      var_type = Parser.tokens.actual_token.token_type
      Parser.tokens.select_next()
      if Parser.tokens.actual_token.token_type == "IDENTIFIER":
        node = VarDec(var_type, [Parser.tokens.actual_token])
        function_name = Parser.tokens.actual_token.value
        children.append(node)
        Parser.tokens.select_next()
        if Parser.tokens.actual_token.token_type == "OPEN_PAR":
          Parser.tokens.select_next()
          if Parser.tokens.actual_token.token_type in ["INT", "STRING", "VOID"]:
            var_type = Parser.tokens.actual_token.token_type
            Parser.tokens.select_next()
            if Parser.tokens.actual_token.token_type == "IDENTIFIER":
              node = VarDec(var_type, [Parser.tokens.actual_token])
              children.append(node)
              Parser.tokens.select_next()
              while Parser.tokens.actual_token.token_type == "SEPARATOR":
                Parser.tokens.select_next()
                if Parser.tokens.actual_token.token_type in ["INT", "STRING", "VOID"]:
                  var_type = Parser.tokens.actual_token.token_type
                  Parser.tokens.select_next()
                  if Parser.tokens.actual_token.token_type == "IDENTIFIER":
                    node = VarDec(var_type, [Parser.tokens.actual_token])
                    children.append(node)
                    Parser.tokens.select_next()

                    if Parser.tokens.actual_token.token_type == "CLOSE_PAR":
                      Parser.tokens.select_next()
                      node = Parser.parse_block()
                      children.append(node)
          
          elif Parser.tokens.actual_token.token_type == "CLOSE_PAR":
            Parser.tokens.select_next()
            node = Parser.parse_block()
            children.append(node)
            
          else:
            raise Exception("Parse declaration error")
    else:
      raise Exception("Parse declaration error")

    return FuncDec(function_name, children)
                
  def parse_program():
    functions = []
    while Parser.tokens.actual_token.token_type != "EOF":
      node = Parser.parse_declaration()
      functions.append(node)
    node = Block(None, functions)
    Parser.tokens.select_next()

    return node
  
  def run(code):
    code_filtered = PrePro(code).filter_expression()
    Parser.tokens = Tokenizer(code_filtered)
    Parser.tokens.select_next()
    node = Parser.parse_program()

    if Parser.tokens.actual_token.token_type != "EOF":
      raise Exception("EOF run error")
    
    node.children.append(FuncCall("primeiramente", []))

    return node

f = open(sys.argv[1],"r")
code = f.read()
f.close()
AST = Parser.run(code)
symbol_table = SymbolTable()
AST.Evaluate(symbol_table)