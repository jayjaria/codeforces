t=int(input())
for i in range(t):
    n,k,x = map(int, input().split())
    

    arr=[0]*k
    res=[]
    for j in range(0,k):
        arr[j]=j+1
    arr.remove(x)

    if k==1 and x==1:
        print('NO')
        continue

    elif arr[0]==1:
        print('YES')
        res=[1]*n
        print(len(res))
        print(*res)
        continue

    elif x==1 and k!=1:
        c=n//2
        
        if len(arr)==1 and n%2==0:
            print('YES')
            d=int(n/2)
            res=[2]*d
            print(len(res))
            print(*res)
            continue
        
        elif len(arr)==1 and n%2!=0:
            print('NO')
            continue

                
        else:
            print('YES')
            res=[2]*(c-1)
            res.append(3)
            print(len(res))
            print(*res)
            continue

