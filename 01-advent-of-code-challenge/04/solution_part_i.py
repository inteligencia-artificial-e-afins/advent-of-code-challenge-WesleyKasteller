import sys

list = []
sum = 0

for line in sys.stdin:
    list.append(line.rstrip())

for idx, i in enumerate(list): 
    arr = i.split(',')
    arr2 = [int(n) for n in arr[0].split('-')]
    arr3 = [int(n) for n in arr[1].split('-')]

    if (arr2[0] >= arr3[0] and arr2[1] <= arr3[1]):
        sum += 1
    elif (arr3[0] >= arr2[0] and arr3[1] <= arr2[1]):
        sum += 1

print(sum)