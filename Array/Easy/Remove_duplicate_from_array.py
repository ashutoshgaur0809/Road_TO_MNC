arr = [0,1,1,2,3,4,4,5,6]

uq = set()
for i in arr:
    uq.add(i)

print("Unique values -",uq)

uq = list(uq)
arr[:] = uq
arr.sort()

print("Len of array after removing duplicates -",len(arr))
    