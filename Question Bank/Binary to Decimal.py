n = int(input())
i = 0
sum = 0

while n!=0:
    sum += (n%10)*(2**i)
    i+=1
    n/=10

print(sum)