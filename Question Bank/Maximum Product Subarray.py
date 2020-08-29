def maxProduct(nums):
    m = a = b =nums[0]
    for n in nums[1:]:
        b,a = max(n, n*b, n*a), min(n, n*b, n*a)
        m = max(m,b)
    return m