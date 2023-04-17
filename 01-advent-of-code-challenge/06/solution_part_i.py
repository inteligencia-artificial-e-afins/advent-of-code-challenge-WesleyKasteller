import sys

b = ''

for i, c in enumerate(sys.stdin.readlines()[0]):
    b += c
    if (len(b) > 4):
        b = b[1:]
    if (len(set(b)) == 4 and len(b) == 4):
        print(i + 1)
        break