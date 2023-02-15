import sys

# A - Rock, B - Paper, C - Scissors
# X - Rock, Y - Paper, Z - Scissors

list = []
pontuation = 0

for line in sys.stdin:
    list.append(line.rstrip())

for i in list:
    arr = i.split()
    if(arr[0] == 'A'):
        if(arr[1] == 'X'):
            pontuation += (3 + 0)
        if(arr[1] == 'Y'):
            pontuation += (1 + 3)
        if(arr[1] == 'Z'):
            pontuation += (2 + 6)
    if(arr[0] == 'B'):
        if(arr[1] == 'X'):
            pontuation += (1 + 0)
        if(arr[1] == 'Y'):
            pontuation += (2 + 3)
        if(arr[1] == 'Z'):
            pontuation += (3 + 6)
    if(arr[0] == 'C'):
        if(arr[1] == 'X'):
            pontuation += (2 + 0)
        if(arr[1] == 'Y'):
            pontuation += (3 + 3)
        if(arr[1] == 'Z'):
            pontuation += (1 + 6)

print(pontuation)