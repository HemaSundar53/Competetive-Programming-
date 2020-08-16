l = list(map(int,input().strip().split(',')))
key = int(input())
beg = 0
end = len(l)-1

while beg<=end:
    mid = (beg+end)//2
    if key==l[mid]:
        print(mid)
        break
    elif key<l[mid]:
        end=mid-1
    else:
        beg=mid+1
