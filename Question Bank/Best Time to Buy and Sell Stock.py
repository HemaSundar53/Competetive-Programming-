def maxProfit(prices):
    p=0
    for i in range(len(prices)-1):
        if max(prices[i+1:])-prices[i]>p:
            p=max(prices[i+1:])-prices[i]
    return p