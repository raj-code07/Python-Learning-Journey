def maximumProfit(prices):
    res=0
    lmax=prices[0]
    lmin=prices[0]
    n=len(prices)
    i=0
    while i<n-1:

        #local minima
        while i<n-1 and prices[i]>=prices[i+1]:
            i+=1
        lmin=prices[i]
        #loacl maxima
        while i<n-1 and prices[i]<=prices[i+1]:
            i+=1
        lmax=prices[i]

        res+=(lmax-lmin)
    return res
prices=[100,180,300,40,50,60,70]
print(maximumProfit(prices))

