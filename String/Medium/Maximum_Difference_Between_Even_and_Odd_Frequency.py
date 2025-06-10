class Solution:
    def maxDifference(self, s: str) -> int:
        from collections import Counter

        freq = Counter(s)
        max_even = -1
        max_odd = -1

        for count in freq.values():
            if count % 2 == 0:
                max_even = max(max_even, count)
            else:
                max_odd = max(max_odd, count)

        if max_even == -1 or max_odd == -1:
            return -1

        return max_odd - max_even


# Test Cases
sol = Solution()

print("Test Case 1:")
s1 = "tzt"  # t:2, z:1 -> max_odd=1, max_even=2 -> 1-2 = -1
print(f"Input: {s1}, Output: {sol.maxDifference(s1)}\n")

print("Test Case 2:")
s2 = "aabbcc"  # All counts = 2 -> only even -> return -1
print(f"Input: {s2}, Output: {sol.maxDifference(s2)}\n")

print("Test Case 3:")
s3 = "aabbbc"  # a:2, b:3, c:1 -> max_odd=3, max_even=2 -> 3-2 = 1
print(f"Input: {s3}, Output: {sol.maxDifference(s3)}\n")

print("Test Case 4:")
s4 = "abcde"  # All counts = 1 -> only odd -> return -1
print(f"Input: {s4}, Output: {sol.maxDifference(s4)}\n")

print("Test Case 5:")
s5 = "aaabbbcccddeee"  # a:3, b:3, c:3, d:2, e:3 -> max_odd=3, max_even=2 -> 3-2 = 1
print(f"Input: {s5}, Output: {sol.maxDifference(s5)}\n")
