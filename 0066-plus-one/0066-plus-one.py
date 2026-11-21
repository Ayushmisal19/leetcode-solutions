class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        ch =""
        result = []
        for i in digits:
            ch = ch + str(i)
        ch = int(ch) + 1
        lh = str(ch)
        for i in lh:
            result.append(int(i))
        return result
        
