# The idea of Kadane’s algorithm is to traverse over the array from left to right and for each element, 
# find the maximum sum among all subarrays ending at that element. The result will be the maximum of all these values. 

# steps
# 1. sum = sum + a[i]
# 2. maxi = max(sum,maxi)
# 3. id sum < 0 then sum = 0

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxi = float("-inf")
        sumi = 0
        for i in nums:
            sumi = sumi + i
            maxi = max(sumi,maxi)
            if sumi < 0:
                sumi = 0
        
        return maxi

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
