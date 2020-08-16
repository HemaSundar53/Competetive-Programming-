def binary_search(l,key,beg,end):
    
    while beg<=end:
        mid = (beg+end)//2
        if key==l[mid]:
            return mid
        elif key<l[mid]:
            end=mid-1
        else:
            beg=mid+1            
    return -1


def search(l,key,beg,end):
    if key<=l[end]:
        return binary_search(l,key,beg,end)
    else:
        beg = end
        end *= 2
        return search(l,key,beg,end)
        

l = list(map(int,input().strip().split(',')))
key = int(input())

print(search(l,key,0,1))
