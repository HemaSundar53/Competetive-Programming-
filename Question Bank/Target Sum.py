def findTargetSumWays(nums, S):
    if not nums:
        return 0
    d = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}
    for i in range(1, len(nums)):
        D = {}
        for j in d:
            D[j + nums[i]] = D.get(j + nums[i], 0) + d.get(j, 0)
            D[j - nums[i]] = D.get(j - nums[i], 0) + d.get(j, 0)
        d = D
    return d.get(S, 0)