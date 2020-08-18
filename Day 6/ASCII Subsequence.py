def subseq(s,sub):
    if len(s)==0:
        print(sub)
        return
    subseq(s[1:],sub+s[0])
    subseq(s[1:],sub)
    subseq(s[1:],sub+str(ord(s[0])))


subseq('AB','')