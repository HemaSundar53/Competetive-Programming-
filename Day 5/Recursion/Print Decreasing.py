def print_d(n):
    if n==1:
        print(1)
    else:
        print(n)
        print_d(n-1)

n = int(input())
print_d(n)