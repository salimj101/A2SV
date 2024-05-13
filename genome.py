x = int(input())
a = input()
count = 0
z = {1: "A", 2: "G", 3: "C", 4: "T"}

for i in a:
    if i in ['A', 'G', 'C', 'T']:
        count += 1

if count >= 4:
    result = ""
    for char in a:
        if char == "?":
            replacement_char = ""
            for i in range(1, 5):
                if z[i] not in a:
                    replacement_char = z[i]
                    break
            result += replacement_char
        else:
            result += char
    print(result)
else:
    print("===")
