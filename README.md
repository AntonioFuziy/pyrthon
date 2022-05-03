# fuziy++
A compiler built for my own programming language

## EBNF

```
BLOCK = "[", STATEMENT, "]";

STATEMENT =  (λ | ASSIGNMENT | BLOCK | PRINT | IF | WHILE), "apenas;";

RELATIONAL_EXPRESSION = EXPRESSION, { ("igual" | "menor que" | "maior que"), EXPRESSION };

EXPRESSION = TERM, { ("mais" | "menos" | "or"), TERM };

TERM = FACTOR, { ("vezes" | "dividido" | "and") };

FACTOR = NUMBER | IDENTIFIER | (("mais" | "menos" | "inverso"), FACTOR) | "[", RELATIONAL_EXPRESSION, "]" | SCANF;

ASSIGNMENT = TYPE, IDENTIFIER, "receba", EXPRESSION;

PRINT = "mostre", "[", EXPRESSION, "]";

IF = "se", "[", RELATIONAL_EXPRESSION, "]", STATEMENT, { ("senao", STATEMENT) | λ };

WHILE = "enquanto", "[", RELATIONAL_EXPRESSION, "]", STATEMENT;

SCANF = "sorta", "[", "]";

TYPE = ("int"| "double" | "string");

FUNCTION = TYPE, IDENTIFIER, BLOCK;

NUMBER = DIGIT, { DIGIT };

DIGIT = ( 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 );

IDENTIFIER = LETTER, { LETTER | DIGIT | "_" };

LETTER = (a | b | c | d | ... x | y | z | A | B | ... | Y | Z );
```
