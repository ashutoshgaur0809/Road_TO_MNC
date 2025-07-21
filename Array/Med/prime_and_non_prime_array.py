class Solution:
    def is_prime(self, n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def splitArray(self, nums: List[int]) -> int:
        a = []
        b = []
        for i in range(len(nums)):
            if self.is_prime(i):
                a.append(nums[i])
            else:
                b.append(nums[i])
            
        return abs(sum(a)-sum(b))
    
# Example 1:

# Input: nums = [2,3,4]

# Output: 1

# Explanation:

# The only prime index in the array is 2, so nums[2] = 4 is placed in array A.
# The remaining elements, nums[0] = 2 and nums[1] = 3 are placed in array B.
# sum(A) = 4, sum(B) = 2 + 3 = 5.
# The absolute difference is |4 - 5| = 1.
# Example 2:

# Input: nums = [-1,5,7,0]

# Output: 3

# Explanation:

# The prime indices in the array are 2 and 3, so nums[2] = 7 and nums[3] = 0 are placed in array A.
# The remaining elements, nums[0] = -1 and nums[1] = 5 are placed in array B.
# sum(A) = 7 + 0 = 7, sum(B) = -1 + 5 = 4.
# The absolute difference is |7 - 4| = 3.
#  ©leetcode