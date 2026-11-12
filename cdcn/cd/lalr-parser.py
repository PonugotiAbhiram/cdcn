
import ply.lex as lex
import ply.yacc as yacc

tokens = ('NUM', 'PLUS', 'MINUS', 'MUL', 'DIV', 'LP', 'RP')

t_PLUS = r'\+'
t_MINUS = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_LP = r'\('
t_RP = r'\)'
t_ignore = ' \t'

def t_NUM(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

def t_error(t):
    global error
    error = True
    t.lexer.skip(1)

lexer = lex.lex()

# Grammar rules

def p_E_plus(p):
    'E : E PLUS T'
    p[0] = p[1] + p[3]

def p_E_minus(p):
    'E : E MINUS T'
    p[0] = p[1] - p[3]

def p_E_T(p):
    'E : T'
    p[0] = p[1]

def p_T_mul(p):
    'T : T MUL F'
    p[0] = p[1] * p[3]

def p_T_div(p):
    'T : T DIV F'
    p[0] = p[1] / p[3]

def p_T_F(p):
    'T : F'
    p[0] = p[1]

def p_F_group(p):
    'F : LP E RP'
    p[0] = p[2]

def p_F_NUM(p):
    'F : NUM'
    p[0] = p[1]

def p_error(p):
    global error
    error = True
    print("Invalid Expression")

parser = yacc.yacc(method="LALR")

s = input("Enter expression: ")
error = False

result = parser.parse(s)

if result is not None and not error:
    print("Expression is valid.")

