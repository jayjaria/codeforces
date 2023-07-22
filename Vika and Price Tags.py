# cant solve

t=int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    c=[0]*n
    if sum(a)==0:
        print("YES")
    for j in range(n):
        if a[j]>b[j]:
            c[j]=a[j]-b[j]
        else:
            c[j]=b[j]-a[j]
    first = c
    print(first)
    a=b
    b=c
    while(sum(a)!=0):
        for j in range(n):
            if a[j]>b[j]:
                c[j]=a[j]-b[j]
            else:
                c[j]=b[j]-a[j]    
            
        if sum(c)==0:
            print("YES")
            break
        elif c==first:
            print("NO")
            break
        else:
            pass
        a = b
        b = c
