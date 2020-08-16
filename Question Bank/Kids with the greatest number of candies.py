def kidsWithCandies(candies, extraCandies):
    l=[]
    for i in candies:
        if i+extraCandies >= max(candies):
            l.append(True)
        else:
            l.append(False)
    return l

cd = list(map(int, input().strip().split()))
n = int(input())
print(kidsWithCandies(cd,n))