if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    arr.sort(reverse=True)
    r = None
    m = arr[0]
    for i in arr:
        if i != m:
            r = i
            break
    print(r)
