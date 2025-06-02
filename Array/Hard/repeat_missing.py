def approach_optimized(a):
    rep, miss = -1, -1
    n = len(a)
    
    count = [0] * (n + 1)  # Count occurrences from 1 to n

    for num in a:
        count[num] += 1

    for i in range(1, n + 1):
        if count[i] == 0:
            miss = i
        elif count[i] > 1:
            rep = i

    print("Repeat Number: ", rep)
    print("Missing Number : ", miss)

# Example usage
a = [3, 1, 2, 4, 3]
approach_optimized(a)
