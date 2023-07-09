t = int(input())

for i in range(t):
    n,k = map(int, input().split())
    arr = list(map(int,input().split()))

    res = []
    for i in range(len(arr)-1):
        if arr[i]>=arr[i+1]:
            d = arr[i]-arr[i+1]
        else:
            d = arr[i+1]-arr[i]
        res.append(d)
    for j in range(k-1):
        res.remove(max(res))

    print(sum(res))