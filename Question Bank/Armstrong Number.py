n = int(input())
num = n
d = 0
while num!=0:
    d+=1
    num/=10
    
sum = 0
num = n

while num!=0:
    sum += ((num%10)**d)
    num/=10
    print(sum)

if sum==n:
    print('{} is an Armstrong number'.format(n))
else:
    print('{} is not a Armstrong number'.format(n))