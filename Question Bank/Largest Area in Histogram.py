def largestRectangleArea(heights):
    m = 0
    for i in range(len(heights)):
        for j in range(i,len(heights)):
            m = max(m,(j-i+1)*min(heights[i:j+1]))
    return m