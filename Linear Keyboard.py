a = int(input())
for i in range(a):
    k = input()
    w = input()

    p = {char: i for i, char in enumerate(k)}
    t = 0
    c= 0

    for i in range(1, len(w)):
        c= w[i]
        y = w[i-1]
        t += abs(p[c] - p[y])
    print(t)
