class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = float('inf')
        max_profit = 0

        for right in range(len(prices)):
            if prices[right] < minimum:
                minimum = prices[right]
            else:
                max_profit = max(max_profit, prices[right] - minimum)

        return max_profit