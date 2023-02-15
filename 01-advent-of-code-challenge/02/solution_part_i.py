import sys

# A - Rock, B - Paper, C - Scissors
# X - Rock, Y - Paper, Z - Scissors

list = []
pontuation = 0

for line in sys.stdin:
    list.append(line.rstrip())

for i in list:
    arr = i.split()
    if(arr[1] == 'X'):
        pontuation += 1
        if(arr[0] == 'A'):
            pontuation += 3
        if(arr[0] == 'B'):
            pontuation += 0
        if(arr[0] == 'C'):
            pontuation += 6
    if(arr[1] == 'Y'):
        pontuation += 2
        if(arr[0] == 'A'):
            pontuation += 6
        if(arr[0] == 'B'):
            pontuation += 3
        if(arr[0] == 'C'):
            pontuation += 0
    if(arr[1] == 'Z'):
        pontuation += 3
        if(arr[0] == 'A'):
            pontuation += 0
        if(arr[0] == 'B'):
            pontuation += 6
        if(arr[0] == 'C'):
            pontuation += 3

print(pontuation)