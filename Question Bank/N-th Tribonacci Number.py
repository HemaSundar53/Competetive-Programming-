def tribonacci(n):
    d = {0:0,1:1,2:1}
    def tri(n):
        if n in d:
            return d[n]
        d[n] = tri(n-1)+tri(n-2)+tri(n-3)
        return d[n]
    return tri(n)


n = int(input())
print(tribonacci(n))