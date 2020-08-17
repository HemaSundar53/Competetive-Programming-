def power(a,b):
    if b==0:
        return 1
    else:
        return a*power(a,b-1)

def super_power(a,b):
    if b==0:
        return 1
    n = super_power(a,b/2)
    n = n*n
    if b%2==0:
        return n
    return a*n

a = int(input())
b = int(input())
print(power(a,b))
print(super_power(a,b)) #OPTIMIZED