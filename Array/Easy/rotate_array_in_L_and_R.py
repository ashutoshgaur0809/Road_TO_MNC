def rotate_array(nums, k, direction="right"):
    k %= len(nums)  # Handle cases where k > len(nums)
    
    if direction == "right":
        return nums[-k:] + nums[:-k]  # Right rotate
    elif direction == "left":
        return nums[k:] + nums[:k]  # Left rotate
    else:
        return "Invalid direction! Use 'left' or 'right'."

# Example usage
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

# Right rotation
print("Right Rotate:", rotate_array(nums, k, "right"))  # Output: [5, 6, 7, 1, 2, 3, 4]

# Left rotation
print("Left Rotate:", rotate_array(nums, k, "left"))  # Output: [4, 5, 6, 7, 1, 2, 3]
