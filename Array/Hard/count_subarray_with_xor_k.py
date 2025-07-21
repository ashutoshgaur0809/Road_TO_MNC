def subarraysWithXorK(a: [int], b: int) -> int:
    n = len(a)  # size of the given array.
    cnt = 0

    # Step 1: Generating subarrays:
    for i in range(n):
        xorr = 0
        for j in range(i, n):

            # step 2: calculate XOR of all elements:
            xorr = xorr ^ a[j]

            # step 3: check XOR and count:
            if (xorr == k):
                cnt += 1

    return cnt

if __name__ == "__main__":
    a = [4, 2, 2, 6, 4]
    k = 6
    ans = subarraysWithXorK(a, k)
    print("The number of subarrays with XOR k is:", ans)

# Example 1:
# Input Format: A = [4, 2, 2, 6, 4] , k = 6
# Result: 4
# Explanation: The subarrays having XOR of their elements as 6 are  [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], [6]

# Example 2:
# Input Format: A = [5, 6, 7, 8, 9], k = 5
# Result: 2
# Explanation: The subarrays having XOR of their elements as 5 are [5] and [5, 6, 7, 8, 9]