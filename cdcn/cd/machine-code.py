ast = ('+', 'a', ('*', 'b', 'c'))

reg = 0

def generate(node):
    global reg

    if isinstance(node, str):
        reg += 1
        r = 'R' + str(reg)
        print('LOAD', r, ',', node)
        return r

    left = generate(node[1])
    right = generate(node[2])

    if node[0] == '+':
        print('ADD', left, ',', right)
    elif node[0] == '-':
        print('SUB', left, ',', right)
    elif node[0] == '*':
        print('MUL', left, ',', right)
    elif node[0] == '/':
        print('DIV', left, ',', right)

    return left

result = generate(ast)
print('RESULT stored in', result)