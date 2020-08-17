def print_id(n):
    if n==1:
        print(1)
        print(0)
    else:
        print(n)
        print_id(n-2)
        print(n-1)
    
n = int(input())
print_id(n)