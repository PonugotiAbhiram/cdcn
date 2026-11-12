import ply.lex as lex
tokens=(
    'KEYWORD','IDENTIFIER','NUMBER','OPERATOR','SPECIALCHARACTER')
def t_COMMENT(t):
    r'//.*|/\*[\s\S]*?\*/'
    pass
def t_KEYWORD(t):
    r'int|char|float|if|else|while|for|return|void'
    return t
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t
def t_NUMBER(t):
    r'[0-9]+'
    return t
def t_OPERATOR(t):
    r'[+\-*/=<>!]+'
    return t  
def t_SPECIALCHARACTER(t):
    r'[(){};,]'
    return t
t_ignore = ' \t\n'
def t_error(t):
    t.lexer.skip(1)
lexer=lex.lex()
data=input("Enter the code snippet:\n")
lexer.input(data)
for tok in lexer:
    print(f"{tok.value} : {tok.type.lower()}")