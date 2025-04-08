# Pascal's Triangle - Full Row Generation
def Creation():
    n = 5  # You can change this to any number of rows
    l = []
    for i in range(n):
        if i == 0:
            l.append([1])
        elif i == 1:
            l.append([1, 1])
        else:
            k = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    k.append(1)
                else:
                    k.append(l[i - 1][j - 1] + l[i - 1][j])
            l.append(k)

    for row in l:
        print(row)

# Pascal's Triangle - Get specific value using Binomial Coefficient
def AtSpecific():
    r = 5  # row
    c = 2  # column

    rf = 1
    cf = 1
    rcf = 1

    for i in range(1, r + 1):
        rf *= i
    for i in range(1, c + 1):
        cf *= i
    for i in range(1, r - c + 1):
        rcf *= i

    res = rf // (cf * rcf)
    print(f"Value at row {r}, column {c}: {res}")

# Optional: Call functions here
if __name__ == "__main__":
    print("Pascal's Triangle:")
    Creation()
    print("\nValue at specific position:")
    AtSpecific()
