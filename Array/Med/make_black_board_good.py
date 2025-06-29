# Problem: No Odd Sum
# ---------------------------------------
# You are given N numbers on a blackboard. Each number is either 1 or 2.
# The blackboard is considered "good" if every pair (i, j) (i < j) satisfies:
# (A[i] + A[j]) is even.
# 
# Rules:
# - You can replace one 2 with two 1s
# - Or replace two 1s with one 2
#
# Goal:
# Find the **minimum number of operations** required to make the blackboard good.
#
# Note:
# - Sum is even only if both numbers are even or both are odd
# - So all numbers must be 1s (odd) or all 2s (even)
#
# Input:
# - First line: T (number of test cases)
# - For each test case:
#   - Line 1: N (number of numbers)
#   - Line 2: N integers (each either 1 or 2)
#
# Output:
# - For each test case, print the minimum number of operations to make the board good

# Sample Input:
# 3
# 4
# 1 1 2 2
# 4
# 1 1 1 1
# 6
# 1 2 1 2 1 2

# Expected Output:
# 1
# 0
# 3

# ---------------------------------------
# Python Implementation:

T = int(input())
for _ in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    
    cnt1 = a.count(1)
    cnt2 = a.count(2)
    
    # Option 1: Convert all 1s to 2s (only if count1 is even)
    ops1 = float('inf')
    if cnt1 % 2 == 0:
        ops1 = cnt1 // 2
    
    # Option 2: Convert all 2s to 1s
    ops2 = cnt2

    # Output the minimum valid option
    print(min(ops1, ops2))
