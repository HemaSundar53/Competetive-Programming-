def cal_val(l):
    s = 0
    for i in l:
        s = s*10 + i
    return s

a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
print(cal_val(a)+cal_val(b))