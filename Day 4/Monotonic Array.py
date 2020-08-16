def isMonotonic(A):
    if A==sorted(A) or A==sorted(A)[::-1]:
        return True
    return False

l = list(map(int,input().strip().split(',')))
print(isMonotonic(l))