def print_i(n):
    if n==1:
        print(1)
    else:
        print_i(n-1)
        print(n)

n = int(input())
print_i(n)