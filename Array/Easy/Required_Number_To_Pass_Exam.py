def min_marks_to_pass(T, test_cases):
    results = []
    for case in test_cases:
        N, scores = case
        total_possible_marks = (N + 1) * 100
        required_marks_to_pass = total_possible_marks / 2
        sum_of_completed_assignments = sum(scores)
        marks_needed_on_last_assignment = required_marks_to_pass - sum_of_completed_assignments
        
        if marks_needed_on_last_assignment > 100:
            results.append(-1)
        else:
            results.append(max(0, marks_needed_on_last_assignment))  # No negative score needed
        
    return results


# Input reading and parsing 
T = int(input())  # Number of test cases
test_cases = []

for _ in range(T):
    N = int(input())  # Number of completed assignments
    scores = list(map(int, input().split()))  # Scores of the N completed assignments
    test_cases.append((N, scores))

# Calculate and output results for each test case
results = min_marks_to_pass(T, test_cases)
for result in results:
    print(result)


# Input
# Output
# 4
# 1
# 67
# 2
# 53 32
# 3
# 0 0 0
# 2
# 100 100
# 33
# 65
# -1
# 0