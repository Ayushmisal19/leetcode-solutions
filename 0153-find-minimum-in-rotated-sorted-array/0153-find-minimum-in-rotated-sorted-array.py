class Solution:
    def findMin(self, nums: list[int]) -> int:
        list_1 = sorted(nums)
        return(list_1[0])