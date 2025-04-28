arr = [1,2,3]
 
 
if len(arr) == 1:
    print(arr)
elif len(set(arr)) == 1:
    l = []
    l.append(arr[0])
    print(l)
elif len(arr) == 2 and len(set(arr)) == 2:
    print(arr)
else:
    d = {}
    l = []
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
 
    for i,j in d.items():
        if j > len(arr) // 3:
            l.append(i)
 
    print("Ans - > ",l)
    
# Example 1:

# Input: nums = [3,2,3]
# Output: [3]
# Example 2:

# Input: nums = [1]
# Output: [1]
# Example 3:

# Input: nums = [1,2]
# Output: [1,2]