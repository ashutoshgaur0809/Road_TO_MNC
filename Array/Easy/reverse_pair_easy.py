# a = [1,3,2,3,1]
a =[2,4,3,5,1]

clk = 0
for i in range(0,len(a)):
    
    for j in range(i+1,len(a)):
        
        print(a[i],a[j])
        
        if a[i] > 2 * a[j]:
            clk += 1

print(clk)

# nums[i] > 2 * nums[j].
 

# Example 1:

# Input: nums = [1,3,2,3,1]
# Output: 2
# Explanation: The reverse pairs are:
# (1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
# (3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1
# Example 2:

# Input: nums = [2,4,3,5,1]
# Output: 3
# Explanation: The reverse pairs are:
# (1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 * 1
# (2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2 * 1
# (3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1