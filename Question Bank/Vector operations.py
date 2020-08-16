def vect(n,nums):
    l = []
    k = 0
    for i in range(len(nums)):
        if nums[i]=='a':
            l.append(nums[i+1])
        elif nums[i]=='b':
            l = sorted(l)
        elif nums[i]=='c':
            l = l[::-1]
        elif nums[i]=='d':
            l.insert(k,str(len(l)))
            k+=1
        elif nums[i]=='f':
            l = sorted(l)[::-1]
        elif nums[i]=='e':
            print(" ".join(l))
        else:
            continue


t =int(input())
for i in range(t):
    c = int(input())
    l = list(map(str,input().strip().split()))
    vect(c,l)
