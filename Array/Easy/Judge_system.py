T = int(input())
for _ in range(T):
    ratings = list(map(int, input().split()))
    total = sum(ratings)

    if total >= 35:
        print(0)
        continue

    ratings.sort()  # Bribe the lowest first
    bribes = 0

    for i in range(5):
        if total >= 35:
            break
        gain = 10 - ratings[i]
        total += gain
        bribes += 1

    print(bribes * 100)
    
# 🧪 Sample Input
# 3
# 7 7 0 7 7
# 7 7 7 7 7
# 0 0 0 0 0
# ✅ Output
# 100
# 0
# 400
