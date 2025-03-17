a = [1,2,2,2]

d = {}
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for i,j in d.items():
    print(f"{i} appears {j} times")
    