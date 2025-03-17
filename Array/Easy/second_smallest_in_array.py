a = [12,35,1,10,34,1]

sm = float('inf')
sec_sm = float('inf')

for i in a:
    if i < sm:
        sec_sm = sm
        sm = i
    if sec_sm > i > sm:
        sec_sm = i

print(sm)
print(sec_sm)