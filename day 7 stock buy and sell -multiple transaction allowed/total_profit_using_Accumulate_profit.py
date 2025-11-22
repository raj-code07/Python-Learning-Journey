def maximumProfit(prices) -> int:
    res=0
    for i in range(1,len(prices)):
        if prices[i]>prices[i-1]:
            res+=prices[i]-prices[i-1]
    return res
prices=[100,180,300,40,50,60,70]
print(maximumProfit(prices))