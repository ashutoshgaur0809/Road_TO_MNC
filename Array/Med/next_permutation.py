# Steps
'''
Step 1: Find the Pivot
Example 1,3,5,4,2
start from right 
2 < 4 (Not pivot)
4 < 5 (Not pivot)
5 < 3 (Pivot)
For  the first decreasing pair is 3 < 5 at index 1 (pivot is 3).

Step 2: Now, on right side from pivot index look the number who is greater then pivot
but smallest in the right side array
In 1,3,5,4,2, numbers to the right of 3 are 5,4,2.

The smallest number greater than 3 is 4.

Swap 3 and 4:
1,4,5,3,2

step 3: Reverse the remain array on the right side of pivot index
'''

a = [1,3,5,4,2]

# find pivot 
pivot = 0
for i in range(len(a)-1,-1,-1):
    if a[i] > a[i-1]:
        pivot = i - 1
        break


l = []
for i in range(pivot,len(a)):
    if a[i] > a[pivot]:
        l.append(a[i])

a[pivot] = min(l)
# reverse the right side array

a[:] = a[0:pivot + 1] + a[pivot::-1]



    
print(pivot)
print(l)
print(a)
