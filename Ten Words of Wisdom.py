t=int(input())
for i in range(t):
    n = int(input())
    dict={}
    B=[]
    for j in range(n):
        a,b = map(int,input().split())
        B.append(b)
        dict[a]=b

    res=[]
    for a,b in dict.items():
        if a<=10:
            res.append(b)
        else:
            pass

    m = max(res)
    c=1
    for j in range(len(B)):
        if B[j]==m:
            break
        else:
            c+=1
        
    print(c)
