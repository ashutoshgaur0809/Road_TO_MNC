class Solution:
    def sortColors(self, nums: List[int]) -> None:

        c0 = 0
        c1 = 0
        c2 = 0

        for i in nums:
            if i == 0:
                c0 += 1
            if i == 1:
                c1 += 1
            if i == 2:
                c2 += 1
        nums[:] = []
        for i in range(0,c0):
            nums.append(0)
        for i in range(c0,c0+c1):
            nums.append(1)
        for i in range(c0+c1,c0+c1+c2):
            nums.append(2)
