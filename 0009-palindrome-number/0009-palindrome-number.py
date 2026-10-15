class Solution:
    def isPalindrome(self, x: int) -> bool:
     y = x
     char =""

     while y>0:
      digits = y % 10
      char = str(char) + str(digits)
      y = y //10
     if str(x) == char:
        return True
     elif x == 0:
        return True
     else:
        return False
            
        