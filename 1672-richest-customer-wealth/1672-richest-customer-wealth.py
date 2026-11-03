class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        l = 0
        sum_2 = 0
        sum_1 = 0
        for i in range(len(accounts)):
            sum_1 = sum(accounts[i])
            sum_2 = max(sum_1,sum_2)
        return sum_2
            


        