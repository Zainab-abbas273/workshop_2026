class Solution(object):
    def maxProfit(self, prices):
        min_price=prices[0]
        profit=0
        for i in range(1,len(prices)):
            cur_price=prices[i]-min_price
            if cur_price>profit:
                profit=cur_price
            min_price=min(min_price,prices[i])
        return profit
prices=[7,1,5,3,6,4]
print(Solution().maxProfit(prices))