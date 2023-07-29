t=int(input())
for i in range(t):
    n=int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    res=[]
    for i in arr:
        if len(res)==0:
            res.append(i)
        elif i in res:
            res.append(i+1)
        else:
            res.append(i)

    set_res = list(set(res))
    print(len(set_res))

# Time Limit Exceeded