a = [3, 0, 1, 0, 4, 0, 2]

lm = [0] * len(a)
rm = [0] * len(a)

for i in range(len(a)):
    lm[i] = max(a[0:i+1])  # left max up to index i

for i in range(len(a)):
    rm[i] = max(a[i:])     # right max from index i to end
    
ans = [0] * len(a)
for i in range(len(a)):
   ans[i] = min(lm[i],rm[i]) - a[i]

print("Left max:", lm)
print("Right max:", rm)
print("Ans is :", ans)
print("total trap of water :",sum(ans))