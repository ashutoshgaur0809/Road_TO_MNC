arr = [2,1,3,4]

cnt = 0

for i in range(len(arr)):
    if arr[i] > arr[(i+1) % len(arr)]:
        cnt += 1
    if cnt > 1:
        print("Not Sorted")
        break

if cnt < 2:
    print("Sorted")    