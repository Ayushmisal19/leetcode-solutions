class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        res = []


        for i in nums1:
            if i in nums2:
                res.append(i)
            else:
                continue
        return res        