def sortedSquares(A):
	l=[]
	for i in A:
	    l.append(i**2)
	return sorted(l)

arr = list(map(int, input().strip().split()))
print(sortedSquares(arr))