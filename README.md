# fuziy-plus-plus
A compiler built for my own programming language

## EBNF

```
BLOCK = "[", STATEMENT, "]";

STATEMENT = "apenas;" | (identifier, "receba", RELATIONAL_EXPRESSION, "apenas;") | (mostre, "[", RELATIONAL_EXPRESSION, "]", "apenas;") | (BLOCK) | (enquanto, "[", RELATIONAL_EXPRESSION, "]", STATEMENT) | (se, "[", RELATIONAL_EXPRESSION, "]", STATEMENT, { senao, STATEMENT });

RELATIONAL_EXPRESSION = EXPRESSION, { ("igual" | "menor que" | "maior que"), EXPRESSION };

EXPRESSION = TERM, { ("mais" | "menos" | "or"), TERM };

TERM = FACTOR, { ("vezes" | "dividido" | "and") };

FACTOR = number | identifier | ("mais" | "menos" | "inverso"), FACTOR | "[", RELATIONAL_EXPRESSION, "]" | sorta, "[", "]";
```