import sys

list = []
sum = 0

for line in sys.stdin:
    list.append(line.rstrip())

for i in list:
    a = i[:int(len(i) / 2)]
    b = i[int(len(i) / 2):]

    for element in a:
        if (element in b):            
            print(element)
            if (element.islower()):
                sum += ord(element) - 96
            else:
                sum += ord(element) - 38
            break

print(sum)