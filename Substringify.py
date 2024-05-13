a = int(input())
s = []
for i in range(a):
    b = input()
    s.append(b)
max_length = max(len(i) for i in s)
for i in s:
    if len(i) == max_length:
        print(i)
