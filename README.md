# Pyrthon
A compiler built for my own programming language based on rural speech.

## EBNF

```
PROGRAM = (λ | DECLARATION);

DECLARATION = ("nurmero" | "tersto" | "vazi"), IDENTIFIER, "(", { ("nurmero" | "tersto"), IDENTIFIER, "," | ("nurmero" | "tersto"), IDENTIFIER }, ")", BLOCK;

BLOCK = ("[", STATEMENT, "]" | "[", "]");

STATEMENT =  (λ | ASSIGNMENT | BLOCK | PRINT | IF | WHILE | VAR_TYPE | RETURN), ";";

RELATIONAL_EXPRESSION = EXPRESSION, { ("iguar" | "mernor " | "marior"), EXPRESSION };

EXPRESSION = TERM, { ("maris" | "mernos" | "ou" | "corcatena"), TERM };

TERM = FACTOR, { ("verzes" | "divirdido" | "tambem"), FACTOR };

FACTOR = INT | STRING | (IDENTIFIER, { "(", { RELATIONAL_EXPRESSION, "," | RELATIONAL_EXPRESSION } ")" }) | (("maris" | "mernos" | "contra"), FACTOR) | "(", RELATIONAL_EXPRESSION, ")" | SCANF;

ASSIGNMENT = (IDENTIFIER, "receba", RELATIONAL_EXPRESSION | "(", { RELATIONAL_EXPRESSION, "," | RELATIONAL_EXPRESSION }, ")");

PRINT = "aspresenti", "(", RELATIONAL_EXPRESSION, ")";

IF = "si", "(", RELATIONAL_EXPRESSION, ")", STATEMENT, { ("sirnao", STATEMENT) | SEMI_COLON };

WHILE = "enquarto", "(", RELATIONAL_EXPRESSION, ")", STATEMENT;

RETURN = "(", RELATIONAL_EXPRESSION, ")";

SCANF = "sorta", "(", ")";

INT = DIGIT, { DIGIT };

STRING = """, (LETTER | DIGIT), """;

DIGIT = (0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9);

IDENTIFIER = LETTER, { LETTER | DIGIT | "_" };

LETTER = (a | b | c | d | ... x | y | z | A | B | ... | Y | Z);

```