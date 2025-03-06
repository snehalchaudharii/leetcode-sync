class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # min_price= float('inf')
        # max_profit=0

        # for price in prices:
        #     if price< min_price:
        #         min_price= price
        #     else:
        #         max_profit= max(max_profit, price-min_price)
        # return max_profit

        maxProfit=0
        bestBuy = prices[0]
        for i in range(1, len(prices)):
            if prices[i]> bestBuy:
                maxProfit = max(maxProfit, prices[i]-bestBuy)
        
            bestBuy = min(bestBuy, prices[i])
        return maxProfit

