import sys

list = []
sum = 0

for line in sys.stdin:
    list.append(line.rstrip())

for i in range(0, len(list), 3):
    aux = list