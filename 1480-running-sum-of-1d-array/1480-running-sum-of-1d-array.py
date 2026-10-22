class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        ch = 0
        list_1 = []
        for i in nums:
            ch = ch + i
            list_1.append(ch)
        return list_1
    
        