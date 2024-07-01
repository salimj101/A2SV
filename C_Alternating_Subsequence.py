t = int(input().strip())

for i in range(t):
    n = int(input().strip())  
    a = list(map(int, input().strip().split()))  

    current = a[0]
    total = 0

    for i in range(1, n):
        if (a[i] > 0 and current < 0) or (a[i] < 0 and current > 0):
            total += current
            current = a[i] 
        else:
            current = max(current, a[i])

    total += current
    print(total)
