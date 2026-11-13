class Solution:
    def reverseBits(self, n: int) -> int:
        binary_1 = format(n, '032b')
        ch = ''

        for i in binary_1[::-1]:
            ch = ch + i

        int_1 = int(ch, 2)

        return int_1