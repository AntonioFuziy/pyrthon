# Pyrthon
A compiler built for my own programming language based on rural speech.

## EBNF

```
BLOCK = "[", STATEMENT, "]";

STATEMENT =  (λ | ASSIGNMENT | BLOCK | PRINT | IF | WHILE | VAR_TYPE), "apenas;";

RELATIONAL_EXPRESSION = EXPRESSION, { ("iguar" | "mernor " | "marior"), EXPRESSION };

EXPRESSION = TERM, { ("maris" | "mernos" | "ou" | "corcatena"), TERM };

TERM = FACTOR, { ("verzes" | "divirdido" | "tambem") };

FACTOR = INT | IDENTIFIER | STRING | CALL_FUNC | (("maris" | "mernos" | "contra"), FACTOR) | "[[", RELATIONAL_EXPRESSION, "]]" | SCANF;

ASSIGNMENT = VAR_TYPE, IDENTIFIER, "receba", RELATIONAL_EXPRESSION;

PRINT = "aspresenti", "[[", RELATIONAL_EXPRESSION, "]]";

IF = "sir", "[[", RELATIONAL_EXPRESSION, "]]", STATEMENT, { ("sirnao", STATEMENT) | λ };

WHILE = "enquarto", "[[", RELATIONAL_EXPRESSION, "]]", STATEMENT;

SCANF = "sorta", "[[", "]]";

VAR_TYPE = ("nurmero" | "tersto"), IDENTIFIER, { (",", IDENTIFIER) | λ };

INT = DIGIT, { DIGIT };

STRING = """, (LETTER | DIGIT), """;

DIGIT = (0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9);

IDENTIFIER = LETTER, { LETTER | DIGIT | "_" };

LETTER = (a | b | c | d | ... x | y | z | A | B | ... | Y | Z);

//sem tanta certeza
DECLARE_FUNC = (λ | FUNC_TYPE, "[[", ((FUNC_TYPE, {",", FUNC_TYPE }) | λ), "]]", STATEMENT);

FUNC_TYPE = { ("nurmero" | "tersto"), IDENTIFIER };

CALL_FUNC = IDENTIFIER, "[[" { IDENTIFIER }, { ",", IDENTIFIER }, "]]";

RETURN = "vorta", RELATIONAL_EXPRESSION;

RUN_CODE = DELCARE_FUNC
```
flex -l tokens.l

bison -dv parser.y

gcc -o pyrthon parser.tab.c lex.yy.c -lfl