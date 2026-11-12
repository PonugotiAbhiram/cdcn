
import ply.lex as lex
import ply.yacc as yacc

# Tokens
tokens = ('ID', 'NUM', 'PLUS', 'MINUS', 'MUL', 'DIV', 'LP', 'RP')

# Token rules
t_PLUS  = r'\+'
t_MINUS = r'-'
t_MUL   = r'\*'
t_DIV   = r'/'
t_LP    = r'\('
t_RP    = r'\)'
t_ignore = ' \t'

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z]+'
    return t

def t_error(t):
    global error
    error = True
    t.lexer.skip(1)

lexer = lex.lex()

# Grammar rules
def p_E_plus(p):
    'E : E PLUS T'
    p[0]=1

def p_E_minus(p):
    'E : E MINUS T'
    p[0]=1

def p_E_T(p):
    'E : T'
    p[0]=1

def p_T_mul(p):
    'T : T MUL F'
    p[0]=1

def p_T_div(p):
    'T : T DIV F'
    p[0]=1

def p_T_F(p):
    'T : F'
    p[0]=1

def p_F_group(p):
    'F : LP E RP'
    p[0]=1

def p_F_ID(p):
    'F : ID'
    p[0]=1

def p_F_NUM(p):
    'F : NUM'
    p[0]=1

def p_error(p):
    global error
    error = True
    print("Invalid Expression")

parser = yacc.yacc()

# Input
s = input("Enter arithmetic expression: ")
result = parser.parse(s)

if result is not None and not error:
    print("Valid Expression")
