a = [12,345,2,6,7896]

clk = 0
for i in a:
    if len(str(i)) % 2 == 0:
        clk += 1

print(clk)