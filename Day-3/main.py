def Solution(self, candies, extraCandies):
    max_candies=max(candies)
    result=[]
    for i in range(len(candies)):
        temp=extraCandies+candies[i]
        if temp>=max_candies:
            result.append(True)
        else:
            result.append(False)
    return result