
import ply.lex as lex
import ply.yacc as yacc

tokens = ('ID', 'PLUS', 'MINUS', 'MUL', 'DIV', 'LP', 'RP')

t_PLUS = r'\+'
t_MINUS = r'-'
t_MUL = r'\*'
t_DIV = r'/'
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

# Grammar rules
def p_E_plus(p):
    'E : E PLUS T'
    p[0] = ('+', p[1], p[3])

def p_E_minus(p):
    'E : E MINUS T'
    p[0] = ('-', p[1], p[3])

def p_E_T(p):
    'E : T'
    p[0] = p[1]

def p_T_mul(p):
    'T : T MUL F'
    p[0] = ('*', p[1], p[3])

def p_T_div(p):
    'T : T DIV F'
    p[0] = ('/', p[1], p[3])

def p_T_F(p):
    'T : F'
    p[0] = p[1]

def p_F_ID(p):
    'F : ID'
    p[0] = p[1]

def p_F_group(p):
    'F : LP E RP'
    p[0] = p[2]

def p_error(p):
    print("Invalid expression")

parser = yacc.yacc()

# Three Address Code
temp = 0

def generate(node):
    global temp

    if isinstance(node, str):
        return node

    left = generate(node[1])
    right = generate(node[2])

    temp += 1
    result = 't' + str(temp)

    print(result, '=', left, node[0], right)
    return result

# Main
s = input("Enter code fragment: ")
ast = parser.parse(s)

if ast is not None:
    print("Three Address Code:")
    generate(ast)
