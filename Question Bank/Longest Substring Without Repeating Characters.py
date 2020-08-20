def lengthOfLongestSubstring(s):
    if len(s)==0:
        return 0
        
    d = {}
    st,ln = 0,0
        
    for i in range(len(s)):
        if s[i] in d and st<=d[s[i]]:
            st = d[s[i]]+1
        else:
            ln = max(ln,i-st+1)
        d[s[i]]=i
        
    return ln
    
st = input()
print(lengthOfLongestSubstring(st))