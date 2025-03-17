

def ans(arr,k):
    n = len(arr)
    # create sub array of k size
    l = []
    for i in range(0,len(arr)-k+1):
        sub_arr = arr[i:i+k]
        len_sub_arr = len(sub_arr)
        sub_arr_with_set = set(sub_arr)
        len_sub_arr_with_set = len(sub_arr_with_set)
        
               
        # check if sub array is sorted and there is no same element in sub array
        if sub_arr == sorted(sub_arr) and len_sub_arr_with_set == len_sub_arr:
            l.append(max(sub_arr))
        
        # if array is not sorted
        else:
            # check any value is same or not in sub array
            l.append(-1)
    return l       
            
                
            



# takes input first 
arr = list(map(int,input("Enter Values of array").split()))
k = int(input("Size of subarray: "))

res = ans(arr,k)
print("Ans is --",res)  # prints the result

# Example 1:

# Input: nums = [1,2,3,4,3,2,5], k = 3

# Output: [3,4,-1,-1,-1]

# Explanation:

# There are 5 subarrays of nums of size 3:

# [1, 2, 3] with the maximum element 3.
# [2, 3, 4] with the maximum element 4.
# [3, 4, 3] whose elements are not consecutive.
# [4, 3, 2] whose elements are not sorted.
# [3, 2, 5] whose elements are not consecutive.
# Example 2:

# Input: nums = [2,2,2,2,2], k = 4

# Output: [-1,-1]

# Example 3:

# Input: nums = [3,2,3,2,3,2], k = 2

# Output: [-1,3,-1,3,-1]