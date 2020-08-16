n = int(input())
for i in range(n):
    if i==n//2:
        print('*'*n)
    elif i<n//2:
        if i==0:
            print('*'+' '*(n//2-1)+'*'*(n//2+1))
        else:
            print('*'+' '*(n//2-1)+'*'+' '*(n//2))
    else:
        if i==n-1:
            print('*'*(n//2+1)+' '*(n//2-1)+'*')
        else:
            print(' '*(n//2)+'*'+' '*(n//2-1)+'*')
