def circular_sum(a, k):
    c = []
    n = len(a)

    if k == 0:
        # If k is 0, all sums are 0
        c = [0] * n
        return c

    if k > 0:
        # For positive k, create the circular list and calculate sums
        b = a[:] + a[:k]  # Extend the list for circular indexing
        for i in range(n):
            c.append(sum(b[i+1:i+k+1]))  # Sum next `k` elements starting from index `i`

    elif k < 0:
        # For negative k, create the reversed circular list
        k = abs(k)
        b = a[-1:-(k+1):-1] + a[:]  # Take last `k` elements reversed and add original list
        for i in range(n):
            c.append(sum(b[i:i+k]))  # Sum `k` elements before index `i`

    return c


# Example usage:
a = [5, 7, 1, 4]
k = -2

result = circular_sum(a, k)
print("Result:", result)


# Example 1:

# Input: code = [5,7,1,4], k = 3
# Output: [12,10,16,13]
# Explanation: Each number is replaced by the sum of the next 3 numbers. The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around.
# Example 2:

# Input: code = [1,2,3,4], k = 0
# Output: [0,0,0,0]
# Explanation: When k is zero, the numbers are replaced by 0. 
# Example 3:

# Input: code = [2,4,9,3], k = -2
# Output: [12,5,6,13]
# Explanation: The decrypted code is [3+9, 2+3, 4+2, 9+4]. Notice that the numbers wrap around again. If k is negative, the sum is of the previous numbers.
 