def uniquePaths(m, n):
    l = [[1 for x in range(n)] for x in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            l[i][j] = l[i][j-1] + l[i-1][j]
        
    return l[m-1][n-1]