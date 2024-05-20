def max_alternating_subsequence_sum(test_cases):
    results = []
    
    for case in test_cases:
        n, a = case
        max_sum = 0
        current_max = a[0]
        
        for i in range(1, n):
            if (a[i] > 0) == (current_max > 0):
                current_max = max(current_max, a[i])
            else:
                max_sum += current_max
                current_max = a[i]
        
        max_sum += current_max
        results.append(max_sum)
    
    return results

t = int(input().strip())
test_cases = []

for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    test_cases.append((n, a))

results = max_alternating_subsequence_sum(test_cases)

for result in results:
    print(result)
