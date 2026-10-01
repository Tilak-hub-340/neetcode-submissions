class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = prices[0] 
        max_val = 0

        for i in range(1, len(prices)):
            if prices[i] < min_val:
                min_val = prices[i]

            profit = prices[i] - min_val 

            if profit > max_val:
                max_val = profit 
        return max_val        