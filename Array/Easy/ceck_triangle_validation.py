class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if nums[0] + nums[1] > nums[2] and nums[1] + nums[2] > nums[0] and nums[0] + nums[2] > nums[1]:
            if len(set(nums)) == 1:
                return "equilateral"
            if len(set(nums)) == 2:
                return "isosceles"
            else:
                return "scalene"
        else:
            return "none"
        
# trianle rule:
#  a + b > c and b + c > a and a + c > b
#  a + b + c = 180

# if 3 sides are equal, it is equilateral
# if 2 sides are equal, it is isosceles
# if no sides are equal, it is scalene