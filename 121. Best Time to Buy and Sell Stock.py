class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices [0]
        profit = []

        if len(prices) == 1:
            return 0
        else:

            for p in prices [1:]:
                if p < buy:
                    buy = p
                profit.append(p - buy)
        
        return max(profit)
        
