n = int(input())
l = []
for i in range(n):
    l.append(list(map(int,input().strip().split(','))))
print(l)

l = [[l[j][i] for j in range(n)] for i in range(n)]
l = [l[i][::-1] for i in range(n)]
print(l)