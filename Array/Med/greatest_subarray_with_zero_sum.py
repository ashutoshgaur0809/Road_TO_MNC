a = [6, -2, 2, -8, 1, 7, 4, -10]
l = []     # This will collect all subarrays tested
clk = 0    # This keeps track of the length of the longest subarray with sum = 0

for i in range(len(a)):
    for j in range(i+1, len(a)+1):
        if sum(a[i:j]) == 0:
            clk = max(len(a[i:j]), clk)  # Update max length if subarray sum is 0
        l.append(a[i:j])  # Save the subarray regardless of its sum

print(l)
print(clk)
