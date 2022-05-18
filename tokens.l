%{
#include <string>
#include "node.h"
#include "parser.hpp"
#define SAVE_TOKEN yylval.string = new std::string(yytext, yyleng)
#define TOKEN(t) (yylval.token = t)
extern "C" int yywrap() { }
%}

%%

[ \t\n]                 ;
[a-zA-Z0-9\]*           SAVE_TOKEN; return STRING;
[a-zA-Z_][a-zA-Z0-9_]*  SAVE_TOKEN; return IDENTIFIER;
[0-9]+                  SAVE_TOKEN; return INT;

"receba"                return TOKEN(EQUAL);
"iguar"                 return TOKEN(EQUALTO);
"mernor"                return TOKEN(MINOR);
"marior"                return TOKEN(GREATER);
"contra"                return TOKEN(NOT);
"tambem"                return TOKEN(AND);
"ou"                    return TOKEN(OR);

"[["                    return TOKEN(OPEN_PAR);
"]]"                    return TOKEN(CLOSE_PAR);
"["                     return TOKEN(OPEN_BRACKET);
"]"                     return TOKEN(CLOSE_BRACKET);
"apenas;"               return TOKEN(SEMI_COLON);

"corcatena"             return TOKEN(CONCATENATE);
","                     return TOKEN(SEPARATOR);
"maris"                 return TOKEN(PLUS);
"mernos"                return TOKEN(MINUS);
"verzes"                return TOKEN(MULT);
"divirdido"             return TOKEN(DIV);

"aspresenti"            return TOKEN(PRINTF);
"sorta"                 return TOKEN(SCANF);
"enquarto"              return TOKEN(WHILE);
"sir"                   return TOKEN(IF);
"sirnao"                return TOKEN(ELSE);
"nurmero"               return TOKEN(INT);
"tersto"                return TOKEN(STRING);
"return"                return TOKEN(RETURN);

.                       printf("Unknown token!n"); yyterminate();

%%