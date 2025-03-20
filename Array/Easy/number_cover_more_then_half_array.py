class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        for i,j in d.items():
            if j > (len(nums) / 2):
                return i

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2