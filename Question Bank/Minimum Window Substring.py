def minWindow(s, t):
    left,right = 0,0
    while left<len(s) and right<len(s):
        if s[left] in t:
            while check(s[left:right+1],t):
                right+=1
        else:
            l.append(s[left:right])
            left+=1
    print(l)
            
def check(s,t):
    d = {}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i in t:
        if i not in d or d[i]!=1:
            return False
    return True