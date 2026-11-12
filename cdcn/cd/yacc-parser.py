
import ply.lex as lex
import ply.yacc as yacc

tokens = ('ID', 'PLUS', 'MUL', 'LP', 'RP')

t_PLUS = r'\+'
t_MUL = r'\*'
t_LP = r'\('
t_RP = r'\)'
t_ignore = ' \t'

def t_ID(t):
    r'[a-zA-Z]+'
    return t

def t_error(t):
    print("Invalid character")
    t.lexer.skip(1)

lexer = lex.lex()

def p_E_plus(p):
    'E : E PLUS T'
    p[0] = ('+', p[1], p[3])

def p_E_T(p):
    'E : T'
    p[0] = p[1]

def p_T_mul(p):
    'T : T MUL F'
    p[0] = ('*', p[1], p[3])

def p_T_F(p):
    'T : F'
    p[0] = p[1]

def p_F_ID(p):
    'F : ID'
    p[0] = p[1]

def p_F_expr(p):
    'F : LP E RP'
    p[0] = p[2]

def p_error(p):
    print("Invalid expression")

parser = yacc.yacc(method="LALR")

s = input("Enter expression: ")
result = parser.parse(s)

print("AST:", result)
