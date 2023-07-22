t = int(input())
for j in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))

    if len(arr)==1:
        print('0')
        continue
    narr=[]
    arr.sort()
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            d = arr[i]-arr[i+1]
        else:
            d = arr[i+1]-arr[i]
        narr.append(d)

    i=0
    c=0
    res=[]
    for i in range(len(narr)):
        if narr[i]<=k:
            c+=1
        else:
            res.append(c)
            c=0
    res.append(c)
    m = max(res)
    l = len(narr)
    print(l-m)
            
