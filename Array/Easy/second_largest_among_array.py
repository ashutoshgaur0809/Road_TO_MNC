a = [12,35,1,10,34,1]

large = float('-inf')
second_large = float('-inf')

for i in a:
    if i > large:
        second_large = large
        large = i
    if second_large < i < large:
        second_large = i

print(large)
print(second_large)