import math

x1, y1, x2, y2 = input().split(" ")
x1 = int(x1)
y1 = int(y1)
x2 = int(x2)
y2 = int(y2)
mas1 = [x1, y1]
mas2 = [x2, y2]
x = math.inf
mas = []
for first in mas1:
    for second in mas2:
        if first == x1:
            xx = first + second
            s = xx * y1
            if s < x:
                x = s
                memory = [xx, y1]
                print(memory)
        else:
            yy = first + second
            s = yy * x1
            memory_erase = [x1, yy]
            if s < x:
                x = s
                memory = [yy, y1]
                print(memory)
        if s == x:
                print(memory)

print(memory)
