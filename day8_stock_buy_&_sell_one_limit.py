def maximumProfit(prices):
        
    minSofar=prices[0]
        
    res=0
    for i in range(1,len(prices)):
        minSofar=min(minSofar,prices[i])
        res=max(res, prices[i]-minSofar)
    return res
prices=[7,10,1,3,6,9,2]
print(maximumProfit(prices))
