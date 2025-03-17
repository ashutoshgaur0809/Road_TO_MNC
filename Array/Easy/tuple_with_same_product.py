# a = [1,2,4,5,10]
a = [2,3,4,6]

# first we create all possible combinations of the list 2 number list 

l = []
m = []
for i in range(0,len(a)):
    
    for j in range(i+1,len(a)):
        
        l.append((a[i],a[j]))
        m.append((a[j]*a[i]))

print(l)
print(m)

# m contains multiplication of i and j
# if any number in m is common then it considered as 8

d = {}
clk = 0
for i in m:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for i,j in d.items():
    if j == 2:
        clk += 1

print(clk * 8)


# Example 1:

# Input: nums = [2,3,4,6]
# Output: 8
# Explanation: There are 8 valid tuples:
# (2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
# (3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
# Example 2:

# Input: nums = [1,2,4,5,10]
# Output: 16
# Explanation: There are 16 valid tuples:
# (1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
# (2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
# (2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
# (4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)

