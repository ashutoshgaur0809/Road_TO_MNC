# Q. find min value of a 
# you can peform some operations on a 
# if a % 2 == 0 then a = a / 2
# if a > 3 then a = a - 3
# if both false then return a


import sys


def solution(a):
    while a > 1:
        if a % 2 == 0:
            a = a // 2
        elif a > 3:
            a = a - 3
        else:
            break
    print(a)

# Read all input at once
print("Kitne test case hai aur kya value deni hai space seperate me dete jao")
inputs = sys.stdin.read().split()
T = int(inputs[0])
for i in range(1, T + 1):
    solution(int(inputs[i]))