def isValid(s):
    if s=="":
        return 1
    if s[0]==']' or s[0]==')' or s[0]=='}' or len(s)%2!=0:
        return 0
    l=[]
    d={'(':')','[':']','{':'}'}
    for i in range(len(s)):
        if s[i]=='{' or s[i]=='[' or s[i]=='(':
            l.append(s[i])
        
        elif s[i]==']' or s[i]==')' or s[i]=='}':
            if s[i]==d[l[-1]]:
                l.pop()
            else:
                return 0
        else:
            return 0
        
    if l==[]:
        return 1
    return 0


s = input()
if isValid(s)==1:
    print(True)
else:
    print(False)
