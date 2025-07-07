# # input
# a = []

# n = int(input("Enter Len of Array - "))

# for i in range(n):
#     b = list(map(int,input().split()))
#     a.append(b)

# print("Array is - ",a)
a = [[7, 8], [1, 5], [2, 4], [4, 6]]

# Sort according to the start value
sa = sorted(a, key=lambda x: x[0])
print("After sort according start position - ", sa)

lb, ub = sa[0][0], sa[0][1]
l = []

for i in range(1, len(sa)):
    if sa[i][0] <= ub:
        ub = max(ub, sa[i][1])  # Merge intervals
    else:
        l.append([lb, ub])
        lb = sa[i][0]
        ub = sa[i][1]

# Don't forget the last interval
l.append([lb, ub])

print("Merged intervals:", l)
# [[1, 6], [7, 8]]
