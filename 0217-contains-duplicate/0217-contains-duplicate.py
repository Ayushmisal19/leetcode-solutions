class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
      nums1 = nums
      
      if len(nums) == len(list(set(nums1))):
        return False
      else:
        return True
        