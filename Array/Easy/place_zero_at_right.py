class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l1 = []
        l2 = []
        for i in nums:
            if i == 0:
                l1.append(i)
            if i != 0:
                l2.append(i)
        
        nums[:] = l2 + l1