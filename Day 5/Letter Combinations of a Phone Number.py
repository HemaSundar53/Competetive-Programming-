def letterCombinations(digits):
    if digits=='':
        return []
    nums = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
    l = []
        
    def combine(s,dig):
        if len(dig)==0:
            l.append(s)
        else:
            for i in nums[dig[0]]:
                combine(s+i,dig[1:])
                    
    combine('',digits)
    return l
    

st = input()
print(letterCombinations(st))