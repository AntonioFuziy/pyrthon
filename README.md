# Pyrthon
A compiler built for my own programming language based on rural speech.

**Instructions to execute:**

Go to this path

```bash
cd compiler
```

Execute the `main.py` script and don't forget to include the `.pyr` script to run the program.

```bash
python3 main.py test_scripts/pyr_scripts/hello_world.pyr

or

python3 main.py test_scripts/pyr_scripts/{ANY_SCRIPT}
```

The Pyrthon scripts are located on 

```bash
cd compiler/test_scripts/pyr_scripts/
```

## EBNF

```
PROGRAM = (λ | DECLARATION);

DECLARATION = ("nurmero" | "tersto" | "vazi"), IDENTIFIER, "(", { ("nurmero" | "tersto"), IDENTIFIER, { "," | ("nurmero" | "tersto"), IDENTIFIER} }, ")", BLOCK;

BLOCK = ("[", STATEMENT, "]" | "[", "]");

STATEMENT =  (((λ | ASSIGNMENT | PRINT  | VAR_TYPE | RETURN), ";") | (BLOCK | IF | WHILE));

FACTOR = INT | STRING | (IDENTIFIER, { "(", { RELEXPRESSION, { "," | RELEXPRESSION } } ")" }) | (("maris" | "mernos" | "contra" FACTOR) | "(", RELEXPRESSION, ")" | SCANF;

TERM = FACTOR, { ("verzes" | "divirdido" | "tambem"), FACTOR };

EXPRESSION = TERM, { ("maris" | "mernos" | "ou"), TERM } ;

RELEXPRESSION = EXPRESSION , {("mernor" | "marior" | iguar") , EXPRESSION } ;

WHILE = "enquarto", "(", RELEXPRESSION ,")", STATEMENT;

IF = "si", "(", RELEXPRESSION ,")", STATEMENT, (("sirnao", STATEMENT) | λ );

ASSIGNMENT = (IDENTIFIER, "receba", RELEXPRESSION) | ( "(", { RELEXPRESSION, { "," | RELEXPRESSION } }, ")" );

RETURN = "vorte" , "(", RELEXPRESSION, ")";

PRINT = "aspresenti", "(", RELEXPRESSION, ")";

SCANF = "sorta", "(", ")";

IDENTIFIER = LETTER, { LETTER | DIGIT | "_" };

DIGIT = (0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9);

INT = DIGIT, { DIGIT };

VAR_TYPE = ("nurmero" | "tersto") , IDENTIFIER , (λ | {"," , IDENTIFIER });

STRING = """, (LETTER | DIGIT), """;

LETTER = ( a | ... | z | A | ... | Z ) ;
```