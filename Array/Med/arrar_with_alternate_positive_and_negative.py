arr = [1,-2,3,-4,5,-6]
pos = []
neg = []
for i in arr:
    if i > 0 :
        pos.append(i)
    if i < 0:
        neg.append(i)
for i in range(len(pos)):
    arr[2*i] = pos[i]
for i in range(len(neg)):
    arr[2*i+1] = neg[i]

print("Now array with alternate and pos and neg -> ",arr)