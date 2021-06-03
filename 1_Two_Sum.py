"""
Hash Table, Array

Time Complexity: O(n), n is the length of nums
Space Complexity: O(n), the extra space stores at most n elements
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, item in enumerate(nums):
            cur = target - item
            if cur in dic:
                return [dic[cur], i]
            dic[item] = i
        return []