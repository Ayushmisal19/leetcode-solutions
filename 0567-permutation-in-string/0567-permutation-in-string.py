from itertools import permutations
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
       s1 =list(s1)
       s2 = list(s2)
       k = len(s1)
       window = s2[0:k]
       l=0
       while l+k<=len(s2):
        window = tuple(s2[l:k+l])
        if sorted(window) == sorted(s1):
            return True
        else:
            l+=1
       return False

        