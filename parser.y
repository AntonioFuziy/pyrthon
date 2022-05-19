%{
  #include<stdio.h>
  int yylex();
  void yyerror(const char *s) { printf("ERROR: %sn", s); }
%}

%token IDENTIFIER INT STRING
%token EQUAL EQUALTO MINOR GREATER NOT AND OR
%token OPEN_PAR CLOSE_PAR OPEN_BRACKET CLOSE_BRACKET SEMI_COLON
%token PRINT SCANF WHILE IF ELSE VAR_TYPE RETURN
%token CONCATENATE SEPARATOR PLUS MINUS MULT DIV

%start program

%%

program : block 
        ;

block : OPEN_BRACKET statement CLOSE_BRACKET
      | OPEN_BRACKET CLOSE_BRACKET
      ;
        
statement : assigment
          | block
          | print
          | if
          | while
          | var_type
          SEMI_COLON
          ;
        
relexpression: expression EQUALTO
             | expression MINOR
             | expression GREATER
             | expression
             ;

expression: term PLUS
          | term MINUS
          | term OR
          | term CONCATENATE
          | term
          ;

term: factor
    | factor MULT
    | factor DIV
    | factor AND
    ;

factor: INT
    | STRING
    | IDENTIFIER
    | PLUS factor
    | MINUS factor
    | NOT factor
    | SCANF OPEN_PAR CLOSE_PAR
    | OPEN_PAR relexpression CLOSE_PAR
    ;

assigment: var_type IDENTIFIER EQUAL relexpression;
print: PRINT OPEN_PAR relexpression CLOSE_PAR;
if: IF OPEN_PAR relexpression CLOSE_PAR statement else;
while: WHILE OPEN_PAR relexpression CLOSE_PAR statement;
else: ELSE statement | ;
var_type: VAR_TYPE IDENTIFIER
        | SEPARATOR IDENTIFIER
        ;

%%

int main(){
  yyparse();
  return 0;
}