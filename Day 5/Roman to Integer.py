def romanToInt(s):
    sum = 0
    d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,' ':0}
    n = len(s)
    s += ' '
    i = 0
    while (i<n):
        if s[i]=='I':
            if s[i+1]=='V' or s[i+1]=='X':
                sum -= d[s[i]]
            else:
                sum += d[s[i]]
        elif s[i]=='X':
            if s[i+1]=='L' or s[i+1]=='C':
                sum -= d[s[i]]
            else:
                sum += d[s[i]]
        elif s[i]=='C':
            if s[i+1]=='D' or s[i+1]=='M':
                sum -= d[s[i]]
            else:
                sum += d[s[i]]
        else:
            sum += d[s[i]]
        i += 1
        
    return sum
    

s = input()
print(romanToInt(s))