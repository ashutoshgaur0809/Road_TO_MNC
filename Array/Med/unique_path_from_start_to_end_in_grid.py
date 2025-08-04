# 🔷 Problem: Unique Paths in Grid
# ----------------------------------
# Ek robot ek m x n grid ke top-left (0,0) se start karta hai 
# aur bottom-right (m-1,n-1) tak pahuchna chahta hai.
# Wo sirf 2 direction me move kar sakta hai: 
# 1. Right 
# 2. Down

# Tumhe batana hai ki robot kitne different unique paths le sakta hai
# jisme wo bottom-right corner tak pahuch jaaye.

# 🔸 Constraints:
# 1 <= m, n <= 100
# Answer hamesha 2 * 10^9 se chhota hoga

# 🧪 Test Cases:
# uniquePaths(3, 7) ➞ 28
# uniquePaths(3, 2) ➞ 3
# uniquePaths(1, 1) ➞ 1
# uniquePaths(10, 10) ➞ 48620

# 🔶 Approach (Hinglish):
# ----------------------------------
# 1. Robot ko bottom-right pahuchne ke liye hamesha (m-1) Down aur (n-1) Right steps lene padenge.
# 2. Total steps = (m-1 + n-1) = m + n - 2
# 3. Tumhe bas yeh decide karna hai ki in total steps me se Down steps (ya Right) kahaan kahaan aayenge.

# formula - C(total steps, down ya right me se koi ek step)
# c((m - 1 + n - 1),(m - 1 ya n - 1))
# 4. Yeh combination ka problem hai:
#    Formula: C(m + n - 2, m - 1) = (m+n-2)! / ((m-1)! * (n-1)!)
# 5. Hum factorial function khud likhenge (koi library use nahi karenge)

# ✅ Python Code:

# Function to calculate factorial (no library)
def factorial(num):
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

# Function to calculate number of unique paths
def uniquePaths(m, n):
    numerator = factorial(m + n - 2)  # total steps factorial
    denominator = factorial(m - 1) * factorial(n - 1)  # down! * right!
    return numerator // denominator  # Integer division for result

# 🔽 Test cases
print("Test Case 1:", uniquePaths(3, 7))   # Output: 28
print("Test Case 2:", uniquePaths(3, 2))   # Output: 3
print("Test Case 3:", uniquePaths(1, 1))   # Output: 1
print("Test Case 4:", uniquePaths(10, 10)) # Output: 48620
print("Test Case 5:", uniquePaths(5, 5))   # Output: 70
