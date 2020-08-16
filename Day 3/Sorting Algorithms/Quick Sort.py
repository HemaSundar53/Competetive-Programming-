def partition(l,low,high):
    i = low
    for j in range(low,high):
        if l[j]<l[high]:
            l[i],l[j]=l[j],l[i]
            i+=1
    
    l[high],l[i]=l[i],l[high]
    return i


def quick(l,low,high):
    if low<high:
        k = partition(l,low,high)
        quick(l,low,k-1)
        quick(l,k+1,high)
    return l


lis = list(map(int,input().strip().split(',')))
print(quick(lis,0,len(lis)-1))