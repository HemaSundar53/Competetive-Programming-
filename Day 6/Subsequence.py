def subseq(s,sub):
    if len(s)==0:
        l.append(sub)
        return
    subseq(s[1:],sub+s[0])
    subseq(s[1:],sub)

l = []
subseq('abc','')
print(sorted(l,key=len))