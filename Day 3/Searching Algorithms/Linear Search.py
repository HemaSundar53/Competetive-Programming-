l = list(map(int,input().strip().split(',')))
key = int(input())
for i in range(len(l)):
	if l[i]==key:
		print(i)