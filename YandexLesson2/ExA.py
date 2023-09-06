def isa(lst):
    i = 0
    p = lst[0]
    while i < len(lst):
        if lst[i + 1] > p:
            p = lst[i + 1]
            i += 1
        else:
            print('NO')
            return 0
    print('YES')


lt = list(map(int, input().split()))
isa(lt)

def IsAscending(A):
    i = 0
    f = True
    while f and i + 1 < len(A):
        f = A[i] < A[i + 1]
        i += 1
    return f


lt = list(map(int, input().split()))
print('YES' if IsAscending(lt) else 'NO')
