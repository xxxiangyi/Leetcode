"""
Two Pointers

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
            
"""
Recursion

Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        def reverse(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                reverse(left + 1, right - 1)
        
        reverse(0, len(s) - 1)