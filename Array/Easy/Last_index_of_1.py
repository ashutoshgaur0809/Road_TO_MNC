s = "00001"

if "1" not in s:
    print("No 1's in the string")

for i in range(len(s)-1,-1,-1):
    if s[i] == "1":
        print("last index of 1 is", i)
        break
# Input: s = 00001
# Output: 4
# Explanation: Last index of  1 in given string is 4.
# Input: s = 0
# Output: -1
# Explanation: Since, 1 is not present, so output is -1.
