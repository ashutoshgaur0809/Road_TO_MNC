a = [1, 2, 2, 3]
# a = [100, 200, 1, 2, 3, 4]/

b = sorted(set(a))  # remove duplicates and sort
clk = 1
maxi = 1
for i in range(len(b) - 1):
    if b[i+1] - b[i] == 1:
        clk += 1
        maxi = max(maxi, clk)
    else:
        clk = 1

print(b)
print(maxi)