class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_sum = 0

        for right in range(len(prices)):
            if prices[right] < prices[left]:
                left = right
            else:
                sum_1 = prices[right] - prices[left]
                max_sum = max(max_sum,sum_1)
        return max_sum
        