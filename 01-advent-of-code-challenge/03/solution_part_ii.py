import sys

list = []
sum = 0

for line in sys.stdin:
    list.append(line.rstrip())

n = 3
splited = [list[i::n] for i in range(n)]

print(splited)