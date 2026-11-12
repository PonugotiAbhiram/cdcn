
grammar = {
    'S': [['A', 'B']],
    'A': [['a'], ['#']],
    'B': [['b']]
}

# first = {nt: set() for nt in grammar}
# follow = {nt: set() for nt in grammar}
first={}
follow={}
for nt in grammar:
    first[nt]=set()
    follow[nt]=set()

def compute_first(nt):
    for p in grammar[nt]:
        if p == ['#']:
            first[nt].add('#')
        elif p[0] not in grammar:
            first[nt].add(p[0])
        else:
            first[nt].update(compute_first(p[0]) - {'#'})
            if '#' in compute_first(p[0]):
                first[nt].update(
                    compute_first(p[1]) if len(p) > 1 else {'#'}
                )
    return first[nt]

for nt in grammar:
    compute_first(nt)

follow['S'].add('$')
for _ in range(len(grammar)):
    for nt in grammar:
        for p in grammar[nt]:
            for i, ch in enumerate(p):
                if ch in grammar:
                    if i == len(p)-1:
                        follow[ch].update(follow[nt])
                    else:
                        nxt = p[i+1]
                        if nxt in grammar:
                            follow[ch].update(first[nxt]-{'#'})
                            if '#' in first[nxt]:
                                follow[ch].update(follow[nt])
                        else:
                            follow[ch].add(nxt)

print("FIRST:")
for nt in grammar:
    print(nt, ":", first[nt])

print("\nFOLLOW:")
for nt in grammar:
    print(nt, ":", follow[nt])
