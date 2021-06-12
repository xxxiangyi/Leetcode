"""
Hash Table, Sliding Window
Time Complexity: O(n)
Space Complexity: O(n), in the worst case, there is no duplicate character in the string, all need to be stored in the hashmap
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        start = 0
        dic = {}
        
        for i, item in enumerate(s):
            if item in dic and start <= dic[item]:
                start = dic[item] + 1
            else:
                length = max(length, i - start + 1)
            
            dic[item] = i
        return length