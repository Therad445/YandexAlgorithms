x = int(input())
y = int(input())
z = int(input())
if (x <= 0) or (y <= 0) or (z <= 0):
    print("NO")
    exit()
maxElem = max(x, y, z)
if x == maxElem:
    if x == ((y ** 2) + (z ** 2)) ** (1/2):
        print("YES")
    else:
        print("NO")
elif y == maxElem:
    if y == ((x ** 2) + (y ** 2)) ** (1/2):
        print("YES")
    else:
        print("NO")
elif z == maxElem:
    if z == ((x ** 2) + (y ** 2)) ** (1 / 2):
        print("YES")
    else:
        print("NO")

a, b, c = map(int, input().split())
if a + b > c and a + c > b and b + c > a:
    print("YES")
else:
    print("NO")
