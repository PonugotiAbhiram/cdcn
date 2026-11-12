import re
keywords=["int","char","float","if","else","while","for","return","void"]
pattern=r'//.*|/\*[\s\S]*?\*/|[a-zA-Z_][a-zA-Z0-9_]*|[0-9]+|[+\-*/=<>!]+|[(){};,]'
print("Enter the code snippet:")
text=input()
tokens=re.findall(pattern,text)
for token in tokens:
    if token.startswith("//") or token.startswith("/*"):
        continue
    elif token in keywords:
        print(f"{token} : keyword")
    elif re.match(r'[0-9]+', token):
        print(f"{token} : number")
    elif re.match(r'[a-zA-Z_][a-zA-Z0-9_]*', token):
        print(f"{token} : identifier")
    elif re.match(r'[+\-*/=<>!]+', token):
        print(f"{token} : operator")
    elif re.match(r'[(){};,]', token):
        print(f"{token} : special character")
    else:
        print(f"{token} : unknown")