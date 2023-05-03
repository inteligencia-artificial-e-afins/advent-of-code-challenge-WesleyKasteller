import sys

b = ''

for i, c in enumerate(sys.stdin.readlines()[0]):
    b += c
    if (len(b) > 14):
        b = b[1:]
    if (len(set(b)) == 14 and len(b) == 14):
        print(i + 1)
        break