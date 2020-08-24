def keypad(s,sub):
    if len(s)==0:
        print(sub)
        return
    
    if (int(s[0])+64)>64 and (int(s[0])+64)<91:
        keypad(s[1:],sub+chr(int(s[0])+64))
    if len(s)>1 and (int(s[0]+s[1])+64)>64 and (int(s[0]+s[1])+64)<91:
        keypad(s[2:],sub+chr(int(s[0]+s[1])+64))


n = int(input())
keypad(str(n),'')
