class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        nums = list(s)
        stack =[]
        result = 0

        for i in range(len(nums)):
            while nums[i] in stack:
                stack.pop(0)
            stack.append(nums[i])
            result = max(result,len(stack))
        return(result)
        