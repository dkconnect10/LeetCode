class Solution:
    def maxProfit(self, prices):
        mini=prices[0]
        profit = 0
        
        for i in range(1,len(prices)):
            newProfit = prices[i]-mini
            profit = max(newProfit,profit)
            mini = min(mini,prices[i])
        return profit