"""
String
"""
class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            sign = 1
        elif x < 0:
            sign = -1
            x *= -1
        else:
            return 0
        
        temp = int(str(x)[::-1])
        if temp > 2 ** 31 - 1:
            return 0
        else:
            return sign * temp
        