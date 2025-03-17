a = [18,43,36,13,7]
l = []
s = []
for i in a:
            sum = 0
            for i in str(i):
                sum += int(i)
            l.append(sum)

for i in range(len(l)):
            for j in range(i+1,len(a)):
                if l[i] == l[j]:
                    s.append(a[i] + a[j])
        
if len(s) == 0:
    print("Not possible")
else:
    print("max sum we get is - ",max(s))


# Test Case 1:
# Input:
# python
# Copy
# Edit
# nums = [18, 43, 36, 13, 7]
# Step 1: Compute Digit Sums
# We calculate the sum of digits for each number:

# Number	Sum of Digits
# 18	1 + 8 = 9
# 43	4 + 3 = 7
# 36	3 + 6 = 9
# 13	1 + 3 = 4
# 7	7
# Step 2: Group Numbers by Digit Sum
# Now, we create groups based on the digit sum:

# Digit Sum	Numbers
# 9	[18, 36]
# 7	[43, 7]
# 4	[13]
# Step 3: Find Maximum Pair Sum
# For digit sum 9: We have numbers [18, 36]. The sum of the two largest numbers is 18 + 36 = 54.
# For digit sum 7: We have numbers [43, 7]. The sum is 43 + 7 = 50.
# For digit sum 4: Only one number (13), so no valid pair.
# Step 4: Return the Maximum Sum
# The highest sum we found is 54, so the output is:

# python
# Copy
# Edit
# Output: 54
# Test Case 2:
# Input:
# python
# Copy
# Edit
# nums = [10, 12, 19, 14]
# Step 1: Compute Digit Sums
# Number	Sum of Digits
# 10	1 + 0 = 1
# 12	1 + 2 = 3
# 19	1 + 9 = 10
# 14	1 + 4 = 5
# Step 2: Group Numbers by Digit Sum
# Digit Sum	Numbers
# 1	[10]
# 3	[12]
# 10	[19]
# 5	[14]
# Step 3: Find Maximum Pair Sum
# Each digit sum group has only one number, so no valid pairs exist.
# Step 4: Return -1
# Since no pairs satisfy the condition, we return:

# python
# Copy
# Edit
# Output: -1
# Summary
# Test Case	Input	Output	Explanation
# 1	[18, 43, 36, 13, 7]	54	The best pair is (18, 36), both have a digit sum of 9.
# 2	[10, 12, 19, 14]	-1	No two numbers have the same digit sum, so no valid pair exists.