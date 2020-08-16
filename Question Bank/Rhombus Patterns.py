n = int(input())
for i in range(n):
	print(' '*(n-(i+1))+'*'*n)
print('')
for i in range(n):
    if i==0 or i==n-1:
        print(' '*(n-(i+1))+'*'*n)
    else:
        print(' '*(n-(i+1))+'*'+' '*(n-2)+'*')