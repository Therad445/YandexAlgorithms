import math

k1, m, k2, p2, n2 = input().split(" ")
k1 = int(k1)
m = int(m)
k2 = int(k2)
p2 = int(p2)
n2 = int(n2)


def apartment_number(k1, m, k2, p2, n2):
    nx = math.ceil(k2 / ((p2 - 1) * m + n2))
    print(nx)
    px = nx * m
    print(px)
    p1 = math.ceil(k1 / px)
    n1 = math.ceil((k1 - ((p1 - 1) * px)) / nx)
    return p1, n1


print(apartment_number(k1, m, k2, p2, n2))