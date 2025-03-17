arr = [10, 5, 2, 7, 1, -10]
k = 15


maxi = float("-inf")
for i in range(0,len(arr)):
    for j in range(0,len(arr)+1):
        
        if sum(arr[i:j]) == k:
            maxi = max(maxi,len(arr[i:j]))
            print(arr[i:j])

print("Array with biggest length to achieve k is :",maxi)
            