n = int(input())
lev = int(input())
p = []
b = []
a = []
ans = 0

for i in range(n):
    p.append(int(input()))
for j in range(n):
    b.append(int(input()))
for k in range(n):
    a.append([p[k], b[k]])

while True:
    defeated = False
    for i in range(len(a)):
        if a[i][0] <= lev:
            lev += a[i][1]
            a.pop(i)
            ans += 1
            defeated = True
            break
    if not defeated:
        break

print(ans)

# 🔍 Problem Summary:
# Tumhare paas initial experience e hai.
# Tumhe n monsters milenge, har monster ke liye do cheezein di gayi hain:
# power[i] → us monster ko harane ke liye minimum experience kitna chahiye.
# bonus[i] → us monster ko harane par tumhe kitna experience milega.
# Tum kisi bhi order mein monsters ko hara sakte ho.
# Agar kisi monster ke against tumhari current experience power[i] se kam hui → Game Over.
# Goal: Aise maximum monsters harao jitne possible hain.

# n = 3
# e = 100
# power = [101, 100, 304]
# bonus = [100, 1, 524]
# o/p - 2
