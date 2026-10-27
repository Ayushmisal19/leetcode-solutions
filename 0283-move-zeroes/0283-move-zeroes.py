class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
       x = 0
       for i in range(len(nums)):
        if nums[i] == 0:
          nums.append(nums[i])
          nums.remove(nums[i])
         
        