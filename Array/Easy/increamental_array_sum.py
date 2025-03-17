def maxAscendingSum(nums):
    max_sum = current_sum = nums[0]

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:  # Continue the ascending subarray
            current_sum += nums[i]
        else:  # Reset to the new subarray
            current_sum = nums[i]
        
        max_sum = max(max_sum, current_sum)  # Update max sum

    return max_sum

# Test cases
print(maxAscendingSum([10, 20, 30, 5, 10, 50]))  # Output: 65
print(maxAscendingSum([10, 20, 30, 40, 50]))    # Output: 150
print(maxAscendingSum([12, 17, 15, 13, 10, 11, 12]))  # Output: 33
