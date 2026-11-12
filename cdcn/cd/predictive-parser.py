
s = input("Enter input: ")
i = 0

def E():
    global i
    if not T():
        return False
    while i < len(s) and s[i] == '+':
        i += 1
        if not T():
            return False
    return True

def T():
    global i
    if not F():
        return False
    while i < len(s) and s[i] == '*':
        i += 1
        if not F():
            return False
    return True

def F():
    global i
    if i < len(s) and s[i] == 'i':
        i += 1
        return True
    if i < len(s) and s[i] == '(':
        i += 1
        if E() and i < len(s) and s[i] == ')':
            i += 1
            return True
    return False

if E() and i == len(s):
    print("String Accepted")
else:
    print("String Rejected")
