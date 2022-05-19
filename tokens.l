%{
#include <stdio.h>
#include <string.h>
#include "parser.tab.h"
%}

%%

[ \t\n]

"receba"                return EQUAL;
"iguar"                 return EQUALTO;
"mernor"                return MINOR;
"marior"                return GREATER;
"contra"                return NOT;
"tambem"                return AND;
"ou"                    return OR;

"[["                    return OPEN_PAR;
"]]"                    return CLOSE_PAR;
"["                     return OPEN_BRACKET;
"]"                     return CLOSE_BRACKET;
"apenas;"               return SEMI_COLON;

"aspresenti"            return PRINT;
"sorta"                 return SCANF;
"enquarto"              return WHILE;
"sir"                   return IF;
"sirnao"                return ELSE;
"nurmero"               return VAR_TYPE;
"tersto"                return VAR_TYPE;
"return"                return RETURN;

"corcatena"             return CONCATENATE;
","                     return SEPARATOR;
"maris"                 return PLUS;
"mernos"                return MINUS;
"verzes"                return MULT;
"divirdido"             return DIV;

[a-zA-Z0-9]            return STRING;
[a-zA-Z_][_a-zA-Z0-9]  return IDENTIFIER;
[0-9]+                 return INT;

.                      printf("Unknown token!n"); yyterminate();

%%