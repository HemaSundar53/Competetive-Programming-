arr = [[1,2,3,4], [11,14,15,16], [21,24,27,28],[31,33,34,37]]
key = 27

# Approach-1, Linear Search
for i in range(4):
	for j in range(4):
		if key==arr[i][j]:
			print(i,j)


# Approach-2, Binary Search for every row


#Approach-3, Staircase
i = 0
j = 3
while i<3:
	while j>=0:
		if arr[i][j]==key:
			print(i,j)
			break
		elif arr[i][j]>key:
			j-=1
		else:
			i+=1
