def longestCommonPrefix(strs):
    if strs==[]:
        return ''
    common = min(strs,key=len)
    
    for i in range(len(common)):
        for s in strs:
            if s[i]!=common[i]:
                return common[:i]
    return common
    

l = list(map(str,input().strip().split(',')))
print(longestCommonPrefix(l))