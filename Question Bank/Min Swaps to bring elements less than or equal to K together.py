def minSwap(arr, n, k) : 

	count = 0
	for i in range(0, n) : 
		if (arr[i] <= k) : 
			count = count + 1

	bad = 0
	for i in range(0, count) : 
		if (arr[i] > k) : 
			bad = bad + 1
	
	ans = bad 
	j = count 
	for i in range(0, n) : 
		
		if(j == n) : 
			break

		if (arr[i] > k) : 
			bad = bad - 1

		if (arr[j] > k) : 
			bad = bad + 1

		j = j + 1

	return ans 


arr = list(map(int,input().split()))
n = len(arr) 
k = int(input())
print (minSwap(arr, n, k)) 