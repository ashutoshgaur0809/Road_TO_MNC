a = [3, 4, 2, 2, 3]
b = [7, 4, 1, 1, 8]

# Map each value in `a` to a list of its corresponding `b` values
value_map = {}

for i in range(len(a)):
    val = a[i]
    b_val = b[i]
    if val in value_map:
        value_map[val].append(b_val)
    else:
        value_map[val] = [b_val]

# Now compute the minimum b value for each unique a value
result = {key: min(values) for key, values in value_map.items()}

print(result)

# {3: 7, 4: 4, 2: 1}