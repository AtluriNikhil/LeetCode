class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for price in prices[1:]:
            if min_price > price:
                min_price = price
            else:
                if max_profit < price - min_price:
                    max_profit = price - min_price
        return max_profit
